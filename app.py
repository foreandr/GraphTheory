import os
from flask import Flask, render_template, request, session, redirect, url_for, g
import Python.database as database
import Python.db_connection as connector
from werkzeug.datastructures import ImmutableMultiDict
import os

from Python import helpers

connection = connector.test_connection()
TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')
# import sql_functions

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = 'demokey'

# user = sql_functions.check_users() #list of user in DB

app.config["FILE UPLOADS"] = "#UserData"


@app.route('/', methods=['GET'])  # homepage
def home():
    print('EXECUTING HOME FUNCTION')
    return render_template('index.html', message="index.html page")


@app.route('/register', methods=['GET', 'POST'])  # homepage
def register():
    print('EXECUTING REGISTER FUNCTION')
    if request.method == 'GET':
        sign_up_message = 'Please sign up'
        return render_template('register.html', message=sign_up_message)

    if request.method == 'POST':
        dict = request.form.to_dict(flat=False)
        try:  # DO NOT EXECUTE UNTIL SUBMIT IS CLICKED
            username = dict['username']
            password = dict['password']
            email = dict['email']

            # database.create_user(conn=connection, username="hello", password="password", email="bce@hotmail.com")
            database.create_user(conn=connection, username=username[0], password=password[0], email=email[0])
        except:
            print("Error on HTML POST Register")
        return render_template('register.html', message="register.html page")


@app.route('/upload', methods=['GET', 'POST'])  # homepage
def upload_file():
    if "email" not in session:
        return render_template('login.html')
    if request.method == "POST":
        password = session["password"]
        email = session["email"]
        user = session["user"]
        print("USERNAME:", user)
        print("PASSWORD:", password)
        print("EMAIL   :", email)
        print("-------")
        if request.files:
            file = request.files['file']  # because name in HTML FORM is csv
            #print(file)
            #print(app.config["FILE UPLOADS"])
            #print(file.filename)
            my_path_with_file = f"{app.config['FILE UPLOADS']}/{user}/{file.filename}"
            my_path = f"{app.config['FILE UPLOADS']}/{user}"
            helpers.check_and_save_dir(my_path)
            file.save(my_path_with_file)

            print(my_path)
            print(my_path_with_file)
            database.insert_image(
                connection,
                file.filename,
                helpers.get_filetype(file.filename),
                my_path_with_file,
                10
            )
            print("-------")
            print("Saved and completed")
    return render_template('upload.html', message="upload.html page")


@app.route('/login', methods=['GET', 'POST'])  # homepage
def login():
    print('EXECUTING LOGIN FUNCTION')
    if "email" in session:
        email = session["email"]  # getting user info from session variable
        return render_template('home.html', message=email)
    if request.method == 'GET':
        login_message = 'Please LOGIN'
        if "email" in session:
            return redirect(url_for("email"))
        return render_template('login.html', message=login_message)
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        signed_in = database.validate_user_from_session(connection, email, password)

        if signed_in[0]:
            session["user"] = signed_in[1]
            session["email"] = email
            session["password"] = password
            print(session)
            print(email)
            print(password)
            return redirect(url_for("email"))
        else:
            return render_template('login.html', message="wrong email or password, try again")


@app.route('/logout', methods=['GET'])
def logout():
    session.pop("email", None)  # remove data from session
    return redirect(url_for("login"))


@app.route('/email', methods=['GET'])  # user_session_home
def email():
    if "email" in session:
        email = session["email"]  # getting user info from session variable
        return render_template('home.html', message=email)
    else:  # if not in session, redirect to login
        return redirect(url_for("login"))


@app.route('/user_profile', methods=['GET'])  # user_session_home
def user_profile():
    if "email" not in session:
        return render_template('login.html')
    else:
        return render_template('user_profile.html', message='PROFILE PAGE')


if __name__ == '__main__':
    my_port = 5006
    app.run(host='localhost', port=my_port, debug=True)  # host is to get off localhost
    # If the debugger is on, I can change my files in real time after saving
