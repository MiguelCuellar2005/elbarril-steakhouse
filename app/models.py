from app import db
from datetime import datetime


class Categoria(db.Model):
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False, default="foodtruck")  # "foodtruck" o "resto"
    nombre_fr = db.Column(db.String(100), nullable=False)
    nombre_en = db.Column(db.String(100))
    nombre_es = db.Column(db.String(100))
    orden = db.Column(db.Integer, default=0)

    platos = db.relationship("Plato", backref="categoria", lazy=True)
    def nombre(self, idioma="es"):
        campo = getattr(self, f"nombre_{idioma}", None)
        return campo or self.nombre_es


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

    def nombre(self, idioma="es"):
        campo = getattr(self, f"nombre_{idioma}", None)
        return campo or self.nombre_es

    def descripcion(self, idioma="es"):
        campo = getattr(self, f"descripcion_{idioma}", None)
        return campo or self.descripcion_es


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
    
    def titulo(self, idioma="es"):
        campo = getattr(self, f"titulo_{idioma}", None)
        return campo or self.titulo_es

    def descripcion(self, idioma="es"):
        campo = getattr(self, f"descripcion_{idioma}", None)
        return campo or self.descripcion_es


class Evento(db.Model):
    __tablename__ = "eventos"

    id = db.Column(db.Integer, primary_key=True)
    nombre_evento = db.Column(db.String(150), nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time)
    hora_fin = db.Column(db.Time)
    notas = db.Column(db.Text)

class SolicitudCatering(db.Model):
    __tablename__ = "solicitudes_catering"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)
    fecha_evento = db.Column(db.Date)
    num_personas = db.Column(db.Integer)
    tipo_evento = db.Column(db.String(100))
    mensaje = db.Column(db.Text)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    atendida = db.Column(db.Boolean, default=False)

class Historia(db.Model):
    __tablename__ = "historia"

    id = db.Column(db.Integer, primary_key=True)
    texto_es = db.Column(db.Text)
    texto_en = db.Column(db.Text)
    texto_fr = db.Column(db.Text)

    def texto(self, idioma="es"):
        campo = getattr(self, f"texto_{idioma}", None)
        return campo or self.texto_es


class FotoGaleria(db.Model):
    __tablename__ = "fotos_galeria"

    id = db.Column(db.Integer, primary_key=True)
    seccion = db.Column(db.String(20), nullable=False, default="galeria")  # "galeria" o "historia"
    imagen = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255))
    orden = db.Column(db.Integer, default=0)