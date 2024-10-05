from openai import OpenAI
import psycopg2
from dotenv import load_dotenv
import os
import setup, query

# make request
def query_gpt(query_str):
    """
    Queries GPT with the query string and returns the text contents of the response
    """
    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": query_str,
        }],
        model="gpt-4o-mini",
    )

    generated_text = response.choices[0].message.content
    return generated_text

def construct_sql_gpt_query(question_str):
    """
    Construct the prompt to pass to gpt given the query string
    Components (based on the paper):
        1. Task instruction
        2. Test database
        3. Test Natural Language Question
        4. [Optional] demonstrations
    """
    sql_gpt_query = ""
    # Component 1. Task Instruction
    sql_gpt_query += "Given the following database and user question, generate postgreSQL code that would query the database and return the answer to the question."
    
    # Component 2: Test Database
    # Use Create Table strategy
    sql_gpt_query += "Database tables and their create table code:\n"
    create_tables = setup.get_create_table_strings()
    for create_table in create_tables:
        sql_gpt_query += create_table + "\n"

    # Component 3: NLQ
    sql_gpt_query += f"Question: {question_str}"

    # Component 4: TODO(?) Add demonstrations

    return sql_gpt_query

def sql_gpt_query(conn_string, question_str):
    """
    Get interpreted results from a natural language question (question_str)
    :param: conn_string connection string to database
    :param: question_str Natural Language query
    """
    print("Question:", question_str)

    # Make a GPT query that includes the task, the database info, the question, etc.
    gpt_query_str = construct_sql_gpt_query(question_str)
    print("GPT query:", gpt_query_str)
    # Ask GPT for the SQL query
    gpt_response = query_gpt(gpt_query_str)
    print(gpt_response)
    # Parse out just the sql code from the GPT response
    code_start = gpt_response.find('```sql') + len('```sql')
    code_end = gpt_response.find('```', code_start+1)
    if code_start == -1:
        print("Fail: Code not found in GPT response.")
        return
    gpt_sql_code = gpt_response[code_start:code_end]

    # Make the SQL query
    query_success = True
    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(gpt_sql_code)
            columns = cursor.description
            sql_results = cursor.fetchall()
        except psycopg2.Error as err:
            query_success = False
            print("Query failed.", err)

    if not query_success: return

    print(columns)
    print("SQL result:", sql_results)

    # Ask GPT to interpret the results
    gpt_interpret_str = f"Here is a question I asked about my database: {question_str}"
    gpt_interpret_str += "Given this data from the database, answer my question.\n"
    gpt_interpret_str += f"Columns: {columns}\n"
    gpt_interpret_str += f"Data: {sql_results}\n"
    gpt_interpretation = query_gpt(gpt_interpret_str)
    print("Friendly Response:", gpt_interpretation)

# Load environment variables from the .env file
load_dotenv(override=True)

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
def print_table_contents():
    query.print_rows(conn_string, "Station")
    query.print_rows(conn_string, "Rollercoaster")
    query.print_rows(conn_string, "FoodStall")
    query.print_rows(conn_string, "Employee")
    query.print_rows(conn_string, "Guest")
print_table_contents()

# test request to gpt
# sql_gpt_query(conn_string, question_str="What are all of the employees' ids?")

# We need at least 8 example questions (1 that worked, 1 that didn't work, 6 more)
questions = [
    "What are all of the employees ids?",
    "When did employee 2 start work?",
    "How many employees work at a food stall?",
    "How many people are at each roller coaster?",
    "What are the names of the people who have ridden rollercoaster 3?",
    "What is the wait time for rollercoaster 4?",
    "What is the location of food stall 1?",
    "How many rollercoasters are there?"
]

for question in questions:
    sql_gpt_query(conn_string, question)
    print()
