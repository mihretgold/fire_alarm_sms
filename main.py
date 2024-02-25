from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from sms import send_twilio_message  # Import the function you created

app = FastAPI()

class MessageRequest(BaseModel):
    body: str
    to: List[str]
    location: Optional[str] = None  # Optional location parameter

@app.post("/send-message")
def send_message(message_request: MessageRequest):
    try:
        message = send_twilio_message(message_request.body, message_request.to, location=message_request.location)
        return {"message": "Message sent successfully", "twilio_message_sid": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
