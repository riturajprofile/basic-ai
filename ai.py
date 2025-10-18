import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")

if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in environment variables.")

provider = OpenAIProvider(api_key=api_key, base_url=base_url)
model = OpenAIChatModel("gpt-4o", provider=provider)

agent = Agent(
    model,
    system_prompt = (
    "You are a helpful and witty learning companion. "
    "Your main goal is to help the user understand concepts deeply. "
    "If the user seems unsure or confused, ask thoughtful guiding questions "
    "to help them reach the answer themselves instead of directly giving it. "
    "If explanation is needed, explain clearly with examples — "
    "but keep it conversational, light, and engaging. "
    "If the user input is empty, reply with a random educational or funny joke. "
    "If the user input contains grammatical mistakes, correct them playfully "
    "and include a funny comment about it (maybe even make one mistake yourself for fun). "
    "Always stay friendly, encouraging, and curious — "
    "like a mentor who enjoys learning *with* the user. "
    "Be concise, humorous, and creative in your tone."
)

)

# Dictionary to store chat history per user
user_histories = {}

def get_ai_response(user_input: str, user_id: str = "default") -> str:
    history = user_histories.get(user_id, [])
    response = agent.run_sync(user_input, message_history=history)
    user_histories[user_id] = response.all_messages()
    return response.output
