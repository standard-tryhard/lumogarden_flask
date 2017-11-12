from flask import render_template, redirect, url_for
from app import lumo_hub
from app.block import Block
from app.card import Card
from app.card_steps import CardSteps
from app.data_manipulation import get_incmplts_tuple
from app.forms import NewCardForm, TodoButtons, TodoButtonsImproved
from itertools import zip_longest

template_card = Card.objects(card_name='...').get()


@lumo_hub.route('/jars/<string:jar_from_url>/', methods=['GET', 'POST'])
def jars_view(jar_from_url):


    def get_jar_positions(position):
        if Card.objects(card_in_jar=jar_from_url,
                        card_active=position):

            found_active = Card.objects(card_in_jar=jar_from_url,
                                        card_active=position).get()
            return found_active

        else:
            return template_card

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

    # form_data_tl = get_incmplts_tuple(tl)
    # form_data_tm = get_incmplts_tuple(tm)
    # form_data_tr = get_incmplts_tuple(tr)
    # form_data_ml = get_incmplts_tuple(ml)
    # form_data_tr = get_incmplts_tuple(tr)
    # form_data_bl = get_incmplts_tuple(bl)
    # form_data_bm = get_incmplts_tuple(bm)
    # form_data_br = get_incmplts_tuple(br)

    # for card in jar_positions.values():
    #     print(card.card_name)
    form = TodoButtonsImproved()

    # def load_chk_data(form, cards)
    for subform, card in zip_longest(form, jar_positions.values()):
        idx = 0
        if subform.type == 'FormField':
            for chk in subform:
                chk.id, chk.label = get_incmplts_tuple(card)[idx]
                idx += 1

    # for subform in form.checkforms:
    #     for todo_chk in subform:
    #         todo_chk.id, todo_chk.label =

    # (form.chk_tl_L1.id,
    #  form.chk_tl_L1.label) = form_data_tl[0]
    #
    # (form.chk_tl_L2.id,
    #  form.chk_tl_L2.label) = form_data_tl[1]
    #
    # (form.chk_tl_L3.id,
    #  form.chk_tl_L3.label) = form_data_tl[2]
    #
    # (form.chk_tm_M1.id,
    #  form.chk_tm_M1.label) = form_data_tm[0]
    #
    # (form.chk_tm_M2.id,
    #  form.chk_tm_M2.label) = form_data_tm[1]
    #
    # (form.chk_tm_M3.id,
    #  form.chk_tm_M3.label) = form_data_tm[2]


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
