from flask import Blueprint, render_template, session, request

public_bp = Blueprint("public", __name__)


@public_bp.route("/")
def home():
    # TODO: traer promociones activas y próximos eventos desde la base de datos
    return render_template("public/home.html")


@public_bp.route("/menu")
def menu():
    # TODO: traer categorías y platos ordenados
    return render_template("public/menu.html")


@public_bp.route("/contacto")
def contacto():
    return render_template("public/contacto.html")


@public_bp.route("/idioma/<lang>")
def cambiar_idioma(lang):
    # Guarda el idioma elegido en la sesión del usuario
    if lang in ("fr", "en", "es"):
        session["idioma"] = lang
    return "", 204