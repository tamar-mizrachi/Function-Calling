from app.models import AnalyzeRequest, PromptAnalysis


def test_request_validation():
    request = AnalyzeRequest(prompt="Explain loops in Python")
    assert request.prompt
    assert request.include_summary is False


def test_output_validation():
    result = PromptAnalysis.model_validate({
        "compliance": "green",
        "category": "coding",
        "riskLevel": "low",
        "manipulative": False,
        "summary": None,
    })
    assert result.category.value == "coding"
