TEXTOS = {
    "hero_titulo_1": {"es": "EL BARRIL", "fr": "EL BARRIL", "en": "EL BARRIL"},
    "hero_titulo_2": {"es": "STEAK HOUSE", "fr": "STEAK HOUSE", "en": "STEAK HOUSE"},
    "btn_ver_menu": {"es": "Ver menú", "fr": "Voir le menu", "en": "View menu"},
    "btn_donde_hoy": {"es": "Dónde estamos hoy", "fr": "Où sommes-nous aujourd'hui", "en": "Where we are today"},

    "card_menu_titulo": {"es": "Menú", "fr": "Menu", "en": "Menu"},
    "card_menu_desc": {"es": "Cortes premium a la leña", "fr": "Coupes premium au feu de bois", "en": "Premium wood-fired cuts"},
    "card_donde_titulo": {"es": "Dónde estamos", "fr": "Où nous trouver", "en": "Where we are"},
    "card_donde_default": {"es": "Consulta nuestras redes para la ubicación de hoy", "fr": "Consultez nos réseaux pour l'emplacement d'aujourd'hui", "en": "Check our socials for today's location"},
    "card_promo_titulo": {"es": "Promociones", "fr": "Promotions", "en": "Promotions"},
    "card_promo_default": {"es": "Sin promociones activas por ahora", "fr": "Aucune promotion active pour le moment", "en": "No active promotions right now"},

    "historia_label": {"es": "Nuestra Historia", "fr": "Notre Histoire", "en": "Our Story"},
    "historia_titulo": {"es": "De dónde venimos", "fr": "D'où nous venons", "en": "Where we come from"},
    "historia_texto": {
        "es": "Nuestra pasión nació entre el humo de las brasas y la tradición familiar de domar el fuego. No solo cocinamos carne; honramos el ritual del barril, donde el calor indirecto y la leña seleccionada crean una textura y sabor inigualables.",
        "fr": "Notre passion est née dans la fumée des braises et la tradition familiale de dompter le feu. Nous ne faisons pas que cuisiner de la viande; nous honorons le rituel du barril, où la chaleur indirecte et le bois sélectionné créent une texture et une saveur inégalées.",
        "en": "Our passion was born in the smoke of embers and the family tradition of taming fire. We don't just cook meat; we honor the ritual of the barril, where indirect heat and selected wood create unmatched texture and flavor."
    },

    "catering_titulo": {"es": "Llevamos el Barril a tu evento", "fr": "Nous apportons le Barril à votre événement", "en": "We bring the Barril to your event"},
    "catering_texto": {
        "es": "Desde reuniones familiares hasta eventos corporativos. Disfruta del sabor premium de la leña en cualquier lugar.",
        "fr": "Des réunions de famille aux événements corporatifs. Profitez de la saveur premium du feu de bois partout.",
        "en": "From family gatherings to corporate events. Enjoy premium wood-fire flavor anywhere."
    },
    "btn_contactar": {"es": "Contactar", "fr": "Contactez-nous", "en": "Contact us"},

    "contacto_titulo": {"es": "Contáctanos", "fr": "Contactez-nous", "en": "Contact us"},
    "contacto_subtitulo": {"es": "Parrilla caliente y sazón latino esperándote", "fr": "Grill chaud et saveurs latines vous attendent", "en": "Hot grill and Latin flavor waiting for you"},
    "btn_whatsapp": {"es": "Escríbenos por WhatsApp", "fr": "Écrivez-nous sur WhatsApp", "en": "Message us on WhatsApp"},
    "llamanos": {"es": "Llámanos directo", "fr": "Appelez-nous directement", "en": "Call us directly"},
    "sms": {"es": "Escríbenos un mensaje de texto", "fr": "Envoyez-nous un SMS", "en": "Send us a text message"},

    "catering_form_titulo": {"es": "Catering para tus eventos", "fr": "Traiteur pour vos événements", "en": "Catering for your events"},
    "catering_form_texto": {
        "es": "Llevamos el sabor del barril directo a tu fiesta. Cuéntanos qué tienes en mente y nosotros ponemos la leña.",
        "fr": "Nous apportons la saveur du barril directement à votre fête. Dites-nous ce que vous avez en tête.",
        "en": "We bring the flavor of the barril straight to your party. Tell us what you have in mind."
    },
    "form_nombre": {"es": "Nombre completo", "fr": "Nom complet", "en": "Full name"},
    "form_telefono": {"es": "Teléfono", "fr": "Téléphone", "en": "Phone"},
    "form_fecha": {"es": "Fecha", "fr": "Date", "en": "Date"},
    "form_personas": {"es": "Personas", "fr": "Personnes", "en": "People"},
    "form_tipo_evento": {"es": "Tipo de evento", "fr": "Type d'événement", "en": "Event type"},
    "form_mensaje": {"es": "Cuéntanos más detalles...", "fr": "Donnez-nous plus de détails...", "en": "Tell us more details..."},
    "form_enviar": {"es": "Enviar solicitud", "fr": "Envoyer la demande", "en": "Send request"},

    "cuartel_titulo": {"es": "Nuestro cuartel general", "fr": "Notre quartier général", "en": "Our headquarters"},
    "cuartel_texto": {
        "es": "Somos un Food Truck, así que nuestro corazón está en el camino, pero esta es la base donde ocurre la magia.",
        "fr": "Nous sommes un Food Truck, donc notre cœur est sur la route, mais voici la base où la magie opère.",
        "en": "We're a Food Truck, so our heart is on the road, but this is the base where the magic happens."
    },
    "cuartel_cita": {
        "es": "\"A veces estamos en festivales, a veces en el puerto. Síguenos en Instagram para saber dónde encenderemos el fuego hoy.\"",
        "fr": "\"Parfois nous sommes dans des festivals, parfois au port. Suivez-nous sur Instagram pour savoir où nous allumerons le feu aujourd'hui.\"",
        "en": "\"Sometimes we're at festivals, sometimes at the port. Follow us on Instagram to know where we'll light the fire today.\""
    },
}


def traducir(clave, idioma="es"):
    entrada = TEXTOS.get(clave, {})
    return entrada.get(idioma) or entrada.get("es") or clave