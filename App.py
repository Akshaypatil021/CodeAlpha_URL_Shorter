from flask import Flask, request, redirect, render_template
import random
import string
import sqlite3

app = Flask(__name__)

# Database setup
DB_name = 'urls.db'
connection = sqlite3.connect(DB_name, check_same_thread=False)
c = connection.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_code TEXT UNIQUE,
    long_url TEXT
)
''')
connection.commit()

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'Clear':
            # Clear short URL display and form input
            return render_template('Index.html', short_url=None)

        if action == 'Cut':
            long_url = request.form['long_url'].strip()

            # Ensure URL has http/https
            if not (long_url.startswith('http://') or long_url.startswith('https://')):
                long_url = 'http://' + long_url

            # Generate unique short_code
            while True:
                short_code = generate_short_code()
                try:
                    c.execute('INSERT INTO urls (short_code, long_url) VALUES (?, ?)', (short_code, long_url))
                    connection.commit()
                    break
                except sqlite3.IntegrityError:
                    continue

            short_url = request.host_url + short_code
            return render_template('Index.html', short_url=short_url)

    # GET request
    return render_template('Index.html', short_url=None)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    row = c.execute("SELECT long_url FROM urls WHERE short_code=?", (short_code,)).fetchone()
    if row:
        return redirect(row[0])
    return "Invalid short URL", 404

if __name__ == '__main__':
    app.run(debug=True)