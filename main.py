from openai import OpenAI
from dotenv import load_dotenv
import os
import setup

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("API_KEY")
conn_string = os.getenv("CONNECTION_STRING")
org_id = os.getenv("ORG_ID")

# setup for OpenAI
client = OpenAI(
    organization= org_id
)

# set up tables
setup.create_tables(conn_string)
setup.fill_tables(conn_string)

# make request
def query_gpt(query_str):
    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": query_str,
        }],
        model="gpt-4o-mini",
    )

    return response