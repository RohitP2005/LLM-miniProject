# Mini LLM with LangChain and Streamlit

Welcome to the **Mini LLM** project! This project demonstrates a mini language model (LLM) integrated with LangChain and Streamlit. The application allows users to interact with a language model via a web interface and make API calls to Gemini for language processing tasks.

## Features

- **Interactive Web Interface**: Built with Streamlit, providing an easy-to-use interface for interacting with the LLM.
- **API Integration**: Uses Gemini API for handling language processing tasks.
- **Dynamic Responses**: Generate and display responses based on user input.

## Tech Stack

- **Frontend**: Streamlit (for creating the web interface)
- **Backend**: LangChain (for managing language model interactions)
- **API**: Gemini (for language processing)
- **Version Control**: Git

## Installation

To set up and run this project locally, follow these steps:

### Prerequisites

- Python (v3.8+)
- Git

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/mini-llm.git
    cd mini-llm
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up environment variables**:
    Create a `.env` file in the project root and add the following variables:
    ```bash
    GEMINI_API_KEY=your_gemini_api_key
    ```

6. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

7. **View the app**:
    Visit `http://localhost:8501` in your browser to interact with the mini LLM.

## Project Structure

```plaintext
├── app.py
├── langchain
│   ├── model_manager.py
│   ├── response_generator.py
├── .env
├── requirements.txt
└── README.md
