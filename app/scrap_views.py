from flask import render_template, redirect, url_for
from app import lumo_hub
from app.card import Card
from app.forms import TodoButtons

template_card = Card.objects(card_name='...').get()


@lumo_hub.route('/dummy/<string:searched_card>/', methods=['GET', 'POST'])
def show_existing_steps(searched_card):
    searched_card = searched_card.capitalize()

    if Card.objects(card_name=searched_card):
        found_card = Card.objects(card_name=searched_card).get()

    else:
        found_card = template_card

    return render_template('dummy_page.html',
                           found_card=found_card)
