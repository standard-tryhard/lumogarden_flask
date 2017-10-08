import mongoengine
from app.card_steps import CardSteps
from config import global_init

global_init()


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

test = Card()
test.name = 'moo'

babies = CardSteps()
babies.step_name = 'another one'
babies.step_no = 1

# updated = Card.objects(name='testie').update_one(push__steps=babies)

if __name__ == '__main__':
    print('ok')

