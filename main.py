from fastapi import FastAPI, HTTPException
from typing import List

from models import JournalEntryCreate, JournalEntryResponse
from services.journal_service import JournalService

app = FastAPI()
journal_service = JournalService()

@app.get("/health")
def health_check():
    return {"status": "API is running"}


@app.post("/entries", response_model=JournalEntryResponse, status_code=201)
def create_entry(entry: JournalEntryCreate):
    new_entry = journal_service.create_entry(entry.text)
    return new_entry


@app.get("/entries", response_model=List[JournalEntryResponse])
def get_all_entries():
    return journal_service.get_all_entries()


@app.get("/entries/{entry_id}", response_model=JournalEntryResponse)
def get_single_entry(entry_id: str):
    entry = journal_service.get_entry_by_id(entry_id)

    if entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry
