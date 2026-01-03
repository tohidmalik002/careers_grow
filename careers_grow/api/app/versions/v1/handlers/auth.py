import frappe

def login(payload: dict) -> dict:
    """
    Handle user login.

    Args:
        payload (dict): The login payload containing user credentials.

    Returns:
        dict: A dictionary containing the login result.
    """
    # Placeholder implementation
    username = payload.get("username")
    password = payload.get("password")

    if username == "admin" and password == "admin":
        return {"status": "success", "message": "Login successful.", "token": "sample_token", "user": {"username": username, "full_name": "Test"}, "role": "Student"}
    else:
        raise frappe.AuthenticationError("Invalid username or password.")