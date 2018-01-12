import itertools
from itertools import zip_longest

from flask import render_template, redirect, url_for
from app import lumo_hub
from app.block_model import Block
from app.card_model import Card
from app.card_step_data_collect import get_incmplts_tuple_and_cardname
from app.forms import VariableChksMultiform

def return_block_positions():
    tl = Block.objects.get(position='top_left')
    tm = Block.objects.get(position='top_mid')
    tr = Block.objects.get(position='top_right')
    ml = Block.objects.get(position='mid_left')
    mr = Block.objects.get(position='mid_right')
    bl = Block.objects.get(position='botm_left')
    bm = Block.objects.get(position='botm_mid')
    br = Block.objects.get(position='botm_right')

    block_positions = {
        'tl': tl,
        'tm': tm,
        'tr': tr,
        'ml': ml,
        'mr': mr,
        'bl': bl,
        'bm': bm,
        'br': br
    }

    return block_positions


@lumo_hub.route('/', methods=['GET', 'POST'])
@lumo_hub.route('/blocks/', methods=['GET', 'POST'])
def blocks_view():
    block_positions = return_block_positions()

    form = VariableChksMultiform()

    subforms = [sf for sf in form if sf.type == "MultiCheckboxField"]


    # Instead of retrieving Card Names as Str, I'd like to refactor this
    # so that it returns card objects; Or I could return UID's...

    # THIS needs to be cleaned
    for sf, block in zip_longest(subforms, block_positions.values()):
        pinned_card_objects = \
            (Card.objects(card_name=c).get() for c in block.card_actives)

        sf.choices = list(map(
            lambda card: get_incmplts_tuple_and_cardname(card)[0], pinned_card_objects))


    if form.validate_on_submit():
        return redirect(url_for('blocks_view'))


    return render_template('blocks.html',
                           block_positions=block_positions,
                           form=form)

