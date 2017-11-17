from collections import namedtuple
from flask import render_template, redirect, url_for
from app import lumo_hub
from app.card import Card
from app.forms import ShowMultipleChkbxForm, EditCardForm

template_card = Card.objects(card_name='...').get()


@lumo_hub.route('/cards/<string:card_from_url>', methods=['GET', 'POST'])
def card_view(card_from_url):
    # create extra variable name to easily reuse and not get confused

    if Card.objects(card_name=card_from_url):
        found_card = Card.objects(card_name=card_from_url).get()
    else:
        found_card = Card.objects(card_name='...').get()

    card_name = card_from_url
    card_in_jar = found_card.card_in_jar

    step_w_num = namedtuple('step_w_num', ['step_name', 'step_no'])
    existing_steps = [step_w_num(s.step_name, s.step_no) for s in
                      found_card.card_steps]

    return render_template('card.html',
                           card_name=card_name,
                           card_in_jar=card_in_jar,
                           existing_steps=existing_steps)
