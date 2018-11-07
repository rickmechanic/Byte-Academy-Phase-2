#!usr/bin/env python

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'the session needs this'

@app.route('/', methods=["GET"])
def send_to_log_in():
    if 'username' in session:
        return redirect('/homepage')
    else:
        return redirect('/')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if check_user(username,password) == True:
            session['username'] = username
            return redirect('/homepage')
        else:
            return render_template('login.html', message='Login error')
        
@app.route('/homepage', methods=["GET"])
def show_homepage():
    return render_template('success.html', username=session['username'])

@app.route('/logout', methods=['GET'])
def log_out():
    session.pop('username', None)
    return redirect('/login')

def check_user(username, password):
    if username == 'Rick' and password == 'Mechanic1':
        return True
    return False







if __name__=="__main__":
    app.run()