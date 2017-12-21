from flask import render_template, redirect, url_for
from app import lumo_hub
from app.card_model import Card, CardSteps
from app.forms import NewCardForm


@lumo_hub.route('/new_card/', methods=['GET', 'POST'])
def new_card_view():

    new_card_form = NewCardForm()

    if new_card_form.validate_on_submit():

        new_card_name = new_card_form.new_card_name.data.title()
        new_card = Card(card_name=new_card_name,
                        card_in_jar=new_card_form.new_card_jar.data)

        new_card.save()

        step_incr = 0
        for field in new_card_form.new_card_steps:
            if field.data and field.type == 'StringField':
                step = CardSteps(step_no=step_incr, step_name=field.data)
                new_card.update(push__card_steps=step)
                step_incr += 1

        return redirect(url_for('jars_view', jar_from_url=new_card.card_in_jar))

    return render_template('new_card.html', new_card_form=new_card_form)


