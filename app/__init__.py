import os

from flask import Flask


def create_app():
    """
    Creates a Flask application with all the necessary configurations and creates the instance directory
    :return: instance of Flask
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='some very very secret key',
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
