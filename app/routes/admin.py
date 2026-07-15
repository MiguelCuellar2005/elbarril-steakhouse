from flask import Blueprint, render_template, request, session, redirect, url_for, current_app
from app.models import Plato, Categoria, Promocion, Evento, SolicitudCatering, Historia, FotoGaleria
from app import db
from datetime import date
from functools import wraps
import os
import uuid
from werkzeug.utils import secure_filename

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


EXTENSIONES_PERMITIDAS = {"png", "jpg", "jpeg", "webp"}


def extension_permitida(nombre_archivo):
    return "." in nombre_archivo and nombre_archivo.rsplit(".", 1)[1].lower() in EXTENSIONES_PERMITIDAS


def guardar_imagen(archivo):
    if archivo and archivo.filename and extension_permitida(archivo.filename):
        extension = archivo.filename.rsplit(".", 1)[1].lower()
        nombre_unico = f"{uuid.uuid4().hex}.{extension}"
        ruta_completa = os.path.join(current_app.config["UPLOAD_FOLDER"], nombre_unico)
        archivo.save(ruta_completa)
        return nombre_unico
    return None


@admin_bp.route("/platos/nuevo", methods=["GET", "POST"])
@admin_requerido
def plato_nuevo():
    categorias = Categoria.query.order_by(Categoria.orden).all()

    if request.method == "POST":
        nombre_imagen = guardar_imagen(request.files.get("imagen"))

        plato = Plato(
            categoria_id=request.form.get("categoria_id"),
            nombre_es=request.form.get("nombre_es"),
            nombre_en=request.form.get("nombre_en"),
            nombre_fr=request.form.get("nombre_fr"),
            descripcion_es=request.form.get("descripcion_es"),
            descripcion_en=request.form.get("descripcion_en"),
            descripcion_fr=request.form.get("descripcion_fr"),
            precio=request.form.get("precio"),
            imagen=nombre_imagen,
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
        nombre_imagen = guardar_imagen(request.files.get("imagen"))
        if nombre_imagen:
            plato.imagen = nombre_imagen

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
# ---------- GESTIÓN DE EVENTOS ----------

@admin_bp.route("/eventos")
@admin_requerido
def eventos():
    lista = Evento.query.order_by(Evento.fecha).all()
    return render_template("admin/eventos.html", eventos=lista)


@admin_bp.route("/eventos/nuevo", methods=["GET", "POST"])
@admin_requerido
def evento_nuevo():
    if request.method == "POST":
        evento = Evento(
            nombre_evento=request.form.get("nombre_evento"),
            ubicacion=request.form.get("ubicacion"),
            fecha=request.form.get("fecha"),
            hora_inicio=request.form.get("hora_inicio") or None,
            hora_fin=request.form.get("hora_fin") or None,
            notas=request.form.get("notas")
        )
        db.session.add(evento)
        db.session.commit()
        return redirect(url_for("admin.eventos"))

    return render_template("admin/evento_form.html", evento=None)


@admin_bp.route("/eventos/<int:evento_id>/editar", methods=["GET", "POST"])
@admin_requerido
def evento_editar(evento_id):
    evento = Evento.query.get_or_404(evento_id)

    if request.method == "POST":
        evento.nombre_evento = request.form.get("nombre_evento")
        evento.ubicacion = request.form.get("ubicacion")
        evento.fecha = request.form.get("fecha")
        evento.hora_inicio = request.form.get("hora_inicio") or None
        evento.hora_fin = request.form.get("hora_fin") or None
        evento.notas = request.form.get("notas")
        db.session.commit()
        return redirect(url_for("admin.eventos"))

    return render_template("admin/evento_form.html", evento=evento)


@admin_bp.route("/eventos/<int:evento_id>/eliminar", methods=["POST"])
@admin_requerido
def evento_eliminar(evento_id):
    evento = Evento.query.get_or_404(evento_id)
    db.session.delete(evento)
    db.session.commit()
    return redirect(url_for("admin.eventos"))
# ---------- SOLICITUDES DE CATERING ----------

@admin_bp.route("/catering")
@admin_requerido
def catering():
    solicitudes = SolicitudCatering.query.order_by(SolicitudCatering.fecha_creacion.desc()).all()
    return render_template("admin/catering.html", solicitudes=solicitudes)


@admin_bp.route("/catering/<int:solicitud_id>/toggle", methods=["POST"])
@admin_requerido
def catering_toggle(solicitud_id):
    solicitud = SolicitudCatering.query.get_or_404(solicitud_id)
    solicitud.atendida = not solicitud.atendida
    db.session.commit()
    return redirect(url_for("admin.catering"))

# ---------- HISTORIA ----------

@admin_bp.route("/historia", methods=["GET", "POST"])
@admin_requerido
def historia():
    hist = Historia.query.first()
    if not hist:
        hist = Historia(texto_es="", texto_en="", texto_fr="")
        db.session.add(hist)
        db.session.commit()

    if request.method == "POST":
        hist.texto_es = request.form.get("texto_es")
        hist.texto_en = request.form.get("texto_en")
        hist.texto_fr = request.form.get("texto_fr")
        db.session.commit()
        return redirect(url_for("admin.historia"))

    fotos = FotoGaleria.query.filter_by(seccion="historia").order_by(FotoGaleria.orden).all()
    return render_template("admin/historia.html", historia=hist, fotos=fotos)


@admin_bp.route("/historia/foto/subir", methods=["POST"])
@admin_requerido
def historia_foto_subir():
    nombre_imagen = guardar_imagen(request.files.get("imagen"))
    if nombre_imagen:
        foto = FotoGaleria(
            seccion="historia",
            imagen=nombre_imagen,
            descripcion=request.form.get("descripcion")
        )
        db.session.add(foto)
        db.session.commit()
    return redirect(url_for("admin.historia"))


@admin_bp.route("/historia/foto/<int:foto_id>/eliminar", methods=["POST"])
@admin_requerido
def historia_foto_eliminar(foto_id):
    foto = FotoGaleria.query.get_or_404(foto_id)
    db.session.delete(foto)
    db.session.commit()
    return redirect(url_for("admin.historia"))


# ---------- GALERÍA GENERAL ----------

@admin_bp.route("/galeria")
@admin_requerido
def galeria():
    fotos = FotoGaleria.query.filter_by(seccion="galeria").order_by(FotoGaleria.orden).all()
    return render_template("admin/galeria.html", fotos=fotos)


@admin_bp.route("/galeria/subir", methods=["POST"])
@admin_requerido
def galeria_foto_subir():
    nombre_imagen = guardar_imagen(request.files.get("imagen"))
    if nombre_imagen:
        foto = FotoGaleria(
            seccion="galeria",
            imagen=nombre_imagen,
            descripcion=request.form.get("descripcion")
        )
        db.session.add(foto)
        db.session.commit()
    return redirect(url_for("admin.galeria"))


@admin_bp.route("/galeria/<int:foto_id>/eliminar", methods=["POST"])
@admin_requerido
def galeria_foto_eliminar(foto_id):
    foto = FotoGaleria.query.get_or_404(foto_id)
    db.session.delete(foto)
    db.session.commit()
    return redirect(url_for("admin.galeria"))
