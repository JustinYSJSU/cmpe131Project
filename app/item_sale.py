
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, FileField
from wtforms.validators import DataRequired, Length, NumberRange

class SellItem(FlaskForm):
 item_sell_name = StringField("Enter item name",validators = [DataRequired(), Length(min=3, max=64)],render_kw={"placeholder": "Item name, between 3 and 64 characters"})
 item_sell_price = DecimalField("Enter item price",render_kw={"placeholder": "Price, must be above $0"}, validators =[DataRequired(), NumberRange(min=0)], places = 2)
 #image submit
 item_sell_desc = StringField("Describe the item", render_kw={"placeholder": "Description, max 128 characters"}, validators = [DataRequired(), Length(max=128)])
 item_image = FileField()
 sell = SubmitField('Sell')
