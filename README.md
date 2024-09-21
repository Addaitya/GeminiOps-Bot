# AI Agent - Terminal Based

This is a terminal-based AI agent that can perform three tasks using the Gemini free API:

1. **Search Wikipedia** for a short answer.
2. **Perform basic math operations** (+, -, *, /) using an API call.
3. **Fetch current currency exchange rates**.

The project is designed to provide a hands-on understanding of function calling in AI agents.

## Features

- Wikipedia search and result summarization.
- Perform basic math operations via API calls.
- Real-time currency exchange rates fetching.

## Prerequisites

- Python 3.10+
- Gemini API access (free plan works)
- Install required packages via `pip`:

  ```bash
  pip install requirements.txt

## How to Use:

1. **Clone the Repository:**
   ```bash
   git clone https://your-github-repository-url.git

2. **Install Dependecies:**
    ```bash
    pip install -r requirements.txt

3. **Run the Agent**
    ```bash
    python main.py

## Code structure
- **main.py:** The main entry point for the agent, handling user input and calling the appropriate functions.

- **lib/actions.py:** This file contains all api fucntions.
- **lib/fun_declare.py:** Here function description is provided that is used by LLM(gemini in our case), know what api call are avaiable to it.
- **lib/chat_bot.py:** This file contains the `Chat_bot` class provide an abstraction to interct with LLM.

### Purpose
The purpose of this project is to understand how AI agents use function calling to handle multiple tasks. Each function callable by the AI agent depending on the task at hand.