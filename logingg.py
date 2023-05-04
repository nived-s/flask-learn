from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/login_check", methods=['POST', 'GET'])
def print_uname_pass():
    if request.method == "POST":

        user_name = request.form.get('uname')
        user_password = request.form.get('upassword')

        return "user name:"+user_name+"\npassword:"+user_password

    return render_template("login_page.html")