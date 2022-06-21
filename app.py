import os
from flask import Flask, render_template, request, session, redirect, url_for, g
import Python.database as database
import Python.db_connection as connector
from werkzeug.datastructures import ImmutableMultiDict
import os

connection = connector.test_connection()
TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')
# import sql_functions

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = 'demokey'

# user = sql_functions.check_users() #list of user in DB

app.config["CSV UPLOADS"] = "C:/Users/forea/PycharmProjects/GraphTheory/#UserData"


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
    if request.method == "POST":
        if request.files:
            csv_file = request.files['csv']  # because name in HTML FORM is csv
            csv_file.save(os.path.join(app.config["CSV UPLOADS"], csv_file.filename))
            print("Saved and completed")
    return render_template('upload.html', message="upload.html page")


@app.route('/login', methods=['GET', 'POST'])  # homepage
def login():
    print('EXECUTING REGISTER FUNCTION')
    if request.method == 'GET':
        login_message = 'Please LOGIN'
        if "email" in session:
            return redirect(url_for("email"))
        return render_template('login.html', message=login_message)
    if request.method == "POST":
        email = request.form["email"]
        # password = request.form["password"]
        session["email"] = email

        print(session)
        print(email)
        # exit()
        return redirect(url_for("email"))


@app.route('/email', methods=['GET'])  # user_session_home
def email():
    if "email" in session:
        email = session["email"]  # getting user info from session variable
        return render_template('home.html', message=email)
    else:  # if not in session, redirect to login
        return redirect(url_for("login"))


@app.route('/logout', methods=['GET'])
def logout():
    session.pop("email", None)  # remove data from session
    return redirect(url_for("login"))


if __name__ == '__main__':
    my_port = 5006
    app.run(host='localhost', port=my_port, debug=True)  # host is to get off localhost
    # If the debugger is on, I can change my files in real time after saving
