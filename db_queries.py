#! venv/bin/python3
from app import mongo

def query_by_grid(grid_category):
	active = mongo.db.Cards.find( {'grid_category': grid_category, 'active_grid': True} )
	card_names = [card['jar_category'].capitalize() for card in active]
	return card_names



