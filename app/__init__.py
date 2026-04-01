from flask import Flask
from .models import db
def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')

    from .routes import main
    app.register_blueprint(main)

    db.init_app(app)
    return app