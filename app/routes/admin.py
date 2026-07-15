from flask import Blueprint, render_template, request, session, redirect, url_for, current_app

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
    # TODO: mostrar resumen de promos activas, próximos eventos, platos
    return render_template("admin/dashboard.html")


@admin_bp.route("/logout")
def logout():
    session.pop("admin_autenticado", None)
    return redirect(url_for("admin.login"))