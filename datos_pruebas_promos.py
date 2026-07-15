from app import create_app, db
from app.models import Promocion, Evento
from datetime import date, timedelta

app = create_app()

with app.app_context():
    promo = Promocion(
        titulo_fr="Rabais spécial",
        titulo_en="Special discount",
        titulo_es="Descuento especial",
        descripcion_fr="10% de rabais cette semaine",
        descripcion_en="10% off this week",
        descripcion_es="10% de descuento esta semana",
        fecha_inicio=date.today(),
        fecha_fin=date.today() + timedelta(days=7)
    )
    db.session.add(promo)

    evento = Evento(
        nombre_evento="Feria de comida de Quebec",
        ubicacion="Place George-V, Quebec",
        fecha=date.today() + timedelta(days=3)
    )
    db.session.add(evento)

    db.session.commit()
    print(f"Promo creada: {promo.titulo_es}")
    print(f"Evento creado: {evento.nombre_evento}")