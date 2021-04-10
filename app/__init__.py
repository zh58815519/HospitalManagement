from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from .config import config
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    from .charges import charges as charges_blueprint
    app.register_blueprint(charges_blueprint, url_prfix="/charges")
    from .inpatient import inpatient as inpatient_blueprint
    app.register_blueprint(inpatient_blueprint, url_prfix="/inpatient")
    
    from .outpatient import outpatient as outpatient_blueprint
    app.register_blueprint(outpatient_blueprint, url_prfix= "/outpatient")

    return app
