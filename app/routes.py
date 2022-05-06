from app import appObj
from app.user_login import LoginUser


from app.item_search import ItemSearch
from app.item_sale import SellItem
from app.createAccount import CreateUser

from app.addToCart import addToCart, sessionCart, checkoutForm

from app.delete_user import DeleteUser

from app.addToCart import addToCart, shoppingCart, checkoutForm

from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from app import db
from app.models import User, Item, Order, ShoppingCart

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

'''sessionCarts = []
for i in range(len(User.query.all())):
  temp = shoppingCart()
  sessionCarts.append(temp)'''

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

#Justin 
@appObj.route('/home', methods = ['GET', 'POST'])
@login_required
#the home page allows users to serach for items
#and put items up for sale
def home():
 search_form = ItemSearch()
  
 if search_form.validate_on_submit(): 
  item_list = Item.query.filter_by(name = search_form.item_name.data).all()
  if len(item_list) != 0:
   return render_template('display_item.html',
          items = item_list, item_name = search_form.item_name.data)   
  else:
   flash('Item was not found. Please try again')

 return render_template('home.html', search_form = search_form)

#Justin
@appObj.route('/sell_item', methods = ['GET', 'POST'])
@login_required
def sell_item():
 sell_form = SellItem()
 if sell_form.validate_on_submit():
  if sell_form.item_sell_price.data > 0:
   #Need to add image in milestone 3
   seller = current_user
   item = Item(name = sell_form.item_sell_name.data, 
               price = sell_form.item_sell_price.data, 
               image = sell_form.item_image.data,
               description = sell_form.item_sell_desc.data, 
               user_seller_name = seller.username)
   db.session.add(item)
   db.session.commit()
   flash("Thank you! Item has been put out for sale")
  else:
   flash('Item price must be above $0.00. Please try again')
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
    db.session.add(user)
    db.session.commit()
    print("user has been created")
    return redirect('/')
  return render_template('createAccount.html', accountForm = accountForm)

#Zach / Justin
@appObj.route('/deleteUser', methods = ['GET', 'POST'])
def deleteAccount():
 account_form = DeleteUser()
 if account_form.validate_on_submit():
  user = User.query.filter_by(username = account_form.username.data).first()
  if user != None:
   if user.check_password(account_form.password.data) == True:
    u = User.query.filter_by(username = account_form.username.data)
    #delete all items that the user was selling, if any 
    item = Item.query.filter_by(user_seller_name = user.username).all()
    if item != None:
     for i in items:
      db.session.delete(i)
     db.session.delete(user)
     db.session.commit()
    flash("Your account has been deleted successfully")
   else:
    flash("Please enter the correct password")
  else:
   flash("Please enter the correct username")
 return render_template('deleteUser.html', accountForm = account_form)

#Joe
@appObj.route('/<itemID>', methods = ['GET', 'POST'])
def landingPage(itemID):
  selectedItem = Item.query.filter_by(id = itemID).all()
  cartOption = addToCart()
  if cartOption.validate_on_submit():
    #sessionCarts[current_user.id - 1].addToCart(selectedItem[0].name, selectedItem[0].price)
    C = ShoppingCart()
    C.buyerID = current_user.id
    C.itemID = itemID
    C.name = selectedItem[0].name
    C.price = selectedItem[0].price
    db.session.add(C)
    db.session.commit()
    print("item has been added to the cart")
    return redirect('/cart')
  return render_template("landing.html", itemID = itemID, selectedItem = selectedItem[0], cartForm = cartOption)

#Joe
@appObj.route('/cart', methods = ['GET', 'POST'])
def displayCart():
  checkout = checkoutForm()
  temp = sessionCart()
  grandCart = ShoppingCart.query.all()
  for i in grandCart:
    if(i.buyerID == current_user.id):
      temp.addToCart(i.name, i.price)
  if checkout.validate_on_submit():
    buyer = current_user
    s = ", "
    s = s.join(temp.cartNames)
    O = Order(itemList = s, subtotal = temp.subtotal, buyerID = buyer.id)
    db.session.query(ShoppingCart).filter(ShoppingCart.buyerID == current_user.id).delete()
    db.session.add(O)
    db.session.commit()

    return redirect('/checkout')
  return render_template("displayCart.html", cart = temp, cartForm = checkout)

#Joe
@appObj.route('/checkout')
def checkout():
  orders = Order.query.filter_by(buyerID = current_user.id)
  return render_template("checkout.html", orders = orders)
