#!/usr/bin/env python3
"""
Example usage of the ADK Stock Research Agent with Poetry
"""

from stock_research_adk import root_agent
from stock_research_adk.researcher_agent import enhanced_researcher, create_researcher

def main():
    """Main example function"""
    print("🚀 ADK Stock Research Agent - Poetry Setup")
    print("=" * 50)
    
    # Example 1: Using the default agent
    print("\n📊 Default Agent (30 days):")
    print(f"Agent name: {root_agent.name}")
    print(f"Model: {root_agent.model}")
    
    # Example 2: Using enhanced researcher directly
    print(f"\n🔬 Enhanced Researcher:")
    print(f"Current timeframe: {enhanced_researcher.timeframe_days} days")
    
    # Example 3: Creating custom timeframe researcher
    print(f"\n⚡ Custom Researcher (7 days):")
    weekly_researcher = create_researcher(7)
    print(f"Weekly researcher timeframe: {weekly_researcher.timeframe_days} days")
    
    # Example 4: Manual timeframe adjustment
    print(f"\n🔧 Adjusting timeframe:")
    enhanced_researcher.set_timeframe(14)
    print(f"Updated timeframe: {enhanced_researcher.timeframe_days} days")
    
    print("\n✅ All examples completed successfully!")
    print("📝 Your agent is ready to use with Poetry!")

if __name__ == "__main__":
    main()