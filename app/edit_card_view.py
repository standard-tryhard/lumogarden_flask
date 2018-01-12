from flask import render_template, redirect, url_for
from app import lumo_hub
from app.card_model import Card, CardSteps
from app.forms import VariableChks, AddSteps

template_card = Card.objects(card_name='...').get()

def validate_jar(jar):
    return jar in ['arte','care', 'erth', 'lght',
                           'musc', 'soft', 'utfh', 'wrte']


@lumo_hub.route('/edit_card/<string:searched_card>/', methods=['GET', 'POST'])
def edit_card_view(searched_card):
    searched_card = searched_card.title()

    match = Card.objects(card_name=searched_card)
    found_card = (Card.objects(card_name=searched_card).get() if match
    else template_card)

    existing_steps = [(s.step_name, s.step_name) for s in found_card.card_steps]
    bools = [s.step_status for s in found_card.card_steps]

    existing_steps_form = VariableChks()
    existing_steps_form.chks.choices = existing_steps

    add_steps_form = AddSteps()


    if add_steps_form.validate_on_submit():


        (updtd_card_name, updtd_to_jar) = [field for field in add_steps_form
                                               if field.type == "StringField"]

        updtd_card_name, updtd_to_jar = updtd_card_name.data, updtd_to_jar.data

        updtd_card_name = updtd_card_name.title()
        updtd_to_jar    = updtd_to_jar.lower()

        if updtd_card_name:
            found_card.update(set__card_name=updtd_card_name)
            searched_card = updtd_card_name.title()

        if updtd_to_jar and validate_jar(updtd_to_jar):
            found_card.update(set__card_in_jar=updtd_to_jar)


        curr_incr = found_card.card_steps.count()

        for step in add_steps_form.added_steps:
            if step.type == "StringField" and step.data:
                curr_incr = curr_incr + 1
                step_doc = CardSteps(step_no=curr_incr, step_name=step.data)
                found_card.update(push__card_steps=step_doc)

        return redirect(url_for('edit_card_view',
                                searched_card=searched_card))


    elif existing_steps_form.validate_on_submit():

        for chk in existing_steps_form.chks:
            n = int(chk.id[-1])
            found_card.card_steps[n].step_status = 1 if chk.checked else 0

        found_card.save()
        return redirect(url_for('edit_card_view',
                                searched_card=searched_card))

    return render_template('edit_card.html',
                           found_card=found_card,
                           existing_steps_form=existing_steps_form,
                           add_steps_form=add_steps_form,
                           bools=bools)
