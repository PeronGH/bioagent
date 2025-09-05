from google.adk.agents import SequentialAgent
from .gene_scanner import gene_scanner_agent
from .go_term_extractor import go_term_extractor_agent

root_agent = SequentialAgent(
    name="pipeline_agent", sub_agents=[gene_scanner_agent, go_term_extractor_agent]
)
