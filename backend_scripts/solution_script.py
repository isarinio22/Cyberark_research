# solution_script.py
# This script would handle information about the 'Our Solution' section.
# It could provide details on the Adaptive Identity Guardian's core offerings.

def get_solution_details():
    """
    Provides details about the Adaptive Identity Guardian solution.
    """
    print("Retrieving Adaptive Identity Guardian solution details...")
    return {
        "name": "Adaptive Identity Guardian",
        "type": "Cloud-native, AI-powered IGA and PAM platform",
        "value_proposition": "Enterprise-grade identity security with unparalleled simplicity, transparent pricing, and proactive automation."
    }

if __name__ == "__main__":
    details = get_solution_details()
    print(f"Solution: {details['name']}")
    print(f"Type: {details['type']}")
    print(f"Value Proposition: {details['value_proposition']}")
