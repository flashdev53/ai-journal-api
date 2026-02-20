from pydantic import BaseModel

class JournalEntryCreate(BaseModel):
    text: str

class JournalEntryResponse(BaseModel):
    id: str
    text: str
    created_at: str
