from openai import OpenAI
from dotenv import load_dotenv
import os
import setup

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("API_KEY")
conn_string = os.getenv("CONNECTION_STRING")

# set up tables
setup.create_tables(conn_string)
setup.fill_tables(conn_string)