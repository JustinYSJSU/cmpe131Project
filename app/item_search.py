
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ItemSearch(FlaskForm):
 item_name = StringField('Search for an item')
 search = SubmitField('Search')
