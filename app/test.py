from app.card import Card

template_card = Card.objects(card_name='...').get()


def jars_test(position, jar):
    if Card.objects(card_in_jar=jar,
                    card_active=position):

        found_active = Card.objects(card_in_jar=jar,
                                    card_active=position).get()
        return found_active
    else:
        return template_card


tl = jars_test('top_left', 'arte')


result = tl.card_steps[0].step_staus(set__step_status=0)

tl.card_steps[0].step_status = 1
tl.save()