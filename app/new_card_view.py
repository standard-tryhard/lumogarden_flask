from flask import render_template, redirect, url_for
from app import lumo_hub
from app.block import Block
from app.card import Card
from app.card_steps import CardSteps
from app.data_manipulation import get_incmplts_tuple
from app.forms import NewCardForm, TodoButtons


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


