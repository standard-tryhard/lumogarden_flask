from flask import render_template
from app import lumo_hub
from app.block import Block
from app.forms import NewCardForm



@lumo_hub.route('/')
@lumo_hub.route('/blocks/')
def blocks():

    tl = Block.objects.get(position='top_left')
    tm = Block.objects.get(position='top_mid')
    tr = Block.objects.get(position='top_right')
    ml = Block.objects.get(position='mid_left')
    mr = Block.objects.get(position='mid_right')
    bl = Block.objects.get(position='botm_left')
    bm = Block.objects.get(position='botm_mid')
    br = Block.objects.get(position='botm_right')

    return render_template('blocks.html',
                           tl=tl,
                           tm=tm,
                           tr=tr,
                           ml=ml,
                           mr=mr,
                           bl=bl,
                           bm=bm,
                           br=br)


@lumo_hub.route('/jars/<string:jars_category>/')
def jars():


    return render_template('jars.html')


@lumo_hub.route('/new_card/', methods=['GET', 'POST'])
def new_card():
    form = NewCardForm()

    return render_template('new_card.html',
                           form=form)