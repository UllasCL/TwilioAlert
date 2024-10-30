from fastapi import FastAPI, Request
from pydantic import BaseModel
from twilio.rest import Client
import os

app = FastAPI()

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_client = Client(account_sid, auth_token)

# Phone numbers
from_phone = '+your_twilio_number'
to_phone = '+recipient_phone_number'

# Request body model
class AlertData(BaseModel):
    title: str

@app.post("/alert")
async def alert(data: AlertData):
    # Parse Grafana alert data
    alert_name = data.title
    message_body = f"Alert triggered: {alert_name}"

    # Make Twilio voice call
    call = twilio_client.calls.create(
        to=to_phone,
        from_=from_phone,
        twiml=f"<Response><Say>{message_body}</Say></Response>"
    )

    return {"message": "Voice call triggered"}
