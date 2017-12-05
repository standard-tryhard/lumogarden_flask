import mongoengine
from config import global_init

global_init()


class CardSteps(mongoengine.EmbeddedDocument):
    step_no = mongoengine.IntField()
    step_name = mongoengine.StringField(required=True)
    step_status = mongoengine.IntField(default=0)

class Card(mongoengine.Document):
    card_name = mongoengine.StringField(required=True)
    card_in_jar = mongoengine.StringField(required=True)
    card_active = mongoengine.StringField(default='inactive')
    card_steps = mongoengine.EmbeddedDocumentListField(CardSteps)


    meta = {
        'db_alias': 'core',
        'collection': 'Card'
    }

