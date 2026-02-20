import uuid
from datetime import datetime
from services.database_service import DatabaseService
from services.llm_service import LLMService


class JournalService:

    def __init__(self):
        self.db = DatabaseService()
        self.llm = LLMService()

    def create_entry(self, text: str):

        analysis = self.llm.analyze_entry(text)

        new_entry = {
            "id": str(uuid.uuid4()),
            "text": text,
            "created_at": datetime.utcnow().isoformat(),
            "analysis": analysis
        }

        return self.db.create_entry(new_entry)

    def get_all_entries(self):
        return self.db.get_all_entries()

    def get_entry_by_id(self, entry_id: str):
        return self.db.get_entry_by_id(entry_id)
