# market_script.py
# This script would handle market analysis data for the 'Market Opportunity' section.
# It could provide market size, growth projections, and ROI justifications.

def get_market_data():
    """
    Retrieves market opportunity data for mid-market enterprises.
    """
    print("Analyzing market opportunity data...")
    return {
        "segment": "Mid-market enterprises (100-2,000 employees, $10M-$1B revenue)",
        "iga_cagr": "13.38% - 14.24% by 2032",
        "pam_cagr": "21.4% - 23.1% by 2033",
        "roi_example": "Average $816,000 annual savings from PAM solutions."
    }

if __name__ == "__main__":
    market_data = get_market_data()
    print(f"Target Segment: {market_data['segment']}")
    print(f"IGA Market CAGR: {market_data['iga_cagr']}")
    print(f"PAM Market CAGR: {market_data['pam_cagr']}")
    print(f"Example ROI: {market_data['roi_example']}")
