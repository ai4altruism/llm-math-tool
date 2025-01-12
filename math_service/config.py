from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = os.getenv('GPT_MODEL', 'gpt-4')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")