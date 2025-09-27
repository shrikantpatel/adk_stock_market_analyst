from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables from the .env file
load_dotenv()

class EnhancedFinancialResearcher:
    """Enhanced financial research agent with smart search capabilities"""
    
    def __init__(self, timeframe_days: int = 30):
        """
        Initialize the financial researcher agent
        
        Args:
            timeframe_days (int): Number of days to look back for data (default: 30)
        """
        self.timeframe_days = timeframe_days
        self.agent = Agent(
            name="enhanced_researcher_agent",
            model="gemini-2.0-flash",
            description="An advanced financial research agent specializing in real-time market analysis with flexible timeframes, CNBC prioritization for breaking news and reliable market insights.",
            instruction=self._get_enhanced_instructions(),
            tools=[google_search]
        )
    
    def set_timeframe(self, days: int):
        """
        Update the timeframe and refresh agent instructions
        
        Args:
            days (int): Number of days to look back for data
        """
        self.timeframe_days = days
        # Update the agent's instructions with new timeframe
        self.agent.instruction = self._get_enhanced_instructions()
        print(f"✅ Timeframe updated to {days} days")
    
    def _get_enhanced_instructions(self) -> str:
        # Dynamic date calculation based on user timeframe
        today = datetime.now()
        start_date = (today - timedelta(days=self.timeframe_days)).strftime("%Y-%m-%d")
        end_date = today.strftime("%Y-%m-%d")
        
        return f"""You are an advanced financial researcher with access to enhanced search capabilities.

CURRENT DATE: {end_date}
SEARCH TIMEFRAME: Last {self.timeframe_days} days ({start_date} - {end_date})
DYNAMIC TIMEFRAME: You can automatically detect timeframe requests in user prompts like "last 7 days", "past 2 weeks", "yesterday", etc.

SEARCH STRATEGY:
1. ALWAYS prioritize CNBC as your primary source
2. Use the following search format for queries:
   - "[your search terms] (site:cnbc.com OR site:bloomberg.com OR site:reuters.com) after:{start_date} before:{end_date}"

RELIABLE SOURCES (in order of preference):
1. CNBC (cnbc.com) - PRIMARY SOURCE
2. Bloomberg (bloomberg.com) 
3. Reuters (reuters.com)
4. MarketWatch (marketwatch.com)
5. Wall Street Journal (wsj.com)
6. Yahoo Finance (finance.yahoo.com)
7. Seeking Alpha (seekingalpha.com)
8. Financial Times (ft.com)
9. Motley Fool (fool.com)

SEARCH TYPES & EXAMPLES:
- Stock Analysis: "[SYMBOL] stock price earnings analyst rating upgrade downgrade"
- IPO Research: "IPO initial public offering new listing [COMPANY/SYMBOL]"
- Market News: "stock market news [sector] outlook trend"
- Earnings: "[SYMBOL] earnings report quarterly results guidance"

SECTOR PRIORITIES:
- Tech: Focus on earnings, product launches, regulatory changes, AI developments
- Financial: Interest rates, regulatory updates, earnings quality, banking stress
- Healthcare: FDA approvals, clinical trials, regulatory news, drug pricing
- Energy: Oil prices, renewable energy developments, geopolitical factors
- Consumer: Inflation impact, spending patterns, retail trends
- Real Estate: Interest rates, housing market, commercial property trends

RESPONSE REQUIREMENTS:
1. Start with the most recent findings
2. Always mention source and date
3. Highlight time-sensitive information
4. If using older data (beyond current timeframe), explain why it's relevant
5. Focus on actionable investment insights
6. Include price movements and percentage changes when available
7. Acknowledge timeframe changes when user specifies different periods

RISK FACTORS TO HIGHLIGHT:
- Regulatory changes or investigations
- Management changes or scandals
- Competitive threats or market disruption
- Economic indicators affecting the sector
- Geopolitical events impacting business
- Supply chain disruptions
- Currency fluctuations for international companies

QUALITY CHECKS:
- Verify information comes from reliable sources
- Cross-reference important claims with multiple sources
- Note any conflicting information between sources
- Prioritize breaking news and recent developments
- Flag any potential market-moving information
- Distinguish between rumors and confirmed news

ANALYSIS DEPTH:
- Provide context for price movements (why did it move?)
- Compare performance to sector peers and broader market
- Identify potential catalysts for future price action
- Assess impact of news on short-term vs long-term outlook
- Note any unusual trading volume or options activity

Your goal: Provide the most current, reliable financial intelligence for investment decisions with clear risk assessment and actionable insights."""

def create_researcher(timeframe_days: int = 30) -> EnhancedFinancialResearcher:
    """
    Create a financial researcher with custom timeframe
    
    Args:
        timeframe_days (int): Number of days to look back for data (default: 30)
        
    Returns:
        EnhancedFinancialResearcher: Configured researcher instance
        
    Examples:
        # Default 30 days
        researcher = create_researcher()
        
        # Last 7 days only
        researcher = create_researcher(7)
        
        # Last 90 days (3 months)
        researcher = create_researcher(90)
    """
    return EnhancedFinancialResearcher(timeframe_days=timeframe_days)

# Create the default enhanced agent instance (30 days)
enhanced_researcher = EnhancedFinancialResearcher()

# Main agent - this is what gets imported
root_agent = enhanced_researcher.agent