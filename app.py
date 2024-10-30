from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_client = Client(account_sid, auth_token)

# Phone numbers
from_phone = '+your_twilio_number'
to_phone = '+recipient_phone_number'

@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json()
    # Parse Grafana alert data
    alert_name = data.get('title')
    message_body = f"Alert triggered: {alert_name}"

    # Make Twilio voice call
    call = twilio_client.calls.create(
        to=to_phone,
        from_=from_phone,
        twiml=f"<Response><Say>{message_body}</Say></Response>"
    )

    return "Voice call triggered", 200

if __name__ == '__main__':
    app.run(port=5000)
