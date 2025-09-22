# ADK Agent Loader - Main entry point for the stock research agent
# This file is required by ADK to locate the root_agent

from .researcher_agent.agent import root_agent

# Expose root_agent at the expected location
__all__ = ['root_agent']