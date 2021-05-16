from flask import Flask
from .main import main,choose,result

#from config import config

def create_app(config_name):
 app = Flask(__name__)
 app.register_blueprint(result)
 app.register_blueprint(choose)
 app.register_blueprint(main)


 return app