import os
from flask import Flask, render_template, request, session, redirect, url_for, g, send_from_directory, Response
import Python.database as database
import Python.db_connection as connector
from werkzeug.datastructures import ImmutableMultiDict
import os
from PIL import Image
import Python.helpers as helpers
from Python import my_email

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
    usernames, paths, descriptions, dates, file_sizes, num_votes = database.GET_ALL_DATASETS_BY_DATE(connection)

    return render_template('index.html',
                           message="index.html page",
                           usernames=usernames,
                           paths=paths,
                           descriptions=descriptions,
                           dates=dates,
                           file_sizes=file_sizes,
                           votes=num_votes
                           )


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

            #my_path = f"{app.config['FILE UPLOADS']}/{username[0]}/profile"
            #my_path_with_file = f"{app.config['FILE UPLOADS']}/{username[0]}/profile/profile_pic.jpg"  # PREVIOUSLY USED file.filename, should use with other types

            #jpgfile = Image.open("#DemoData/DEFAULT_PROFILE.png")
            #helpers.check_and_save_dir(my_path)
            #jpgfile.save(my_path_with_file)

        except Exception as e:
            print("Error on HTML POST Register", e)
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

        password = session["password"]  # DON'T NEED?
        email = session["email"]  # DON'T NEED?
        user = session["user"]
        id = session["id"]

        # print("ID:", id)
        # print("USERNAME:", user)
        # print("PASSWORD:", password)
        # print("EMAIL   :", email)
        # print("-------")
        if request.files:
            file = request.files['file']  # because name in HTML FORM is file
            my_description = ""  # only here because needs to be global
            my_file_size = 0
            # print(request.headers)

            # print(file)
            # print(app.config["FILE UPLOADS"])
            # print(file.filename)
            my_path_with_file = ""
            # print("FILE", file.content_type, type(file.content_type))
            if file.content_type == "text/csv":  # if it's a csv file, store it at the user location
                my_path_with_file = f"{app.config['FILE UPLOADS']}/{user}/csv_files/{file.filename}"
                file.save(my_path_with_file)

                my_description = request.form["description"]
                my_file_size = request.form["hidden_file_size"]

            elif file.content_type == "image/jpeg" or file.content_type == "image/png":
                my_path_with_file = f"{app.config['FILE UPLOADS']}/{user}/profile/profile_pic.jpg"  # overriding file type
                file.save(my_path_with_file)

            # print("MY PATH:", my_path)
            print("MY PATH W/F:", my_path_with_file)
            database.FILE_INSERT(
                connection,
                image_path=my_path_with_file,
                description=my_description,
                user_id=id,
                file_size=my_file_size

            )
            print("OUT OF CHECKING FILETYPE-------")
            print("Saved and completed")
        # return redirect(url_for("user_profile", message="hi")) # THIS APPEARS IN THE ADDRESS BAR AS A QUERY
        return redirect(url_for("user_profile"))


@app.route('/<username>', methods=['GET', 'POST'])
def user_profile_name(username):
    print('EXECUTING WITH ARGUMENT: ', username)
    # IF WE ARE GOING TO A CSV PROFILE
    # TODO: IF IT IS A CSV FILE, DIFFERENT PROFILE LOGIC/ #NEEDS TO BE BETTER HERE, ALL KINDS OF FAILURE CASES
    if 'csv' in username.lower():
        print('REDIRECTING TO DATASET PAGE...MANY POTENTIAL ERRORS HERE IF NOT CAREFL')
        ds_hosts_username = username.split("-")[0]
        ds_hosts_file_name = username.split("-")[1]

        file_id = database.GET_FILE_ID_W_USERNAME(connection,
                                                  username=ds_hosts_username,
                                                  file_name=ds_hosts_file_name)
        print('CURRENT FILE ID', file_id)
        model_ids, \
        local_paths, \
        model_descriptions, \
        dates, \
        foreign_file_id, \
        model_uploaders, \
        model_user_ids, \
        csv_file_paths, \
        file_sizes, \
        csv_description, \
        csv_user_id, \
        csv_upload_date, \
        num_model_votes = database.GET_MODELS_BY_FILE_ID(connection, file_id)

        helpers.print_model_details(model_ids, local_paths, model_descriptions, dates, foreign_file_id, model_uploaders,
                                    model_user_ids, csv_file_paths, file_sizes, csv_description, csv_user_id,
                                    csv_upload_date, num_model_votes)

        return render_template('dataset_details.html',
                               message="dataset_details.html page",
                               full_string=username,
                               host_name=ds_hosts_username,
                               file_name=ds_hosts_file_name,
                               model_ids=model_ids,
                               local_paths=local_paths,
                               model_descriptions=model_descriptions,
                               dates=dates,
                               foreign_file_id= foreign_file_id,
                               model_user_ids=model_user_ids,
                               csv_file_paths=csv_file_paths,
                               file_sizes=file_sizes,
                               csv_description=csv_description,
                               csv_user_id=csv_user_id,
                               csv_upload_date=csv_upload_date,
                               num_model_votes=num_model_votes,
                               )
    # IF WE ARE NOT SIGNED IN & TRYING TO GO ELSEWHEREW
    if "email" not in session:
        return redirect(url_for('login'))
    else:
        # IF WE ARE GOING TOA  USER PROFILE
        if username != "favicon.ico":  # DEFAULT CHECK FOR NULL PROFILE I THINK?
            my_friends = database.GET_FRIENDS(connection, username)
            filenames, descriptions, dates, sizes = database.GET_FILES(connection, username)
            # print("FILENAMES: ", filenames)
            return render_template(f"user_profile.html",
                                   friends=my_friends,
                                   account_name=username,
                                   filenames=filenames,
                                   descriptions=descriptions,
                                   dates=dates,
                                   file_sizes=sizes
                                   )
    return redirect(url_for('home'))


