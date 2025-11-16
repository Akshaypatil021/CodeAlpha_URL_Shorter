🔗 CodeAlpha_URL_Shorter
A simple yet powerful URL Shortener built using Flask (Python) or Express.js (Node.js). It generates short unique codes for long URLs, stores them in a database, and redirects users to the original links. Includes an optional frontend to create and view short URLs.

💡 Bonus: Share shortened links with others and even monetize them by tracking usage.

✨ Features
🔒 Unique Short Codes – Automatically generates unique codes for each long URL.

🗄️ Database Storage – Supports SQLite, MongoDB, or other databases for mapping short codes to original URLs.

🔀 Redirects – Accessing a short URL instantly redirects to the original long URL.

🌐 Optional Frontend – Simple UI to input long URLs and view shortened versions.

💰 Monetization Ready – Share short links and earn money through link tracking.

🛠️ Tech Stack
Backend: Flask (Python 3.11.9) or Express.js (Node.js)

Server: Gunicorn (Flask deployment)

Database: SQLite / MongoDB

Frontend (Optional): HTML, CSS, JavaScript

⚙️ Installation & Setup
🔧 Prerequisites
Python 3.11.9 or Node.js (latest stable)

pip / npm package manager

SQLite or MongoDB installed

📦 Install Dependencies
bash
# For Flask
pip install Flask==3.0.3 gunicorn==23.0.0

# For Express.js
npm install express mongoose
▶️ Run the Project
bash
# Flask
web: gunicorn App:app

# Express.js
node server.js
📌 Usage
Send a POST request to /shorten with a long URL → receive a short code.

Access /<short_code> → instantly redirects to the original URL.

Use the optional frontend to generate and manage short links visually.

📷 Demo (Optional)
Add screenshots of your frontend UI or terminal output here.

🤝 Contributing
Fork the repo

Create a new branch (feature/your-feature)

Commit changes and open a Pull Request

📜 License
MIT License – free to use, modify, and distribute.
