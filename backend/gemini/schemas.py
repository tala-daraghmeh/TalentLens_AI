from pydantic import BaseModel, Field
from typing import Literal


class JobRequirement(BaseModel):
    name: str = Field(description="Normalized short name of the requirement")
    category: Literal[
        "architecture",
        "code_quality",
        "api_backend",
        "data",
        "authentication_security",
        "testing_qa",
        "reliability",
        "devops",
        "documentation",
        "product_thinking",
        "other",
    ]
    requirement_type: Literal["required", "preferred"]
    importance: Literal[1.0, 1.25, 1.5] = Field(
        description="1.0 normal, 1.25 elevated, 1.5 critical"
    )
    description: str = Field(description="One sentence explaining what this requirement means")
    expected_evidence: str = Field(
        description="What kind of repository evidence would prove this requirement"
    )


class JobRequirementsList(BaseModel):
    requirements: list[JobRequirement]