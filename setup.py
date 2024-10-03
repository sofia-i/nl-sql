import psycopg2

def drop_tables(conn_string):
    drop_station_table = """
    DROP TABLE IF EXISTS Station;
    """

    drop_employee_table = """
    DROP TABLE IF EXISTS Employee;
    """

    drop_foodstall_table = """
    DROP TABLE IF EXISTS FoodStall;
    """

    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(drop_employee_table)
        cursor.execute(drop_foodstall_table)
        cursor.execute(drop_station_table)

def create_foodstall_table(conn_string):
    create_foodstall_table_str = """
    CREATE TABLE FoodStall(
    StationID      INT UNSIGNED PRIMARY KEY,
    Location       TEXT,
    AvailableItems TEXT,
    FOREIGN KEY(StationID) REFERENCES Station(StationID)
        ON DELETE CASCADE
        ON UPDATE RESTRICT
    );
    """

    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(create_foodstall_table_str)


def create_employee_table(conn_string):
    create_employee_table_str = """
    CREATE TABLE Employee(
    EmployeeID      INT UNSIGNED PRIMARY KEY,
    StationLocation TEXT,       
    TimeIn          TIME,
    TimeOut         TIME
    );
    """

    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(create_employee_table_str)

def create_station_table(conn_string):
    create_station_table_str = """
    CREATE TABLE Station(
    StationID   INT UNSIGNED PRIMARY KEY,
    Location    TEXT
    );
    """

    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(create_station_table_str)

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