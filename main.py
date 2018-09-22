from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('home.html')
    return template.render(uname = "", pword = "", vpword = "", eml = "", usernameerror = "", passworderror = "", verifypassworderror = "", emailerror = "")

@app.route("/", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']
    errors = False
    usernameerror = ""
    passworderror = ""
    verifypassworderror = ""
    emailerror = ""
    if (username == "") or (len(username)<3) or (len(username)>20) or (" " in username):
        errors = True
        usernameerror = " Error in username, please resubmit. Between 3 and 20 characters with no spaces, please."
    if (password == "") or (len(password)<3) or (len(password)>20) or (" " in password):
        errors = True
        passworderror = " Error in password, please resubmit. Between 3 and 20 characters with no spaces, please."
    if (verifypassword == "") or (len(verifypassword)<3) or (len(verifypassword)>20) or (" " in verifypassword) or (verifypassword != password):
        errors = True
        verifypassworderror = " Error in username, please resubmit. Between 3 and 20 characters with no spaces, please, and must match password."
    if email != "":
        if (len(email)<3) or (len(email)>20) or (" " in email) or (email.count("@") != 1) or (email.count(".") != 1):
            errors = True
            emailerror = " Error in email, please resubmit. Between 3 and 20 characters with no spaces, 1 '@' and 1 '.'."
    if errors == False:
       return redirect('/welcome?username={0}'.format(username))

    else: 
        template = jinja_env.get_template('home.html')
        return template.render(uname = username, pword = "", vpword = "", eml = email, usernameerror = usernameerror, passworderror = passworderror, verifypassworderror = verifypassworderror, emailerror = emailerror)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return '<h1>Welcome, {0}.</h1>'.format(username)


app.run()
