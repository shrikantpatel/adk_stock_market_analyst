# ADK Stock Market Analyst

A stock research and analysis tool using ADK (Agent Development Kit).

## Environment Setup

### Prerequisites
- Python 3.13.3 (or compatible version)
- Git

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd adk_stock_market_analyst
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # OR
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation:**
   ```bash
   python -c "import google_adk; print('Environment ready!')"
   ```

### Environment Details
- **Python Version**: 3.13.3
- **Main Dependencies**: 
  - `google-adk==1.14.1`
  - `fastapi==0.117.1`
  - `pydantic==2.11.9`
  - Google Cloud services (AI Platform, BigQuery, etc.)

## Project Structure
```
adk_stock_market_analyst/
├── stock_research_adk/
│   └── researcher_agent/
│       ├── __init__.py
│       └── agent.py
├── venv/
├── requirements.txt
└── README.md
```

## Usage
[Add usage instructions here]

## Development
[Add development guidelines here]