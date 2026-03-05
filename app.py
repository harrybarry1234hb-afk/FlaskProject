from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# About route
@app.route("/about")
def about():
    return render_template("about.html")

# Contact route
@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = ""
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")

        # Print to terminal
        print(f"Form submitted -> Name: {name}, Email: {email}")

        # Save to file
        with open("submissions.txt", "a") as f:
            f.write(f"Name: {name}, Email: {email}\n")

        # Message to show on page
        message = f"Thank you {name}! We received your email: {email}"

    return render_template("contact.html", message=message)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)