import sys
import os

# Add the parent directory of the current script to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import app and db after modifying the search path
from app import app, db
from flask import request, redirect, url_for, flash, render_template
from flask_login import login_user
from werkzeug.security import check_password_hash

# Import User model
from models.user import User  # Make sure models/user.py exists and has User class

@app.route('/login', methods=['GET', 'POST'])
def login():
    with app.app_context():  # Ensure app context for database operations
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                flash('Logged in successfully!')
                return redirect(url_for('home'))
            else:
                flash('Invalid credentials. Please try again.')
        return render_template('login.html')
