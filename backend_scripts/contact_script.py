# contact_script.py
# This script would simulate backend logic for the 'Contact' or 'Request Demo' section.
# In a real application, this would handle form submissions, send emails, etc.

def handle_demo_request(name, email, company):
    """
    Simulates handling a demo request submission.
    In a real scenario, this would save data to a DB or trigger an email.
    """
    print(f"Received demo request from: {name}")
    print(f"Email: {email}")
    print(f"Company: {company}")
    print("Demo request successfully processed (simulation).")
    return {"status": "success", "message": "Your demo request has been received."}

if __name__ == "__main__":
    # Example usage:
    response = handle_demo_request("John Doe", "john.doe@example.com", "Acme Corp")
    print(response)
