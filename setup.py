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
        cursor.execute(drop_guest)
        cursor.execute(drop_foodstall_table)
        cursor.execute(drop_rollercoaster)
        cursor.execute(drop_station_table)

def create_foodstall_table(conn_string):
    create_foodstall_table_str = """
    CREATE TABLE FoodStall(
    StationID      INT PRIMARY KEY,
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
    EmployeeID      INT PRIMARY KEY,
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
    StationID   INT PRIMARY KEY,
    Location    TEXT
    );
    """

    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(create_station_table_str)

def create_tables(conn_string):
    drop_tables(conn_string)

    create_station_table(conn_string)
    create_foodstall_table(conn_string)
    create_employee_table(conn_string)

    create_rollercoaster = """
        CREATE TABLE Rollercoaster (
        StationID      INT PRIMARY KEY,
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
        RollercoasterID INTEGER,
        FOREIGN KEY (RollercoasterID) REFERENCES Rollercoaster(StationID)
            ON DELETE CASCADE
            ON UPDATE RESTRICT
        );
    """
    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(create_guest)


def fill_tables(conn_string):
    station_data = [
        (1, "3 Rollercoaster Rd"),
        (2, "2 Fun Way"),
        (3, "51 Waverly Place"),
        (4, "23 Oklahoma Drive") 
    ]
    station_insert_str = """
    INSERT INTO Station (StationID, Location)
    VALUES(%s, %s)
    """

    rollercoaster_data = [
        (3, 15, 60),
        (4, 27, 328)     
    ]
    rollercoaster_insert_str = """
    INSERT INTO Rollercoaster (StationID, WaitTime, NumRiders)
    VALUES (%s, %s, %s)
    """

    foodstall_data = [
        (1, "Hamburgers, Hot Dogs, Soda"),
        (2, "Salads, Tacos")
    ]
    foodstall_insert_str = """
    INSERT INTO FoodStall (StationID, AvailableItems)
    VALUES (%s, %s)
    """

    employee_data = [
        (1, "3 Rollercoaster Rd", "09:00:00", "5:00:00"),
        (2, "2 Fun Way", "12:00:00", "3:00:00")
    ]
    employee_insert_str = """
    INSERT INTO Employee (EmployeeID, StationLocation, TimeIn, TimeOut)
    VALUES (%s, %s, %s, %s)
    """

    guest_data = [
        (120958, "Maria Rodriguez", 3),
        (904367, "Jose Ultman", 4),
        (983257, "Marx Helion", 4),
        (165835, "Abigail Ryan", 4),
        (664287, "Joe Marion", 3)

    ]
    guest_insert_str = """
    INSERT INTO Guest (ID, Name, RollerCoasterID)
    VALUES(%s, %s, %s)
    """

    with psycopg2.connect(conn_string) as conn:
        cursor = conn.cursor()
        cursor.executemany(station_insert_str, station_data)
        cursor.executemany(rollercoaster_insert_str, rollercoaster_data)
        cursor.executemany(foodstall_insert_str, foodstall_data)
        cursor.executemany(employee_insert_str, employee_data)
        cursor.executemany(guest_insert_str, guest_data)