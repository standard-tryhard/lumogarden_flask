import pymongo
from flask import render_template, flash, redirect
from app import lumo_hub, mongo
import db_queries

@lumo_hub.route('/')
@lumo_hub.route('/grids/')
def grids():

	
	# print(arte_card)
	# tasks = [t for t in task = #arte_card['tasks'][:3]

	return render_template('grids.html',  
							active_lght_cards=db_queries.query_by_grid('lght'),
							active_care_cards=db_queries.query_by_grid('care'),
							active_arte_cards=db_queries.query_by_grid('arte'),

							active_soft_cards=db_queries.query_by_grid('soft'),
							active_musc_cards=db_queries.query_by_grid('musc'),

							active_utfh_cards=db_queries.query_by_grid('utfh'),
							active_erth_cards=db_queries.query_by_grid('erth'),
							active_wrte_cards=db_queries.query_by_grid('wrte')
							)


@lumo_hub.route('/jars/<string:jars_name>/')
def jars(jars_name):
	return render_template('jars.html', 
						  jars_name=jars_name)

@lumo_hub.route('/test/')
def test():
	return render_template('grids.html')


