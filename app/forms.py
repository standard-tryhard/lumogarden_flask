from flask_wtf import FlaskForm
from wtforms import (StringField, FormField,
                     SubmitField, BooleanField,
                     SelectMultipleField, widgets)

from wtforms.validators import DataRequired


class NewCardSteps(FlaskForm):
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


class NewCard(FlaskForm):
    new_card_name = StringField('new_card_name', validators=[DataRequired()])
    new_card_jar = StringField('new_card_jar', validators=[DataRequired()])
    new_card_steps = FormField(NewCardSteps)

    submit = SubmitField('create card')


class AddSteps(FlaskForm):
    edit_card_name = StringField('edit_card_name')
    edit_card_jar = StringField('edit_card_jar')
    added_steps = FormField(NewCardSteps)

    submit = SubmitField('complete edit')


class EditCardSteps(FlaskForm):
    new_card_step_A = StringField('')
    new_card_step_B = StringField('')
    new_card_step_C = StringField('')
    new_card_step_D = StringField('')
    new_card_step_E = StringField('')


class EditCard(FlaskForm):
    edit_card_name = StringField('edit_card_name',
                                 validators=[DataRequired()])
    additional_steps = FormField(EditCardSteps)

    submit = SubmitField('add steps')


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


class CheckboxGroup(FlaskForm):
    chk_one = BooleanField('')
    chk_two = BooleanField('')
    chk_thr = BooleanField('')

    class Meta:
        # This overrides the default value from the base form.
        csrf = False


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


class VariableChks(FlaskForm):
    chks = MultiCheckboxField('Label', choices=[])
    submit = SubmitField('rebloom')


class VariableChksMultiform(FlaskForm):
    tl_chks = MultiCheckboxField(choices=[])
    tm_chks = MultiCheckboxField(choices=[])
    tr_chks = MultiCheckboxField(choices=[])

    ml_chks = MultiCheckboxField(choices=[])
    mr_chks = MultiCheckboxField(choices=[])

    bl_chks = MultiCheckboxField(choices=[])
    bm_chks = MultiCheckboxField(choices=[])
    br_chks = MultiCheckboxField(choices=[])

    submit = SubmitField('rebloom')
