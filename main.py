from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from ai import agent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Allow CORS (you can tighten this in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store message history per user (in memory)
user_histories = {}

class Message(BaseModel):
    text: str

class ResponseModel(BaseModel):
    reply: str


# ---- UI ROUTE ----
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def chat():
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chat with AI</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #chatbox { border: 1px solid #ccc; padding: 10px; height: 400px; overflow-y: auto; }
            .user { color: blue; }
            .assistant { color: green; }
            input { width: 80%; padding: 10px;height: 40px;bg-color: #f0f0f0; border: 2px solid #c54ecc; }
            button { padding: 10px; }
        </style>
    </head>
    <body>
        <h1>Chat with AI</h1>
        <div id="chatbox"></div>
        <input type="text" id="userInput" placeholder="Type your message here...">
        <button onclick="sendMessage()">Send</button>
        <script>
            const chatbox = document.getElementById("chatbox");
            const input = document.getElementById("userInput");

            input.addEventListener("keypress", (e) => {
                if (e.key === "Enter") sendMessage();
            });

            async function sendMessage() {
                const userInput = input.value.trim();
                if (!userInput) return;

                chatbox.innerHTML += `<div class='user'>You: ${userInput}</div>`;
                input.value = "";

                const response = await fetch("/chat", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ text: userInput })
                });
                const data = await response.json();

                chatbox.innerHTML += `<div class='assistant'>AI: ${data.reply}</div>`;
                chatbox.scrollTop = chatbox.scrollHeight;
            }
        </script>
    </body>
    </html>
    '''
    return HTMLResponse(content=html)


# ---- API ROUTE ----
@app.post("/chat", response_model=ResponseModel)
async def chat_endpoint(message: Message, request: Request):
    user_id = request.client.host  # crude but works for demo; use tokens/cookies later
    history = user_histories.get(user_id, [])

    # Run sync call in thread-safe manner
    response = await run_in_threadpool(agent.run_sync, message.text, message_history=history)

    # Update user's history
    user_histories[user_id] = response.all_messages()

    return ResponseModel(reply=response.output)

