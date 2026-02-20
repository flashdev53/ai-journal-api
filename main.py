from fastapi import FastAPI, HTTPException
from typing import List
import uuid
from datetime import datetime

from models import JournalEntryCreate, JournalEntryResponse


app = FastAPI()

journal_entries = []


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/entries", response_model=JournalEntryResponse, status_code=201)
def create_entry(entry: JournalEntryCreate):
    new_entry = {
        "id": str(uuid.uuid4()),
        "text": entry.text,
        "created_at": datetime.utcnow().isoformat()
    }
    journal_entries.append(new_entry)
    return new_entry


@app.get("/entries", response_model=List[JournalEntryResponse])
def get_all_entries():
    return journal_entries


@app.get("/entries/{entry_id}", response_model=JournalEntryResponse)
def get_single_entry(entry_id: str):
    for entry in journal_entries:
        if entry["id"] == entry_id:
            return entry
    raise HTTPException(status_code=404, detail="Entry not found")
