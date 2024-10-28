from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Registrar blueprints
    from .routes.auth import auth_bp
    from .routes.user import user_bp
    from .routes.threat import threat_bp
    from .routes.privacy import privacy_bp
    from .routes.avsd import avsd_bp
    from .routes.satc import satc_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(threat_bp, url_prefix='/api/threat')
    app.register_blueprint(privacy_bp, url_prefix='/api/privacy')
    app.register_blueprint(avsd_bp, url_prefix='/api/avsd')
    app.register_blueprint(satc_bp, url_prefix='/api/satc')

    return app
