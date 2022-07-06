from PIL import Image

from Python.db_connection import connection
from Python.helpers import print_green, print_title, print_error, turn_pic_to_hex, check_and_save_dir


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
            username varchar(200) UNIQUE,
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
    full_register(conn, 'foreandr', 'cooldood', 'foreandr@gmail.com')
    full_register(conn, 'andrfore', 'cooldood', 'andrfore@gmail.com')
    full_register(conn, 'cheatsie', 'cooldood', 'cheatsieog@gmail.com')
    full_register(conn, 'dnutty', 'cooldood', 'dnutty@gmail.com')
    full_register(conn, 'bigfrog', 'cooldood', 'bigfrog@gmail.com')
    print_green("USER MULTI INSERT COMPLETED")


def CONNECTION_CREATE_TABLE(conn):
    cursor = conn.cursor()
    cursor.execute(
        f"""
            CREATE TABLE dbo.CONNECTIONS
            (
                Friendship_Id INT IDENTITY(1, 1),
                User_Id1 INT,
                User_Id2 INT,
                
                FOREIGN KEY (User_Id1) REFERENCES USERS(User_Id),
                FOREIGN KEY (User_Id2) REFERENCES USERS(User_Id),
                PRIMARY KEY (Friendship_Id, User_Id1, User_Id2)
            );
        """)
    conn.commit()
    cursor.close()
    print_green("CONNECTION CREATE COMPLETED")


def CONNECTION_INSERT(conn, user_id1, user_id2):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        EXECUTE  dbo.CUSTOM_INSERTION {user_id1}, {user_id2} ;
        """)
    conn.commit()
    cursor.close()
    print_green('CONNECTION INSERT COMPLETED')


def CONNECTION_INSERT_MULTIPLE(conn):
    CONNECTION_INSERT(conn, 1, 2)
    CONNECTION_INSERT(conn, 1, 3)
    CONNECTION_INSERT(conn, 1, 4)
    CONNECTION_INSERT(conn, 1, 5)

    CONNECTION_INSERT(conn, 2, 3)
    CONNECTION_INSERT(conn, 2, 4)
    CONNECTION_INSERT(conn, 2, 5)

    CONNECTION_INSERT(conn, 3, 4)
    CONNECTION_INSERT(conn, 3, 5)

    print_green("USER MULTI INSERT COMPLETED")


def USER_FULL_RESET(conn):
    print_title("\nEXECUTING FULL RESET")
    cursor = conn.cursor()

    cursor.execute(f"DROP TABLE dbo.FILES;")
    conn.commit()

    cursor.execute(f"DROP TABLE dbo.CONNECTIONS;")
    conn.commit()

    cursor.execute(f"DROP TABLE dbo.USERS;")
    conn.commit()

    # CREATE NEW USERS
    USER_CREATE_TABLE(conn)
    USER_INSERT_MULTIPLE(conn)

    # FILE TABLE CREATIONS
    FILES_CREATE_TABLE(conn)

    # CONNECTION TABLE
    CONNECTION_CREATE_TABLE(conn)
    CONNECTION_INSERT_MULTIPLE(conn)

    cursor.close()
    print_green("USER FULL_RESET COMPLETED")


def FILES_CREATE_TABLE(conn):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        CREATE TABLE FILES
        (
        File_id INT IDENTITY(1, 1),   
        File_PATH varchar(200),
        UserId INT NOT NULL,
        Date_Time DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (UserId) REFERENCES USERS(User_Id),
        PRIMARY KEY (File_id)
        );
        """)
    conn.commit()
    cursor.close()
    print_green("FILES CREATE COMPLETED")


def FILE_INSERT(conn, image_path="NO PATH", user_id=1):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        INSERT INTO dbo.FILES
        (File_PATH, UserId)
        VALUES
        ('{image_path}', '{user_id}');
        """)
    conn.commit()
    cursor.close()
    print_green("FILE INSERT COMPLETED")


def GET_FRIENDS(conn, username):
    print('GET FRIENDS: ', username)
    cursor = conn.cursor()
    cursor.execute(f"EXECUTE GET_FRIENDS {username} ;")
    user_friends = []
    friends = cursor.fetchall()
    for friend in friends:
        # print(friend)
        user_friends.append(friend[8])  # friend index is 8
    return user_friends


def register_user_files(username):
    check_and_save_dir(f"../static/#UserData/{username}/profile")
    check_and_save_dir(f"../static/#UserData/{username}/csv_files")
    check_and_save_dir(f"../static/#UserData/{username}/photos")

    my_path = f"../static/#UserData/{username}/profile"
    my_path_with_file = f"../static/#UserData/{username}/profile/profile_pic.jpg"  # PREVIOUSLY USED file.filename, should use with other types

    jpgfile = Image.open("./#DemoData/DEFAULT_PROFILE.png")
    check_and_save_dir(my_path)
    jpgfile.save(my_path_with_file)


def full_register(connection, username, password, email):
    # print_green(F"INSERT VALUES: \nUSERNAME: {username}\nPASSWORD: {password}\nEMAIL: {email}")
    # TODO: DELETE ALL FILES ASSOCIATED WITH USER
    USER_INSERT(connection, username, password, email)
    register_user_files(username)

def GET_FILES(conn, username):
    print('GET FRIENDS: ', username)
    cursor = conn.cursor()
    cursor.execute(f"EXECUTE GET_FILES {username} ;")
    user_friends = []
    friends = cursor.fetchall()
    #for friend in friends:
    #     # print(friend)
    #    user_friends.append(friend[8])  # friend index is 8
    return user_friends

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
# FILES_CREATE_TABLE(connection)
