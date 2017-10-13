import mongoengine
from app.card_steps import CardSteps
from config import global_init
from itertools import islice

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



if __name__ == '__main__':
    # data = Card.objects().update(set__card_active='inactive')


    card = Card.objects().get(card_name='People In The Tree')

    all_incompletes = (c.step_name for c in card.card_steps if c.step_status == 0)
    three_incompletes = list(islice(all_incompletes, 3))

    print(three_incompletes)



