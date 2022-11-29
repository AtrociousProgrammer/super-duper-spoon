import os

import config

from flask import Flask

flask_app = Flask(__name__, instance_relative_config=True)

# Developement Config options
# When deploying to prod, change this to config.ProductionConfig
flask_app.config.from_object(config.Config)

# instance config for development only
flask_app.config.from_pyfile('config.py', silent=True)

# create instance/ dir which contains files not to be commited
# like sqlite db
if not os.path.exists(flask_app.instance_path):

    os.makedirs(flask_app.instance_path)

# declared down here to avoid circular imports
# app/routes.py includes `from app import flask_app`
from app import routes
