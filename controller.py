import time
import sqlite3 as sql
# def createDB():# Crear o conectar a la BD 'autoconocimiento.db'
    # conn = sql.connect("autoconocimiento.db")
    # print("Base de datos creada o conectada correctamente.")
    # conn.close()

def createTable(): 
    conn = sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    ); """)
    print("tabla creada exitosamente")    


if __name__ == "__main__":
    #createDB()     # Primero creamos la base de datos
    createTable()