from fastapi import FastAPI, Request, status
from fastapi.responses import PlainTextResponse
from app.twilio_client import send_whatsapp_message
from app.utils import get_env_variable
from twilio.twiml.messaging_response import MessagingResponse
import logging

app = FastAPI()

MY_WHATSAPP_NUMBER = get_env_variable("MY_WHATSAPP_NUMBER")

@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    try:
        form = await request.form()
        incoming_msg = form.get("Body", "")
        from_number = form.get("From", "")

        # For now, just echo the message or send a simple AI reply
        reply = f"You said: {incoming_msg}"

        # Respond to Twilio with TwiML (optional, for instant reply)
        twiml = MessagingResponse()
        twiml.message(reply)

        # Optionally, use Twilio REST API to send message (for more control)
        # send_whatsapp_message(from_number, reply)

        return PlainTextResponse(str(twiml), status_code=status.HTTP_200_OK)
    except Exception as e:
        logging.exception("Error in webhook handler")
        return PlainTextResponse("Error processing message", status_code=500)
