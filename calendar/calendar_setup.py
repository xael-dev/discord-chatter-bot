import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Delete token.pickle if the following needs editing
SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = '../credentials.json'

def get_calendar_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If no valid credentials exist then let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

            # Save the credentials for the next instance
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    return service
