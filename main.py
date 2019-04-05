from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route('/welcome-user', methods=['POST'])
def welcome_user():
    user = request.form['user']
    passwd = request.form['pass']
    ver_passwd = request.form['ver_pass']
    email = request.form['email']

    if user and passwd == ver_passwd:
        return render_template('welcome-user.html', new_user = user)

@app.route('/')
def index():

    return render_template('index.html')

app.run()