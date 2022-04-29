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
 payment_method_number = db.Column(db.String(19))
 payment_method_cvc = db.Column(db.String(3))
 payment_method_expdate = db.Column(db.String(5))
 #sum of all review scores
 review_total_score = db.Column(db.Integer)
 #number of total reviews
 review_total = db.Column(db.Integer)
 items = db.relationship('Item')

 def set_password(self, password):
  self.password_hash = generate_password_hash(password)

 def check_password(self, password):
  return check_password_hash(self.password_hash, password)

 def __repr__(self):
  return f'<User {self.username} {self.email} {self.address}>'

class Item(db.Model):
 id = db.Column(db.Integer, primary_key = True)
 name = db.Column(db.String(128))
 price = db.Column(db.Float)
 image = db.Column(db.LargeBinary)
 description = db.Column(db.String(256))
 user_seller_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@login.user_loader
def load_user(id):
 return User.query.get(int(id))
