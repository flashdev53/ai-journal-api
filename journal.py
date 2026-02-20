import json
import uuid
from datetime import datetime

class JournalEntry:
    def __init__(self, text):
            self.id = str(uuid.uuid4())
            self.text = text
            self.created_at = datetime.utcnow().isoformat()
    def to_dict(self):
          return {
                "id": self.id,
                "text": self.text,
                "created_at": self.created_at
          }

def save_entry(entry):
    try:
        with open("entries.json", "r") as f:
             data = json.load(f)
    except FileNotFoundError:
         data=[]
    data.append(entry.to_dict())
    with open("entries.json", "w") as f:
         json.dump(data, f, indent=4)

def load_entries():
    try:
        with open("entries.json", "r") as f:
             return json.load(f)
    except FileNotFoundError:
         return []

if __name__=="__main__":
    text = input("Enter your journal entry: ")
    entry=JournalEntry(text)
    save_entry(entry)
    print("Saved Successfully!")
    print(load_entries())
    