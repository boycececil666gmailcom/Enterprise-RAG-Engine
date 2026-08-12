#region Imports & Driver Initialization
import json
import re
from functools import lru_cache

from langchain_core.messages import HumanMessage, SystemMessage

from .config import NEO4J_PASSWORD, NEO4J_URI, NEO4J_USERNAME
from .llm_client import llm


@lru_cache(maxsize=1)
def get_driver():
    """Lazily initializes and caches Neo4j GraphDatabase driver using lru_cache."""
    try:
        from neo4j import GraphDatabase
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
        driver.verify_connectivity()
        return driver
    except Exception:
        return None

#endregion

def sanitize_rel_type(rel_type: str) -> str:
    """Sanitizes relationship type to avoid Cypher injection and conform to Cypher naming rules."""
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', rel_type).upper().strip('_')
    return sanitized if sanitized else "RELATED_TO"

def clean_json_response(content) -> str:
    """Cleans code blocks (```json ... ```) from LLM response text."""
    if isinstance(content, list):
        content = "".join(part if isinstance(part, str) else part.get("text", "") for part in content)
    elif not isinstance(content, str):
        content = str(content)
        
    content = content.strip()
    if content.startswith("```"):
        # split by newline, drop the first and last line
        lines = content.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        content = "\n".join(lines).strip()
    return content

def extract_entities_and_relations(text: str) -> dict:
    """Uses Gemini LLM to extract entities and relations from a text chunk."""
    if not llm:
        return {"entities": [], "relationships": []}
    
    system_prompt = (
        "You are an expert knowledge graph extractor. Your task is to extract entities and their relationships "
        "from the provided text. You must output ONLY a valid JSON object matching this schema:\n"
        "{\n"
        "  \"entities\": [\n"
        "    {\"name\": \"Entity Name (keep it concise and normalized, e.g., 'Supernova')\", \"type\": \"Entity Type (e.g., 'Product', 'Company', 'PricingPlan')\", \"description\": \"Brief description of the entity based on the text\"}\n"
        "  ],\n"
        "  \"relationships\": [\n"
        "    {\"source\": \"Source Entity Name\", \"type\": \"Relationship Type (uppercase, e.g., 'HAS_PLAN', 'OPERATED_BY')\", \"target\": \"Target Entity Name\"}\n"
        "  ]\n"
        "}\n"
        "Do not include any explanation or markdown formatting like ```json. Output raw JSON only."
    )
    
    try:
        response = llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Text to extract from:\n{text}")
        ])
        
        cleaned = clean_json_response(response.content)
        data = json.loads(cleaned)
        return {
            "entities": data.get("entities", []),
            "relationships": data.get("relationships", [])
        }
    except Exception:
        return {"entities": [], "relationships": []}

def add_graph_relations(entities: list, relationships: list):
    """Saves extracted entities and relationships to the Neo4j database."""
    driver = get_driver()
    if not driver:
        return
        
    try:
        with driver.session() as session:
            # Create/Merge entities
            for ent in entities:
                name = ent.get("name")
                ent_type = ent.get("type", "Unknown")
                desc = ent.get("description", "")
                if name:
                    session.run(
                        "MERGE (e:Entity {name: $name}) "
                        "ON CREATE SET e.type = $type, e.description = $description "
                        "ON MATCH SET e.description = CASE WHEN e.description CONTAINS $description THEN e.description ELSE e.description + '; ' + $description END",
                        name=name, type=ent_type, description=desc
                    )
            
            # Create/Merge relationships
            for rel in relationships:
                source = rel.get("source")
                target = rel.get("target")
                rel_type = sanitize_rel_type(rel.get("type", "RELATED_TO"))
                if source and target:
                    # First ensure both nodes exist
                    session.run("MERGE (:Entity {name: $name})", name=source)
                    session.run("MERGE (:Entity {name: $name})", name=target)
                    
                    # Merge relationship dynamically
                    query = (
                        f"MATCH (s:Entity {{name: $source}}) "
                        f"MATCH (t:Entity {{name: $target}}) "
                        f"MERGE (s)-[r:{rel_type}]->(t)"
                    )
                    session.run(query, source=source, target=target)
    except Exception:
        pass

def extract_query_entities(query: str) -> list:
    """Uses Gemini LLM to identify main entity names mentioned in a user search query."""        
    system_prompt = (
        "You are an entity extractor. Identify and list the main entities (proper nouns, products, services, terms) "
        "mentioned in the user query. Output ONLY a valid JSON array of strings representing entity names, e.g.:\n"
        "[\"Supernova\", \"Premium Plan\"]\n"
        "Do not include any explanation or markdown formatting like ```json. Output raw JSON only."
    )
    
    try:
        response = llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Query to extract entities from: '{query}'")
        ])
        cleaned = clean_json_response(response.content)
        entities = json.loads(cleaned)
        if isinstance(entities, list):
            return [str(item) for item in entities]
        return []
    except Exception:
        return []

def retrieve_graph_relations(query_entities: list) -> str:
    """Queries Neo4j for the listed entities and their 1-hop relationships to format context."""
    driver = get_driver()
    if not driver or not query_entities:
        return ""
        
    context_parts = []
    try:
        with driver.session() as session:
            for entity_name in query_entities:
                # Use substring matching to handle variations in entity naming (e.g., 'Aurora' matching 'Aurora Project')
                result = session.run(
                    "MATCH (e:Entity) WHERE toLower(e.name) CONTAINS toLower($name) OR toLower($name) CONTAINS toLower(e.name) "
                    "OPTIONAL MATCH (e)-[r]-(neighbor:Entity) "
                    "RETURN e.name as name, e.type as type, e.description as description, "
                    "       type(r) as rel_type, neighbor.name as neighbor_name, "
                    "       startNode(r) = e as is_source",
                    name=entity_name
                )
                
                records = list(result)
                if not records:
                    continue
                    
                first = records[0]
                entity_info = f"Entity: {first['name']} (Type: {first['type']}, Description: {first['description']})"
                relations_info = []
                
                for record in records:
                    rel_type = record.get("rel_type")
                    neighbor_name = record.get("neighbor_name")
                    is_source = record.get("is_source")
                    if rel_type and neighbor_name:
                        if is_source:
                            relations_info.append(f"- ({first['name']}) -[{rel_type}]-> ({neighbor_name})")
                        else:
                            relations_info.append(f"- ({neighbor_name}) -[{rel_type}]-> ({first['name']})")
                
                part = entity_info
                if relations_info:
                    part += "\nRelationships:\n" + "\n".join(relations_info)
                context_parts.append(part)
        
        return "\n\n".join(context_parts) if context_parts else ""
    except Exception:
        return ""

#region Knowledge Ingestion API
def ingest_graph_document(text: str) -> int:
    """Extracts entities and relationships from document text using Gemini LLM and saves them into Neo4j."""
    try:
        extracted = extract_entities_and_relations(text)
        if extracted.get("entities") or extracted.get("relationships"):
            add_graph_relations(extracted["entities"], extracted["relationships"])
            return len(extracted.get("entities", [])) + len(extracted.get("relationships", []))
    except Exception:
        pass
    return 0
#endregion

