import mongoengine
from app.card_steps import CardSteps
from config import global_init

global_init()


class Card(mongoengine.Document):
    card_name = mongoengine.StringField(required=True)
    card_in_jar = mongoengine.StringField(required=True)
    card_active = mongoengine.StringField(default='inactive')
    card_steps = mongoengine.EmbeddedDocumentListField(CardSteps)


    meta = {
        'db_alias': 'core',
        'collection': 'Card'
    }
