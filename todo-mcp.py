from fastmcp import FastMCP
from todo_db import TodoDB  # our fake database

# Load the fake DB
todo_db = TodoDB()
todo_db.sample_data()

# Create the MCP server
# creating & naming the server (some clients dont allow spaces in names)
mcp = FastMCP("TODO_MCP")











# Start the MCP
def run():
    mcp.run()


if __name__ == "__main__":
    run()
