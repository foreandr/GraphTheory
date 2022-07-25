import os
import shutil
from pathlib import Path

from PIL import Image
import datetime

from pyodbc import Error

from Python.db_connection import connection
from Python.helpers import print_green, print_title, print_error, turn_pic_to_hex, check_and_save_dir, print_warning


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


def GET_USER_ID(conn, username):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        EXECUTE  dbo.GET_USER_ID {username};
        """)
    tables = cursor.fetchall()
    user_id = 0
    for i in tables:
        print(i)
        user_id = i[0]
    cursor.close()
    print_green('GET_USER_ID')
    return user_id


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
    print_green("USER CREATE COMPLETED\n")


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
    # Change the current working directory

    shutil.rmtree('../static/#UserData/')
    full_register(conn, 'foreandr', 'cooldood', 'foreandr@gmail.com')
    full_register(conn, 'andrfore', 'cooldood', 'andrfore@gmail.com')
    full_register(conn, 'cheatsie', 'cooldood', 'cheatsieog@gmail.com')
    full_register(conn, 'dnutty', 'cooldood', 'dnutty@gmail.com')
    full_register(conn, 'bigfrog', 'cooldood', 'bigfrog@gmail.com')
    print_green("USER MULTI INSERT COMPLETED\n")


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
    print_green("CONNECTION CREATE COMPLETED\n")


def CONNECTION_INSERT(conn, user_id1, user_id2):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        EXECUTE  dbo.CUSTOM_INSERTION {user_id1}, {user_id2} ;
        """)
    conn.commit()
    cursor.close()
    print_green('CONNECTION INSERT COMPLETED')


def CONNECTION_REMOVE(connection, user_id_first, user_id_second):
    cursor = connection.cursor()
    cursor.execute(
        f"""
        EXECUTE dbo.CUSTOM_DELETION {user_id_first}, {user_id_second} ;
        """)
    connection.commit()
    cursor.close()
    print_green('CONNECTION DELETION COMPLETED')


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

    print_green("USER MULTI INSERT COMPLETED\n")


def USER_INSERT_MULTPLE_FILES(conn):
    FILE_INSERT(conn,
                image_path=f'static/#UserData/foreandr/csv_files/CSV1.csv',
                description=f"description 1",
                user_id=1)
    FILE_INSERT(conn,
                image_path=f'static/#UserData/foreandr/csv_files/CSV10.csv',
                description=f"description 10",
                user_id=1)
    FILE_INSERT(conn,
                image_path=f'static/#UserData/andrfore/csv_files/CSV5.csv',
                description=f"description 5",
                user_id=2)
    FILE_INSERT(conn,
                image_path=f'static/#UserData/cheatsie/csv_files/CSV3.csv',
                description=f"description 3",
                user_id=3)
    FILE_INSERT(conn,
                image_path=f'static/#UserData/bigfrog/csv_files/CSV2.csv',
                description=f"description 2",
                user_id=5)
    FILE_INSERT(conn,
                image_path=f'static/#UserData/dnutty/csv_files/CSV4.csv',
                description=f"description 4",
                user_id=4)
    print_green("USER INSERT MULTPLE FILES COMPLETED\n")


def VOTE_CREATE_TABLE(conn):
    cursor = conn.cursor()
    cursor.execute(
        f"""
            CREATE TABLE dbo.CSV_VOTES(
            CSV_Vote_Id INT IDENTITY(1, 1),
            File_id INT,
            Voter_Username varchar(50) UNIQUE,
            FOREIGN KEY (File_id) REFERENCES FILES(File_id),
            PRIMARY KEY (CSV_Vote_Id)
        )
        """)
    conn.commit()
    cursor.close()
    print_green("VOTE CREATE TABLE COMPLETED")


