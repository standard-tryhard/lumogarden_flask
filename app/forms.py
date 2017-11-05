from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                     SubmitField, BooleanField)


class NewCardForm(FlaskForm):
    new_card_name = StringField('new_card_name')
    new_card_steps = TextAreaField('new_card_steps')
    add_task = SubmitField('add')

class Buttons(FlaskForm):
    checkbox = BooleanField('checkbox')
    submit = SubmitField('Bloom')