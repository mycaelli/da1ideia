from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/profile')
def profile():
    return render_template('profile.html')

@auth.route('/social')
def social():
    return render_template('social.html')

