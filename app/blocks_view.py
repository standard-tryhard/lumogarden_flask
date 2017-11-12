from flask import render_template, redirect, url_for
from app import lumo_hub
from app.block import Block
from app.card import Card
from app.card_steps import CardSteps
from app.data_manipulation import get_incmplts_tuple
from app.forms import NewCardForm, TodoButtons


@lumo_hub.route('/', methods=['GET', 'POST'])
@lumo_hub.route('/blocks/', methods=['GET', 'POST'])
def blocks_view():
    form = TodoButtons()

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

    if form.validate_on_submit():
        return redirect(url_for('blocks_view'))

    return render_template('blocks.html',
                           block_positions=block_positions,
                           form=form)
