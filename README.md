# Discord MCP Server

A Model Context Protocol (MCP) server that provides Discord integration capabilities to AI agents like Goose, Claude Desktop, and other MCP clients.

## Features

The Discord MCP Server provides a comprehensive set of tools for interacting with Discord servers:

### Server Information
- `get_server_info`: Get detailed server information including channels, categories, and settings
- `list_members`: List server members with their roles and other details

### Message Management
- `send_message`: Send messages to any channel
- `read_messages`: Read message history with reaction information
- `add_reaction`: Add reactions to messages
- `add_multiple_reactions`: Add multiple reactions at once
- `remove_reaction`: Remove specific reactions
- `moderate_message`: Delete messages and optionally timeout users

### Channel Management
- `create_text_channel`: Create new text channels
- `delete_channel`: Delete existing channels
- `create_thread`: Create threads from messages or as standalone
- `set_channel_permissions`: Configure channel permissions for roles
- `create_category`: Create new channel categories

### Role Management
- `create_role`: Create new server roles with customizable settings
- `delete_role`: Remove existing roles
- `list_roles`: Get a list of all server roles
- `add_role`: Assign roles to users
- `remove_role`: Remove roles from users

### User Management
- `get_user_info`: Get detailed information about users
- `kick_user`: Kick users from the server
- `ban_user`: Ban users with optional message deletion

## Installation

1. Clone and set up the environment:
```
# Clone the repository
git clone https://github.com/netixc/mcp-discord.git
cd mcp-discord

# Create and activate virtual environment
uv venv
.venv\Scripts\activate

### If using Python 3.13+ 
uv pip install audioop-lts

# Install the package
uv pip install -e .
```

2. Configure Claude Desktop 
    (%APPDATA%\Claude\claude_desktop_config.json on Windows, 
    ~/Library/Application Support/Claude/claude_desktop_config.json on macOS).

```
    "discord": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\PATH\\TO\\mcp-discord",
        "run",
        "mcp-discord"
      ],
      "env": {
        "DISCORD_TOKEN": "your_bot_token"
        "DEFAULT_SERVER_ID": "your_default_server_id"  # Optional
      }
    }
```


## License

MIT License - see LICENSE file for details.
