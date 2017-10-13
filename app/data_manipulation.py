def get_incmplts(card, stop_sign=3):
    incmplts_all = (c.step_name for c in card.card_steps if
                       c.step_status == 0)
    incmplts_to_stop_sign = list(islice(incmplts_all, stop_sign))

    return incmplts_to_stop_sign
