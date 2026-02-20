# AI Journal API

A FastAPI-based application that allows users to create journal entries and automatically analyzes them using AI to extract sentiment, summaries, topics, and detect potential struggles. The application stores the entries and their analysis in Azure Cosmos DB.


## Prerequisites

Before running the project, you need to have the following:

- **Python 3.8+** installed on your machine.
- **Azure Cosmos DB** account. You will need the endpoint URL, key, database name, and container name.
- **GitHub Personal Access Token (PAT)** with access to GitHub Models (for LLM inference).

## File Structure

```text
├── main.py                    # Entry point of the FastAPI application, defines routes
├── models.py                  # Pydantic models for request/response validation
├── requirements.txt           # Python dependencies required for the project
├── .env                       # Environment variables (not tracked in version control)
└── services/                  # Business logic and external service integrations
    ├── database_service.py    # Handles Azure Cosmos DB connection and CRUD operations
    ├── journal_service.py     # Orchestrates creating entries and calling the LLM analyzer
    └── llm_service.py         # Integrates with OpenAI SDK via GitHub Models for text analysis
```

## Configuration (`.env`)

You must create a `.env` file in the root of your project. It should contain the following environment variables:

```env
# Azure Cosmos DB Configuration
COSMOS_ENDPOINT="<your-cosmos-db-endpoint-url>"
COSMOS_KEY="<your-cosmos-db-primary-key>"
COSMOS_DB="<your-database-name>"             # e.g., journal-db
COSMOS_CONTAINER="<your-container-name>"     # e.g., entries

# AI Models Configuration (Using GitHub Models via OpenAI SDK)
GITHUB_TOKEN="<your-github-personal-access-token>"
GITHUB_MODEL="<your-model-name>"             # e.g., gpt-4o-mini
```

## Installation & Setup

1. **Clone the repository** (if you haven't already) and navigate to the project folder.

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your environment variables**:
   Create a `.env` file in the root directory and populate it with the required keys as shown in the Configuration section.

## Execution

To run the FastAPI server, use `uvicorn`:

```bash
uvicorn main:app --reload
```

The API will be accessible at `http://127.0.0.1:8000`. 
You can view the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

### Available Endpoints

- `GET /health` - Check API running status.
- `POST /entries` - Create a new journal entry (Body requires `{"text": "your journal text"}`).
- `GET /entries` - Get a list of all entries.
- `GET /entries/{entry_id}` - Get a specific entry by its ID.

---
**Thank you!**
