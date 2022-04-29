from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class CreateUser(FlaskForm):
    username = StringField( 'Username', validators = [DataRequired()])
    email = StringField ( 'Email', validators = [DataRequired()])
    password = StringField( 'Password', validators = [DataRequired()])
    address = StringField( 'Address', validators = [DataRequired()])
    paymentMethodCompany = StringField( 'PaymentProvidor', validators = [DataRequired()])
    paymentNumber = StringField('PaymentNumber', validators = [DataRequired()])
    paymentCVC = StringField('PaymentCVC', validators = [DataRequired()])
    paymentExpDate = StringField('PaymentExpDate', validators = [DataRequired()])
    submit = SubmitField('Create Account')
