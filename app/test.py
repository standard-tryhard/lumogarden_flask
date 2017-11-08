from flask import render_template  # render_template_string, redirect, url_for
from app import lumo_hub
from app.card import Card
from app.data_manipulation import get_incmplts
from app.forms import ExampleForm

# template_card = Card.objects(card_name='...').get()


# @lumo_hub.route('/test/<string:jar_from_url>', methods=['GET', 'POST'])
# def test(jar_from_url):
#     form = ExampleForm()
#
#     def get_jar_positions(position):
#         if Card.objects(card_in_jar=jar_from_url,
#                         card_active=position):
#
#             found_active = Card.objects(card_in_jar=jar_from_url,
#                                         card_active=position).get()
#             return found_active
#
#         else:
#             # template card assigned at top of this file for all routes to use
#             return template_card
#
#     # renamed this to make it more readable when using it as part of link
#     jar_name = jar_from_url.upper()
#
#     tl = get_jar_positions('top_left')
#     tm = get_jar_positions('top_mid')
#     tr = get_jar_positions('top_right')
#     ml = get_jar_positions('mid_left')
#     mr = get_jar_positions('mid_right')
#     bl = get_jar_positions('botm_left')
#     bm = get_jar_positions('botm_mid')
#     br = get_jar_positions('botm_right')
#
#     jar_positions = {
#         'tl': tl,
#         'tm': tm,
#         'tr': tr,
#         'ml': ml,
#         'mr': mr,
#         'bl': bl,
#         'bm': bm,
#         'br': br
#         }
#
#     next_actionable_steps = {
#         'tl': get_incmplts(tl),
#         'tm': get_incmplts(tm),
#         'tr': get_incmplts(tr),
#         'ml': get_incmplts(ml),
#         'mr': get_incmplts(mr),
#         'bl': get_incmplts(bl),
#         'bm': get_incmplts(bm),
#         'br': get_incmplts(br)
#         }
#
#     if form.validate_on_submit():
#             if form.chk_A.data:
#                 print('it is')
#             return redirect(url_for('test', jar_from_url=jar_from_url))
#
#     return render_template('testing.html',
#                            jar_name=jar_name,
#                            jar_positions=jar_positions,
#                            next_actionable_steps=next_actionable_steps,
#                            form=form)

