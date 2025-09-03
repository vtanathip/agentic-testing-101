# Playwright MCP Agent Example

## 1. How It Works

This example demonstrates how to use a chatbot agent to automate browser actions using Playwright via the Model Context Protocol (MCP). The agent leverages a local LLM (Ollama's `llama3.2`) to interpret natural language instructions and execute them step-by-step through Playwright tools.

- The agent is initialized with a local LLM and connects to a Playwright MCP server.
- It receives a high-level instruction (e.g., "Navigate to a login page, fill in credentials, and verify login").
- The agent reasons about the steps required, interacts with the Playwright server to perform browser automation, and returns the result.

## 2. Prerequisites

- **Python 3.9+**
- **Ollama** installed and running
- **Llama 3.2** model pulled in Ollama
- **Playwright Tool Server** running in standalone mode on port `8931`
- **Phoenix** LLM Monitoring Tool

## 3. How to Run the Script

1. **Clone the repository (if needed):**

    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2. **Install Python dependencies:**

    ```bash
    uv venv
    uv sync
    ```

3. **Pull the Ollama model:**

    ```bash
    ollama pull llama3.2
    ollama list
    ollama serve
    ```

4. **Start the Playwright Tool Server:**

    ```bash
    npx @playwright/mcp@latest --port 8931
    ```

5. **Start Phoenix Monitoring**

    ```bash
    docker-compose up -d
    ```

6. **Run the agent script:**

    ```bash
    python playwright_client.py
    ```

The script will instruct the agent to:

- Navigate to a login page,
- Fill in the username and password,
- Click the submit button,
- Verify successful login by checking for a confirmation message.

The result will be printed in the terminal.
