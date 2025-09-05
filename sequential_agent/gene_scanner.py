from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner
from google.genai import types
from mcp_tools import pubmed_mcp, plasmodb_mcp

gene_scanner_agent = LlmAgent(
    name="gene_scanner",
    description="Scans full text of a pubmed article and uses PlasmoDB to identify gene IDs.",
    instruction="""You are a bioinformatics agent that scans the full text of a PubMed article and uses PlasmoDB to identify gene IDs.
You will be provided with a PMID. You will fetch the full text and look for potential genes mentioned in the article.
Sometimes the gene may not be explicitly mentioned, so you will need to use your knowledge and the tools at your disposal to identify relevant genes.
If a gene is mentioned but you cannot find it in PlasmoDB, try different variations of the query, for example, remove the hyphen. You can also try to search for its product or function.
For genes that you cannot find in PlasmoDB after multiple attempts, skip them.
""",
    model="gemini-2.5-flash",
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
        ),
    ),
    tools=[pubmed_mcp, plasmodb_mcp],
)
