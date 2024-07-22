from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
import base64
import os

# Credentials from Google Cloud Console (OAuth 2.0 Client IDs)
CREDENTIALS_FILE = "client_secret.json"
TOKEN_FILE = "token.json"

# Grab sender email from sender.txt
with open("sender.txt", "r") as sender_file:
    SENDER_EMAIL = sender_file.read().strip()


def create_message(sender, recipient, subject, body_text):
    message = MIMEText(body_text, "plain")
    message["to"] = recipient
    message["from"] = sender
    message["subject"] = subject
    return {"raw": base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def build_service():
    scopes = ["https://www.googleapis.com/auth/gmail.send"]
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, scopes=scopes)
    # Check for existing token file
    if os.path.exists(TOKEN_FILE):
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE, scopes)
    else:
        # If token file doesn't exist, go through authorization flow
        credentials = flow.run_local_server(port=0)
        # Save the credentials for future use
        with open(TOKEN_FILE, "w") as token_out:
            token_out.write(credentials.to_json())
    return build("gmail", "v1", credentials=credentials)


def send_email(recipient, subject, body, CDT_TIMESTAMP):
    service = build_service()
    message_prepared = create_message(SENDER_EMAIL, recipient, subject, body)
    try:
        message = (
            service.users()
            .messages()
            .send(userId="me", body=message_prepared)
            .execute()
        )

        # Export message and timestamp for README
        saved_message = f"{body}"
        saved_timestamp = (
            f"Last updated on {CDT_TIMESTAMP['today']} at {CDT_TIMESTAMP['time']} CDT"
        )
        with open("message.txt", "w") as message_file:
            message_file.write(str(saved_message))
        with open("timestamp.txt", "w") as timestamp_file:
            timestamp_file.write(str(saved_timestamp))

        print("Message sent successfully!")
    except Exception as e:
        print("Error sending message:", e)


def send_email_notification(recipient, subject, body, CDT_TIMESTAMP):
    send_email(recipient, subject, body, CDT_TIMESTAMP)
