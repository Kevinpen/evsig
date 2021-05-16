from flask import Flask
from .main import main as main_blueprint
from .main import sig as sig_blueprint
#from config import config

def create_app(config_name):
 app = Flask(__name__)
 
 app.register_blueprint(main_blueprint)
 app.register_blueprint(sig_blueprint)
 

 return app