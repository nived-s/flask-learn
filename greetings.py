from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<name>")
def wish_user(name = None):
    return render_template('wishing.html', name = name)