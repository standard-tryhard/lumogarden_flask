from collections import namedtuple
from flask import render_template, redirect, url_for
from app import lumo_hub
from app.card import Card
from app.forms import ShowMultipleChkbxForm

template_card = Card.objects(card_name='...').get()


@lumo_hub.route('/cards/<string:card_from_url>', methods=['GET', 'POST'])
def card_view(card_from_url):
    # create extra variable name to easily reuse and not get confused

    if Card.objects(card_name=card_from_url):
        found_card = Card.objects(card_name=card_from_url).get()
    else:
        found_card = Card.objects(card_name='...').get()

    card_name = card_from_url
    card_in_jar = found_card.card_in_jar

    existing_steps = [(s.step_name, s.step_name) for s in found_card.card_steps]
    bools = [s.step_status for s in found_card.card_steps]

    existing_steps_form = ShowMultipleChkbxForm()
    existing_steps_form.chks.choices = existing_steps

    if existing_steps_form.validate_on_submit():
        for chk in existing_steps_form.chks:
            n = int(chk.id[-1])
            if chk.checked:
                found_card.card_steps[n].step_status = 1
            else:
                found_card.card_steps[n].step_status = 0

        found_card.save()
        return redirect(url_for('card_view',
                                card_from_url=card_from_url))


    return render_template('card.html',
                           card_name=card_name,
                           card_in_jar=card_in_jar,
                           found_card=found_card,
                           existing_steps_form=existing_steps_form,
                           bools=bools)

    # step_w_num = namedtuple('step_w_num', ['step_name', 'step_no'])
    # existing_steps = [step_w_num(s.step_name, s.step_no) for s in
    #                   found_card.card_steps]
    #
    # return render_template('card.html',
    #                        card_name=card_name,
    #                        card_in_jar=card_in_jar,
    #                        existing_steps=existing_steps)
