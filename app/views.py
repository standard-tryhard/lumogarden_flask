from flask import render_template, flash, redirect
from app import lumo_hub, mongo
import pymongo

@lumo_hub.route('/')
@lumo_hub.route('/grids/')
def grids():
	user = {'nickname': 'Thomas'}

	arte_card = mongo.db.Cards.find_one( {'grid_category': 'arte'} )
	tasks = arte_card['tasks']
	tasks = [t['step'] for t in tasks if t['status'] == "incomplete"][:3]
	# print(arte_card)
	# tasks = [t for t in task = #arte_card['tasks'][:3]

	return render_template('grids.html',  
							user=user,
							tasks=tasks)


@lumo_hub.route('/jars/<string:jars_name>/')
def jars(jars_name):
	return render_template('jars.html', 
						  jars_name=jars_name)

@lumo_hub.route('/test/')
def test():
	return render_template('grids.html')


