from flask import Blueprint, render_template, request, session, redirect, url_for, current_app
from app.models import Plato, Promocion, Evento, SolicitudCatering
from datetime import date

admin_bp = Blueprint("admin", __name__)


def admin_requerido(vista):
    from functools import wraps

    @wraps(vista)
    def envoltura(*args, **kwargs):
        if not session.get("admin_autenticado"):
            return redirect(url_for("admin.login"))
        return vista(*args, **kwargs)

    return envoltura


@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")

        if (
            usuario == current_app.config["ADMIN_USERNAME"]
            and contrasena == current_app.config["ADMIN_PASSWORD"]
        ):
            session["admin_autenticado"] = True
            return redirect(url_for("admin.dashboard"))

        return render_template("admin/login.html", error="Usuario o contraseña incorrectos")

    return render_template("admin/login.html")


@admin_bp.route("/dashboard")
@admin_requerido
def dashboard():
    hoy = date.today()

    total_platos = Plato.query.count()
    promos_activas = Promocion.query.filter(
        Promocion.fecha_inicio <= hoy,
        Promocion.fecha_fin >= hoy
    ).count()
    proximos_eventos = Evento.query.filter(Evento.fecha >= hoy).count()
    catering_pendiente = SolicitudCatering.query.filter_by(atendida=False).count()

    return render_template(
        "admin/dashboard.html",
        total_platos=total_platos,
        promos_activas=promos_activas,
        proximos_eventos=proximos_eventos,
        catering_pendiente=catering_pendiente
    )


@admin_bp.route("/logout")
def logout():
    session.pop("admin_autenticado", None)
    return redirect(url_for("admin.login"))