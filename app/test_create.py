from app.card import Card
import config

config.global_init()

# card = Card()
# card.card_name = "house of cards"
#
# card.save()

card = Card.objects().find_one()