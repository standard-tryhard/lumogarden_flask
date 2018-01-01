import mongoengine
from config import global_init


global_init()


class GridPositions(mongoengine.Document):
    positions = mongoengine.DictField()

    meta = {
        'db_alias': 'core',
        'collection': 'Block'
    }


class Block(mongoengine.Document):
    position = mongoengine.StringField(required=True)
    block_name = mongoengine.StringField(min_length=1, max_length=100)

    card_actives = mongoengine.ListField(mongoengine.StringField(
                                        min_length=1, max_length=100))

    meta = {
        'db_alias': 'core',
        'collection': 'Block'
    }
