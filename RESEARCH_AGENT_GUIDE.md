# Enhanced Financial Research Agent

## Overview

Your research agent now uses the **EnhancedFinancialResearcher class** and focuses on the **last 1 month of data** from September 20, 2025 (searching from August 21 - September 20, 2025) and prioritizes **reliable financial sources**, especially **CNBC**.

## Key Improvements

### 🎯 Time-Focused Research
- **Automatic date filtering**: Only searches for information from the last 30 days
- **Current date awareness**: Set to September 20, 2025
- **Time-sensitive priority**: Focuses on breaking news, recent earnings, and market movements

### 📰 Reliable Source Prioritization
1. **CNBC** (cnbc.com) - Primary source
2. **Bloomberg** (bloomberg.com)
3. **Reuters** (reuters.com)
4. **MarketWatch** (marketwatch.com)
5. **Wall Street Journal** (wsj.com)

### 🔍 Enhanced Class Features
- **EnhancedFinancialResearcher class** with specialized methods
- **Template-based queries** for common research tasks
- **Flexible search options** (CNBC-only, multi-source, custom timeframes)
- **Source validation** and reliability checking

## Usage Examples

### Basic Agent Usage (Backward Compatible)
```python
from stock_research_adk.researcher_agent import root_agent

# The agent automatically applies date filtering and source prioritization
result = root_agent.run("Research Apple stock performance")
```

### Enhanced Class Usage (Recommended)
```python
from stock_research_adk.researcher_agent import (
    enhanced_researcher,
    get_enhanced_researcher,
    EnhancedFinancialResearcher
)

# Use the pre-configured instance
researcher = get_enhanced_researcher()

# Advanced search methods
apple_query = researcher.search_stock_info("AAPL", "earnings")
cnbc_query = researcher.search_cnbc_only("market outlook", "week")
templates = researcher.get_available_templates()

# Create new instances
new_researcher = EnhancedFinancialResearcher()
```

### Helper Functions
```python
from stock_research_adk.researcher_agent import (
    search_recent_stock_news,
    search_cnbc_only,
    build_focused_search_query
)

# Get optimized search query for a specific stock
apple_query = search_recent_stock_news("AAPL")
# Result: "AAPL stock news earnings analyst rating (site:cnbc.com OR site:bloomberg.com...) after:2025-08-21 before:2025-09-20"

# Search only CNBC
cnbc_query = search_cnbc_only("market outlook September 2025")
# Result: "market outlook September 2025 site:cnbc.com after:2025-08-21 before:2025-09-20"

# Build custom focused query
custom_query = build_focused_search_query("IPO new listings", date_range="week")
```

### Enhanced Methods Available

#### Search Methods
```python
researcher = get_enhanced_researcher()

# Stock-specific search with templates
query = researcher.search_stock_info("TSLA", "earnings")

# CNBC-only search with timeframe options
cnbc_query = researcher.search_cnbc_only("AI stocks", "week")

# Get all available query templates
templates = researcher.get_available_templates()
```

#### Available Templates
- `stock_analysis`: Stock price, earnings, analyst ratings
- `ipo_research`: IPO and new listing information
- `market_news`: General market trends and outlook
- `earnings`: Quarterly results and guidance
- `analyst_coverage`: Price targets and ratings
- `insider_trading`: Insider buying/selling activity
- `institutional_activity`: Hedge fund and institutional moves

## Search Query Examples

The agent now automatically generates queries like these:

### Enhanced Stock Research
```
AAPL earnings report quarterly results guidance after:2025-08-21 before:2025-09-20 (site:cnbc.com OR site:bloomberg.com OR site:reuters.com)
```

### CNBC-Focused Search
```
market outlook after:2025-09-13 before:2025-09-20 (site:cnbc.com)
```

### Multi-Template Query
```
NVDA analyst price target rating buy sell hold after:2025-08-21 before:2025-09-20 (site:cnbc.com OR site:bloomberg.com...)
```

## Agent Architecture

The enhanced agent now uses a proper class structure:

```python
class EnhancedFinancialResearcher:
    def __init__(self):
        self.agent = Agent(...)  # Core ADK agent
    
    def search_stock_info(self, symbol, search_type):
        # Template-based stock research
    
    def search_cnbc_only(self, query, timeframe):
        # CNBC-specific searches
    
    def get_available_templates(self):
        # Access to all query templates
```

## File Structure

```
stock_research_adk/
├── __init__.py              # Enhanced exports
├── agent.py                 # ADK agent loader
├── .env                     # Environment configuration
└── researcher_agent/
    ├── __init__.py          # Enhanced exports
    ├── agent.py             # EnhancedFinancialResearcher class
    └── utils.py             # Utility functions and templates
```

## Benefits

1. **Class-Based Architecture**: Proper OOP design with specialized methods
2. **Template System**: Pre-built queries for common research tasks
3. **Flexible Search Options**: Multiple ways to search (basic, enhanced, CNBC-only)
4. **Source Validation**: Built-in reliability checking
5. **Time-Focused**: Always gets the most recent financial information
6. **Backward Compatible**: Existing code still works with `root_agent`

## Testing

You can test the agent functionality by importing and using the components directly:
```python
from stock_research_adk.researcher_agent import enhanced_researcher

# Test enhanced methods
query = enhanced_researcher.search_stock_info("AAPL", "earnings")
print(query)
```

The agent provides:
- Basic agent usage
- Enhanced class methods
- Helper functions
- Advanced search building
- New instance creation

Your research agent now uses the **EnhancedFinancialResearcher class** for maximum flexibility and functionality!