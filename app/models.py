from app import db
from datetime import datetime


class Categoria(db.Model):
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)
    nombre_fr = db.Column(db.String(100), nullable=False)
    nombre_en = db.Column(db.String(100))
    nombre_es = db.Column(db.String(100))
    orden = db.Column(db.Integer, default=0)

    platos = db.relationship("Plato", backref="categoria", lazy=True)


class Plato(db.Model):
    __tablename__ = "platos"

    id = db.Column(db.Integer, primary_key=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"), nullable=False)

    nombre_fr = db.Column(db.String(150), nullable=False)
    nombre_en = db.Column(db.String(150))
    nombre_es = db.Column(db.String(150))

    descripcion_fr = db.Column(db.Text)
    descripcion_en = db.Column(db.Text)
    descripcion_es = db.Column(db.Text)

    precio = db.Column(db.Numeric(6, 2), nullable=False)
    imagen = db.Column(db.String(255))
    disponible = db.Column(db.Boolean, default=True)


class Promocion(db.Model):
    __tablename__ = "promociones"

    id = db.Column(db.Integer, primary_key=True)
    titulo_fr = db.Column(db.String(150), nullable=False)
    titulo_en = db.Column(db.String(150))
    titulo_es = db.Column(db.String(150))

    descripcion_fr = db.Column(db.Text)
    descripcion_en = db.Column(db.Text)
    descripcion_es = db.Column(db.Text)

    imagen = db.Column(db.String(255))
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)

    def esta_activa(self):
        hoy = datetime.utcnow().date()
        return self.fecha_inicio <= hoy <= self.fecha_fin


class Evento(db.Model):
    __tablename__ = "eventos"

    id = db.Column(db.Integer, primary_key=True)
    nombre_evento = db.Column(db.String(150), nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time)
    hora_fin = db.Column(db.Time)
    notas = db.Column(db.Text)