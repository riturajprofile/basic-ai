import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

# Set up AIPipe environment
os.environ["OPENAI_API_KEY"] = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDQzOTBAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.d6mXwx9OIY4hni22YaQcTMs8SidoeGLKn77KkrhVX1A"
os.environ["OPENAI_BASE_URL"] = "https://aipipe.org/openai/v1"

# Create provider with AIPipe endpoint
provider = OpenAIProvider(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

# Create model (pick model name that AIPipe supports)
model = OpenAIChatModel("gpt-4o", provider=provider)

# Create agent
agent = Agent(model)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = agent.run_sync(user_input)
    print("Agent:", response.output)
# Run synchronously
# result = agent.run_sync("hello i am rituraj")
# print(result.output)
