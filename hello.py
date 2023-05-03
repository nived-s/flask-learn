from flask import Flask
from markupsafe import escape
# escape is used to protect from injection attacks
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"

@app.route("/login/")
def login_page():
    return "<p>login page</p>"

@app.route("/signup")
def signup_page():
    return "<p>signup page</p>"

@app.route("/login/success")
def ret_succ():
    return "<p>login successful</p>"

@app.route("/user/<uname>")
def user_page():
    url_for("user_page", uname='john')
    return "<p>profile page</p>"


"""
HTTP methods GET & POST

@app.route('/login_page', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

"""