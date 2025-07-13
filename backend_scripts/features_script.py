# features_script.py
# This script would manage data or logic for the 'Features' section.
# For example, listing key differentiators and their benefits.

def get_feature_list():
    """
    Lists the key features and differentiators of Adaptive Identity Guardian.
    """
    print("Loading Adaptive Identity Guardian features...")
    return [
        {"feature": "Transparent & Predictable Pricing", "benefit": "Eliminates hidden fees."},
        {"feature": "Simplified Setup & Low-Code Integrations", "benefit": "Reduces implementation time."},
        {"feature": "Unified Hybrid Identity Fabric", "benefit": "Seamless policy enforcement across environments."},
        {"feature": "Proactive AI-driven Posture Management", "benefit": "Predictive risk identification."},
        {"feature": "Automated Remediation & Self-Healing Identity", "benefit": "Reduces manual oversight."},
        {"feature": "Extended Audit & Forensic Capabilities", "benefit": "In-depth investigations and compliance."},
        {"feature": "Integrated, Simplified PAM", "benefit": "Ease of use and rapid deployment."},
    ]

if __name__ == "__main__":
    features = get_feature_list()
    print("Key Features:")
    for item in features:
        print(f"- {item['feature']}: {item['benefit']}")
