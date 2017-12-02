from itertools import zip_longest

from app import lumo_hub
from flask import render_template, redirect, url_for
from app.card import Card
from app.forms import ShowMultipleChkbxForm

template_card = Card.objects(card_name='...').get()
positions_ref = ['top_left',
                 'top_mid',
                 'top_right',
                 'mid_left',
                 'mid_right',
                 'botm_left',
                 'botm_mid',
                 'botm_right']


@lumo_hub.route('/set_actives/<string:jar_from_url>', methods=['GET', 'POST'])
def set_actives_view(jar_from_url):
    all_cards_per_jar = sorted(Card.objects(card_in_jar=jar_from_url),
                               key=lambda card: card.card_name)

    choices = [(c.card_name, c.card_name) for c in all_cards_per_jar]
    positions = [c.card_active for c in all_cards_per_jar]

    actives_form = ShowMultipleChkbxForm()
    actives_form.chks.choices = choices

    if actives_form.validate_on_submit():
        # unset all cards in jar to be inactive
        # reset according zip_longest

        active_chks = [chk for chk in actives_form.chks if chk.checked]
        for chk, p in zip_longest(active_chks, positions_ref):
            print(chk.data, p)

        # found_card.save()
        return redirect(url_for('jars_view', jar_from_url=jar_from_url))

    return render_template('set_actives.html',
                           all_cards_per_jar=all_cards_per_jar,
                           actives_form=actives_form,
                           positions=positions)
