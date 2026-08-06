---
title: Kanzi Documentation MCP server
source: https://docs.kanzi.com/4.1.0/en/working-with/ai-tools/kanzi-documentation-mcp-server.html
---

# Kanzi Documentation MCP server


The Kanzi Documentation MCP server connects your AI assistant to the Kanzi documentation sources. This allows your AI assistant to search and retrieve information from the Kanzi documentation to answer your questions about Kanzi concepts, features, workflows, and best practices.

The Kanzi Documentation MCP server is available at `https://docs.mcp.kanzi.com/mcp`.

> **Tip:** You can set up the Kanzi Documentation MCP server in Claude Desktop and VS Code from two places on the Documentation website: from the AI assistant button next to any topic title, or from the **Get Kanzi guidance in your IDE** pill inside Ask Kanzi.
## Setting up the Kanzi Documentation MCP server

### Setting up in Claude Desktop


To set up the Kanzi Documentation MCP server in Claude Desktop:

1.

Download the zipped mcpb file from https://docs.kanzi.com/mcp/kanzi-docs-mcp.zip.
2.

Extract the zip file to get `kanzi-docs-mcp.mcpb`.
3.

Double-click the mcpb file to open it in Claude Desktop.
4.

In Claude Desktop, click **Install**.

### Setting up in VS Code


To set up the Kanzi Documentation MCP server in VS Code:

1.

In VS Code, open the **Command Palette** (Ctrl Shift P) and select **MCP: Open User Configuration**.
2.

In the `mcp.json` file, add the server configuration:

```
{
   "servers": {
      "kanzi-docs": {
         "type": "http",
         "url": "https://docs.mcp.kanzi.com/mcp"
      }
   },
   "inputs": []
}

```

3.

Open the **Command Palette** and select **Developer: Reload Window**.
4.

Open the **Chat** window with Ctrl Alt I.

### Setting up in Claude Code


To set up the Kanzi Documentation MCP server in Claude Code:

```
claude mcp add --scope user --transport http kanzi-docs https://docs.mcp.kanzi.com/mcp

```

### Setting up in other tools


To set up the Kanzi Documentation MCP server in other AI tools that support MCP, refer to the documentation of that tool. In the tool configuration, use the server URL with `mcp-remote`:

```
{
   "mcpServers": {
      "kanzi-docs": {
         "command": "npx",
         "args": [
            "-y",
            "mcp-remote",
            "https://docs.mcp.kanzi.com/mcp"
         ]
      }
   }
}

```

### Available tools


The Kanzi Documentation MCP server provides these tools:

- **list_versions**: List all available Kanzi documentation versions
- **set_version**: Switch to a specific Kanzi version
- **search_docs**: Search Kanzi documentation for relevant information
- **ask_question**: Get answers to questions about Kanzi
- **get_page**: Retrieve a full documentation page
- **search_across_versions**: Search across all loaded Kanzi versions
- **compare_versions**: Compare documentation between two Kanzi versions
