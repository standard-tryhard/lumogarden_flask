# from app.forms import ExampleForm
from itertools import islice

def get_incmplts(card, stop_sign=3):
    incmplts_all = (c.step_name for c in card.card_steps if
                       c.step_status == 0)
    incmplts_to_stop_sign = list(islice(incmplts_all, stop_sign))
    add_placeholders = stop_sign - len(incmplts_to_stop_sign)

    if add_placeholders > 0:
        for i in range(add_placeholders):
            incmplts_to_stop_sign.append('...')

    return incmplts_to_stop_sign

def get_incmplts_tuple(card, stop_sign=3):
    incmplts_all = ((c.step_no, c.step_name, card.card_name) for c in card.card_steps if
                       c.step_status == 0)
    incmplts_to_stop_sign = list(islice(incmplts_all, stop_sign))
    add_placeholders = stop_sign - len(incmplts_to_stop_sign)
    if add_placeholders > 0:
        for i in range(add_placeholders):
            incmplts_to_stop_sign.append(('...', -1, '...'))

    return incmplts_to_stop_sign

