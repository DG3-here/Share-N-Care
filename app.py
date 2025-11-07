from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Database initialization
def init_db():
    if not os.path.exists("share_n_care.db"):
        conn = sqlite3.connect("share_n_care.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS requests (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        category TEXT,
                        description TEXT,
                        contact TEXT
                    )''')
        conn.commit()
        conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect("share_n_care.db")
    c = conn.cursor()
    c.execute("SELECT * FROM requests ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return render_template('index.html', requests=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/request_help', methods=['GET', 'POST'])
def request_help():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        contact = request.form['contact']
        conn = sqlite3.connect("share_n_care.db")
        c = conn.cursor()
        c.execute("INSERT INTO requests (name, category, description, contact) VALUES (?, ?, ?, ?)",
                  (name, category, description, contact))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template('request_help.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
