from app import create_app, db
from app.models import Categoria, Plato, Promocion, Evento  # necesario para que se registren las tablas

app = create_app()

with app.app_context():
    db.create_all()
    print("Tablas creadas correctamente en:", db.engine.url)