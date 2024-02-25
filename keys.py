from dotenv import load_dotenv

from dotenv import load_dotenv

try:
  # Attempt to load environment variables
  load_dotenv()
  print(".env file found and loaded successfully.")
except FileNotFoundError:
  print(".env file not found.")
  
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

twilio_number = os.environ.get("TWILIO_PHONE_NUMBER")