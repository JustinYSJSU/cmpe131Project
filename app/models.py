from app import db

class User(db.Model):
 id = db.Column(db.Integer, primary_key = True)
 username = db.Column(db.String(64))
 email = db.Column(db.String(64))
 password_hash = db.Column(db.String(64))
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

 def __repr__(self):
  return f'<User {self.username} {self.email} {self.address}>'
