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
    
    drop_rollercoaster = """
    DROP TABLE IF EXISTS Rollercoaster;
    """
    
    drop_guest = """
    DROP TABLE IF EXISTS Guest;
    """

    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(drop_employee_table)
        cursor.execute(drop_foodstall_table)
        cursor.execute(drop_station_table)
        cursor.execute(drop_rollercoaster)
        cursor.execute(drop_guest)

def create_foodstall_table(conn_string):
    create_foodstall_table_str = """
    CREATE TABLE FoodStall(
    StationID      INT UNSIGNED PRIMARY KEY,
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

def create_tables(conn_string):
    create_rollercoaster = """
        CREATE TABLE Rollercoaster (
        StationID      INT UNSIGNED PRIMARY KEY,
        WaitTime INTEGER,
        NumRiders INTEGER,
        FOREIGN KEY(StationID) REFERENCES Station(StationID)
            ON DELETE CASCADE
            ON UPDATE RESTRICT
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


def fill_tables(conn_string):
    station_data = [
        
    ]
    station_insert_str = """
    INSERT INTO Station (StationID, Location)
    VALUES(%s, %s)
    """

    rollercoaster_data = [
        
    ]
    rollercoaster_insert_str = """
    """

    foodstall_data = [

    ]
    foodstall_insert_str = """
    """

    employee_data = [

    ]
    employee_insert_str = """
    """

    guest_data = [

    ]
    guest_insert_str = """
    """

    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        # cursor.executemany(station_insert_str, station_data)
        # cursor.executemany(rollercoaster_insert_str, rollercoaster_data)
        # cursor.executemany(foodstall_insert_str, foodstall_data)
        # cursor.executemany(employee_insert_str, employee_data)
        # cursor.executemany(guest_insert_str, guest_data)