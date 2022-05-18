from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import DataRequired, NumberRange

class RateForm(FlaskForm):
 username = StringField('Username', validators = [DataRequired()], render_kw = {"placeholder": "Enter the name of the user you want to rate"})
 rating_number = IntegerField('Rating', validators = [DataRequired(), NumberRange(min = 1, max = 3)], render_kw = {"placeholder": "1, 2, 3"})
 rate = SubmitField('Rate')
