from Python import CONSTANTS
from Python.db_connection import connection
from Python.helpers import print_green, print_title, print_error,  turn_pic_to_hex

# import CONSTANTS


def validate_user_from_session(conn, email, password):
    print(f"VALIDATE {email} | {password}")  # GET THIS FROM JAVASCRIPT
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT * 
    FROM USERS
    WHERE email = '{email}'
    AND password = '{password}'
    """)
    tables = cursor.fetchall()
    user = ""
    user_id = ""
    for i in tables:
        # print(i)
        user_id = i[0]
        user = i[1]

    if len(tables) > 0:
        print("SIGNING IN")
        return [True, user_id, user, email, password]
    else:
        print("NOT SIGNING IN")
        return [False]


def EXISTS_EMAIL(conn, email="foreandr@gmail.com"):
    table_name = "USERS"
    cursor = conn.cursor()
    cursor.execute(
        f"""
            SELECT *
            FROM {table_name}
            WHERE email = '{email}'
        """)

    tables = cursor.fetchall()
    if len(tables) > 0:
        return True
    else:
        return False


def USER_CREATE_TABLE(conn):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        CREATE TABLE USERS 
        (
            User_Id INT IDENTITY(1, 1) UNIQUE,
            username varchar(200),
            password varchar(200),
            email varchar(200) UNIQUE,
            PRIMARY KEY (User_Id)
        );
        """)
    conn.commit()
    cursor.close()
    print_green("USER CREATE COMPLETED")


def USER_INSERT(conn, username="Andre", password="password", email="foreandr@gmail.com"):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        INSERT INTO dbo.USERS
        (username, password, email)
        VALUES
        ('{username}', '{password}', '{email}');
        """)
    conn.commit()
    cursor.close()
    print_green("USER INSERT COMPLETED")


def USER_INSERT_MULTIPLE(conn):
    cursor = conn.cursor()
    cursor.execute(
        f"""
            INSERT INTO dbo.USERS
            (username, password, email)
            VALUES
            ('foreandr', 'cooldood', 'foreandr@gmail.com'),
            ('andrfore', '77734381', 'andrfore@gmail.com'),
            ('cheatsie', 'doodmanman', 'cheatsieog@gmail.com'),
            ('dnutty', 'helloworld', 'dnutty@gmail.com'),
            ('bigfrog', 'helloworld', 'bigfrog@gmail.com');
        """)
    conn.commit()
    cursor.close()
    print_green("USER MULTI INSERT COMPLETED")


def USER_FULL_RESET(conn):
    print_title("\nEXECUTING FULL RESET")
    cursor = conn.cursor()

    cursor.execute(f"DROP TABLE dbo.FILES;")
    conn.commit()

    cursor.execute(f"DROP TABLE dbo.USERS;")
    conn.commit()

    USER_CREATE_TABLE(conn)
    USER_INSERT_MULTIPLE(conn)
    FILES_CREATE_TABLE(conn)
    cursor.close()
    print_green("USER FULL_RESET COMPLETED")


def FILES_CREATE_TABLE(conn):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        CREATE TABLE FILES
        (
        File_id INT IDENTITY(1, 1),
        File_Type varchar(200),      
        File_PATH varchar(200),
        UserId INT NOT NULL,
        FOREIGN KEY (UserId) REFERENCES USERS(User_Id),
        PRIMARY KEY (File_id)
        );
        """)
    conn.commit()
    cursor.close()
    print_green("IMAGES CREATE COMPLETED")


def IMAGE_INSERT(conn, image_type, image_path, user_id):
    # print(conn, image_type, image_path, user_id)
    pass


'''
def IMAGE_INSERT(conn):
    cursor = conn.cursor()
    cursor.execute(
        f"""
            INSERT INTO dbo.IMAGES(Image_Type, Image_PATH, UserId)
            VALUES ('profile', 'GraphTheory\#DemoData', (SELECT User_Id from USERS WHERE User_Id = 17));
        );
        """)
    conn.commit()
    cursor.close()
    print("IMAGES INSERT COMPLETED")
    
'''

# USERS
# USER_FULL_RESET(connection)
# USER_CREATE_TABLE(connection)
# USER_INSERT(connection)
# USER_INSERT_MULTIPLE(connection)

# FILES
# FILES_CREATE_TABLE(connection)
