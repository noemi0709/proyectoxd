from db.db import conn

cur = conn.cursor()

"""
crear_actividad recibe un diccionario con: titulo, descripcion y fecha.
Devuelve una tupla (status, mensaje)
"""

def crear_actividad(data):
    if not data["titulo"]:
        return (False, "Es necesario enviar un título")
    try:
        cur.execute(
            "INSERT INTO activities (titulo, descripcion, fecha) VALUES (%s, %s, %s)",
            (data["titulo"], data["descripcion"], data["fecha"])
        )
        conn.commit()
        return (True, "Actividad guardada con éxito")
    except Exception as e:
        print(e)
        return (False, "Ocurrió un error al registrar la actividad")


def actualizar_actividad(actividad_id, data):
    if not actividad_id:
        return (False, "Es necesario enviar el ID de la actividad")
    if not data["titulo"] or not data["descripcion"] or not data["fecha"]:
        return (False, "Es necesario enviar todos los parámetros para actualizar")

    cur.execute("SELECT * FROM activities WHERE id = %s", (actividad_id,))
    actividad = cur.fetchone()
    if not actividad:
        return (False, "El ID de la actividad no está registrado en la DB")

    cur.execute(
        "UPDATE activities SET titulo=%s, descripcion=%s, fecha=%s WHERE id = %s",
        (data["titulo"], data["descripcion"], data["fecha"], actividad_id)
    )
    conn.commit()
    return (True, "Actividad actualizada con éxito")


def eliminar_actividad(actividad_id):
    cur.execute("DELETE FROM activities WHERE id = %s", (actividad_id,))
    conn.commit()
    return (True, "Actividad eliminada con éxito")


def obtener_actividades():
    cur.execute("SELECT * FROM activities ORDER BY id")
    actividades = cur.fetchall()
    return actividades
