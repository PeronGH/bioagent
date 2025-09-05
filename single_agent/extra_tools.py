from google.adk.tools.tool_context import ToolContext


def submit_success(content: str, tool_context: ToolContext):
    print(f"[SUCCESS]{content}")


def submit_error(reason: str, tool_context: ToolContext):
    print(f"[ERROR]{reason}")
