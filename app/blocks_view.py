from flask import render_template, redirect, url_for
from app import lumo_hub
from app.block_model import Block
from app.forms import TodoButtonsImproved


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
    blocks_form = TodoButtonsImproved()

    if blocks_form.validate_on_submit():
        return redirect(url_for('blocks_view'))

    return render_template('blocks.html',
                           block_positions=return_block_positions(),
                           blocks_form=blocks_form)
