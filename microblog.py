from app import app, db
from app.models import User, Post
from logging import FileHandler, WARNING
import os, logging
from logging.handlers import RotatingFileHandler

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


#file_handler =  FileHandler('err.log')
#file_handler.setLevel(WARNING)
#file_handler.setFormatter(logging.Formatter(
#        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

#app.logger.addHandler(file_handler)







if not app.debug:
    # ...

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')
