from flask import Flask, render_template, request, jsonify
import os
from utils.email_utils import send_bulk_emails


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bulk-email", methods=["GET", "POST"])
def bulk_email():
    if request.method == "POST":
        email_list = request.form["emails"].split(",")
        subject = request.form["subject"]
        message = request.form["message"]
        send_bulk_emails(email_list, subject, message)
        return "Emails sent successfully!"
    return render_template("bulk_email.html")

from flask import Flask, render_template, request, redirect, url_for, flash

app.secret_key = 'shashank'

# Simulated database
users = {}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            flash('Login successful!', 'success')
            return redirect(url_for('bulk_email'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
        elif email in users:
            flash('Email already registered.', 'danger')
        else:
            users[email] = password
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')




if __name__ == "__main__":
    app.run(debug=True)
