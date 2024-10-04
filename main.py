from openai import OpenAI
from dotenv import load_dotenv
import os
import setup, query

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("API_KEY")
conn_string = os.getenv("CONNECTION_STRING")
org_id = os.getenv("ORG_ID")

# setup for OpenAI
client = OpenAI(
    organization= org_id,
    api_key=api_key
)

# set up tables
setup.create_tables(conn_string)
setup.fill_tables(conn_string)

# test that it worked by printing the tables
query.print_rows(conn_string, "Station")
query.print_rows(conn_string, "Rollercoaster")
query.print_rows(conn_string, "FoodStall")
query.print_rows(conn_string, "Employee")
query.print_rows(conn_string, "Guest")

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