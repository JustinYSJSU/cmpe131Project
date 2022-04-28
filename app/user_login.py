from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginUser(FlaskForm):
 username = StringField('Username', validators = [DataRequired()])
 password = StringField('Password', validators = [DataRequired()])
 submit = SubmitField('Log in')
