import frappe
import jwt
from datetime import datetime, timedelta

# from frappe.utils.password import check_password

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
    # decrypted_password = frappe.utils.password.get_decrypted_password("App User", username, fieldname="password")
    # print(decrypted_password, "decrypted_password")

    user = frappe.get_doc("App User", username) 

    if frappe.utils.password.get_decrypted_password("App User", username, fieldname="password") == password:
        user_details = {"username": user.username, "full_name": user.full_name, "role": user.role_profile}
        token = generate_jwt_token(user_details, frappe.utils.password.get_encryption_key(), "HS256")        
        return {"message": "Login successful.", "token": token, "user": user_details}
    else:
        raise frappe.AuthenticationError("Invalid username or password.")


def generate_jwt_token(
    payload: dict,
    jwt_secret: str,
    jwt_algo: str = "HS256",
    expires_in_minutes: int = 60
) -> str:
    """
    Generate a signed JWT token.

    Args:
        payload (dict): Custom payload data
        jwt_secret (str): Secret key
        jwt_algo (str): Signing algorithm
        expires_in_minutes (int): Token validity

    Returns:
        str: JWT token
    """
    if not jwt_secret:
        raise ValueError("JWT secret is required")

    token_payload = payload.copy()
    now = datetime.utcnow()

    token_payload.update({
        "iat": now,
        "exp": now + timedelta(minutes=expires_in_minutes),
    })

    token = jwt.encode(token_payload, jwt_secret, algorithm=jwt_algo)

    return token

def authenticate_request():
    """Authenticate incoming request using JWT token."""
    auth_header = frappe.get_request_header("App-Authorization")
    if not auth_header or not auth_header.startswith("token"):
        frappe.throw("Authorization header missing or invalid", frappe.AuthenticationError)

    token = auth_header.split(" ")
    if len(token) < 2:
        frappe.throw("Authorization header missing or invalid", frappe.AuthenticationError)
        
    token = token[1]
    api_secret = frappe.utils.password.get_encryption_key()

    payload = decode_jwt(token, api_secret, "HS256")
    frappe.local.jwt_payload = payload

def decode_jwt(custom_jwt, api_secret, algo="HS256"):
    """Decode and validate JWT token from Authorization header."""
    try:
        payload = jwt.decode(custom_jwt, api_secret, algorithms=[algo])
        return payload

    except jwt.ExpiredSignatureError:
        frappe.throw("Token expired", frappe.AuthenticationError)

    except Exception:
        frappe.throw("Invalid token", frappe.AuthenticationError)