import pyodbc


def test_connection():
    global conn
    try:
        conn = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-8SOG0DL\SQLFOREMAN;"
            "Database=Logos;"
            "Trusted_Connection=yes;"
        )
        print("MySQL Database connection successful")
    except pyodbc.Error as err:
        print(f"Error: '{err}'")
    return conn


connection = test_connection()
