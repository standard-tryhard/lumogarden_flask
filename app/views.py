from flask import render_template
from app import lumo_hub
from app.block import Block
from app.card import Card
from app.data_manipulation import get_incmplts
from app.forms import NewCardForm, Buttons


template_card = Card.objects(card_name='...').get()

@lumo_hub.route('/')
@lumo_hub.route('/blocks/')
def blocks():

    tl = Block.objects.get(position='top_left')
    tm = Block.objects.get(position='top_mid')
    tr = Block.objects.get(position='top_right')
    ml = Block.objects.get(position='mid_left')
    mr = Block.objects.get(position='mid_right')
    bl = Block.objects.get(position='botm_left')
    bm = Block.objects.get(position='botm_mid')
    br = Block.objects.get(position='botm_right')

    block_positions = {}
    block_positions['tl'] = tl
    block_positions['tm'] = tm
    block_positions['tr'] = tr
    block_positions['ml'] = ml
    block_positions['mr'] = mr
    block_positions['bl'] = bl
    block_positions['bm'] = bm
    block_positions['br'] = br

    return render_template('blocks.html',
                           block_positions=block_positions)

@lumo_hub.route('/jars/<string:jar_from_url>/')
def jars(jar_from_url):
    jar_buttons=Buttons()

    def get_jar_positions(position):
        if Card.objects(card_in_jar=jar_from_url,
                        card_active=position):

            found_active = Card.objects(card_in_jar=jar_from_url,
                                        card_active=position).get()
            return found_active

        else:
            # template card assigned at top of this file for all routes to use
            return template_card

    tl = get_jar_positions('top_left')
    tm = get_jar_positions('top_mid')
    tr = get_jar_positions('top_right')
    ml = get_jar_positions('mid_left')
    mr = get_jar_positions('mid_right')
    bl = get_jar_positions('botm_left')
    bm = get_jar_positions('botm_mid')
    br = get_jar_positions('botm_right')

    jar_positions = {}
    jar_positions['tl'] = tl
    jar_positions['tm'] = tm
    jar_positions['tr'] = tr
    jar_positions['ml'] = ml
    jar_positions['mr'] = mr
    jar_positions['bl'] = bl
    jar_positions['bm'] = bm
    jar_positions['br'] = br

    next_actionable_steps = {}
    next_actionable_steps['tl'] = get_incmplts(tl)
    next_actionable_steps['tm'] = get_incmplts(tm)
    next_actionable_steps['tr'] = get_incmplts(tr)
    next_actionable_steps['ml'] = get_incmplts(ml)
    next_actionable_steps['mr'] = get_incmplts(mr)
    next_actionable_steps['bl'] = get_incmplts(bl)
    next_actionable_steps['bm'] = get_incmplts(bm)
    next_actionable_steps['br'] = get_incmplts(br)



    # return render_template('jars.html', jar_from_url=get_jar_positions('money'))

    return render_template('jars.html',
                           jar_positions=jar_positions,
                           next_actionable_steps=next_actionable_steps,
                           jar_buttons=jar_buttons)


@lumo_hub.route('/new_card/', methods=['GET', 'POST'])
def new_card():
    form = NewCardForm()

    return render_template('new_card.html',
                           form=form)