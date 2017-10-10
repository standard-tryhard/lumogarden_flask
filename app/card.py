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


# steps = CardSteps()
# steps.step_name = "Find mouse"
# steps.step_no = 0
# steps.step_status = 1


card = Card()
card.name = 'works in blue'.title()

card_steps = CardSteps()
card_steps.step_name = 'email 20 galleries'
card_steps.step_no = 1

# card.save()

updated = Card.objects(name='works in blue'.title()).update_one(push__steps=card_steps)

if __name__ == '__main__':
    print('ok')

print(updated)