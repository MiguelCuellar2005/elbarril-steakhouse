from flask import Blueprint, render_template, request, session, redirect, url_for, current_app
from app.models import Plato, Categoria, Promocion, Evento, SolicitudCatering
from app import db
from datetime import date
from functools import wraps

admin_bp = Blueprint("admin", __name__)


def admin_requerido(vista):
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


@admin_bp.route("/logout")
def logout():
    session.pop("admin_autenticado", None)
    return redirect(url_for("admin.login"))


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


# ---------- GESTIÓN DE PLATOS ----------

@admin_bp.route("/platos")
@admin_requerido
def platos():
    categorias = Categoria.query.order_by(Categoria.orden).all()
    return render_template("admin/platos.html", categorias=categorias)


@admin_bp.route("/platos/nuevo", methods=["GET", "POST"])
@admin_requerido
def plato_nuevo():
    categorias = Categoria.query.order_by(Categoria.orden).all()

    if request.method == "POST":
        plato = Plato(
            categoria_id=request.form.get("categoria_id"),
            nombre_es=request.form.get("nombre_es"),
            nombre_en=request.form.get("nombre_en"),
            nombre_fr=request.form.get("nombre_fr"),
            descripcion_es=request.form.get("descripcion_es"),
            descripcion_en=request.form.get("descripcion_en"),
            descripcion_fr=request.form.get("descripcion_fr"),
            precio=request.form.get("precio"),
            disponible=bool(request.form.get("disponible"))
        )
        db.session.add(plato)
        db.session.commit()
        return redirect(url_for("admin.platos"))

    return render_template("admin/plato_form.html", categorias=categorias, plato=None)


@admin_bp.route("/platos/<int:plato_id>/editar", methods=["GET", "POST"])
@admin_requerido
def plato_editar(plato_id):
    plato = Plato.query.get_or_404(plato_id)
    categorias = Categoria.query.order_by(Categoria.orden).all()

    if request.method == "POST":
        plato.categoria_id = request.form.get("categoria_id")
        plato.nombre_es = request.form.get("nombre_es")
        plato.nombre_en = request.form.get("nombre_en")
        plato.nombre_fr = request.form.get("nombre_fr")
        plato.descripcion_es = request.form.get("descripcion_es")
        plato.descripcion_en = request.form.get("descripcion_en")
        plato.descripcion_fr = request.form.get("descripcion_fr")
        plato.precio = request.form.get("precio")
        plato.disponible = bool(request.form.get("disponible"))
        db.session.commit()
        return redirect(url_for("admin.platos"))

    return render_template("admin/plato_form.html", categorias=categorias, plato=plato)


@admin_bp.route("/platos/<int:plato_id>/eliminar", methods=["POST"])
@admin_requerido
def plato_eliminar(plato_id):
    plato = Plato.query.get_or_404(plato_id)
    db.session.delete(plato)
    db.session.commit()
    return redirect(url_for("admin.platos"))


@admin_bp.route("/platos/<int:plato_id>/toggle", methods=["POST"])
@admin_requerido
def plato_toggle(plato_id):
    plato = Plato.query.get_or_404(plato_id)
    plato.disponible = not plato.disponible
    db.session.commit()
    return redirect(url_for("admin.platos"))
# ---------- GESTIÓN DE PROMOCIONES ----------

@admin_bp.route("/promociones")
@admin_requerido
def promociones():
    lista = Promocion.query.order_by(Promocion.fecha_inicio.desc()).all()
    return render_template("admin/promociones.html", promociones=lista)


@admin_bp.route("/promociones/nueva", methods=["GET", "POST"])
@admin_requerido
def promocion_nueva():
    if request.method == "POST":
        promo = Promocion(
            titulo_es=request.form.get("titulo_es"),
            titulo_en=request.form.get("titulo_en"),
            titulo_fr=request.form.get("titulo_fr"),
            descripcion_es=request.form.get("descripcion_es"),
            descripcion_en=request.form.get("descripcion_en"),
            descripcion_fr=request.form.get("descripcion_fr"),
            fecha_inicio=request.form.get("fecha_inicio"),
            fecha_fin=request.form.get("fecha_fin")
        )
        db.session.add(promo)
        db.session.commit()
        return redirect(url_for("admin.promociones"))

    return render_template("admin/promocion_form.html", promocion=None)


@admin_bp.route("/promociones/<int:promo_id>/editar", methods=["GET", "POST"])
@admin_requerido
def promocion_editar(promo_id):
    promo = Promocion.query.get_or_404(promo_id)

    if request.method == "POST":
        promo.titulo_es = request.form.get("titulo_es")
        promo.titulo_en = request.form.get("titulo_en")
        promo.titulo_fr = request.form.get("titulo_fr")
        promo.descripcion_es = request.form.get("descripcion_es")
        promo.descripcion_en = request.form.get("descripcion_en")
        promo.descripcion_fr = request.form.get("descripcion_fr")
        promo.fecha_inicio = request.form.get("fecha_inicio")
        promo.fecha_fin = request.form.get("fecha_fin")
        db.session.commit()
        return redirect(url_for("admin.promociones"))

    return render_template("admin/promocion_form.html", promocion=promo)


@admin_bp.route("/promociones/<int:promo_id>/eliminar", methods=["POST"])
@admin_requerido
def promocion_eliminar(promo_id):
    promo = Promocion.query.get_or_404(promo_id)
    db.session.delete(promo)
    db.session.commit()
    return redirect(url_for("admin.promociones"))

