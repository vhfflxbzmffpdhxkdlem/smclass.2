from flask import Flask, redirect, request, url_for, session, jsonify
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Google OAuth2 Client Information
GOOGLE_CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"
GOOGLE_CLIENT_SECRET = "YOUR_GOOGLE_CLIENT_SECRET"
REDIRECT_URI = "http://localhost:5000/callback"

# Authorization URL
AUTHORIZATION_URL = (
    f"https://accounts.google.com/o/oauth2/auth?"
    f"response_type=code&client_id={GOOGLE_CLIENT_ID}&"
    f"redirect_uri={REDIRECT_URI}&scope=email profile"
)

# Token Endpoint
TOKEN_URL = "https://oauth2.googleapis.com/token"


@app.route("/")
def index():
    return '<a href="/login">Login with Google</a>'


@app.route("/login")
def login():
    return redirect(AUTHORIZATION_URL)


@app.route("/callback")
def callback():
    # Get authorization code from Google
    auth_code = request.args.get("code")

    # Exchange authorization code for access token
    token_data = {
        "code": auth_code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    token_response = requests.post(TOKEN_URL, data=token_data)
    token_json = token_response.json()
    access_token = token_json.get("access_token")
    id_token_str = token_json.get("id_token")

    try:
        # Verify the ID token
        id_info = id_token.verify_oauth2_token(
            id_token_str, google_requests.Request(), GOOGLE_CLIENT_ID
        )

        # User information
        user_info = {
            "id": id_info["sub"],
            "name": id_info["name"],
            "email": id_info["email"],
            "picture": id_info["picture"],
        }

        # Save user info in session (optional)
        session["user"] = user_info
        return jsonify(user_info)

    except ValueError as e:
        return f"Token verification failed: {e}", 400


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
