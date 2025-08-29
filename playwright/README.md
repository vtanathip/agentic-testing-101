# LangGraph ReAct Agent with Playwright Tools

This project demonstrates how to build a simple, yet powerful, autonomous agent using **LangGraph**. The agent is powered by a local LLM from **Ollama** (`llama3.2`) and equipped with web browsing tools provided by **Playwright**.

The core of this example is to show how an agent can be given a high-level task (like "search for something on Google") and use external tools to execute it step-by-step.

---

## ⚙️ How It Works

The script executes the following steps:

1. **Initialize Client:** It connects to a `MultiServerMCPClient`, which is a server exposing tools to our LangChain application. In this case, it's configured to connect to a server that provides **Playwright** browser automation tools.
2. **Fetch Tools:** It asynchronously retrieves the list of available tools from the server (e.g., `open_url`, `search`, `click_element`).
3. **Setup LLM:** It initializes a `ChatOllama` instance to use the local `llama3.2` model as the agent's "brain."
4. **Create Agent:** It uses LangGraph's prebuilt `create_react_agent` function. A **ReAct** agent works in a loop: it Reasons about what to do next and then Acts by selecting a tool to achieve its goal.
5. **Invoke Agent:** The agent is given the prompt "open google.com and search for langchain mcp".
6. **Execute & Respond:** The agent reasons that it first needs to open a URL and then search. It calls the appropriate Playwright tools in sequence to complete the task and returns the final result.

---

## 📋 Prerequisites

Before you can run this script, you need to have the following running on your machine:

* **Python 3.9+**
* **Ollama:** You must have Ollama installed and running.
* **Llama 3.2 Model:** The specific model used in the script must be pulled.
* **Playwright Tool Server:** The `Playwright Standalone Mode` must be running and listening on port `8931`.

---

## 🚀 Setup and Installation

1. **Clone the repository (if applicable)**

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
    ```

4. **Start the Playwright Tool Server:**
    In a separate terminal, run the `playwright standalone mode`

    ```bash
    npx @playwright/mcp@latest --port 8931
    ```

    *This server acts as a bridge, allowing the LangGraph agent to call Playwright functions.*

---

## ▶️ Running the Script

Once the setup is complete and the tool server is running, execute the Python script:

```bash
python playwright_client.py
```
