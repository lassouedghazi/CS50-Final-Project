import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Show all the messages received"""
    user_id = session["user_id"]
    username = db.execute("SELECT username FROM users WHERE id = ?", user_id)[0]["username"]
    messages = db.execute("SELECT * FROM messages WHERE receiver = ?", username)
    return render_template("index.html", messages=messages)

@app.route("/send", methods=["GET", "POST"])
@login_required
def send():
    """Send a message."""
    if request.method == "POST":
        sender = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]
        receiver = request.form.get("receiver")
        subject = request.form.get("subject")
        body = request.form.get("body")

        # Ensure no field is empty
        if not receiver or not subject or not body:
            return apology("No empty fields allowed", 400)

        # Insert the new message into the messages table
        db.execute("INSERT INTO messages (sender, receiver, subject, body) VALUES (?, ?, ?, ?)",sender, receiver, subject, body)

        return redirect("/")

    return render_template("send.html")

@app.route("/history")
@login_required
def history():
    """Show history of messages sent"""
    user_id = session["user_id"]
    username = db.execute("SELECT username FROM users WHERE id = ?", user_id)[0]["username"]
    messages = db.execute("SELECT * FROM messages WHERE sender = ?", username)
    return render_template("history.html", messages=messages)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]
        return redirect("/")

    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect("/")

@app.route("/message/<int:message_id>")
@login_required
def message(message_id):
    """View a specific message"""
    user_id = session["user_id"]
    message = db.execute("SELECT * FROM messages WHERE id = ? AND (receiver = (SELECT username FROM users WHERE id = ?) OR sender = (SELECT username FROM users WHERE id = ?))", message_id, user_id, user_id)

    if not message:
        return apology("Message not found")

    return render_template("message.html", message=message[0])

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if not email or not password or not confirm:
            return apology("no empty fields")
        if password != confirm:
            return apology("passwords do not match")
        hash = generate_password_hash(password)

        try:
            newUser = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", email, hash)
        except:
            return apology("email already used")

        session["user_id"] = newUser
        return redirect("/")

@app.route("/answer/<int:message_id>", methods=["GET", "POST"])
@login_required
def answer(message_id):
    """Answer the message received"""
    user_id = session["user_id"]
    message = db.execute("SELECT * FROM messages WHERE id = ? AND receiver = (SELECT username FROM users WHERE id = ?)", message_id, user_id)

    if not message:
        return apology("Message not found")

    if request.method == "GET":
        return render_template("answer.html", message=message[0])

    else:
        # Get the reply details from the form
        sender = message[0]["receiver"]
        receiver = message[0]["sender"]
        subject = "Re: " + message[0]["subject"]
        body = request.form.get("body")

        # Ensure the reply body is provided
        if not body:
            return apology("Reply body cannot be empty")

        # Insert the reply into the database
        db.execute(
            "INSERT INTO messages (sender, receiver, subject, body) VALUES (?, ?, ?, ?)",
            sender, receiver, subject, body
        )

        flash("Reply sent!")
        return redirect("/history")

