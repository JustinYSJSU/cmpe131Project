from crypt import methods
from wsgiref.util import request_uri
from bleach import ALLOWED_ATTRIBUTES

from requests import request
from app import appObj
from app.user_login import LoginUser


from app.item_search import ItemSearch, SellerSearch
from app.item_sale import SellItem
from app.createAccount import CreateUser

from app.addToCart import addToCart, sessionCart, checkoutForm

from app.delete_user import DeleteUser

from app.addToCart import addToCart, sessionCart, checkoutForm

from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from app import db
from app.models import User, Item, Order, ShoppingCart

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

import urllib.request

import os



#Justin
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

#Trung
@appObj.route('/logout') #as of right now only included on home.html
def logout():
    logout_user() #from flask_login
    return redirect(url_for('home'))

#Justin 
@appObj.route('/home', methods = ['GET', 'POST'])
@login_required
#the home page allows users to serach for items
#and put items up for sale
def home():
 search_form = ItemSearch()
 search_seller = SellerSearch()
 temp = [0,0]
 if search_form.validate_on_submit(): 
  temp[0] = 0
  item_list = Item.query.filter_by(name = search_form.item_name.data).all()
  if len(item_list) != 0:
   return render_template('display_item.html',
          items = item_list, item_name = search_form.item_name.data)   
  else:
   temp[0] = 1

 if search_seller.validate_on_submit(): 
  temp[1] = 0
  item_list = Item.query.filter_by(user_seller_name = search_seller.seller_name.data).all()
  if len(item_list) != 0:
   return render_template('display_item.html',
          items = item_list, item_name = search_seller.seller_name.data)
  else:
    temp[1] = 1
 if(temp[0] & temp[1]):
   flash('your search did not yield any results. Please try again')
 return render_template('home.html', search_form = search_form, search_seller = search_seller)

#Zach / Justin
@appObj.route('/see_all_items', methods =  ['GET', 'POST'])
@login_required
def see_all_items():
 items = Item.query.all()
 return render_template('see_all_items.html', items = items)

#Trung
appObj.config['SECRET_KEY'] = 'you-will-never-guess'
appObj.config['UPLOAD_FOLDER'] = 'static/files' 
# appObj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# appObj.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#Justin / Trung
@appObj.route('/sell_item', methods = ['GET', 'POST'])
@login_required
def sell_item():
 sell_form = SellItem()
 if sell_form.validate_on_submit():
   seller = current_user

   '''IMAGE HANDLING'''
   file = sell_form.file.data #grab the file
   sec_filename = secure_filename(file.filename) #name of image file submitted
   file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
            appObj.config['UPLOAD_FOLDER'],
            sec_filename)) #save the file

   item = Item(name = sell_form.item_sell_name.data, 
               price = sell_form.item_sell_price.data, 
               image = sec_filename, #storing the name of the image submitted
               description = sell_form.item_sell_desc.data, 
               user_seller_name = seller.username)
   db.session.add(item)
   db.session.commit()
   flash("Thank you! Item has been put out for sale")
   return redirect('/home')
 return render_template('sell_item.html', sell_form = sell_form)

#Joe
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

    #assuming a new account will have no ratings
    user.num_positive_reviews=0
    user.num_neutral_reviews=0
    user.num_negative_reviews=0

    db.session.add(user)
    db.session.commit()
    #take the user back to login screen so they can log in with their new account
    flash('Your account has been created successfully')
    return redirect('/')
  return render_template('createAccount.html', accountForm = accountForm)

#Zach / Justin
@appObj.route('/view_profile', methods = ['GET', 'POST'])
@login_required
def view_profile():
 user = current_user
 return render_template('user_profiles.html', user = user)

#Zach / Justin
@appObj.route('/deleteUser', methods = ['GET', 'POST'])
@login_required
def deleteAccount():
 account_form = DeleteUser()
 if account_form.validate_on_submit():
  user = User.query.filter_by(username = account_form.username.data).first()
  if user != None:
   if user.check_password(account_form.password.data) == True:
    u = User.query.filter_by(username = account_form.username.data)
    #delete all items that the user was selling, if any 
    items = Item.query.filter_by(user_seller_name = user.username).all()
    if items != None:
     for i in items:
      db.session.delete(i)
     db.session.delete(user)
     db.session.commit()
    flash("Your account has been deleted successfully")
    return redirect('/') #after deleting account, redirect to login page
   else:
    flash("Please enter the correct password")
  else:
   flash("Please enter the correct username")
 return render_template('deleteUser.html', accountForm = account_form)

#Joe / Trung
@appObj.route('/<itemID>', methods = ['GET', 'POST'])
def landingPage(itemID):
  selectedItem = Item.query.filter_by(id = itemID).first()
  user = current_user
  # image_abs_path = '../static/files/amd-pc-1-tech-pc-7-techpc7.in_.jpg' #this works--it wants a relative path
  # image_abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), #it does not want an absolute path
  #           appObj.config['UPLOAD_FOLDER'],
  #           selectedItem[0].image) #absolute path of image so it can be used on HTML
  image_rel_path = '../static/files/' + selectedItem.image #concatenate for relative path
  print(image_rel_path) #DEBUGGING
  cartOption = addToCart()
  if cartOption.validate_on_submit() and selectedItem:
    #users cannot buy items that they themselves are selling
    if selectedItem.user_seller_name == user.username:
     flash('You are selling this item, and therefore cannot buy it')
    else:
     C = ShoppingCart()
     #item will be stored in shopping cart database where it can be reference by the buyer's id
     C.buyerID = current_user.id
     C.itemID = itemID
     C.name = selectedItem.name
     C.price = selectedItem.price
     db.session.add(C)
     db.session.commit()
     flash("Item has been added to the cart")
     return redirect('/cart')
  return render_template("landing.html", itemID = itemID, selectedItem = selectedItem, cartForm = cartOption, image_rel_path = image_rel_path)

#Joe
@appObj.route('/cart', methods = ['GET', 'POST'])
@login_required
def displayCart():
  checkout = checkoutForm()
  temp = sessionCart()
  #get a list of every item in the shopping cart database belonging to the current user
  grandCart = ShoppingCart.query.all()
  for i in grandCart:
    if(i.buyerID == current_user.id):
      #add these items to our local shopping cart class for easier management
      temp.addToCart(i.name, i.price)
  if checkout.validate_on_submit():
    for i in grandCart:
      if(i.buyerID == current_user.id):
        db.session.query(Item).filter(Item.id == i.itemID).delete()
    if(temp.subtotal > 0):
      buyer = current_user
      s = ", "
      s = s.join(temp.cartNames)
      #store the order in a database
      O = Order(itemList = s, subtotal = temp.subtotal, buyerID = buyer.id)
      db.session.query(ShoppingCart).filter(ShoppingCart.buyerID == current_user.id).delete()
      db.session.add(O)
      db.session.commit()
      flash("Thank you for your purchase!")
      return redirect('/checkout')
    else:
      flash("Your shopping cart appears to be empty")
  return render_template("displayCart.html", cart = temp, cartForm = checkout)

#Joe
@appObj.route('/checkout')
@login_required
def checkout():
  orders = Order.query.filter_by(buyerID = current_user.id)
  return render_template("checkout.html", orders = orders)

#Joe
@appObj.route('/sellerItems')
def viewSellerItems():
  pass
