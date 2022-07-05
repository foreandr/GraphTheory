import os
from flask import Flask, render_template, request, session, redirect, url_for, g
import Python.database as database
import Python.db_connection as connector
from werkzeug.datastructures import ImmutableMultiDict
import os
from PIL import Image
import Python.helpers as helpers

connection = connector.test_connection()
TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')
# import sql_functions

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = 'demokey'

# user = sql_functions.check_users() #list of user in DB

app.config["FILE UPLOADS"] = "static/#UserData"


@app.route('/', methods=['GET'])  # homepage
def home():
    print('EXECUTING INDEX FUNCTION')
    return render_template('index.html', message="index.html page")


@app.route('/register', methods=['GET', 'POST'])
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
            database.full_register(connection=connection, username=username[0], password=password[0], email=email[0])

            my_path = f"{app.config['FILE UPLOADS']}/{username[0]}/profile"
            my_path_with_file = f"{app.config['FILE UPLOADS']}/{username[0]}/profile/profile_pic.jpg"  # PREVIOUSLY USED file.filename, should use with other types

            jpgfile = Image.open("static/#DemoData/DEFAULT_PROFILE.png")
            helpers.check_and_save_dir(my_path)
            jpgfile.save(my_path_with_file)

        except:
            print("Error on HTML POST Register")
        return render_template('register.html', message="register.html page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    print('EXECUTING LOGIN FUNCTION')
    if "email" in session:
        email = session["email"]  # getting user info from session variable
        return render_template('index.html', message=email)
    if request.method == 'GET':
        login_message = 'Please LOGIN'
        if "email" in session:
            return redirect(url_for("index"))
        return render_template('login.html', message=login_message)
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        signed_in = database.validate_user_from_session(connection, email, password)

        if signed_in[0]:
            session["id"] = signed_in[1]
            session["user"] = signed_in[2]
            session["email"] = email
            session["password"] = password
            print('SESSION INFO: ', session)
            return redirect(url_for("home"))
        else:
            return render_template('login.html', message="wrong email or password, try again")


@app.route('/logout', methods=['GET'])
def logout():
    session.pop("email", None)  # remove data from session
    return redirect(url_for("login"))


@app.route('/user_profile', methods=['GET', 'POST'])  # user_session_home
def user_profile():
    print('USING USER PROFILE')
    # print(request)
    if "email" not in session:
        return redirect(url_for('login'))
    elif request.method == "GET":
        print('USING USER PROFILE - GET')
        print(session)
        # return redirect(url_for("user_profile"))
        return redirect(url_for('user_profile_name', username=session['user']))

        # return render_template(f"user_profiles/{session['user']}.html", friends=my_friends,account_name=session['user'])

    elif request.method == "POST":

        password = session["password"]
        email = session["email"]
        user = session["user"]
        id = session["id"]

        print("ID:", id)
        print("USERNAME:", user)
        print("PASSWORD:", password)
        print("EMAIL   :", email)
        print("-------")
        if request.files:
            file = request.files['file']  # because name in HTML FORM is file
            # print(file)
            # print(app.config["FILE UPLOADS"])
            # print(file.filename)

            print("FILE", file.content_type, type(file.content_type))
            if file.content_type == "text/csv": # if it's a csv file, store it at the user location
                # TODO: SAVE CSV FILES TO SPECIFIC LOCATION
                pass
            my_path = f"{app.config['FILE UPLOADS']}/{user}/profile"
            my_path_with_file = f"{app.config['FILE UPLOADS']}/{user}/profile/profile_pic.jpg"  # PREVIOUSLY USED file.filename, should use with other types

            helpers.check_and_save_dir(my_path)
            file.save(my_path_with_file)

            print("MY PATH:", my_path)
            print("MY PATH W/F:", my_path_with_file)
            database.IMAGE_INSERT(
                connection,
                image_type=helpers.get_filetype(file.filename),
                image_path=my_path_with_file,
                user_id=id
            )
            print("-------")
            print("Saved and completed")
        # return redirect(url_for("user_profile", message="hi")) # THIS APPEARS IN THE ADDRESS BAR AS A QUERY
        return redirect(url_for("user_profile"))


@app.route('/<username>', methods=['GET', 'POST'])
def user_profile_name(username):
    # return f"welcome to profile page {username}"
    my_friends = database.GET_FRIENDS(connection, username)
    # print(send_string)
    return render_template(f"user_profile.html", friends=my_friends, account_name=username)


if __name__ == '__main__':
    my_port = 5006
    app.run(host='localhost', port=my_port, debug=True)  # host is to get off localhost
    # If the debugger is on, I can change my files in real time after saving
