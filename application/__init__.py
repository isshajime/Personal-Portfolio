from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_application():
    # Initialize the core application
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize plugin
    db.init_app(app)

    with app.app_context():
        from . import routes, models, api_data
        db.create_all()

        app.register_blueprint(routes.main_bp)

        return app