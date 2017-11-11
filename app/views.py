from flask import render_template, redirect, url_for
from app import lumo_hub
from app.block import Block
from app.card import Card
from app.card_steps import CardSteps
from app.data_manipulation import get_incmplts_tuple
from app.forms import NewCardForm, TodoButtons

template_card = Card.objects(card_name='...').get()


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


@lumo_hub.route('/jars/<string:jar_from_url>/', methods=['GET', 'POST'])
def jars_view(jar_from_url):

    def get_jar_positions(position):
        if Card.objects(card_in_jar=jar_from_url,
                        card_active=position):

            found_active = Card.objects(card_in_jar=jar_from_url,
                                        card_active=position).get()
            return found_active

        else:
            # template card assigned at top
            # of this file for all routes to use
            return template_card

    # renamed this to make it more
    # readable when using it as part of link
    jar_name = jar_from_url.upper()

    tl = get_jar_positions('top_left')
    tm = get_jar_positions('top_mid')
    tr = get_jar_positions('top_right')
    ml = get_jar_positions('mid_left')
    mr = get_jar_positions('mid_right')
    bl = get_jar_positions('botm_left')
    bm = get_jar_positions('botm_mid')
    br = get_jar_positions('botm_right')

    jar_positions = {
        'tl': tl,
        'tm': tm,
        'tr': tr,
        'ml': ml,
        'mr': mr,
        'bl': bl,
        'bm': bm,
        'br': br
        }

    # next_actions = {
    #     'tl': get_incmplts(tl),
    #     'tm': get_incmplts(tm),
    #     'tr': get_incmplts(tr),
    #     'ml': get_incmplts(ml),
    #     'mr': get_incmplts(mr),
    #     'bl': get_incmplts(bl),
    #     'bm': get_incmplts(bm),
    #     'br': get_incmplts(br)
    #     }

    form_data_tl = get_incmplts_tuple(tl)
    form_data_tm = get_incmplts_tuple(tm)
    form = TodoButtons()

    (form.chk_tl_L1.id,
     form.chk_tl_L1.label) = form_data_tl[0]

    (form.chk_tl_L2.id,
     form.chk_tl_L2.label) = form_data_tl[1]

    (form.chk_tl_L3.id,
     form.chk_tl_L3.label) = form_data_tl[2]

    (form.chk_tm_M1.id,
     form.chk_tm_M1.label) = form_data_tm[0]

    (form.chk_tm_M2.id,
     form.chk_tm_M2.label) = form_data_tm[1]



    if form.validate_on_submit():
            for field in form:
                if field.type == 'BooleanField' and field.data:
                    c = field.name[4:6]; card = jar_positions[c]
                    n = field.id
                    card.card_steps[n].step_status = 1
            card.save()

            return redirect(url_for('jars_view', jar_from_url=jar_from_url))

    return render_template('jars.html',
                           jar_name=jar_name,
                           jar_positions=jar_positions,
                           form=form)


# I'd like to put in some kind of save message or something...
# ...or... like a display new_card field...

@lumo_hub.route('/new_card/', methods=['GET', 'POST'])
def new_card_view():

    form = NewCardForm()

    if form.validate_on_submit():

        new_card = Card(card_name=form.new_card_name.data,
                        card_in_jar=form.new_card_jar.data)

        new_card.save()
        step_incr = 0
        for field in form.new_card_steps:
            if field.data and field.type == 'StringField':
                step = CardSteps(step_no=step_incr, step_name=field.data)
                new_card.update(push__card_steps=step)
                step_incr += 1

        return redirect(url_for('new_card_view'))

    return render_template('new_card.html', form=form)


