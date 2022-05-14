from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

class CreateUser(FlaskForm):
    username = StringField('Username', validators = [DataRequired(),Length(min=3, max=32)], render_kw={"placeholder": "Ex: yabe, between 3 and 32 characters"})
    email = StringField ( 'Email', validators = [DataRequired()], render_kw={"placeholder": "Ex: yabe@gmail.com"})
    password = PasswordField( 'Password', validators = [DataRequired(), Length(min=4)], render_kw={"placeholder": "Minumum 4 characters"})
    address = StringField( 'Address', validators = [DataRequired()], render_kw={"placeholder": "Ex: 1234 yabe Drive"})
    paymentMethodCompany = StringField( 'PaymentProvidor', validators = [DataRequired(), Length(max=16)],render_kw={"placeholder": "Ex: Visa, max 16 characters"})
    paymentNumber = IntegerField('PaymentNumber', validators = [DataRequired()], render_kw={"placeholder": "Ex: 1234xxxxxxxxxxxx"})
    paymentCVC = IntegerField('PaymentCVC', validators = [DataRequired()], render_kw={"placeholder": "Ex: 123"})
    paymentExpDate = IntegerField('PaymentExpDate', validators = [DataRequired()], render_kw={"placeholder": "Ex: 0522"})
    submit = SubmitField('Create Account')
