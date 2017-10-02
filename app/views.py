from flask import render_template
from app.card import Card
from app import lumo_hub


@lumo_hub.route('/')
@lumo_hub.route('/grids/')
def grids():

    sample_card = Card.objects().find_one()

    return render_template('grids.html', sample_card=sample_card)


@lumo_hub.route('/jars/<string:jars_category>/')
def jars():
    pass

