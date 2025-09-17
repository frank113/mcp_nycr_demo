from mcp.server.fastmcp import FastMCP, Context
from mcp.server.fastmcp.prompts import base
import httpx

# Initialize the MCP server
mcp = FastMCP("GitHubAssistant")

# Resource: Fetch the README of a GitHub repository
@mcp.resource("github://repo/{owner}/{repo}/readme")
async def get_readme(owner: str, repo: str) -> str:
    """Retrieve the README content of a GitHub repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    headers = {"Accept": "application/vnd.github.v3.raw"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return f"Error fetching README: {response.status_code}"

# Tool: Analyze open issues in a GitHub repository
@mcp.tool()
async def analyze_issues(owner: str, repo: str) -> str:
    """Analyze open issues in a GitHub repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            issues = response.json()
            open_issues = [issue for issue in issues if issue.get("state") == "open"]
            return f"Repository '{owner}/{repo}' has {len(open_issues)} open issues."
        return f"Error fetching issues: {response.status_code}"

# Prompt: Review a code snippet
@mcp.prompt()
def review_code(code: str) -> list[base.Message]:
    """Provide a prompt for code review."""
    return [
        base.UserMessage("Please review the following code:"),
        base.UserMessage(code),
        base.AssistantMessage("Certainly! Here's my review:")
    ]

# Start the MCP server
if __name__ == "__main__":
    mcp.run()