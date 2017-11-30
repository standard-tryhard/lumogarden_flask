from flask import render_template, redirect, url_for
from app import lumo_hub
from app.card import Card
from app.forms import ShowMultipleChkbxForm

template_card = Card.objects(card_name='...').get()


@lumo_hub.route('/edit_card/<string:searched_card>/', methods=['GET', 'POST'])
def edit_card_view(searched_card):
    searched_card = searched_card.capitalize()

    if Card.objects(card_name=searched_card):
        found_card = Card.objects(card_name=searched_card).get()

    else:
        found_card = template_card

    existing_steps = [(s.step_name, s.step_name) for s in found_card.card_steps]
    bools = [s.step_status for s in found_card.card_steps]

    existing_steps_form = ShowMultipleChkbxForm()
    existing_steps_form.chks.choices = existing_steps

    # added_steps_form = EditCardForm()

    if existing_steps_form.validate_on_submit():
        for chk in existing_steps_form.chks:
            n = int(chk.id[-1])
            if chk.checked:
                found_card.card_steps[n].step_status = 1
            else:
                found_card.card_steps[n].step_status = 0

        found_card.save()
        return redirect(url_for('edit_card_view',
                                searched_card=searched_card))

    return render_template('edit_card.html',
                           found_card=found_card,
                           existing_steps_form=existing_steps_form,
                           bools=bools)
