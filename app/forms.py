from flask_wtf import FlaskForm
from wtforms import (StringField, FormField,
                     SubmitField, BooleanField)
from wtforms.validators import DataRequired


class NewCardStepsForm(FlaskForm):
    new_card_step_A = StringField('')
    new_card_step_B = StringField('')
    new_card_step_C = StringField('')
    new_card_step_D = StringField('')
    new_card_step_E = StringField('')
    new_card_step_F = StringField('')
    new_card_step_G = StringField('')
    new_card_step_H = StringField('')
    new_card_step_I = StringField('')
    new_card_step_J = StringField('')
    new_card_step_K = StringField('')
    new_card_step_L = StringField('')


class NewCardForm(FlaskForm):
    new_card_name = StringField('new_card_name', validators=[DataRequired()])
    new_card_jar = StringField('new_card_jar', validators=[DataRequired()])
    new_card_steps = FormField(NewCardStepsForm)

    submit = SubmitField('add')


# class TelephoneForm(Form):
#     country_code = IntegerField('Country Code', [validators.required()])
#     area_code    = IntegerField('Area Code/Exchange', [validators.required()])
#     number       = StringField('Number')
#
# class ContactForm(Form):
#     first_name   = StringField()
#     last_name    = StringField()
#     mobile_phone = FormField(TelephoneForm)
#     office_phone = FormField(TelephoneForm)



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


# class ExampleForm(FlaskForm):
#
#     fields = SelectMultipleField(
#         'Form',
#         choices=[],
#         option_widget=widgets.CheckboxInput(),
#         widget=widgets.ListWidget(prefix_label=False)
#         )

