from flask import (abort, make_response, request,
                   jsonify)

from flask_restful import (Api, Resource, reqparse,
                           fields, marshal)

'''
card_name = mongoengine.StringField(required=True)
card_in_jar = mongoengine.StringField(required=True)
card_active = mongoengine.StringField(default='inactive')
card_steps = mongoengine.EmbeddedDocumentListField(CardSteps)'''

# card_fields = {
# 	'card_name':fields.String,
# 	'card_in_jar': fields.String,
# 	'card_active': fields.Boolean,
# 	'card_steps': fields.
# 	'uri': fields.Url('task')
# }

@lumo_hub.route('/api/lumogarden/card/<string:card_name>',
                methods=['GET', 'POST'])

def return_single_card(card_name):

    return render_template(card.html)
