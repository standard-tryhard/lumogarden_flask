#! venv/bin/python3
from app import mongo

def query_by_grid(grid_category):
	active = mongo.db.Cards.find( {'grid_category': grid_category, 'active_grid': True} )
	card_names = [card['jar_category'].capitalize() for card in active]
	return card_names

def query_active_blocks():
	active_blocks_object = mongo.db.ActiveBlocks.find_one({'name':'active_blocks'}, {'positions':1, '_id':0})
	active_blocks = active_blocks_object['positions'][0]
	return active_blocks

