import mongoengine
from config import global_init

global_init()

class Card(mongoengine.Document):
    card_name = mongoengine.StringField(required=True)
    jar_category = mongoengine.StringField(required=True)

    grid_active = mongoengine.BooleanField(default=False)
    jar_active = mongoengine.BooleanField(default=False)

    steps = mongoengine.EmbeddedDocumentListField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'Cards'
    }

card = Card()
card.card_name = "plums"

card.save()