from flask import Flask, request, redirect, render_template, url_for

import random
import string
import sqlite3
import os

app = Flask(__name__)

#create the database

DB_name = 'urls.db'
connection = sqlite3.connect(DB_name,check_same_thread=False)
c = connection.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_code TEXT UNIQUE,
    long_url TEXT
)
''')

connection.commit()

#home page for the submit urls

@app.route('/')
def home():
    return render_template('Index.html', short_url = None)

 
if __name__ == '__main__':
    app.run(debug=True)

