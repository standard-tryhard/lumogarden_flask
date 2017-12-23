from flask import Flask


lumo_hub = Flask(__name__)
lumo_hub.config['SECRET_KEY'] = 'SECRET!'
lumo_hub.config.from_object('config')
from app import (blocks_view, jars_view, pins_view,
                 new_card_view, edit_card_view, card_view,
                 all_cards)
