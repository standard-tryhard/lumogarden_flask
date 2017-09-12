from flask import render_template, flash, redirect
from app import lumo_hub, db

@lumo_hub.route('/')
@lumo_hub.route('/grids/')
def grids():
	user = {'nickname': 'Thomas'}

	# db = mongo.db.lumogrids_flask

	return render_template('grids.html',  
							user=user)


@lumo_hub.route('/jars/<string:jars_name>/')
def jars(jars_name):
	return render_template('jars.html', 
						  jars_name=jars_name)

@lumo_hub.route('/test/')
def test():
	return render_template('grids.html')


