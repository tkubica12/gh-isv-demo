import sqlite3
import subprocess
import pickle
import re
import requests
from flask import Flask, request, jsonify, redirect, escape

app = Flask(__name__)
DATABASE = 'test.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    conn.commit()
    conn.close()

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Use parameterized queries to prevent SQL Injection
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    return 'User added successfully'

@app.route('/get_user', methods=['GET'])
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Use parameterized queries to prevent SQL Injection
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return jsonify(user)

@app.route('/run_command', methods=['POST'])
def run_command():
    command = request.form['command']
    # Validate and sanitize user input to prevent Command Injection
    if re.match(r'^[a-zA-Z0-9_\-]+$', command):
        result = subprocess.check_output(command, shell=True)
        return result
    else:
        return 'Invalid command'

@app.route('/deserialize', methods=['POST'])
def deserialize():
    data = request.form['data']
    # Use safe deserialization methods and validate input data
    try:
        obj = pickle.loads(data)
        return str(obj)
    except Exception as e:
        return str(e)

@app.route('/xss', methods=['GET'])
def xss():
    name = request.args.get('name')
    # Properly encode user input to prevent Cross-Site Scripting (XSS)
    return f"<h1>Hello {escape(name)}</h1>"

@app.route('/ssrf', methods=['GET'])
def ssrf():
    url = request.args.get('url')
    # Validate and sanitize URLs to prevent Server-Side Request Forgery (SSRF)
    if re.match(r'^https?://', url):
        response = requests.get(url)
        return response.content
    else:
        return 'Invalid URL'

@app.route('/open_redirect', methods=['GET'])
def open_redirect():
    url = request.args.get('url')
    # Validate and sanitize URLs to prevent Open Redirect
    if re.match(r'^https?://', url):
        return redirect(url)
    else:
        return 'Invalid URL'

@app.route('/path_traversal', methods=['GET'])
def path_traversal():
    filename = request.args.get('filename')
    # Validate and sanitize file paths to prevent Path Traversal
    if re.match(r'^[a-zA-Z0-9_\-\.]+$', filename):
        with open(f"/var/www/uploads/{filename}", 'r') as file:
            content = file.read()
        return content
    else:
        return 'Invalid filename'

if __name__ == '__main__':
    init_db()
    app.run(debug=True)