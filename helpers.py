from flask import redirect, render_template, request, session
from functools import wraps

def apology(message, code=400):
    """Render message as an apology to user."""
    return render_template("apology.html", top=code, bottom=message), code

def login_required(f):
    """Decorator to require login for routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def lookup(symbol):
    # Placeholder for a stock quote lookup function.
    return None

def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
