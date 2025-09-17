import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
// Creates the metadata for the
const server = new McpServer({
  name: "demo-server",
  version: "1.0.0"
});

const additionProperties = {
    title: "Addition Tool",
    description: "Add two numbers",
    inputSchema: { a: z.number(), b: z.number() }
};
const addFnDefinition = function(a, b) {
  return String(a, b)
}
// Add an addition tool
server.registerTool("add",
  additionProperties,
  async ({ a, b }) => ({
    content: [{ type: "text", text: addFnDefinition(a, b) }]
  })
);

// Add a dynamic greeting resource
server.registerResource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  {
    title: "Greeting Resource",      // Display name for UI
    description: "Dynamic greeting generator"
  },
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
await server.connect(transport);