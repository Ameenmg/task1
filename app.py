from flask import Flask
from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for, request
import os
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    hostname = os.uname()[1]
    randomid = uuid.uuid4()
    my_name = os.getenv("MY_NAME")
    return 'Container Hostname: ' + hostname + ' , ' + 'UUID: ' + str(randomid) + '\n ' + 'Name: '+ str(my_name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)