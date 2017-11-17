from itertools import zip_longest

from flask import render_template, redirect, url_for
from app import lumo_hub
from app.card import Card
from app.forms import TodoButtons, ShowMultipleChkbxForm

template_card = Card.objects(card_name='...').get()


@lumo_hub.route('/dummy/<string:searched_card>/', methods=['GET', 'POST'])
def show_existing_steps(searched_card):
    searched_card = searched_card.capitalize()

    if Card.objects(card_name=searched_card):
        found_card = Card.objects(card_name=searched_card).get()

    else:
        found_card = template_card

    steps_for_form = [(s.step_name, s.step_name) for s in found_card.card_steps]
    bools = [s.step_status for s in found_card.card_steps]

    form = ShowMultipleChkbxForm()
    form.chk.choices = steps_for_form


    return render_template('dummy_page.html',
                           found_card=found_card,
                           form=form)
