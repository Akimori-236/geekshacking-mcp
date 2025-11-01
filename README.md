# geekshacking-mcp

The workshop assumes that you are familiar with Python.

Software Installation

    Python - please install or upgrade your Python runtime to 3.12 or greater

    There are different installation options for Mac and Windows. Please use the distribution you are familiar with

    NodeJS - Version 22 or greater

    https://nodejs.org/en/download

    Git
    uv - Extremely fast Python package and project manager

    https://docs.astral.sh/uv/getting-started/installation/

    An IDE or editor capable of editing Python source

    The workshop will be conducted using Visual Studio Code (https://code.visualstudio.com/download)

Setup
Python Environment

Use the distribution you have installed to create a Python environment for the workshop eg, with Conda or virtualenv. Activate the environment after creating and check the Python version (3.12.x), either with

        python --version

or

        python3 --version

You should see an output similar to the following

Node Environment

Open a terminal and type the following commands to verify that NodeJS has been installed

Git

Note: You may skip this step if you have git installed

If you do not have a public Git repository, go to GitHub or GitLab to create one.

Configure Git with your username and email

        git config --global user.name "Your Name"

        git config --global user.email your_email@example.com

Visual Studio Code

If you are using VSC, please install the following extension

    Python - https://marketplace.visualstudio.com/items?itemName=ms-python.python
    Python Debugger - https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy
    Python Environment - https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-python-envs
    Pylance - https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
    Cline - https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev

Cline

After installing Cline, restart VSC and click on the Cline icon on the left menu bar. Follow the instructions to sign up for Cline. See https://docs.cline.bot/getting-started/installing-cline.

You will now need to configure an LLM provider. See https://docs.cline.bot/getting-started/selecting-your-model.

You can use the free models or configure an alternative provider. See the notice box regarding 'Free Models', which is subject to the free credits. My advice is to use the alternative provider so that you will not be disrupted when you run out of the free credits. Use either OpenAI, Gemini or Anthropic by funding the minimum amount (USD 5). Once you have funded your LLM account, create an API key and add it to Cline. See https://docs.cline.bot/getting-started/selecting-your-model#quick-start%3A-choose-your-provider.

Workshop Workspace

Create a directory for this workshop eg geekshacking-mcp

Copy the following file into the workshop directory

https://drive.google.com/file/d/1agUEwpR5Za9z6ljb4_ZO3md6KXM8M-g9/view?usp=drive_link

Initialise the directory as a Git repo, commit the changes and push it to your favourite Git repository.

## RUN - UVX

`uvx --from "git+https://github.com/Akimori-236/geekshacking-mcp.git" todo_mcp`

## RUN

- `fastmcp dev todo_mcp.py` for MCP inspector site
- `fastmcp run todo_mcp.py`
