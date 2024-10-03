from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("API_KEY")
conn_string = os.getenv("CONNECTION_STRING")