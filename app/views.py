import pymongo
from flask import render_template, flash, redirect
from app import lumo_hub, mongo
import db_queries

@lumo_hub.route('/')
@lumo_hub.route('/grids/')
def grids():

	active_blocks = db_queries.query_active_blocks()

	return render_template('grids.html',  
					tl=db_queries.query_active_grids(active_blocks['top_left']),
					tm=db_queries.query_active_grids(active_blocks['top_mid']),
					tr=db_queries.query_active_grids(active_blocks['top_right']),

					ml=db_queries.query_active_grids(active_blocks['mid_left']),
					mr=db_queries.query_active_grids(active_blocks['mid_right']),

					bl=db_queries.query_active_grids(active_blocks['botm_left']),
					bm=db_queries.query_active_grids(active_blocks['botm_mid']),
					br=db_queries.query_active_grids(active_blocks['botm_right']),
					active_blocks=active_blocks
							)


@lumo_hub.route('/jars/<string:jars_category>/')
def jars(jars_category):

	active_jars = db_queries.query_active_jars(jars_category)

	return render_template('jars.html',
					# tl=db_queries.query_active_grids(active_jars['top_left']),
					# tm=db_queries.query_active_grids(active_jars['top_mid']),
					# tr=db_queries.query_active_grids(active_jars['top_right']),

					# ml=db_queries.query_active_grids(active_jars['mid_left']),
					# mr=db_queries.query_active_grids(active_jars['mid_right']),

					# bl=db_queries.query_active_grids(active_jars['botm_left']),
					# bm=db_queries.query_active_grids(active_jars['botm_mid']),
					# br=db_queries.query_active_grids(active_jars['botm_right']),
					active_jars=active_jars)



