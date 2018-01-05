from app import lumo_hub
from flask import render_template, redirect, url_for
from app.card_model import Card
from app.blocks_view import return_block_positions

template_card = Card.objects(card_name='...').get()


@lumo_hub.route('/all_cards/', methods=['GET'])
def all_cards_view():
    block_positions = return_block_positions()
    total_cards = Card.objects.count()

    all_blocks = (b.block_name for b in block_positions.values())
    all_jars = (Card.objects(card_in_jar=card) for card in all_blocks)
    all_cards = (card for jar in all_jars for card in jar)


    return render_template('all_cards.html',
                           all_cards=all_cards,
                           total_cards=total_cards)


@lumo_hub.route('/delete_card/<string:card>/', methods=['GET', 'POST'])
def delete_card(card):
    print('ok')
    print(card)

    Card.objects(card_name=card).delete()

    return redirect(url_for('all_cards_view'))
