from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner
from google.genai import types
from mcp_tools import pubmed_mcp, quickgo_mcp

go_term_extractor_agent = LlmAgent(
    name="go_term_extractor",
    description="Extracts GO terms from a PubMed article using QuickGO.",
    instruction="""You are a bioinformatics agent that extracts GO terms from a PubMed article using QuickGO.
You will be provided with a PMID and a list of gene IDs and their descriptions.
Your task is to extract relevant GO terms for each gene based on the article's content.""",
    model="gemini-2.5-flash",
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
        ),
    ),
    tools=[pubmed_mcp, quickgo_mcp],
)
