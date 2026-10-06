from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from .llm import LLMError, analyze_with_llm
from .models import AnalyzeRequest, PromptAnalysis

load_dotenv()

app = FastAPI(
    title="Prompt Analyzer",
    version="1.0.0",
    description="LLM-based Prompt Engineering analyzer with few-shot classification and output validation.",
)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/analyze", response_model=PromptAnalysis)
async def analyze(request: AnalyzeRequest):
    try:
        return analyze_with_llm(request.prompt, request.include_summary)
    except LLMError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="LLM analysis failed") from exc
