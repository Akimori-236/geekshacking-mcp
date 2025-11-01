from fastmcp import FastMCP
from todo_db import TodoDB  # our fake database
from typing import Annotated, NamedTuple

# Load the fake DB
todo_db = TodoDB()
todo_db.sample_data()


# instead of BaseModel
class Todo(NamedTuple):
    filename: Annotated[str, "Source file containing the #TODO"]
    text: Annotated[str, "Text of the #TODO"]
    line_num: Annotated[int, "Line number in the source file of the #TODO"]


# Create the MCP server
# creating & naming the server (some clients dont allow spaces in names)
mcp = FastMCP("TODO_MCP")


# TOOLS
# name the tool and describe what it does
@mcp.tool(
    name="tool_add_todo",
    description="Add a single #TODO text from a source file",
)
# most mcps to
def add_todo(
    filename: Annotated[str, "Source file containing the #TODO"],
    text: Annotated[str, "Text of the #TODO"],
    line_num: Annotated[int, "Line number in the source file of the #TODO"],
) -> bool:
    return todo_db.add(
        filename=filename,
        text=text,
        line_num=line_num,
    )


@mcp.tool(
    name="tool_batch_add_todos",
    description="Add a list of #TODO from a source file",
)
def add_todos(todos: list[Todo]) -> int:
    for todo in todos:
        todo_db.add(todo[0], todo[1], todo[2])
    return len(todos)


# RESOURCE
@mcp.resource(
    name="resource_get_todo_for_file",
    description="Get all todo texts for a file. Returns empty array if source file does not exist, or if there are no #TODOs in the file",
    # parameterised route - does not support query strings
    uri="todo://{filename}/todos",
)
def get_todos_for_file(
    filename: Annotated[str, "Source file containing the #TODO"],
) -> list[str]:
    todos = todo_db.get(filename=filename)
    # returning all the todo texts, keys are the line numbers
    return [text for text in todos.values()]


# Start the MCP
def run():
    mcp.run()


if __name__ == "__main__":
    run()
