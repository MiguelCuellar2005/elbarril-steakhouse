from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    Config.validate()  # falla rápido si falta alguna variable en .env

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Blueprints: rutas públicas y de administración separadas
    from app.routes.public import public_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")

    @app.context_processor
    def inject_idioma():
        from flask import session
        return {"idioma": session.get("idioma", "es")}

    return app