def VOTE_INSERT_DEMO(conn):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        EXECUTE dbo.ENTER_CSV_VOTE 2, 'foreandr';
        """)
    cursor.execute(
        f"""
        EXECUTE dbo.ENTER_CSV_VOTE 5, 'andrfore'
        """)
    cursor.execute(
        f"""
        EXECUTE dbo.ENTER_CSV_VOTE 5, 'cheatsie'
        """)
    cursor.execute(
        f"""
        EXECUTE dbo.ENTER_CSV_VOTE 5, 'dnutty'
        """)
    cursor.execute(
        f"""
        EXECUTE dbo.ENTER_CSV_VOTE 2, 'bigfrog'
        """)
    conn.commit()
    cursor.close()
    print_green("VOTE_INSERT_DEMO\n")


def FILE_GET_VOTES_COUNT_BY_ID(conn, file_id):
    cursor = conn.cursor()
    cursor.execute(f"""EXECUTE dbo.GET_FILE_VOTE_COUNT {file_id};""")
    votes = cursor.fetchall()
    num_votes = 0
    for i in votes:
        num_votes = i[0]
    cursor.close()
    # print_green("GOT VOTES BY ID")
    return num_votes


def MODEL_CREATE_TABLE(conn):
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE dbo.MODEL(
        Model_id INT IDENTITY(1,1) NOT NULL,
        Local_File_PATH varchar(200),
        Model_Description varchar(400),
        Date_Time datetime,
        Foreign_File_id int,
        Uploader varchar(200) UNIQUE,
        FOREIGN KEY (Foreign_File_id) REFERENCES FILES(File_id),
        FOREIGN KEY (Uploader) REFERENCES USERS(Username),
        PRIMARY KEY (Model_id)
        )"""
                   )
    conn.commit()
    cursor.close()
    print_green("CREATED MODEL TABLE\n")


def MODEL_VOTES_CREATE_TABLE(conn):
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE dbo.MODEL_VOTES(
        MODEL_Vote_Id INT IDENTITY(1, 1),
        Model_id INT,
        Voter_Username varchar(50) UNIQUE, -- so there can only be one vote per person
        FOREIGN KEY (Model_id) REFERENCES dbo.MODEL(Model_id),
        PRIMARY KEY (MODEL_Vote_Id)
        )"""
                   )
    conn.commit()
    cursor.close()
    print_green("CREATED MODEL VOTES TABLE\n")


def USER_FULL_RESET(conn):
    print_title("\nEXECUTING FULL RESET")
    cursor = conn.cursor()

    try:
        cursor.execute(f"DROP TABLE dbo.MODEL_VOTES;")
        conn.commit()
    except Exception as e:
        print_warning("NO dbo.MODEL VOTES" + str(e))

    try:
        cursor.execute(f"DROP TABLE dbo.MODEL;")
        conn.commit()
    except Exception as e:
        print_warning("NO dbo.MODEL" + str(e))

    try:
        cursor.execute(f"DROP TABLE dbo.CSV_VOTES;")
        conn.commit()
    except Exception as e:
        print_warning("NO dbo.CSV_VOTES" + str(e) )

    try:
        cursor.execute(f"DROP TABLE dbo.FILES;")
        conn.commit()
    except Exception as e:
        print_warning("NO dbo.FILES" + str(e))

    try:
        cursor.execute(f"DROP TABLE dbo.CONNECTIONS;")
        conn.commit()
    except Exception as e:
        print_warning("NO dbo.dbo.CONNECTIONS" + str(e))

    try:
        cursor.execute(f"DROP TABLE dbo.USERS;")
        conn.commit()
    except Exception as e:
        print_warning("NO dbo.dbo.USERS: " + str(e))

    # CREATE NEW USERS
    USER_CREATE_TABLE(conn)
    USER_INSERT_MULTIPLE(conn)

    # FILE TABLE CREATIONS
    FILES_CREATE_TABLE(conn)
    USER_INSERT_MULTPLE_FILES(conn)

    # VOTE RELATED
    VOTE_CREATE_TABLE(conn)
    VOTE_INSERT_DEMO(conn)

    # MODEL RELATED
    MODEL_CREATE_TABLE(conn)
    MODEL_MULTIPLE_INSERT(conn)
    MODEL_VOTES_CREATE_TABLE(conn)

    # CONNECTION TABLE
    CONNECTION_CREATE_TABLE(conn)
    CONNECTION_INSERT_MULTIPLE(conn)

    cursor.close()
    print_title("USER FULL RESET COMPLETED")


def FILES_CREATE_TABLE(conn):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        CREATE TABLE FILES
        (
        File_id INT IDENTITY(1, 1),   
        File_PATH varchar(200),
        File_size BIGINT,
        Description varchar(400),
        UserId INT NOT NULL,        
        Date_Time DATETIME DEFAULT CURRENT_TIMESTAMP,      
        FOREIGN KEY (UserId) REFERENCES USERS(User_Id),
        PRIMARY KEY (File_id)
        );
        """)
    conn.commit()
    cursor.close()
    print_green("FILES CREATE COMPLETED\n")


