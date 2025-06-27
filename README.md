# WhatsApp Chatbot Agent (Python + FastAPI + Twilio)

A modular, production-ready WhatsApp chatbot agent built with Python, FastAPI, and Twilio's WhatsApp API. Easily extendable for AI, LLM, or database integrations.

---

## Features
- **Receive and send WhatsApp messages** using Twilio's WhatsApp API
- **FastAPI backend** for webhook handling
- **Environment variable-based secrets management**
- **Clean, modular code** for future upgrades (AI, LLMs, databases, etc.)
- **Basic error handling**

---

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/Vaibhav-0018/Whatsapp-chat-bot.git
cd Whatsapp-chat-bot
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables
- Copy `.env.example` to `.env` and fill in your Twilio credentials and WhatsApp numbers:

```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
MY_WHATSAPP_NUMBER=whatsapp:+91XXXXXXXXXX
```

### 4. Set Up Twilio Sandbox for WhatsApp
- Go to [Twilio Console WhatsApp Sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox)
- Join the sandbox as instructed
- Set your webhook URL to `https://<your-ngrok-url>/webhook`

### 5. Run the FastAPI Server
```sh
uvicorn app.main:app --reload
```

### 6. Expose Your Local Server (for Twilio Webhooks)
```sh
ngrok http 8000
```
- Copy the HTTPS forwarding URL from ngrok and set it as your Twilio webhook.

### 7. Test
- Send a WhatsApp message to your Twilio sandbox number from your WhatsApp.
- You should receive an echo reply.

---

## Project Structure
```
whatsapp-bot/
│
├── app/
│   ├── main.py            # FastAPI app and webhook endpoint
│   ├── twilio_client.py   # Twilio send message logic
│   └── utils.py           # Utility functions (env loading)
├── .env.example           # Example env file
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## Extending the Bot
- Integrate AI/LLMs: Replace the echo logic in `main.py` with your AI model or API call.
- Add a database: Use SQLAlchemy or an ORM and connect in `main.py` or a new module.
- Add more endpoints or features as needed.

---

## Security & Best Practices
- **Never commit your actual `.env` file or secrets to version control.**
- Use the `.env.example` as a template for collaborators.
- For production, use secure secret management and HTTPS.

---

## License
MIT

---

## Author
[Your Name] · [your.email@example.com]
