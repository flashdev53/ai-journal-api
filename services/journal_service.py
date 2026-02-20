import uuid
from datetime import datetime


class JournalService:

    def __init__(self):
        self.entries = []

    def create_entry(self, text: str):
        new_entry = {
            "id": str(uuid.uuid4()),
            "text": text,
            "created_at": datetime.utcnow().isoformat()
        }
        self.entries.append(new_entry)
        return new_entry

    def get_all_entries(self):
        return self.entries

    def get_entry_by_id(self, entry_id: str):
        for entry in self.entries:
            if entry["id"] == entry_id:
                return entry
        return None
