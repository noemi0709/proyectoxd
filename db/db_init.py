from db.db import conn

sql_schema = """
CREATE TABLE IF NOT EXISTS 
activities(
    id SERIAL PRIMARY KEY,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    fecha TEXT
);
"""

def iniciar_db():
    try:
       cur= conn.cursor () 
       cur.execute(sql_schema)
       conn.commit()
       print("SQL Schema ejecutado con éxito")
    except Exception as e:
        print("Ocurrió un error al ejecutar el script.")
        print(e)