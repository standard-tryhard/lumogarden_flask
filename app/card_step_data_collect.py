from itertools import islice


def min_of(step_name, limit):
    # return step_name[:limit] if limit < len(step_name) else step_name

    if limit < len(step_name):
        return f"{step_name[:limit]}..."
    else:
        return step_name

def get_incmplts_tuple(card, stop_sign=3):
    incmplts_all = ((c.step_no, min_of(c.step_name, 45))
                    for c in card.card_steps if c.step_status == 0)

    incmplts_to_stop_sign = list(islice(incmplts_all, stop_sign))
    add_placeholders = stop_sign - len(incmplts_to_stop_sign)
    if add_placeholders > 0:
        for i in range(add_placeholders):
            incmplts_to_stop_sign.append((-1, '...'))

    return incmplts_to_stop_sign


def get_incmplts_tuple_and_cardname(card, stop_sign=1):
    incmplts_all = ((card.card_name, min_of(c.step_name, 40))
                    for c in card.card_steps if c.step_status == 0)

    incmplts_to_stop_sign = list(islice(incmplts_all, stop_sign))
    add_placeholders = stop_sign - len(incmplts_to_stop_sign)
    if add_placeholders > 0:
        for i in range(add_placeholders):
            incmplts_to_stop_sign.append((-1, '...'))

    return incmplts_to_stop_sign
