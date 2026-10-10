from flask import Flask,render_template,request,redirect,url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
database = "inventory.db"

def init_db():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    passwd TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def index():
    return redirect(render_template('login'))

@app.route('/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        passwd = request.form['passwd']
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute("INSERT INTO users (name,passwd) VALUES (?,?)",(name,passwd))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template("login.html")####################################################!!!!!

@app.route('/home')
def home():
    return render_template("LAKSH 2.html")


if __name__ == '__main__':
    init_db()
    app.run(debug=True,port=5000)