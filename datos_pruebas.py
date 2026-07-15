from app import create_app, db
from app.models import Categoria, Plato

app = create_app()

with app.app_context():
    # Crear una categoría de ejemplo
    categoria = Categoria(
        nombre_fr="Plats principaux",
        nombre_en="Main dishes",
        nombre_es="Platos fuertes",
        orden=1
    )
    db.session.add(categoria)
    db.session.commit()  # se guarda para obtener su id

    # Crear un plato de ejemplo, vinculado a esa categoría
    plato = Plato(
        categoria_id=categoria.id,
        nombre_fr="Steak grillé",
        nombre_en="Grilled steak",
        nombre_es="Bistec a la parrilla",
        descripcion_fr="Steak grillé au feu de bois",
        descripcion_en="Wood-fire grilled steak",
        descripcion_es="Bistec asado al fuego de leña",
        precio=15.99,
        disponible=True
    )
    db.session.add(plato)
    db.session.commit()

    print(f"Categoría creada: {categoria.nombre_es} (id={categoria.id})")
    print(f"Plato creado: {plato.nombre_es} - ${plato.precio} (id={plato.id})")