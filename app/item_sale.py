
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, FileField
from wtforms.validators import DataRequired

class SellItem(FlaskForm):
 item_sell_name = StringField('Item Name', validators = [DataRequired()])
 item_sell_price = DecimalField('Item Price', validators =[DataRequired()], places = 2)
 #image submit
 item_sell_desc = StringField('Description', validators = [DataRequired()])
 item_image = FileField()
 sell = SubmitField('Put for sale')
