import os
import json
from dotenv import load_dotenv
from openai import OpenAI

class LLMService:

    def __init__(self):
        load_dotenv()

        self.client= OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=os.getenv("GITHUB_TOKEN")
        )
        self.model = os.getenv("GITHUB_MODEL")
        
    def analyse_entry(self, text):
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": "You are a learning analytics assistant."
                    
                },
                {
                    "role": "user",
                    "content": f"""
Analyze the journal entry below and respond ONLY with valid JSON.

Return this format:
{{
    "sentiment": "positive/negative/neutral",
    "summary": "2 sentence summary",
    "topics": "["topic1", "topic2"],
    "struggle_detected": true/false
}}
---BEGIN ENTRY---
{text}
---END ENTRY---
"""

                }
            ]
        )
        content = response.choices[0].message.content
        try:
            return json.loads(content)
        except Exception:
            return{
                "sentiment": "unknown",
                "summary": "Couldn't parse response",
                "topics": [],
                "struggle_detected": False 
            }