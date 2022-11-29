import os

from flask import Flask

flask_app = Flask(__name__, instance_relative_config=True)

flask_app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(flask_app.instance_path, 'super_duper_spoon.sqlite')
        )

# create instance/ dir which contains files not to be commited
# like sqlite db
if not os.path.exists(flask_app.instance_path):

    os.makedirs(flask_app.instance_path)

# declared down here to avoid circular imports
# app/routes.py includes `from app import flask_app`
from app import routes