def FILE_INSERT(conn, image_path="NO PATH", description="default description", user_id=1, file_size=0):
    print("MY_PATH :", image_path)
    cursor = conn.cursor()
    cursor.execute(
        f"""
        INSERT INTO dbo.FILES
        (File_PATH, Description, UserId, File_size)
        VALUES
        ('{image_path}', '{description}','{user_id}',{file_size});
        """)
    conn.commit()
    cursor.close()
    print_green("FILE INSERT COMPLETED")


def GET_FRIENDS(conn, username):
    print('GET FRIENDS: ', username)
    cursor = conn.cursor()
    cursor.execute(f"EXECUTE GET_FRIENDS {username};")
    user_friends = []
    friends = cursor.fetchall()
    for friend in friends:
        # print(friend)
        user_friends.append(friend[8])  # friend index is 8
    return user_friends


def CUSTOM_MODEL_INSERT(conn, new_path="/PATH.JPG", description='DEAFULT MODEL DESCRIPTION', csv_id=2,
                        uploader_username='foreandr'):
    print_green(f'INSERT INTO MODELS {new_path}.{csv_id},{uploader_username}')
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"EXECUTE dbo.CUSTOM_MODEL_INSERT '{new_path}', '{description}', {csv_id} , '{uploader_username}';")
    except Exception as e:
        print_error(F"CANNOT INSERT {new_path} INTO {uploader_username} - NOT SURE WHY\n" + str(e))

    conn.commit()
    cursor.close()


def GET_ALL_DATASETS_BY_DATE(conn, minimum=1, maximum=100):
    print(f'GET ALL DATASETS | MIN:{minimum} MAX:{maximum}')
    cursor = conn.cursor()
    cursor.execute(f"EXECUTE dbo.GET_ALL_DATASETS_BY_DATE {maximum};")
    user_info = []
    files = cursor.fetchall()
    for details in files:
        user_info.append([details[0], details[1], details[2], details[3], details[4], details[5]])

    # for i in user_info:
    #    print(i)

    names = ""
    files = ""
    descriptions = ""
    dates = ""
    sizes = ""
    num_votes = ""
    for i in user_info:
        # print(i)
        names += i[0] + "//"

        filename = i[1].split('//')[-1]
        files += filename + "//"

        descriptions += i[2] + "//"

        dates += str(i[3]) + "//"

        sizes += str(i[4]) + "//"

        num_votes += str(FILE_GET_VOTES_COUNT_BY_ID(conn, i[5])) + "//"

    # print("Worked", names, files, descriptions, dates)
    return names, files, descriptions, dates, sizes, num_votes


def register_user_files(conn, username):
    # Change the current working directory
    os.chdir('/GraphTheory')

    check_and_save_dir(f"static/#UserData/{username}/profile")
    check_and_save_dir(f"static/#UserData/{username}/csv_files")
    check_and_save_dir(f"static/#UserData/{username}/models")

    my_path = f"static/#UserData/{username}/profile"
    my_path_with_file = f"static/#UserData/{username}/profile/profile_pic.jpg"  # PREVIOUSLY USED file.filename, should use with other types

    jpgfile = Image.open("#DemoData/DEFAULT_PROFILE.png")
    check_and_save_dir(my_path)
    jpgfile.save(my_path_with_file)

    # SETTING UP DEFAULT FILES
    default_csv = ""
    target = ""
    fake_chart = ""
    model_target = ""
    # print('PRINTING WORKING DIRECTORY', os.getcwd())
    if username == 'foreandr':
        default_csv = r'#DemoData/CSV1.csv'
        target = rf'static/#UserData/{username}/csv_files/CSV1.csv'
        shutil.copyfile(default_csv, target)

        # DO TWICE FOR TEST WITH MULTIPLE FILES
        default_csv2 = r'#DemoData/CSV1.csv'
        target2 = rf'static/#UserData/{username}/csv_files/CSV10.csv'
        shutil.copyfile(default_csv2, target2)

    elif username == 'bigfrog':
        default_csv = r'#DemoData/CSV2.csv'
        target = rf'static/#UserData/{username}/csv_files/CSV2.csv'
        shutil.copyfile(default_csv, target)

    elif username == 'cheatsie':
        default_csv = r'#DemoData/CSV3.csv'
        target = rf'static/#UserData/{username}/csv_files/CSV3.csv'
        shutil.copyfile(default_csv, target)

    elif username == 'dnutty':
        default_csv = r'#DemoData/CSV4.csv'
        target = rf'static/#UserData/{username}/csv_files/CSV4.csv'
        shutil.copyfile(default_csv, target)

    elif username == 'andrfore':
        default_csv = r'#DemoData/CSV5.csv'
        target = rf'static/#UserData/{username}/csv_files/CSV5.csv'
        shutil.copyfile(default_csv, target)


