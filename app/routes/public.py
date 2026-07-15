from flask import Blueprint, render_template, session, request, flash, redirect, url_for
from app.models import Categoria, Promocion, Evento, SolicitudCatering
from app import db
from datetime import date, datetime

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


@public_bp.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        fecha_evento_str = request.form.get("fecha_evento")
        fecha_evento = None
        if fecha_evento_str:
            fecha_evento = datetime.strptime(fecha_evento_str, "%Y-%m-%d").date()

        solicitud = SolicitudCatering(
            nombre=request.form.get("nombre"),
            telefono=request.form.get("telefono"),
            fecha_evento=fecha_evento,
            num_personas=request.form.get("num_personas") or None,
            tipo_evento=request.form.get("tipo_evento"),
            mensaje=request.form.get("mensaje")
        )
        db.session.add(solicitud)
        db.session.commit()

        flash("¡Gracias! Tu solicitud fue enviada, te contactaremos pronto.")
        return redirect(url_for("public.contacto"))

    return render_template("public/contacto.html")


@public_bp.route("/idioma/<lang>")
def cambiar_idioma(lang):
    if lang in ("fr", "en", "es"):
        session["idioma"] = lang
    return "", 204