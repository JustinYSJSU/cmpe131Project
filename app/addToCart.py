from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class addToCart(FlaskForm):
    submit = SubmitField('Add to Cart')

class checkoutForm(FlaskForm):
    submit = SubmitField('Checkout')

class shoppingCart:
    def __init__(self):
        self.subtotal=0
        self.cart=[]
        self.cartNames=[]

    def addToCart(self, Name, Price):
        self.subtotal+=Price
        self.cart.append([Name, Price])
        self.cartNames.append(Name)

    def reset(self):
        self.subtotal=0
        self.cart=[]