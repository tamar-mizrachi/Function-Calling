import os
from openai import OpenAI
from .models import PromptAnalysis
from .prompt import SYSTEM_PROMPT, build_user_prompt


class LLMError(RuntimeError):
    pass


def analyze_with_llm(prompt: str, include_summary: bool) -> PromptAnalysis:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise LLMError("OPENAI_API_KEY is not configured")

    client = OpenAI(api_key=api_key)
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    response = client.beta.chat.completions.parse(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(prompt, include_summary)},
        ],
        response_format=PromptAnalysis,
    )

    parsed = response.choices[0].message.parsed
    if parsed is None:
        raise LLMError("The model did not return a valid structured response")
    return parsed
