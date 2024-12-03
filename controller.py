import time
import sqlite3 as sql
# def createDB():# Crear o conectar a la BD 'autoconocimiento.db'
#     conn = sql.connect("autoconocimientoFelipeCruz.db")
#     print("Base de datos creada o conectada correctamente.")
#     conn.close()

# def createTable(): 
#     conn = sql.connect("autoconocimientoFelipeCruz.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#                    CREATE TABLE IF NOT EXISTS users (
#                     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     full_name TEXT NOT NULL,
#                     email TEXT UNIQUE NOT NULL,
#                     password_hash TEXT NOT NULL,
#                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#                     ); """)
#     print("tabla creada exitosamente")    

# def insertRow(user_id,full_name, email, password_hash, created_at):
#     try:
#         conn = sql.connect("autoconocimientoFelipeCruz.db")
#         cursor = conn.cursor()
#         instruction = f"INSERT INTO users VALUES ('{user_id}','{full_name}','{email}','{password_hash}','{created_at}')"
#         cursor.execute(instruction)
#         conn.commit()
#         print("fila de 'users' insertada correctamente.")
#     except sql.OperationalError as e:
#         time.sleep(1) #espera de 1 segundo antes de reintentar
#         insertRow(user_id,full_name,email,password_hash,created_at)
#     finally:
#         conn.close()

def readRows():
    conn = sql.connect("autoconocimientoFelipeCruz.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM users"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

if __name__ == "__main__":
    #createDB()     # Primero creamos la base de datos
    #createTable()
    #insertRow(70000,"Luisa Holguin","Luisa@gmail.com","1234Luisa",3/12/2024)
    readRows()