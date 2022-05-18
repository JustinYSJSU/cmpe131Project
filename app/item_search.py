
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ItemSearch(FlaskForm):
 item_name = StringField(render_kw={"placeholder": "Search for an item"})
 search = SubmitField("Search")

class SellerSearch(FlaskForm):
    seller_name = StringField(render_kw={"placeholder": "Search for a user and see items they're selling"})
    submit = SubmitField('Search')
