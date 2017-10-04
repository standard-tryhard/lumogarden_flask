from flask import render_template
from app import lumo_hub
from app.forms import NewCardForm


@lumo_hub.route('/')
@lumo_hub.route('/grids/')
def grids():

    # sample_card = Card.objects[1]

    return render_template('grids.html')


@lumo_hub.route('/jars/<string:jars_category>/')
def jars():
    pass


@lumo_hub.route('/new_card/', methods=['GET', 'POST'])
def new_card():
    form = NewCardForm()

    return render_template('new_card.html',
                           form=form)