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

@app.route('/validate-signup', methods=['POST'])
def validate_signup():

        user = request.form['user']
        passwd = request.form['pass']
        ver_passwd = request.form['ver_pass']
        email = request.form['email']

        user_error = ''
        passwd_error = ''
        ver_passwd_error = ''
        email_error = ''

        
        if not user:
                user_error = 'You need to enter a username. Try again.'
        else: 
                if len(user) < 3 or len(user) > 20:
                        user_error = 'The username needs to be between 3-20 characters. Try again.'
                        user = ''

        if not passwd:
                passwd_error = 'You need to enter a password. Try again.'
        else:
                if len(passwd) < 3 or len(passwd)> 20:
                        passwd_error = 'The password needs to be between 3-20 characters. Try again.'
                        passwd = ''

        if not ver_passwd:
                ver_passwd_error = 'You need to enter a password that matches. Try again.'

        else: 
                if passwd != ver_passwd:
                        ver_passwd_error = "The passwords didn't match they need to match."
                        passwd = ''
                        ver_passwd = ''
                elif len(ver_passwd) < 3 or len(ver_passwd) > 20:
                        ver_passwd_error = 'The password needs to be between 3-20 characters. Try again.'
                        ver_passwd = ''
                
        
        
        return render_template('index.html', u_error = user_error, p_error = passwd_error, vp_error = ver_passwd_error, e_error = email_error)





@app.route('/')
def index():

        return render_template('index.html')

app.run()