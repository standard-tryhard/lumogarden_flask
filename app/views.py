from flask import render_template
from app import lumo_hub
from app.block import Block
from app.card import Card
from app.data_manipulation import get_incmplts
from app.forms import NewCardForm


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

    return render_template('blocks.html',
                           tl=tl,
                           tm=tm,
                           tr=tr,
                           ml=ml,
                           mr=mr,
                           bl=bl,
                           bm=bm,
                           br=br)


@lumo_hub.route('/jars/<string:jar_from_url>/')
def jars(jar_from_url):


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

    positions_dict = {}
    positions_dict['tl'] = tl
    positions_dict['tm'] = tm
    positions_dict['tr'] = tr
    positions_dict['ml'] = ml
    positions_dict['mr'] = mr
    positions_dict['bl'] = bl
    positions_dict['bm'] = bm
    positions_dict['br'] = br

    next_actionable_steps = {}
    next_actionable_steps['tl'] = get_incmplts(tl)


    # return render_template('jars.html', jar_from_url=get_jar_positions('money'))

    return render_template('jars.html',
                           positions_dict=positions_dict,
                           next_actionable_steps=next_actionable_steps)


@lumo_hub.route('/new_card/', methods=['GET', 'POST'])
def new_card():
    form = NewCardForm()

    return render_template('new_card.html',
                           form=form)