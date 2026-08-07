---
title: Kanzi API MCP server
source: https://docs.kanzi.com/4.1.0/en/working-with/ai-tools/kanzi-api-mcp-server.html
---

# Kanzi API MCP server

The Kanzi API MCP server connects your AI assistant to the Kanzi API reference documentation. This allows the AI assistant to look up API signatures, check deprecation status, resolve include directives, and compare APIs between Kanzi versions. The server covers Kanzi APIs across C++, Java, C#, Lua, and Rust.

The Kanzi API MCP server prevents the AI assistant from hallucinating API signatures. Instead of guessing, the assistant retrieves verified API information directly from the server.

The Kanzi API MCP server supports these API sets:
|

API set |

Language |

Description |
|

`kanzi-runtime-api` |

C++ |

Kanzi Engine core API |
|

`kanzi-java-api` |

Java |

Kanzi Engine Java bindings |
|

`kanzi-droidfw-api` |

Java |

Kanzi Android Framework API |
|

`kanzi-appfw-android-api` |

Java |

Kanzi Android App Framework API |
|

`kanzi-studio-plugin-api` |

C# |

Kanzi Studio Plugin API |
|

`kanzi-localization-api` |

C# |

Kanzi Localization Plugin API |
|

`kanzi-lua-api` |

Lua |

Kanzi Engine Lua API |
|

`kanzi-rust-api` |

Rust |

Kanzi Engine Rust API |
## Setting up the Kanzi API MCP server

### Setting up in Claude Desktop

To set up the Kanzi API MCP server in Claude Desktop, add the server to your Claude Desktop configuration file:

1.

In your Claude Desktop configuration file, add the following:

```
{
   "mcpServers": {
      "kanzi-api": {
         "command": "npx",
         "args": [
            "-y",
            "mcp-remote",
            "https://api.mcp.kanzi.com"
         ]
      }
   }
}

```

2.

Restart Claude Desktop.

### Setting up in VS Code

To set up the Kanzi API MCP server in VS Code:

1.

In VS Code, open the **Command Palette** (Ctrl Shift P) and select **MCP: Open User Configuration**.
2.

In the `mcp.json` file, add the server configuration:

```
{
   "servers": {
      "kanzi-api": {
         "type": "http",
         "url": "https://api.mcp.kanzi.com"
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

To set up the Kanzi API MCP server in Claude Code, run:

```
claude mcp add --scope user --transport http kanzi-api https://api.mcp.kanzi.com

```

### Setting up in other tools

To set up the Kanzi API MCP server in other AI tools that support MCP, refer to the documentation of that tool. In the tool configuration, use the server URL with `mcp-remote`:

```
{
   "mcpServers": {
      "kanzi-api": {
         "command": "npx",
         "args": [
            "-y",
            "mcp-remote",
            "https://api.mcp.kanzi.com"
         ]
      }
   }
}

```

## Example queries

After you set up the Kanzi API MCP server, you can ask your AI assistant questions like the following. The assistant uses the server tools to retrieve accurate API information.
### Basic lookups

You can search for API members, verify signatures, check deprecation status, and get include directives:

- âFind the Node class in the Java API.â
- âWhat is the signature of `kanzi::Node::setName`?â
- âIs `kanzi::Page` deprecated? What should I use instead?â
- âWhat header do I need to include to use `Button2D` in C++?â

### Cross-version migration

The Kanzi API MCP server can compare APIs across versions, which helps you estimate the effort required for a migration and identify the changes that you need to address. This is where the server is most valuable, because no human could quickly diff tens of thousands of API records across multiple versions.

- âI am migrating a Kanzi project from 3.9.8 to 4.0.0. What C++ APIs were removed or changed? Focus on the `Node` and `RenderPass` classes.â
- âShow me every API that was deprecated between Kanzi 3.9.13 and 4.0.0, with their replacements.â
- âWhich Java APIs were added between Kanzi 3.9.9 and 3.9.12? I want to know what new capabilities became available.â

### API evolution tracking

You can track how a specific API member changed across all available Kanzi versions:

- âHow has `kanzi::ResourceManager` evolved from Kanzi 3.6.21 to 4.0.0? Show me the full history.â
- âTrack the history of `kanzi::Node::trySetFocus` across all versions. Did its signature change?â
- âWhen was the Lua API for `Button2D` introduced, and has its interface changed across versions?â

### Cross-language comparison

You can compare how the same functionality is exposed across different Kanzi language APIs:

- âCompare how property types work in C++ versus Java versus Lua. Show me `PropertyType` or equivalent in each language.â
- âI need to load a prefab at runtime. Show me the API for this in C++, Java, and Lua with the correct includes and imports.â
- âHow does animation timeline creation differ between C++ and Java? Show signatures for `TimelinePlayer` or `AnimationPlayer`.â

### Real-world coding tasks

You can ask the AI assistant to help you write code using verified API calls:

- âWrite a Kanzi Studio plugin in C# that iterates all `Node2D` items in a project and lists their names. Use only verified API calls.â
- âShow me how to create a custom `RenderPass` in C++ for Kanzi 3.9.15. What do I need to subclass, what headers to include, and what virtual methods to override?â
- âI am writing a Java Android app with Kanzi. How do I handle touch input? Show me the relevant classes and their methods.â

## Configuring your AI assistant

For best results, add instructions to your AI assistant that tell it how to use the Kanzi API MCP server tools effectively. These instructions help the AI assistant choose the right tool for each task, use the correct naming conventions, and verify API information before using it in code.

How you add these instructions depends on the AI assistant that you use:

- In Claude Code, add the instructions to the `CLAUDE.md` file in your project root directory.
- In VS Code with GitHub Copilot, add the instructions to the `.github/copilot-instructions.md` file in your project root directory.
- In Claude Desktop, add the instructions to the system prompt of your project.

The following instructions are a recommended starting point. You can adjust them based on your needs.

```
Kanzi API MCP server â tool selection guide:
- Discovery (do not know exact name): search_kanzi_api() â supports
  member_type filter (class/function/variable/enum/struct/interface/typedef)
  and n_results up to 20.
