from app import create_app, db
from app.models import Categoria, Plato

app = create_app()


def get_or_create_categoria(tipo, nombre_es, nombre_fr, orden):
    categoria = Categoria.query.filter_by(tipo=tipo, nombre_es=nombre_es).first()
    if categoria:
        return categoria
    categoria = Categoria(tipo=tipo, nombre_es=nombre_es, nombre_fr=nombre_fr, orden=orden)
    db.session.add(categoria)
    db.session.commit()
    return categoria


def get_or_create_plato(categoria_id, nombre_es, nombre_fr, precio):
    plato = Plato.query.filter_by(categoria_id=categoria_id, nombre_es=nombre_es).first()
    if plato:
        plato.nombre_fr = nombre_fr
        plato.precio = precio
        db.session.commit()
        return plato
    plato = Plato(
        categoria_id=categoria_id,
        nombre_es=nombre_es,
        nombre_fr=nombre_fr,
        precio=precio,
        disponible=True
    )
    db.session.add(plato)
    db.session.commit()
    return plato


with app.app_context():
    # ---------- CATEGORÍAS FOOD TRUCK ----------
    cat_platos_ft = get_or_create_categoria("foodtruck", "Platos", "Plats", 1)
    cat_extras_ft = get_or_create_categoria("foodtruck", "Extras", "Extras", 2)
    cat_entradas_ft = get_or_create_categoria("foodtruck", "Entradas", "Entrées", 3)
    cat_postres_ft = get_or_create_categoria("foodtruck", "Postres", "Desserts", 4)

    # ---------- PLATOS: Extras ----------
    get_or_create_plato(cat_extras_ft.id, "Costillas St-Louis (extra)", "Côtes Ste Louis", 7.50)
    get_or_create_plato(cat_extras_ft.id, "Cerdo Bally (extra)", "Porc Bally", 7.50)
    get_or_create_plato(cat_extras_ft.id, "Queso (extra)", "Fromage", 6.50)

    print("Platos de 'Extras' listos.")

    # ---------- PLATOS: Entradas ----------
    get_or_create_plato(cat_entradas_ft.id, "Empanadas", "Empanadas", 4.00)

    print("Platos de 'Entradas' listos.")

    # ---------- PLATOS: Postres ----------
    get_or_create_plato(cat_postres_ft.id, "Churros de caramelo o chocolate", "Churros Caramel ou Chocolat", 10.00)

    print("Platos de 'Postres' listos.")

    print("Categorías del Food Truck listas.")

    # ---------- PLATOS: Platos ----------
    get_or_create_plato(cat_platos_ft.id, "Papas con cerdo desmechado", "Frites au porc effiloché", 16.50)
    get_or_create_plato(cat_platos_ft.id, "Nachos con cerdo desmechado", "Nachos au porc effiloché", 16.50)
    get_or_create_plato(cat_platos_ft.id, "Papas con costillas St-Louis", "Frites au côtes St-Louis", 18.50)
    get_or_create_plato(cat_platos_ft.id, "Papas con cerdo Bally", "Frites au porc Bally", 14.50)
    get_or_create_plato(cat_platos_ft.id, "Poutine clásica", "Poutine Classique", 12.50)
    get_or_create_plato(cat_platos_ft.id, "Poutine con cerdo desmechado", "Poutine au porc effiloché", 18.50)

    print("Platos de 'Platos' (Food Truck) listos.")