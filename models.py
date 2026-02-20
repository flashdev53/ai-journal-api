from pydantic import BaseModel
from typing import List


class JournalEntryCreate(BaseModel):
    text: str


class AnalysisModel(BaseModel):
    sentiment: str
    summary: str
    topics: List[str]
    struggle_detected: bool


class JournalEntryResponse(BaseModel):
    id: str
    text: str
    created_at: str
    analysis: AnalysisModel
