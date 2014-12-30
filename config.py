WTF_CSRF_ENABLED = True
SECRET_KEY = 'beep62656570'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/acounts/o8/id'}
]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
