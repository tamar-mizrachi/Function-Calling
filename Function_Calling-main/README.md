# Prompt Analyzer – Prompt Engineering Project

A FastAPI service that receives a natural-language prompt and asks an LLM to analyze it using explicit Prompt Engineering techniques.

## Requirements covered

- Context: the system prompt defines the role, categories, compliance levels, risk levels, manipulation rules, and output rules.
- Clear instructions: the model is explicitly told to analyze rather than answer the user's underlying request.
- Few-shot learning: five input/output examples are embedded in the system prompt.
- Temperature: `0` for stable classification.
- Classification: `category` field with a fixed enum.
- Compliance: `green`, `yellow`, `red`.
- Risk: `low`, `medium`, `high`.
- Manipulation detection: boolean `manipulative` field.
- Structured JSON output: Pydantic model is supplied as the response schema.
- Output validation: Pydantic validates the returned structure and enum values.
- Optional summary: controlled by `include_summary`.

## Project structure

```text
prompt_analyzer_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── llm.py
│   ├── models.py
│   └── prompt.py
├── tests/
│   └── test_models.py
├── .env.example
├── requirements.txt
└── README.md
```

## Installation

Python 3.11+ is recommended.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` from `.env.example` and put your OpenAI API key there.

## Run

From the project root:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Example request

```json
{
  "prompt": "Explain how a REST API works in Python",
  "include_summary": true
}
```

Expected shape:

```json
{
  "compliance": "green",
  "category": "coding",
  "riskLevel": "low",
  "manipulative": false,
  "summary": "A request for a programming explanation."
}
```

## Tests

```bash
pytest
```

## Important implementation note

The project intentionally validates both the input and the model output. The LLM is not trusted to return arbitrary text: the response is parsed into the `PromptAnalysis` Pydantic model, which enforces the required fields and allowed enum values.
