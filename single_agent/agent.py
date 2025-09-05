import json
from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner
from google.adk.models.lite_llm import LiteLlm
from google.genai import types
from mcp_tools import pubmed_mcp, plasmodb_mcp, quickgo_mcp
from .model import Output
from .extra_tools import submit_success, submit_error

AGENT_MODEL = LiteLlm(model="anthropic/claude-sonnet-4-20250514")

root_agent = LlmAgent(
    name="BioAgent",
    instruction=f"""You are a bioinformatics agent that annotates PubMed articles by identifying genes and their associated GO terms.

**Task:** Given a PMID, extract genes mentioned in the article and annotate them with relevant Gene Ontology (GO) terms based on the functional evidence described in the paper.

**Step-by-Step Process:**

1. **Text Retrieval:** Fetch and analyze the full text of the provided PMID.

2. **Gene Identification:** 
   - Extract genes explicitly mentioned in the article
   - Use biological context to identify relevant genes not explicitly named
   - Search PlasmoDB using multiple query strategies:
     * Exact gene names/IDs
     * Name variations (remove hyphens, try synonyms)
     * Gene products or functional descriptions
   - Skip genes that cannot be found after multiple search attempts

3. **GO Term Annotation:**
   - For each identified gene, extract relevant information from the article
   - Use QuickGO to find relevant GO terms matching the described biological processes, molecular functions, and cellular components
   - Ensure GO terms are supported by evidence described in the article
   - Refine terms by navigating the GO hierarchy, especially by checking child terms

**Output Requirements:**
- On error: Submit "error" with detailed reasoning
- On success: Submit "success" with results in this JSON format:
```json
{json.dumps(Output.model_json_schema(), indent=2)}
```

**Quality Standards:**
- GO terms must be directly supported by evidence in the article
- Ensure GO terms are extremely specific, avoiding general terms
- Use appropriate evidence codes to establish gene-function relationships
- Prioritize precision over recall (better to miss uncertain annotations than include incorrect ones)
""",
    model=AGENT_MODEL,
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
        ),
    ),
    tools=[pubmed_mcp, plasmodb_mcp, quickgo_mcp, submit_success, submit_error],
)
