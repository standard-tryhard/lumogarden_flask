from flask import render_template
from app import lumo_hub


@lumo_hub.route('/')
@lumo_hub.route('/grids/')
def grids():
    pass


@lumo_hub.route('/jars/<string:jars_category>/')
def jars():
    pass

