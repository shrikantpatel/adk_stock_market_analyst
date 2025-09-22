from .agent import (
    root_agent, 
    enhanced_researcher,
    EnhancedFinancialResearcher,
    create_researcher
)

# Easy access function for dynamic searches
def smart_search(query: str):
    """
    Perform a smart search that automatically detects timeframe from query
    
    Args:
        query (str): Search query (can include timeframe like "last 7 days")
        
    Returns:
        str: Search result with automatically applied timeframe
        
    Examples:
        smart_search("AAPL stock news last 7 days")
        smart_search("Tesla earnings from past 2 weeks") 
        smart_search("Microsoft data yesterday")
    """
    return enhanced_researcher.search(query)

__all__ = [
    'root_agent',
    'enhanced_researcher', 
    'EnhancedFinancialResearcher',
    'create_researcher',
    'smart_search'
]