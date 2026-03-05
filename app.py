from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Create database if it doesn't exist
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO submissions (name,email) VALUES (?,?)", (name, email))
        conn.commit()
        conn.close()

        return "Form submitted successfully!"

    return render_template("contact.html")


@app.route("/admin")
def admin():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM submissions")
    data = cursor.fetchall()
    conn.close()

    return render_template("admin.html", data=data)


port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)