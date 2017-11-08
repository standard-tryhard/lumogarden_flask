from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                     SubmitField, BooleanField,
                     SelectMultipleField, widgets)


class NewCardForm(FlaskForm):
    new_card_name = StringField('new_card_name')
    new_card_steps = TextAreaField('new_card_steps')
    add_task = SubmitField('add')


# There are other ways to do this
# but I'm hacking it this way for now to
# focus on application logic
class TodoButtons(FlaskForm):
    chk_tl_L1 = BooleanField('')
    chk_tl_L2 = BooleanField('')
    chk_tl_L3 = BooleanField('')

    chk_tm_M1 = BooleanField('')
    chk_tm_M2 = BooleanField('')
    chk_tm_M3 = BooleanField('')

    chk_tr_R1 = BooleanField('')
    chk_tr_R2 = BooleanField('')
    chk_tr_R3 = BooleanField('')

    submit = SubmitField('Bloom')


class ExampleForm(FlaskForm):

    fields = SelectMultipleField(
        'Form',
        choices=[],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
        )

