#region Imports & Setup
import os
import sys
import argparse
import json
from qdrant_client import QdrantClient

# Define log_step for clean ANSI border logging
def log_step(step_idx: str, description: str):
    script_name = os.path.basename(__file__)
    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [{step_idx}] [{script_name}] {description}\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")
#endregion

#region Inspection Logic
def inspect_vector_database(url: str, collection_name: str, limit: int, query_filter: str = None):
    log_step("1/2", f"Connecting to Qdrant VDB at {url}")
    
    try:
        client = QdrantClient(url=url)
        collection_info = client.get_collection(collection_name)
    except Exception as e:
        print(f"\033[1;31mError connecting to Qdrant VDB at {url}: {e}\033[0m")
        sys.exit(1)

    print(f"\033[1;93m=== COLLECTION OVERVIEW ===\033[0m")
    print(f"Collection Name  : {collection_name}")
    print(f"Collection Status: {collection_info.status.value}")
    print(f"Total Points     : \033[1;92m{collection_info.points_count}\033[0m")
    
    vector_params = collection_info.config.params.vectors
    if hasattr(vector_params, 'size'):
        print(f"Vector Dimension : {vector_params.size}")
        print(f"Distance Metric  : {vector_params.distance.value}")
    
    log_step("2/2", f"Fetching Top {limit} Stored Points")
    
    points, _ = client.scroll(
        collection_name=collection_name,
        limit=limit,
        with_payload=True,
        with_vectors=False
    )
    
    if not points:
        print("No document points found in collection.")
        return

    for idx, pt in enumerate(points, 1):
        payload = pt.payload or {}
        content = payload.get("page_content", "N/A")
        meta = payload.get("metadata", {})
        
        # Apply optional text filter
        if query_filter and query_filter.lower() not in content.lower() and query_filter.lower() not in json.dumps(meta).lower():
            continue

        print(f"\033[1;94m--- Point [{idx}/{len(points)}] ID: {pt.id} ---\033[0m")
        print(f"\033[1;97mContent Preview:\033[0m {content[:200]}...")
        if meta:
            print(f"\033[1;36mMetadata:\033[0m {json.dumps(meta, ensure_ascii=False, indent=2)}")
        print()

    print(f"\033[1;92mInspection complete! Total documents listed: {len(points)}\033[0m")
#endregion

#region CLI Handler
def main():
    parser = argparse.ArgumentParser(description="Inspect stored document points in Qdrant Vector Database")
    parser.add_argument("--url", type=str, default="http://localhost:6333", help="Qdrant VDB server URL")
    parser.add_argument("--collection", type=str, default="local_rag_documents", help="Qdrant collection name")
    parser.add_argument("--limit", type=int, default=5, help="Number of records to display")
    parser.add_argument("--query", type=str, default=None, help="Filter records by keyword")

    args = parser.parse_args()
    inspect_vector_database(args.url, args.collection, args.limit, args.query)

if __name__ == "__main__":
    main()
#endregion
