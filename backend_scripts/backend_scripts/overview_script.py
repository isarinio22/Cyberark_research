# overview_script.py
# This script would handle data or logic related to the 'Overview' section of the landing page.
# For example, fetching high-level statistics or introductory content.

def get_overview_data():
    """
    Fetches high-level overview data for the Adaptive Identity Guardian service.
    """
    print("Fetching Adaptive Identity Guardian overview data...")
    return {
        "title": "Adaptive Identity Guardian: Securing the Mid-Market Frontier",
        "description": "A cloud-native, AI-powered IGA and PAM platform designed to deliver enterprise-grade identity security with unparalleled simplicity, transparent pricing, and proactive automation for mid-market enterprises."
    }

if __name__ == "__main__":
    data = get_overview_data()
    print(data)
