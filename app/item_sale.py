
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, FileField
from wtforms.validators import DataRequired

class SellItem(FlaskForm):
 item_sell_name = StringField("Enter item name",validators = [DataRequired()],render_kw={"placeholder": "Item name"})
 item_sell_price = DecimalField("Enter item price",render_kw={"placeholder": "Price"}, validators =[DataRequired()], places = 2)
 #image submit
 item_sell_desc = StringField("Describe the item", render_kw={"placeholder": "Description"}, validators = [DataRequired()])
 item_image = FileField()
 sell = SubmitField('Sell')
