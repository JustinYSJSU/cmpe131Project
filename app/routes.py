from app import appObj
from app.user_login import LoginUser

from flask import render_template, flash, redirect, url_for

from app import db
from app.models import User 

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

@appObj.route('/', methods = ['GET', 'POST'])
def login():
 login_form = LoginUser()
 if login_form.validate_on_submit():
  user = User.query.filter_by(username = login_form.username.data).first()
  if user != None:
   if user.check_password(login_form.password.data) == True:
    login_user(user)
    return redirect(url_for('home'))
   else:
    flash('Incorrect password. Please try again.')
  else:
   flash('Username does not exist. Please enter an existing username')
 return render_template('login.html', login_form = login_form)


@appObj.route('/home')
@login_required
def home():
 return render_template('home.html')