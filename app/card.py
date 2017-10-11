import mongoengine
from app.card_steps import CardSteps
from config import global_init

global_init()


class Card(mongoengine.Document):
    card_name = mongoengine.StringField(required=True)
    card_in_jar = mongoengine.StringField(required=True)
    card_steps = mongoengine.EmbeddedDocumentListField(CardSteps)


    meta = {
        'db_alias': 'core',
        'collection': 'Card'
    }


# card = Card()
# card.card_name = 'baby bear'.title()
#
# card_steps = CardSteps()
# card_steps.step_name = 'email 20 galleries'
# card_steps.step_no = 1
#
# card.save()

# updated = Card.objects(card_name='Baby Bear').update_one(push__card_steps=card_steps)

if __name__ == '__main__':
    print('ok')

