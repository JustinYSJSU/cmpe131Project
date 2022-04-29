from app import appObj
from app.user_login import LoginUser
from app.createAccount import CreateUser

from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash

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

@appObj.route('/createAccount', methods = ['GET', 'POST'])
def createAccount():
  accountForm = CreateUser()
  if accountForm.validate_on_submit():
    user=User()
    user.username=accountForm.username.data
    user.email=accountForm.email.data
    user.set_password(accountForm.password.data)
    user.address=accountForm.address.data
    user.payment_method_company=accountForm.paymentMethodCompany.data
    user.payment_method_number=accountForm.paymentNumber.data
    user.payment_method_expdate=accountForm.paymentExpDate.data
    user.payment_method_cvc=accountForm.paymentCVC.data
    db.session.add(user)
    db.session.commit()
    print("user has been created")
    return redirect('/')
  return render_template('createAccount.html', accountForm = accountForm)

@appObj.route('/testing')
def redirectTest():
  return redirect('/')