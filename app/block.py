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
    jar_slots = mongoengine.IntField(default=3)


    jar_a = mongoengine.ObjectIdField(default=None)
    jar_b = mongoengine.ObjectIdField(default=None)
    jar_c = mongoengine.ObjectIdField(default=None)
    jar_d = mongoengine.ObjectIdField(default=None)
    jar_e = mongoengine.ObjectIdField(default=None)


    meta = {
        'db_alias': 'core',
        'collection': 'Block'
    }


# test = Block.objects[0]
#
# print(test.jar_a)
# test_card = Card.objects.get(id='59d284036c0f8a061f65e2f0')

# a = test_card.steps[0].step_no
# print(a)



