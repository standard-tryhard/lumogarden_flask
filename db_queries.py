#! venv/bin/python3
from app import mongo

def query_active_blocks():
	active_blocks_object = mongo.db.ActiveBlocks.find_one({'name':'active_blocks'}, {'positions':1, '_id':0})
	active_blocks = active_blocks_object['positions'][0]
	return active_blocks

def query_active_grids(grid_category):
	active = mongo.db.Cards.find( {'grid_category': grid_category, 'active_grid': True} )
	active_grid_cards = [card['jar_category'].capitalize() for card in active]
	return active_grid_cards

def query_active_jars(jar_category):
	active = mongo.db.Cards.find(  {"active_jar":True, "grid_category":jar_category}  )
	active_jar_cards = [card['jar_category'].capitalize() for card in active]
	return active_jar_cards


