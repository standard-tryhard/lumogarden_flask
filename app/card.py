import mongoengine
from app.card_steps import CardSteps
from config import global_init

global_init()

# class Cards(mongoengine.Document):
#     card_name = mongoengine.StringField(required=True)
#     jar_category = mongoengine.StringField(required=True)
#
#     grid_active = mongoengine.BooleanField(default=False)
#     jar_active = mongoengine.BooleanField(default=False)
#
#     steps = mongoengine.EmbeddedDocumentListField(CardSteps)
#
#     meta = {
#         'db_alias': 'core',
#         'collection': 'Cards'
#     }


class Card(mongoengine.Document):
    name = mongoengine.StringField()
    steps = mongoengine.EmbeddedDocumentListField(CardSteps)

    meta = {
        'db_alias': 'core',
        'collection': 'Card'
    }


steps = CardSteps()
steps.step_name = "Find mouse"
steps.step_no = 0
steps.step_status = 1

updated = Card.objects[0].update(
    add_to_set__steps=steps)


