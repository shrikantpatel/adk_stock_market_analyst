# ADK Stock Market Analyst

A powerful financial research agent using Google's Agent Development Kit (ADK) with enhanced search capabilities, CNBC prioritization, and flexible timeframe analysis.

## 🚀 Features

- **CNBC-Focused Research**: Prioritizes CNBC as primary source with fallback to Bloomberg, Reuters, etc.
- **Dynamic Timeframe Analysis**: Automatically detects and applies timeframes from user queries
- **Real-time Market Data**: Focuses on recent market developments and breaking news
- **Intelligent Source Ranking**: Uses reliable financial sources in order of preference
- **Sector-Specific Intelligence**: Tailored analysis for Tech, Financial, Healthcare, Energy sectors
- **Risk Assessment**: Highlights regulatory changes, management issues, and market disruptions

## 📦 Poetry Setup

This project uses **Poetry** for dependency management and packaging.

### Prerequisites
- Python 3.11+ (tested with 3.13.7)
- Poetry (install from [python-poetry.org](https://python-poetry.org/docs/#installation))
- Git

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shrikantpatel/adk_stock_market_analyst.git
   cd adk_stock_market_analyst
   ```

2. **Install dependencies with Poetry:**
   ```bash
   # Install all dependencies (creates virtual environment automatically)
   poetry install
   ```

3. **Activate the environment:**
   ```bash
   # Option 1: Activate shell
   poetry shell
   
   # Option 2: Run commands directly
   poetry run python your_script.py
   ```

4. **Test the setup:**
   ```bash
   poetry run python poetry_example.py
   ```

### Environment Details
- **Python Version**: 3.11+ (currently using 3.13.7)
- **Package Manager**: Poetry 2.2.1+
- **Main Dependencies**: 
  - `google-adk>=1.14.1`
  - `fastapi>=0.117.1`
  - `pydantic>=2.11.9`
  - `python-dotenv>=1.1.1`
  - Google Cloud AI Platform, GenAI, and Auth packages

## 🏗️ Project Structure
```
adk_stock_market_analyst/
├── pyproject.toml              # Poetry configuration
├── poetry.lock                 # Dependency lock file
├── poetry_example.py          # Usage example
├── stock_research_adk/        # Main package
│   ├── __init__.py
│   ├── agent.py               # Root agent exports
│   └── researcher_agent/      # Enhanced research agent
│       ├── __init__.py
│       └── agent.py           # Core agent implementation
└── README.md                  # This file
```

## 📊 Usage

### Basic Usage
```python
from stock_research_adk import root_agent
from stock_research_adk.researcher_agent import enhanced_researcher

# The agent automatically handles:
# - "Give me Apple stock news from the last 7 days"
# - "Show me Tesla earnings from yesterday"
# - "Find Microsoft data from past 2 weeks"
```

### Custom Timeframes
```python
from stock_research_adk.researcher_agent import create_researcher

# Create agents with specific timeframes
weekly_agent = create_researcher(7)      # 7 days
monthly_agent = create_researcher(30)    # 30 days (default)
quarterly_agent = create_researcher(90)  # 90 days

# Manual timeframe adjustment
enhanced_researcher.set_timeframe(14)    # 2 weeks
```

### Agent Capabilities
The agent automatically:
- **Detects timeframes** from natural language ("last week", "yesterday", "past month")
- **Prioritizes CNBC** while using multiple reliable financial sources
- **Applies date filtering** with dynamic date ranges
- **Provides risk assessment** and actionable insights
- **Cross-references sources** for accuracy

## 🛠️ Development

### Code Quality Tools
```bash
# Format code
poetry run black .

# Sort imports
poetry run isort .

# Type checking
poetry run mypy stock_research_adk/

# Linting
poetry run flake8 stock_research_adk/
```

### Testing
```bash
# Run tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=stock_research_adk
```

### Dependency Management
```bash
# Add runtime dependency
poetry add requests

# Add development dependency
poetry add --group dev pytest-mock

# Update dependencies
poetry update

# Remove dependency
poetry remove requests
```

## 🎯 Agent Features

### Search Intelligence
- **Source Prioritization**: CNBC → Bloomberg → Reuters → MarketWatch → WSJ
- **Date Filtering**: Automatic recent data focus with configurable timeframes
- **Sector Analysis**: Specialized knowledge for different market sectors
- **Breaking News**: Prioritizes recent developments and market-moving information

### Risk Assessment
- Regulatory changes and investigations
- Management changes or scandals
- Competitive threats and market disruption
- Economic indicators and geopolitical events
- Supply chain disruptions
- Currency fluctuations

### Response Quality
- Always mentions source and publication date
- Includes price movements and percentage changes
- Provides context for market movements
- Compares performance to sector peers
- Identifies potential future catalysts

## 📚 Documentation

- **[RESEARCH_AGENT_GUIDE.md](./RESEARCH_AGENT_GUIDE.md)** - Detailed agent capabilities and examples

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Install dependencies: `poetry install`
4. Make your changes
5. Run tests: `poetry run pytest`
6. Format code: `poetry run black . && poetry run isort .`
7. Commit changes: `git commit -m 'Add amazing feature'`
8. Push to branch: `git push origin feature/amazing-feature`
9. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🚀 Getting Started

Ready to analyze the markets? Run the example:

```bash
poetry run python poetry_example.py
```

Your enhanced financial research agent is ready to provide intelligent, CNBC-focused market analysis with dynamic timeframe detection! 📈