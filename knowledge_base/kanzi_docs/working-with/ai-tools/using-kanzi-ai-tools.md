---
title: Using Kanzi AI tools
source: https://docs.kanzi.com/4.1.0/en/working-with/ai-tools/using-kanzi-ai-tools.html
---

# Using Kanzi AI tools

Kanzi provides AI tools that help you find information, understand Kanzi concepts and APIs, and get unblocked faster:

- **Ask Kanzi** is the AI assistant built into the Documentation at https://docs.kanzi.com without any extra setup, just click the Ask Kanzi button at the top right of any documentation page to open it.
- **MCP servers** connect your own AI coding agent, such as Claude Code, VS Code, Cursor, and similar, to the same underlying Documentation and API references. Useful when you want to query Kanzi from inside your editor or agent.

## Quick setup

The fastest way to use Kanzi from your own AI coding agent is to let the agent set itself up. Paste this into your agent:

```
Fetch https://docs.kanzi.com/agent-setup/prompt.md and follow it.

```

The agent reads the instructions and registers both Kanzi MCP servers for you, with no manual configuration. This works with Claude Code, VS Code, Cursor, Windsurf, Codex, and any other tool that supports MCP.

When the agent finishes, start a new chat if your tool needs it. Then ask a Kanzi question to confirm the tools respond, for example âUsing the Kanzi docs tools, how do data sources work in Kanzi 4.1?â.

To configure the servers yourself instead, see MCP servers below.
## Ask Kanzi

Ask Kanzi is grounded in the Documentation and API references, so it answers from verified content rather than from general training data. You can ask conceptual questions (âHow do data sources work?â), how-to questions (âHow do I bind a property to a data source value?â), API questions (âWhat is the signature of `kanzi::Node::setProperty` in Kanzi 4.1?â), or migration questions (âWhat changed in render passes between Kanzi 3.9.15 and 4.0.0?â).

Key things to know:

- **Page context.** When you open Ask Kanzi from a documentation page, Ask Kanzi automatically uses that page as context, so you can ask follow-up questions about it without copy-pasting. Ask Kanzi shows the current page as a pill above the chat input. Click the Ã on the pill to remove the page from the context.
- **Selection context.** Select any text on the page before opening Ask Kanzi, and that selection becomes additional context. This is useful when you want to ask about a specific code snippet, table cell, or paragraph.
- **Version.** Ask Kanzi grounds its answer in the Kanzi version that matches the documentation page you opened it from.
- **Sources.** Each answer lists the documentation pages it was based on. Click a source to open it in a new tab and verify the answer in context.
- **Find in chat.** In the panel header, click the magnifier glass icon and type to find text in the current conversation. Use the up and down arrows (or Enter and Shift+Enter) to step through found terms. Press Esc or click the close button to clear the highlights.
- **New chat.** In the panel header, click the pencil icon to clear the current conversation and start a new chat.

For details on how to use search across the same documentation, see Searching Documentation.
## MCP servers

Kanzi MCP servers are built on the [Model Context Protocol](https://modelcontextprotocol.io/) (MCP), an open standard for connecting AI assistants to external tools and data sources. After you connect a Kanzi MCP server to your AI assistant, the assistant can use the tools that the server provides to look up Kanzi information and answer your questions.

Kanzi provides two public MCP servers. They require no authentication and serve every Kanzi version (you switch versions from within the tools):

- Kanzi documentation MCP server at `https://docs.mcp.kanzi.com/mcp` connects your AI assistant to the Kanzi documentation. Use it to get answers about Kanzi concepts, features, workflows, and best practices.
- Kanzi API MCP server at `https://api.mcp.kanzi.com` connects your AI assistant to the Kanzi API reference. Use it to look up API signatures, check deprecation status, find include directives, and compare APIs between Kanzi versions.

The quickest way to add both servers is the one-step Quick setup above. To add a server yourself, use your toolâs MCP configuration:
|

AI tool |

How to add a server |
|

Claude Code |

Run `claude mcp add --scope user --transport http <name> <url>`. |
|

VS Code |

Add the server to `mcp.json` (open it with **MCP: Open User Configuration**). |
|

Cursor |

Add the server to `~/.cursor/mcp.json`. |
|

Windsurf |

Add the server to `~/.codeium/windsurf/mcp_config.json`. |
|

Codex, or any other MCP tool without direct HTTP support |

Bridge the server with `npx -y mcp-remote <url>`. |

Use `https://docs.mcp.kanzi.com/mcp` as `<url>` for the documentation server and `https://api.mcp.kanzi.com` for the API server. For the full step-by-step configuration in each tool, see Kanzi Documentation MCP server and Kanzi API MCP server.
## Tips for working with Kanzi AI tools

- Be specific in your questions. For example, instead of asking âHow do bindings work?â, ask âHow do I create a binding in Kanzi Studio that changes the color of a node based on a data source value?â.
- When asking about API use, mention the programming language and Kanzi version that you are using.
- You can ask for verification of API signatures, check for deprecations, and suggest replacements for deprecated APIs.
- When migrating between Kanzi versions, use the Kanzi API MCP server with your AI assistant to compare APIs between versions. This helps you identify what changed and estimate the migration effort.
