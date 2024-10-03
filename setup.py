
def create_tables():
    create_rollercoaster = """
        CREATE TABLE Rollercoaster (
        ID INTEGER PRIMARY KEY,
        WaitTime INTEGER,
        Location TEXT,
        NumRiders INTEGER
        ); 
    """
    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(create_rollercoaster)
    create_guest = """
        CREATE TABLE Guest (
        ID INTEGER PRIMARY KEY,
        Name TEXT,
        RollercoasterID INT,
        FOREIGN KEY (RollercoasterID) REFERENCES Rollercoaster(ID)
        );
    """
    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(create_guest)