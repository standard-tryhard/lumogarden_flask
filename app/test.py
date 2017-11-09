from app.card import Card


def jars_test(position, jar):
    if Card.objects(card_in_jar=jar,
                    card_active=position):

        found_active = Card.objects(card_in_jar=jar,
                                    card_active=position).get()
        return found_active

    else:
        # template card assigned at top
        # of this file for all routes to use
        return template_card

# renamed this to make it more
# readable when using it as part of link

tl = jars_test('top_left', 'arte')


result = tl.card_steps[0].step_staus(set__step_status=0)
# hey = tl.card_steps.get(step_no__0)

tl.card_steps[0].step_status = 1
tl.save()
# print(tl.card_steps[0].step_status)
# print(tl.card_steps[0])