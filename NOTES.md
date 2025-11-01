# MCP

- agents - autonomous software - might or might not have AI

## Alpha Go

- monte carlo tree search - to search for move options
- policy network
  - find best moves
- value network
  - solution space too big
  - find when to stop

## SMOL agent?

## MCP SERVER

- mcp server
  - exposes tools for agents to use
- mcp clients / host
  - uses the mcp server
  - intelligence is here

based on json rpc

## uv

- uv init
  - create venv, lock file, and toml file
- uv sync
  - replaces pip install -r requirements.txt

## python linter

- ruff - linter
- astral pyx
- ty - type checker <- pylance

## PRIMITIVES

- TOOLS (model-controlled - LLM decides when to use)
  - function for the model to use/call
  - can have structured data
  - can provide RESOURCEs and PROMPTs
- RESOURCE (application-controlled - host/IDE determines what to serve)
  - data that the MCP can use
- PROMPT (user-controlled)
  - instructions (system)

(uncommon ones)

- SAMPLING (dangerous)
  - allows MCP server to use LLM
  - send resources to model to categorise yes/no
  - exposes alot more data than requested
- ELICITATION
  - allows long running interactive workflows
- ROOTS
  - dynamic, can change
  - defines restrictions categories of resources that it can access