def MODEL_MULTIPLE_INSERT(conn):
    # SETTING UP DEFAULT FILES

    fake_chart = ""
    model_target = ""

    fake_chart = r'#DemoData/fakechart1.jpg'
    model_target = rf'static/#UserData/foreandr/models/fakechart1.jpg'
    CUSTOM_MODEL_INSERT(conn, model_target, 'description', 2, 'foreandr')
    shutil.copyfile(fake_chart, model_target)

    fake_chart = r'#DemoData/fakechart2.jpg'
    model_target = rf'static/#UserData/bigfrog/models/fakechart2.jpg'
    CUSTOM_MODEL_INSERT(conn, model_target, 'description', 1, 'andrfore')
    shutil.copyfile(fake_chart, model_target)

    fake_chart = r'#DemoData/fakechart4.jpg'
    model_target = rf'static/#UserData/dnutty/models/fakechart4.jpg'
    CUSTOM_MODEL_INSERT(conn, model_target, 'description', 2, 'dnutty')
    shutil.copyfile(fake_chart, model_target)

    fake_chart = r'#DemoData/fakechart5.jpg'
    model_target = rf'static/#UserData/andrfore/models/fakechart5.jpg'
    CUSTOM_MODEL_INSERT(conn, model_target, 'description', 3, 'bigfrog')
    shutil.copyfile(fake_chart, model_target)

    fake_chart = r'#DemoData/fakechart3.jpg'
    model_target = rf'static/#UserData/cheatsie/models/fakechart3.jpg'
    CUSTOM_MODEL_INSERT(conn=conn, new_path=model_target, description='description', csv_id=2,
                        uploader_username='cheatsie')
    shutil.copyfile(fake_chart, model_target)

    print_green('MODEL MULTIPLE INSERTS COMPELTED\n')


def full_register(connection, username, password, email):
    # print_green(F"INSERT VALUES: \nUSERNAME: {username}\nPASSWORD: {password}\nEMAIL: {email}")
    # DELETING A PARTCIULAR USER
    # try:
    #    DELETE_USER_FILES(username)
    # except:
    #    print_warning("User doesn't exist")
    USER_INSERT(connection, username, password, email)
    register_user_files(connection, username)
    # FILE_INSERT(connection


def GET_FILES(conn, username):
    print('GET FILES: ', username)
    cursor = conn.cursor()
    cursor.execute(f"EXECUTE GET_FILES {username} ;")
    user_files = []
    files = cursor.fetchall()
    for file in files:
        # print(friend)
        user_files.append([file[1], file[3], file[5], file[2]])  # friend index is 8
    # print(user_files)
    # print_title("PRINTING USER FILES")
    for i in user_files:
        print(i)
    file_names = ""
    descriptions = ""
    dates = ""
    sizes = ""
    for i in user_files:
        filename = i[0].split('/')[-1]  # split the string by / and get the last for filename\
        file_names += filename + "//"

        description = i[1]
        descriptions += str(description) + "//"
        # print("DESCRIPTION: ", description)
        # print("DESCRIPTIONS: ", descriptions)

        t = str(i[2])
        dates += t + "//"

        size = str(i[3])
        sizes += size + "//"
    # print(file_names)
    # print(descriptions)
    # print(dates)
    return file_names, descriptions, dates, sizes


