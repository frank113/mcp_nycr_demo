# NYC HackR MCP Demo

## Setup

Step 1: Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

Step 2: Set up un environment:

```sh
uv python install 3.12
uv python pin 3.12
uv venv --python 3.12
source .venv/bin/activate
uv sync
```

Optional:

Install [nvm](https://github.com/nvm-sh/nvm)

Step 4: Install node packages

```sh
npm install .
```

## Run

To run the client / server pairing use the following command:

```sh
uv run client.py servers/tutorial.py
```


To inspect:

```shell
npx @modelcontextprotocol/inspector python weather.py

```

Then to run the inspection:

```shell
uv run mcp dev weather.py
```