@app.route("/get_csv/<account_name>/<folder>/<filename>", methods=['GET', 'POST'])
def get_csv(account_name, folder, filename):
    print('Filename:', account_name, folder, filename)
    full_file = "static/" + "#UserData/" + account_name + "/" + folder + "/" + filename
    print(full_file)
    with open(full_file) as fp:
        csv = fp.read()

    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                     "attachment; filename=myplot.csv"})


@app.route("/add_user/<username>", methods=['POST'])
def add_user(username):
    # print('do something')
    user_id_first = database.GET_USER_ID(connection, username=session['user'])
    user_id_second = database.GET_USER_ID(connection, username=username)
    # print("USERNAME 1: ", session['user'], " | ID 1: ", user_id_first)
    # print("USERNAME 2: ", username, " | ID 2: ", user_id_second)
    if user_id_first == user_id_second:
        print("NOT ADDING YOURSELF")
        return redirect(url_for('user_profile_name', username=session['user']))
    else:
        database.CONNECTION_INSERT(connection, user_id_first, user_id_second)
        return redirect(url_for('user_profile_name', username=session['user']))


@app.route("/remove_user/<username>", methods=['POST'])
def remove_user(username):
    user_id_first = database.GET_USER_ID(connection, username=session['user'])
    user_id_second = database.GET_USER_ID(connection, username=username)
    if user_id_first == user_id_second:
        print("NOT REMOVING YOURSELF")
        return redirect(url_for('user_profile_name', username=session['user']))
    else:
        database.CONNECTION_REMOVE(connection, user_id_first, user_id_second)
        return redirect(url_for('user_profile_name', username=session['user']))


@app.route("/password_recovery", methods=['GET', 'POST'])
def password_recovery():
    print("LOADING PASSWORD RECOVERY")

    if request.method == "POST":
        recovery_email = request.form["email"]
        print(recovery_email)
        my_email.send_email(recovery_email)
    return render_template(f"password_recovery.html")


@app.route("/password_reset", methods=['GET', 'POST'])
def password_reset():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        recov_test_password = request.form["repeat_password"]
        # print(email)
        # print(password)
        # print(recov_test_password)
        if password == recov_test_password:

            database.CHANGE_PASSWORD(connection, email, password)
            print(email, " Password changed")
            return redirect(url_for("login"))
        else:
            return render_template(f"password_reset.html", message="Passwords are not the same!")
    else:
        return render_template(f"password_reset.html")


@app.route("/order_by_votes", methods=['GET', 'POST'])
def order_by_votes():
    print('EXECUTING INDEX FUNCTION')
    usernames, paths, descriptions, dates, file_sizes, num_votes = database.GET_ALL_DATASETS_BY_DATE(connection)
    by_date = False
    by_votes = True
    return render_template('index.html',
                           message="index.html page",
                           usernames=usernames,
                           paths=paths,
                           descriptions=descriptions,
                           dates=dates,
                           file_sizes=file_sizes,
                           votes=num_votes,
                           by_votes=by_votes,
                           by_date=by_date
                           )


@app.route("/order_by_date", methods=['GET', 'POST'])
def order_by_date():
    print('EXECUTING INDEX FUNCTION')
    usernames, paths, descriptions, dates, file_sizes, num_votes = database.GET_ALL_DATASETS_BY_DATE(connection)
    by_date = True
    by_votes = False
    return render_template('index.html',
                           message="index.html page",
                           usernames=usernames,
                           paths=paths,
                           descriptions=descriptions,
                           dates=dates,
                           file_sizes=file_sizes,
                           votes=num_votes,
                           by_votes=by_votes,
                           by_date=by_date
                           )


@app.route("/<csv_file_name>", methods=['GET', 'POST'])
def dataset_details_filename(csv_file_name):
    return render_template('dataset_details.html',
                           message="dataset_details.html page",
                           file=csv_file_name
                           )


if __name__ == '__main__':
    my_port = 5006
    app.run(host='localhost', port=my_port, debug=True)  # host is to get off localhost
    # If the debugger is on, I can change my files in real time after saving
