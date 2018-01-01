import collections
from itertools import zip_longest

import itertools

from app import lumo_hub
from flask import render_template, redirect, url_for
from app.card_model import Card
from app.forms import ShowMultipleChkbxForm, PinCardsBlocks
from app.blocks_view import block_positions


# print(block_positions['tm'])

template_card = Card.objects(card_name='...').get()
positions_ref = ['top_left',
                 'top_mid',
                 'top_right',
                 'mid_left',
                 'mid_right',
                 'botm_left',
                 'botm_mid',
                 'botm_right']


@lumo_hub.route('/pin_to_jars/<string:jar_from_url>', methods=['GET', 'POST'])
def pin_to_jars(jar_from_url):
    all_cards_per_jar = sorted(Card.objects(card_in_jar=jar_from_url),
                               key=lambda card: card.card_name)

    choices = [(c.card_name, c.card_name) for c in all_cards_per_jar]
    positions = [c.card_active for c in all_cards_per_jar]

    actives_form = ShowMultipleChkbxForm()
    actives_form.chks.choices = choices

    if actives_form.validate_on_submit():
        Card.objects(card_in_jar=jar_from_url).update(
            set__card_active='inactive')


        active_chks = [chk for chk in actives_form.chks if chk.checked]
        for chk, p in zip_longest(active_chks, positions_ref):
            if chk:
                Card.objects(card_name=chk.data,
                             card_in_jar=jar_from_url).update_one(
                    set__card_active=p)

        return redirect(url_for('jars_view', jar_from_url=jar_from_url))

    return render_template('pin_to_jars.html',
                           all_cards_per_jar=all_cards_per_jar,
                           actives_form=actives_form,
                           positions=positions)


@lumo_hub.route('/pin_to_blocks/', methods=['GET', 'POST'])
def pin_to_blocks():


    def cards_by_block(block):
        retrieved_cards = sorted(Card.objects(card_in_jar=block.block_name),
                                  key=lambda card: card.card_name)
        card_names = [c.card_name for c in retrieved_cards]
        return card_names


    form = PinCardsBlocks()
    subforms = [sf for sf in form if sf.type == "MultiCheckboxField"]

    # I don't think this a good implementation, what if all the blocks aren't full?
    # I should come back to this...
    for sf, bp in itertools.zip_longest(subforms, block_positions.values()):
        sf.choices = [(c, c) for c in cards_by_block(bp)]
        sf.label = bp.block_name


    subforms_dict = {sf.name: sf for sf in subforms}
    all_pinned_dict = ({b.block_name: b.card_actives
                        for b in block_positions.values()})
    print(all_pinned_dict)

    if form.validate_on_submit():
        for sf in subforms_dict.values():
            block_str = sf.id[:2]
            block = block_positions[block_str]
            for chk in sf:
                data = chk.__dict__['data']
                if chk.checked == True:
                    block.update(add_to_set__card_actives=data)
                else:
                    block.update(pull__card_actives=data)

        return redirect(url_for('pin_to_blocks'))



    return render_template('pin_to_blocks.html',
                           form=form,
                           subforms_dict=subforms_dict)
