# ADK Stock Research Package
# This file exposes the root_agent at the package level as required by ADK

from .researcher_agent.agent import root_agent, enhanced_researcher

# ADK looks for root_agent at this level
__all__ = ['root_agent', 'enhanced_researcher']