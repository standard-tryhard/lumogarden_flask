from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField


class NewCardForm(FlaskForm):
    new_card_name = StringField('new_card_name')
    new_card_steps = TextAreaField('new_card_steps')

