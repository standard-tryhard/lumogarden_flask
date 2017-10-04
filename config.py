import mongoengine


WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'  # make it really hard when it's deployed


def global_init():
    mongoengine.register_connection(alias='core', name='lumogrids_flask_test')
