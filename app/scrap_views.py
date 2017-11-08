@lumo_hub.route('/test/<string:jar_from_url>/', methods=['GET', 'POST'])
def test(jar_from_url):

    def get_jar_positions(position):
        if Card.objects(card_in_jar=jar_from_url,
                        card_active=position):

            found_active = Card.objects(card_in_jar=jar_from_url,
                                        card_active=position).get()
            return found_active

        else:
            return template_card

    jar_name = jar_from_url.upper()

    tl = get_jar_positions('top_left')
    tm = get_jar_positions('top_mid')
    tr = get_jar_positions('top_right')
    ml = get_jar_positions('mid_left')
    mr = get_jar_positions('mid_right')
    bl = get_jar_positions('botm_left')
    bm = get_jar_positions('botm_mid')
    br = get_jar_positions('botm_right')

    jar_positions = {
        'tl': tl,
        'tm': tm,
        'tr': tr,
        'ml': ml,
        'mr': mr,
        'bl': bl,
        'bm': bm,
        'br': br
        }

    next_actionable_steps = {
        'tl': get_incmplts_form(tl),
        'tm': get_incmplts_form(tm),
        'tr': get_incmplts_form(tr),
        'ml': get_incmplts_form(ml),
        'mr': get_incmplts_form(mr),
        'bl': get_incmplts_form(bl),
        'bm': get_incmplts_form(bm),
        'br': get_incmplts_form(br)
        }

    form = Buttons()
    if form.validate_on_submit():
            # for form in next_actionable_steps.values():
            #     print(form)
            print('hi')
            return redirect(url_for('testing', jar_from_url=jar_from_url))



    return render_template('testing.html',
                           jar_name=jar_name,
                           jar_positions=jar_positions,
                           next_actionable_steps=next_actionable_steps,
                           form=form)


@lumo_hub.route('/test_checkbox/', methods=['GET', 'POST'])
def test_checkbox():
    form = ExampleForm()
    form.fields.choices = [('a', 'A')]

    # if form.validate_on_submit():
    #         return redirect(url_for('test_checkbox'))

    return render_template('test_checkbox.html',
                           # test_jar=test_jar,
                           # jar_positions=jar_positions,
                           # next_actionable_steps=next_actionable_steps,
                           form=form)


