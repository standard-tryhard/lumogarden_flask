import mongoengine
from config import global_init


global_init()


class GridPositions(mongoengine.Document):
    positions = mongoengine.DictField()

    meta = {
        'db_alias': 'core',
        'collection': 'Block'
    }


class CardActives(mongoengine.EmbeddedDocument):
    card_active = mongoengine.StringField(min_length=1, max_length=100)


class Block(mongoengine.Document):
    position = mongoengine.StringField(required=True)
    block_name = mongoengine.StringField(min_length=1, max_length=100)
    card_actives = mongoengine.EmbeddedDocumentListField(CardActives)

    meta = {
        'db_alias': 'core',
        'collection': 'Block'
    }
