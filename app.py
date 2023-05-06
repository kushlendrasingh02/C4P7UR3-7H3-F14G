import sqlite3
from flask import Flask, session, redirect, url_for, request, render_template, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return redirect(url_for('index'))

@app.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['passwd']

        if not username:
            flash('username is required!', 'error')
        elif not passwd:
            flash('passwd is required!', 'error')
        else:
            conn = get_db_connection()
            cur = conn.cursor()
            statement = f"SELECT username FROM user WHERE username='{username}' AND password='{password}'"

            cur.execute(statement)
            if not cur.fetchone():
                flash('Wrong uername or password!', 'error')
            else:
                conn.close()
                flash('ICT{Yq2XFnte5baxFszPTfTGNVehv}', 'success')
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/task1')
def task1():
    return render_template('task1.html')

@app.route('/task2')
def task2():
    return render_template('task2.html')

@app.route('/task3')
def task3():
    return render_template('task3.html')

@app.route('/task4')
def task4():
    return render_template('task4.html')

@app.route('/noob')
def noob():
    return render_template('noob.html')

@app.route('/robot')
def robot():
    return render_template('robot.html')

@app.route('/task5/', methods=('GET', 'POST'))
def task5():
    if request.method == 'POST':
        email = request.form['email']

        if not email:
            flash('username is required!', 'error')
        else:
            if email == "Prashant.Janisir@gmail.com":
                flash('ICT{xfk5VRj8zSFEVSSpb7pit8yBH}', 'success')
            else:
                flash('Wrong uername or password!', 'error')
    return render_template('task5.html')

@app.route('/task6')
def task6():
    return render_template('task6.html')
