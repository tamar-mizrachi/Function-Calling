from enum import Enum
from pydantic import BaseModel, Field


class Compliance(str, Enum):
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Category(str, Enum):
    GENERAL = "general"
    CODING = "coding"
    EDUCATION = "education"
    BUSINESS = "business"
    PERSONAL = "personal"
    SECURITY = "security"
    OTHER = "other"


class AnalyzeRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=12000)
    include_summary: bool = False


class PromptAnalysis(BaseModel):
    compliance: Compliance
    category: Category
    riskLevel: RiskLevel
    manipulative: bool
    summary: str | None = None
