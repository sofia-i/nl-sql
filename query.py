import psycopg2

def print_rows(conn_string, table_name):
    sql_select_all = f"SELECT * FROM {table_name};"

    print(table_name)

    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_select_all)
        result = cursor.fetchall()

    for row in result:
        print(row)