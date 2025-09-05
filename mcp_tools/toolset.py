from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

BIO_MCP_BASE_URL = "http://localhost:8000/"

pubmed_mcp = MCPToolset(
    connection_params=StreamableHTTPServerParams(
        url=BIO_MCP_BASE_URL + "pubmed",
    )
)

plasmodb_mcp = MCPToolset(
    connection_params=StreamableHTTPServerParams(
        url=BIO_MCP_BASE_URL + "plasmodb",
    )
)

quickgo_mcp = MCPToolset(
    connection_params=StreamableHTTPServerParams(
        url=BIO_MCP_BASE_URL + "quickgo",
    )
)
