import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 7
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587 or 25
    MAIL_USE_TLS=1 is not None
    MAIL_USERNAME='testpstbx@gmail.com'
    MAIL_PASSWORD='PatrickMahomes'
    ADMINS = ['pstbx9-21@yandex.ru']
