
from flask import render_template, redirect, url_for
from app import lumo_hub
from app.card import Card
from app.forms import ShowMultipleChkbxForm, EditCardForm

template_card = Card.objects(card_name='...').get()


@lumo_hub.route('/dummy/<string:searched_card>/', methods=['GET', 'POST'])
def show_existing_steps(searched_card):
    searched_card = searched_card.capitalize()

    if Card.objects(card_name=searched_card):
        found_card = Card.objects(card_name=searched_card).get()

    else:
        found_card = template_card

    existing_steps = [(s.step_name, s.step_name) for s in found_card.card_steps]
    bools = [s.step_status for s in found_card.card_steps]

    existing_steps_form = ShowMultipleChkbxForm()
    existing_steps_form.chks.choices = existing_steps

    added_steps_form = EditCardForm()


    return render_template('dummy_page.html',
                           found_card=found_card,
                           existing_steps_form=existing_steps_form,
                           added_steps_form=added_steps_form,
                           bools=bools)