def DELETE_USER_FILES(user):
    file_location = f"../static/#UserData/{user}/profile"
    file_location2 = f"../static/#UserData/{user}/csv_files"
    file_location3 = f"../static/#UserData/{user}/photos"

    user_folders = [file_location, file_location2, file_location3]
    ## Try to remove tree; if failed show an error using try...except on screen
    for i in user_folders:
        try:
            shutil.rmtree(i)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))


def CHANGE_PASSWORD(conn, email, password):
    cursor = conn.cursor()
    cursor.execute(
        f"""
            EXECUTE dbo.CHANGE_PASSWORD_FOR_EMAIL '{email}', '{password}' ;
        """)
    conn.commit()
    cursor.close()
    print_green('CHANGE_PASSWORD COMPLETED')


def MODEL_DROP_TABLE(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(f"DROP TABLE dbo.MODEL;")
        conn.commit()
    except Exception as e:
        print_warning("NO dbo.MODEL" + str(e))


def GET_FILE_ID_W_USERNAME(conn, username, file_name):
    cursor = conn.cursor()
    cursor.execute(f"EXECUTE dbo.GET_FILE_ID '{username}', '{file_name}';")
    id = None
    user_results = cursor.fetchall()
    for result in user_results:
        id = result[0]  # friend index is 8
    return id


def MODEL_GET_NUM_VOTES_BY_MODEL_ID(conn, model_id):
    cursor = conn.cursor()
    cursor.execute(f"EXECUTE dbo.MODEL_GET_NUM_VOTES_BY_MODEL_ID {model_id};")
    count = cursor.fetchall()
    num = ""
    for i in count:
        # print('zzzzz', i)
        num = i[0]
    return num


def GET_MODELS_BY_FILE_ID(conn, file_id):
    cursor = conn.cursor()
    cursor.execute(f"EXECUTE dbo.GET_MODELS_BY_FILE_ID {file_id};")
    file_results = cursor.fetchall()

    model_ids = ""
    local_paths = ""
    model_descriptions = ""
    dates = ""
    foreign_file_id = ""
    model_uploaders = ""
    model_user_ids = ""
    csv_file_paths = ""
    file_sizes = ""
    csv_description = ""
    csv_user_id = ""
    csv_upload_date = ""
    num_model_votes = ""
    for i in file_results:
        # print(i)
        model_ids += str(i[0]) + "//"
        local_paths += str(i[1]) + "//"
        model_descriptions += str(i[2]) + "//"
        dates += str(i[3]) + "//"
        foreign_file_id += str(i[4]) + "//"
        model_uploaders += str(i[5]) + "//"
        model_user_ids += str(i[6]) + "//"
        csv_file_paths += str(i[7]) + "//"
        file_sizes += str(i[8]) + "//"
        csv_description += str(i[9]) + "//"
        csv_user_id += str(i[10]) + "//"
        csv_upload_date += str(i[11]) + "//"
        num_model_votes += str(MODEL_GET_NUM_VOTES_BY_MODEL_ID(conn, i[0])) + "//"
        # print('MODEL ID: ', i[0])
    print_green('COMPLETED GET_MODELS_BY_FILE_ID')
    return model_ids, local_paths, model_descriptions, dates, foreign_file_id, model_uploaders, model_user_ids, csv_file_paths, file_sizes, csv_description, csv_user_id, csv_upload_date, num_model_votes
# USERS
# USER_CREATE_TABLE(connection)
# USER_INSERT(connection)
# USER_INSERT_MULTIPLE(connection)

# FILES
# FILES_CREATE_TABLE(connection)
# FILES_CREATE_TABLE(connection)
# GET_FILES(connection, 'foreandr')
# GET_ALL_DATASETS_BY_DATE(connection)
# print(FILE_GET_VOTES_COUNT_BY_ID(connection, 1))

# VOTE RELATED
# VOTE_INSERT_DEMO(connection)

# MODEL RELATED
# CUSTOM_MODEL_INSERT(connection, new_path="/PATH.JPG", csv_id=2, uploader_username='foreandr')
# MODEL_DROP_TABLE(connection)
# MODEL_CREATE_TABLE(connection)
# MODEL_MULTIPLE_INSERT(connection)
# GET_MODELS_BY_FILE_ID(connection, 2)