- Verification (know the fully-qualified name): get_method_signature() â also
  finds overloads through prefix matching. For example,
  "kanzi::Node::setProperty" returns all setProperty variants.
- Include and import directives: get_include() â returns #include (C++),
  import (Java), using (C#), or use (Rust).
- Full class overview: get_class_reference() â shows all members at a glance,
  including inherited members labeled with their origin class.
- Deprecation check: get_deprecation_warnings() â check before using any API.
- Migration: compare_versions() â scope with class_name and change_type
  (added/removed/changed/deprecated) for focused diffs. Supports pagination
  with limit/offset.
- API evolution: get_api_history() â shows signature changes across all
  versions.

Naming conventions:
- C++ uses :: separators (kanzi::Node::setName).
- Java and C# use . separators (com.rightware.kanzi.Node).
- All tools accept optional language (cpp/java/csharp/lua/rust) and api
  parameters to narrow results.

Workflow:
- When writing Kanzi code, verify each API with get_method_signature()
  before using it.
- When migrating between versions, start with compare_versions(), then
  drill into changed APIs with get_api_history().
- After finding a class, use get_class_reference() to see available methods
  rather than guessing member names.
- Do not hallucinate Kanzi API signatures. Use these tools to verify.

```

## Kanzi API MCP tools reference

When you connect the Kanzi API MCP server to your AI assistant, the assistant gains access to these tools.
### list_apis

Lists available Kanzi versions, API sets, and the number of records in each. Shows which version is currently active and what other versions are available.
|

**Parameters** |

None. |
|

**Examples** |

```
# List all available Kanzi versions and API sets.
list_apis()

```
   |
### set_kanzi_version

Switches to a different Kanzi version for all subsequent queries.
|

**Parameters** |
|

`version` (required) |

Kanzi version string. For example, `3.9.15` or `4.0.0`. |      |
|

**Examples** |

```
# Switch to Kanzi 3.9.15.
set_kanzi_version(version="3.9.15")

```

```
# Switch to Kanzi 4.0.0.
set_kanzi_version(version="4.0.0")

```
   |
### search_kanzi_api

Searches Kanzi API documentation by keyword. Use this tool to find Kanzi classes, methods, properties, and types.
|

**Parameters** |
|

`query` (required) |

Search terms. For example, `Node setProperty`, `Button2D click`, or `Matrix4x4 multiply`. |
|

`n_results` |

Maximum number of results to return. Default: `5`. Maximum: `20`. |
|

`language` |

Language filter: `cpp`, `java`, `csharp`, `lua`, or `rust`. |
|

`member_type` |

Member type filter: `class`, `struct`, `interface`, `function`, `variable`, `enum`, or `typedef`. |
|

`api` |

API set filter. Use `list_apis` to see available sets. |      |
|

**Examples** |

```
# Find all classes related to RenderPass.
search_kanzi_api(query="RenderPass", member_type="class")

```

```
# Search for touch handling in the Java API.
search_kanzi_api(query="touch input", language="java", n_results=10)

```

```
# Find all enums in the C++ runtime API.
search_kanzi_api(query="enum", language="cpp", member_type="enum", n_results=20)

```
   |
### get_method_signature

Returns the exact signature of a Kanzi API member by name. Use this tool when you know the specific API and need its exact parameters, return type, and deprecation status. Also finds overloads through prefix matching.
|

**Parameters** |
|

`name` (required) |

API member name, either short (`setProperty`, `Node`) or fully-qualified (`kanzi::Node::setProperty`, `com.rightware.kanzi.Node`). C++ uses `::` separators, Java and C# use `.` separators. |
|

`language` |

Language filter: `cpp`, `java`, `csharp`, `lua`, or `rust`. |
|

`api` |

API set filter. Use `list_apis` to see available sets. |      |
|

**Examples** |

```
# Get the exact signature of a fully-qualified C++ method.
get_method_signature(name="kanzi::Node::setProperty")

```

```
# Find all overloads of addChild in C++.
get_method_signature(name="kanzi::Node::addChild", language="cpp")

```

```
# Look up a Java method by short name.
get_method_signature(name="setName", language="java")

```
   |
### get_include

Returns the correct include directive for a Kanzi type: `#include` for C++, `import` for Java, `using` for C#, or `use` for Rust.
|

**Parameters** |
|

`name` (required) |

Class or type name. For example, `Node`, `Button2D`, `Matrix4x4`, or `PropertyType`. |
|

`language` |

Language filter: `cpp`, `java`, `csharp`, `lua`, or `rust`. |
|

`api` |

API set filter. Use `list_apis` to see available sets. |      |
|

**Examples** |

```
# Get the C++ include directive for Button2D.
get_include(name="Button2D", language="cpp")

```

```
# Get the Java import statement for Node.
get_include(name="Node", language="java")

```
   |
### get_class_reference

Returns a complete reference for a Kanzi class with all public methods, properties, and enums. Includes inherited members from parent classes and interfaces.
|

**Parameters** |
|

`name` (required) |

Class name with or without namespace. For example, `Node`, `Button2D`, `kanzi::Node`, or `Matrix4x4`. |
|

`language` |

Language filter: `cpp`, `java`, `csharp`, `lua`, or `rust`. |
|

`api` |

API set filter. Use `list_apis` to see available sets. |      |
|

**Examples** |

```
# Get all members of the Node class in C++.
get_class_reference(name="kanzi::Node", language="cpp")

```

```
# Get the Java Button2D class reference.
get_class_reference(name="Button2D", language="java")

```

```
# Get the Lua API for Node.
get_class_reference(name="Node", language="lua")

```
   |
### get_deprecation_warnings

Checks whether a Kanzi API member is deprecated and returns the replacement. Use this tool before using any API that you suspect might be outdated.
|

**Parameters** |
|

`name` (required) |

Class or member name to check. For example, `Node`, `setProperty`, or `kanzi::Node::setFocusable`. |
|

`language` |

Language filter: `cpp`, `java`, `csharp`, `lua`, or `rust`. |
|

`api` |

API set filter. Use `list_apis` to see available sets. |      |
|

**Examples** |

```
# Check whether the Page class is deprecated.
get_deprecation_warnings(name="kanzi::Page", language="cpp")

```

```
# Check deprecation status of a specific method.
get_deprecation_warnings(name="kanzi::Node::setFocusable")

```
   |
### compare_versions

Compares Kanzi APIs between two versions to find what changed. Use this tool for migration guidance. Shows APIs that were added, removed, changed, or deprecated between two versions.
|

**Parameters** |
|

`from_version` (required) |

Source version. For example, `3.9.12`. |
|

`to_version` (required) |

Target version. For example, `4.0.0`. |
|

`language` |

Language filter: `cpp`, `java`, `csharp`, `lua`, or `rust`. |
|

`api` |

API set filter. Use `list_apis` to see available sets. |
|

`member_type` |

Member type filter: `class`, `function`, `variable`, `enum`, `struct`, `interface`, or `typedef`. |
|

`class_name` |

Scope the comparison to a single class. For example, `Node`. |
|

`change_type` |

Filter by type of change: `added`, `removed`, `changed`, or `deprecated`. |
|

`limit` |

Maximum number of results per category. Default: `50`. Maximum: `200`. |
|

`offset` |

Pagination offset for results. Default: `0`. |      |
|

**Examples** |

```
# Show all C++ API changes between two versions.
compare_versions(from_version="3.9.8", to_version="4.0.0", language="cpp")

```

```
# Show only removed APIs in the Node class between two versions.
compare_versions(from_version="3.9.13", to_version="4.0.0", class_name="Node", change_type="removed")

```

```
# Show newly deprecated Java APIs between two versions.
compare_versions(from_version="3.9.9", to_version="3.9.12", language="java", change_type="deprecated")

```
   |
### get_api_history

Shows how a specific Kanzi API member evolved across all loaded versions. Use this tool to track when an API was introduced, its signature changed, or it was deprecated or removed.
|

**Parameters** |
|

`fqn` (required) |

Fully-qualified name. For example, `kanzi::Node::setProperty`. |
|

`language` |

Language filter: `cpp`, `java`, `csharp`, `lua`, or `rust`. |
|

`api` |

API set filter. Use `list_apis` to see available sets. |      |
|

**Examples** |

```
# Track how a C++ method evolved across all versions.
get_api_history(fqn="kanzi::Node::trySetFocus", language="cpp")

```

```
# Track the history of ResourceManager::acquireResource.
get_api_history(fqn="kanzi::ResourceManager::acquireResource")

```
   |
