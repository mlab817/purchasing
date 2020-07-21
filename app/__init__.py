from flask import Flask
from flask_cors import CORS, logging

app = Flask(__name__)
CORS(app)

logging.getLogger('flask_cors').level = logging.DEBUG

app.config['SECRET_KEY'] = 'you-will-never-guess'

from app import routes