from flask import render_template, flash, redirect
from app import lumo_hub, mongo

@lumo_hub.route('/')
@lumo_hub.route('/grids/')
def grids():
	user = {'nickname': 'Thomas'}

	users = mongo.db.users.find( {} )

	return render_template('grids.html',  
							user=user,
							users=users)


@lumo_hub.route('/jars/<string:jars_name>/')
def jars(jars_name):
	return render_template('jars.html', 
						  jars_name=jars_name)

@lumo_hub.route('/test/')
def test():
	return render_template('grids.html')


