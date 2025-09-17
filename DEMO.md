# Demo

First we will examine the `client.py` file. Notice that this file is actually the application host and the 

Next we will use the dev tool to inspect a server. **Remember to activate your uv and nvm environments**.

```sh
nvm use
source .venv/bin/activate
```

```sh
npx @modelcontextprotocol/inspector python servers/tutorial.py
```

We can see an example of the payloads that are used.

We can now run the client / server combination. 

```sh
uv run client.py servers/server.py
```

In case it does not format we can look at the below block:

```md

initializing MCP Client
[09/17/25 17:33:26] INFO     Processing request of type ListToolsRequest                                     server.py:624

Connected to server with tools: ['get_lat_long']

MCP Client Started!
Type your queries or 'quit' to exit.

Query: What is the latitude and longitude of Seton Hall Prep?
[09/17/25 17:33:36] INFO     Processing request of type ListToolsRequest                                     server.py:624
                    INFO     Processing request of type ListResourcesRequest                                 server.py:624
meta=None nextCursor=None resources=[]
TextBlock(citations=None, text="I'll help you find the latitude and longitude coordinates for Seton Hall Prep.", type='text')
ToolUseBlock(id='toolu_01WjDge7AFB1oeRa6oBeezJk', input={'place': 'Seton Hall Prep'}, name='get_lat_long', type='tool_use')
[09/17/25 17:33:39] INFO     Processing request of type CallToolRequest                                      server.py:624

I'll help you find the latitude and longitude coordinates for Seton Hall Prep.
[Calling tool get_lat_long with args {'place': 'Seton Hall Prep'}]
The latitude and longitude of Seton Hall Prep are:

**Latitude:** 40.7747901
**Longitude:** -74.2473224

These coordinates place the school in West Orange, New Jersey, where Seton Hall Preparatory School is located.

Query: 
```