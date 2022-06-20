import os
from flask import Flask, render_template, request, session, redirect, url_for, g
import Python.database as database
import Python.db_connection as connector
from werkzeug.datastructures import ImmutableMultiDict

connection = connector.test_connection()
TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')
# import sql_functions

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = 'demokey'

# user = sql_functions.check_users() #list of user in DB

@app.route('/', methods=['GET'])  # homepage
def home():
    print('EXECUTING HOME FUNCTION')
    return render_template('index.html', message="index.html page")


@app.route('/register', methods=['GET', 'POST'])  # homepage
def register():
    print('EXECUTING REGISTER FUNCTION')
    print(request.form)
    dict = request.form.to_dict(flat=False)
    try: # DO NOT EXECUTE UNTIL SUBMIT IS CLICKED
        username = dict['username']
        password = dict['password']
        email = dict['email']

        # database.create_user(conn=connection, username="hello", password="password", email="bce@hotmail.com")
        database.create_user(conn=connection, username=username[0], password=password[0], email=email[0])
        print("REGISTERED USER")
    except:
        print("Error on HTML POST Register")


    return render_template('register.html', message="register.html page")


if __name__ == '__main__':
    my_port = 5006
    app.run(host='localhost', port=my_port, debug=True)  # host is to get off localhost
    # If the debugger is on, I can change my files in real time after saving
