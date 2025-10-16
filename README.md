# AI Chat Agent with Pydantic AI

A simple interactive chat agent powered by [Pydantic AI](https://ai.pydantic.dev/) and OpenAI's API. This project demonstrates how to build a basic conversational AI agent using the Pydantic AI framework.

## Features

- Interactive command-line chat interface
- Configurable OpenAI provider (supports custom base URLs like AIPipe)
- Environment-based configuration using `.env` files
- Simple and extensible architecture

## Prerequisites

- Python 3.13 or higher
- An OpenAI API key (or compatible API endpoint)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/riturajprofile/basic-ai.git
   cd basic-ai
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   
   Using pip:
   ```bash
   pip install pydantic-ai python-dotenv
   ```
   
   Or using uv (faster):
   ```bash
   uv pip install pydantic-ai python-dotenv
   ```

## Configuration

### Option 1: Using a `.env` file (Recommended)

Create a `.env` file in the project root directory:

```bash
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_BASE_URL=https://api.openai.com/v1  # Optional: change if using a custom endpoint
```

**Note:** Never commit your `.env` file to GitHub. It's already included in `.gitignore`.

### Option 2: Using Environment Variables

Set the environment variables directly in your shell:

**Linux/macOS:**
```bash
export OPENAI_API_KEY="sk-your-api-key-here"
export OPENAI_BASE_URL="https://api.openai.com/v1"  # Optional
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="sk-your-api-key-here"
$env:OPENAI_BASE_URL="https://api.openai.com/v1"  # Optional
```

## Usage

Run the chat agent:

```bash
python ai.py
```

The agent will start an interactive session:

```
You: Hello, how are you?
Agent: [Response from the AI model]
You: Tell me a joke
Agent: [AI's response]
You: exit
```

### Commands

- Type your message and press Enter to chat with the agent
- Type `exit` or `quit` to end the session
- Press `Ctrl+C` to force quit

## Customization

### Changing the Model

Edit `ai.py` and modify the model name on line 17:

```python
model = OpenAIChatModel("gpt-4o", provider=provider)
```

You can use any OpenAI model like:
- `gpt-4o` (default)
- `gpt-4`
- `gpt-3.5-turbo`
- Or any custom model supported by your endpoint

### Using Custom API Endpoints (e.g., AIPipe)

If you're using a custom OpenAI-compatible endpoint:

1. Set the `OPENAI_BASE_URL` environment variable to your endpoint URL
2. Ensure your API key is valid for that endpoint
3. Update the model name to match what your endpoint supports

Example:
```bash
OPENAI_API_KEY=your-aipipe-key
OPENAI_BASE_URL=https://your-aipipe-endpoint.com/v1
```

## Troubleshooting

### Error: "The api_key client option must be set"

**Solution:** Make sure you've set the `OPENAI_API_KEY` environment variable or created a `.env` file with your API key.

Verify the environment variable is set:
```bash
# Linux/macOS/Windows Git Bash
echo $OPENAI_API_KEY

# Windows PowerShell
echo $env:OPENAI_API_KEY
```

### Error: Module not found

**Solution:** Make sure you've activated your virtual environment and installed all dependencies:
```bash
source .venv/bin/activate  # Linux/macOS
pip install pydantic-ai python-dotenv
```

### Connection errors

**Solution:** If using a custom `OPENAI_BASE_URL`, verify:
- The URL is correct and accessible
- Your API key is valid for that endpoint
- You have internet connectivity

## Project Structure

```
.
├── ai.py              # Main chat agent script
├── pyproject.toml     # Project metadata and dependencies
├── README.md          # This file
└── .env              # Environment variables (create this, not in repo)
```

## Dependencies

- **pydantic-ai** (>=1.1.0): The core AI framework
- **python-dotenv** (>=1.1.1): Environment variable management
- **openai**: OpenAI Python client (installed as a pydantic-ai dependency)

See `pyproject.toml` for the complete dependency list.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests


## Resources

- [Pydantic AI Documentation](https://ai.pydantic.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Python dotenv Documentation](https://pypi.org/project/python-dotenv/)

## Author

**Rituraj**  
GitHub: [@riturajprofile](https://github.com/riturajprofile)

---

**⚠️ Security Warning:** Never commit your `.env` file or expose your API keys in public repositories. Always use environment variables or secure secret management for sensitive credentials.
