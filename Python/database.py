from Python.db_connection import connection


def create_users_table(conn, table_name="USERS"):
    if not check_table_existence(conn, table_name):
        cursor = conn.cursor()
        cursor.execute(
            f"""
            CREATE TABLE {table_name} 
            (
                Id INT IDENTITY(1, 1),
                username varchar(200),
                password varchar(200),
                email varchar(200),
                PRIMARY KEY (Id)
                
            );
            """)
        conn.commit()
        cursor.close()


def create_data_table(conn, table_name="DATA"):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        CREATE TABLE {table_name} 
        (
            Id INT NOT NULL PRIMARY KEY,
            username varchar(200),
            password varchar(200)
        );
        """)
    conn.commit()
    cursor.close()


def check_table_existence(conn, table_name="USERS"):
    tables_exists = False
    cursor = conn.cursor()
    cursor.execute(
        f"""
        SELECT *
        FROM information_schema.TABLES
        """)
    tables = cursor.fetchall()

    conn.commit()
    cursor.close()

    # print(tables)
    for i in tables:
        # print(type(i), i, i[2])
        if i[2] == table_name:
            tables_exists = True
            print(F"{table_name} exists already")
            return tables_exists
    print(F"{table_name} Does not exist")
    return tables_exists


def create_user(conn, table_name="USERS", username="andre", password="11111111", email="abc@email.com"):
    # print("FUNCTION: Insert")
    if not check_email_exists(conn, email):
        cursor = conn.cursor()
        cursor.execute(f"""
        
        INSERT INTO {table_name}
        (username, password, email)
        values('{username}', '{password}', '{email}');
        
        """)
        conn.commit()
        print("REGISTERED USER")
    else:
        print("Email already exists")


def check_email_exists(conn, email="foreandr@gmail.com"):
    table_name = "USERS"
    cursor = conn.cursor()
    cursor.execute(f"""

    SELECT *
    FROM {table_name}
    WHERE email = '{email}'
    """)

    tables = cursor.fetchall()
    # for i in tables:
    #    print(i)

    # print(len(tables))
    if len(tables) > 0:
        return True
    else:
        return False


def delete_user(conn, table_name="USERS", user_id=0):
    cursor = conn.cursor()
    cursor.execute(
        f"""
        DELETE 
        FROM {table_name} 
        WHERE Id = {user_id};
        """)
    conn.commit()
    cursor.close()


def delete_all(conn, table_name="USERS"):
    cursor = conn.cursor()
    cursor.execute(f"""
    DELETE FROM {table_name};
    """)
    conn.commit()
    cursor.close()


def delete_data(conn):
    pass


def drop_table(conn, table_name="USERS"):
    if check_table_existence(conn, table_name):
        cursor = conn.cursor()
        cursor.execute(f"""
        DROP TABLE {table_name};
        
        """)
        conn.commit()
        cursor.close()
        print(F"DROPPED {table_name} successfully")


def select_users(conn):
    print("FUNCTION: SELECT\n")
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT * 
    FROM USERS

    """)

    tables = cursor.fetchall()
    for i in tables:
        print(i)
    cursor.close()


# TABLE RELATED
# drop_table(connection)
# create_users_table(connection)
# create_data_table(connection)

# USER RELATED
# create_user(conn=connection, username="hello", password="password", email="bce@hotmail.com")
# create_user(connection)
# delete_user()
# delete_all(connection)

# READ RELATED
#select_users(connection)
# check_email_exists(connection)
