import os
import dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Create provider with AIPipe endpoint
provider = OpenAIProvider(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

# Create model (pick model name that AIPipe supports)
model = OpenAIChatModel("gpt-4o", provider=provider)

# Create agent
agent = Agent(model,system_prompt="you are a helpful assistant.give very short answers.answer in funny way with jokes")

message_history=[]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = agent.run_sync(user_input, message_history=message_history)
    message_history=response.all_messages()
    print("Agent:", response.output)
# Run synchronously
# result = agent.run_sync("hello i am rituraj")
# print(result.output)
