from db.db_init import iniciar_db
from views.main import ventana
from views.activities.home import mostrar_crear_actividad
#Iniciamos la DB
iniciar_db()
#Ejecutamos las ventanas. 
mostrar_crear_actividad(ventana)