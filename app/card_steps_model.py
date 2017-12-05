import mongoengine


class CardSteps(mongoengine.EmbeddedDocument):
    step_no = mongoengine.IntField()  # So how do I autoincrement???
    step_name = mongoengine.StringField(required=True)
    step_status = mongoengine.IntField(default=0)
