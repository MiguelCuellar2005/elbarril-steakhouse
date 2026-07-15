from flask import Blueprint, render_template, session, request

from app.models import Categoria, Promocion, Evento

from datetime import date

public_bp = Blueprint("public", __name__)


@public_bp.route("/")
def home():
    hoy = date.today()

    promociones_activas = Promocion.query.filter(
        Promocion.fecha_inicio <= hoy,
        Promocion.fecha_fin >= hoy
    ).all()

    proximos_eventos = Evento.query.filter(
        Evento.fecha >= hoy
    ).order_by(Evento.fecha).limit(3).all()

    return render_template(
        "public/home.html",
        promociones=promociones_activas,
        eventos=proximos_eventos
    )



@public_bp.route("/menu")
def menu():
    categorias = Categoria.query.order_by(Categoria.orden).all()
    return render_template("public/menu.html", categorias=categorias)


@public_bp.route("/contacto")
def contacto():
    return render_template("public/contacto.html")


@public_bp.route("/idioma/<lang>")
def cambiar_idioma(lang):
    # Guarda el idioma elegido en la sesión del usuario
    if lang in ("fr", "en", "es"):
        session["idioma"] = lang
    return "", 204