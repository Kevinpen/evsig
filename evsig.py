#import os
#from flask import g
from app import create_app

#g.datasets, g.datasets_name, g.examples = load_data()


app = create_app()


if __name__ == '__main__':
    app.run()