from flask import Flask
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps
from config import config, keys
from .util import ListConverter

bootstrap = Bootstrap()
googlemaps = GoogleMaps(key=keys['GOOGLE_MAPS_JS_KEY'])

def create_app(config_name):
    app = Flask(__name__)

    app.url_map.converters['list'] = ListConverter

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    googlemaps.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
