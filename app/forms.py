from flask_wtf import FlaskForm
from wtforms import (StringField, FormField,
                     SubmitField, BooleanField,
                     SelectMultipleField, widgets)

from wtforms.validators import DataRequired


class NewCardStepsForm(FlaskForm):
    new_card_step_A = StringField(' ')
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

    submit = SubmitField('create card')


class EditCardStepsForm(FlaskForm):
    new_card_step_A = StringField('')
    new_card_step_B = StringField('')
    new_card_step_C = StringField('')
    new_card_step_D = StringField('')
    new_card_step_E = StringField('')


class EditCardForm(FlaskForm):
    edit_card_name = StringField('edit_card_name',
                                 validators=[DataRequired()])
    additional_steps = FormField(EditCardStepsForm)

    submit = SubmitField('add steps')


class CheckboxGroup(FlaskForm):
    chk_one = BooleanField('')
    chk_two = BooleanField('')
    chk_thr = BooleanField('')

    class Meta:
        # This overrides the value from the base form.
        csrf = False


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

    submit = SubmitField('Rebloom')


class TodoButtonsImproved(FlaskForm):
    tl_form = FormField(CheckboxGroup)
    tm_form = FormField(CheckboxGroup)
    tr_form = FormField(CheckboxGroup)

    ml_form = FormField(CheckboxGroup)
    mr_form = FormField(CheckboxGroup)

    bl_form = FormField(CheckboxGroup)
    bm_form = FormField(CheckboxGroup)
    br_form = FormField(CheckboxGroup)

    submit = SubmitField('Rebloom')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=True)
    option_widget = widgets.CheckboxInput()


class ShowMultipleChkbxForm(FlaskForm):
    chks = MultiCheckboxField('Label', choices=[])
    submit = SubmitField()


'''
class ChoiceObj(object):
    def __init__(self, name, choices):
        # this is needed so that BaseForm.process will accept the object for the named form,
        # and eventually it will end up in SelectMultipleField.process_data and get assigned
        # to .data
        setattr(self, name, choices)

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.TableWidget()
    option_widget = widgets.CheckboxInput()

    # uncomment to see how the process call passes through this object
    # def process_data(self, value):
    #     return super(MultiCheckboxField, self).process_data(value)

class ColorLookupForm(Form):
    submit = SubmitField('Save')
    colors = MultiCheckboxField(None)

allColors = ( 'red', 'pink', 'blue', 'green', 'yellow', 'purple' )

@app.route('/', methods=['GET', 'POST'])
def color():
    selectedChoices = ChoiceObj('colors', session.get('selected') )
    form = ColorLookupForm(obj=selectedChoices)
    form.colors.choices =  [(c, c) for c in allColors]
'''
