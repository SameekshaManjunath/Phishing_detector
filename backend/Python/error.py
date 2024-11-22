from app import app  # Import app from app.py
from flask import redirect, url_for, flash
from flask_login import logout_user
app.errorhandler(404)
def not_found(error):
    return "Page Not Found", 404