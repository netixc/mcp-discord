"""Discord integration for Model Context Protocol."""

from . import server
import asyncio
import warnings
import tracemalloc

__version__ = "0.1.0"


def main():
    """Main entry point for the package."""
    # Enable tracemalloc for better debugging
    tracemalloc.start()

    # Suppress PyNaCl warning since we don't use voice features
    warnings.filterwarnings(
        "ignore", module="discord.client", message="PyNaCl is not installed"
    )

    try:
        # Properly handle async execution
        asyncio.run(server.main())
    except KeyboardInterrupt:
        print("\nShutting down Discord MCP server...")
    except Exception as e:
        print(f"Error running Discord MCP server: {e}")
        raise


# Expose important items at package level
__all__ = ["main", "server"]
