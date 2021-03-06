from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
 id = db.Column(db.Integer, primary_key = True)
 username = db.Column(db.String(16))
 email = db.Column(db.String(64))
 password_hash = db.Column(db.String(128))
 address = db.Column(db.String(128))
 payment_method_company = db.Column(db.String(10))
 #number is 19 characters to account for spaces between every 4 numbers
 payment_method_number = db.Column(db.Integer)
 payment_method_cvc = db.Column(db.Integer)
 #expdate is in the format mm/yy
 payment_method_expdate = db.Column(db.Integer)

 #changed the review system--total reviews and just be summed later
 num_positive_reviews = db.Column(db.Integer)
 num_neutral_reviews = db.Column(db.Integer)
 num_negative_reviews = db.Column(db.Integer)
#  #sum of all review scores
#  review_total_score = db.Column(db.Integer)
#  #number of total reviews
#  review_total = db.Column(db.Integer)

 items = db.relationship('Item')
 orders = db.relationship('Order')

 def set_password(self, password):
  self.password_hash = generate_password_hash(password)

 def check_password(self, password):
  return check_password_hash(self.password_hash, password)

class Item(db.Model):
 id = db.Column(db.Integer, primary_key = True)
 name = db.Column(db.String(128))
 price = db.Column(db.Float)
 image = db.Column(db.String(256)) #changed from LargeBinary to String--this will be the name of the image 
 description = db.Column(db.String(256))
 #username is linked to item in order to display seller name
 user_seller_name = db.Column(db.String, db.ForeignKey('user.username'))

class Order(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  itemList = db.Column(db.String(1024))
  subtotal = db.Column(db.Float)
  buyerID = db.Column(db.Integer, db.ForeignKey('user.id'))

class ShoppingCart(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(128))
  price = db.Column(db.Float)
  itemID = db.Column(db.Integer)
  buyerID = db.Column(db.Integer, db.ForeignKey('user.id'))

@login.user_loader
def load_user(id):
 return User.query.get(int(id))
