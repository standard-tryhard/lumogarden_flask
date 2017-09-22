import pymongo
from flask import render_template, flash, redirect
from app import lumo_hub, mongo
import db_queries

@lumo_hub.route('/')
@lumo_hub.route('/grids/')
def grids():

	active_blocks = db_queries.query_active_blocks()

	
	# print(arte_card)
	# tasks = [t for t in task = #arte_card['tasks'][:3]

	return render_template('grids.html',  
					tl=db_queries.query_by_grid(active_blocks['top_left']),
					tm=db_queries.query_by_grid(active_blocks['top_mid']),
					tr=db_queries.query_by_grid(active_blocks['top_right']),

					ml=db_queries.query_by_grid(active_blocks['mid_left']),
					mr=db_queries.query_by_grid(active_blocks['mid_right']),

					bl=db_queries.query_by_grid(active_blocks['botm_left']),
					bm=db_queries.query_by_grid(active_blocks['botm_mid']),
					br=db_queries.query_by_grid(active_blocks['botm_right']),
					active_blocks=active_blocks
							)


@lumo_hub.route('/jars/<string:jars_name>/')
def jars(jars_name):
	return render_template('jars.html', 
						  jars_name=jars_name)

@lumo_hub.route('/test/')
def test():
	return render_template('grids.html')


