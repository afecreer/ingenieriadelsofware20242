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

def insertRow(user_id,full_name, email, password_hash, created_at):
    try:
        conn = sql.connect("autoconocimientoFelipeCruz.db")
        cursor = conn.cursor()
        instruction = f"INSERT INTO users VALUES ('{user_id}','{full_name}','{email}','{password_hash}','{created_at}')"
        cursor.execute(instruction)
        conn.commit()
        print("fila de 'users' insertada correctamente.")
    except sql.OperationalError as e:
        time.sleep(1) #espera de 1 segundo antes de reintentar
        insertRow(user_id,full_name,email,password_hash,created_at)
    finally:
        conn.close()

# def readRows():
#     conn = sql.connect("autoconocimientoFelipeCruz.db")
#     cursor = conn.cursor()
#     instruction = f"SELECT * FROM users"
#     cursor.execute(instruction)
#     datos = cursor.fetchall()
#     conn.commit()
#     conn.close()
#     print(datos)

def updateRow(user_id, full_name=None, email=None, password_hash=None):
    """
    Actualiza una fila en la tabla 'users' con base en el user_id.
    Los parámetros no proporcionados no se actualizan.
    """
    try:
        conn = sql.connect("autoconocimientoFelipeCruz.db")
        cursor = conn.cursor()

        # Construir la instrucción SQL dinámicamente según los parámetros proporcionados
        updates = []
        if full_name:
            updates.append(f"full_name = '{full_name}'")
        if email:
            updates.append(f"email = '{email}'")
        if password_hash:
            updates.append(f"password_hash = '{password_hash}'")

        if not updates:
            print("No se proporcionaron campos para actualizar.")
            return

        instruction = f"UPDATE users SET {', '.join(updates)} WHERE user_id = {user_id}"
        cursor.execute(instruction)
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Usuario con ID {user_id} actualizado correctamente.")
        else:
            print(f"No se encontró un usuario con ID {user_id}.")
    except sql.Error as e:
        print(f"Error al actualizar el usuario: {e}")
    finally:
        conn.close()

def deleteRow(user_id):
    """
    Elimina un registro de la tabla 'users' según su ID.
    
    Args:
    user_id (int): ID del usuario que se desea eliminar.
    """
    try:
        conn = sql.connect("autoconocimientoFelipeCruz.db")
        cursor = conn.cursor()
        
        # Instrucción para eliminar el registro
        instruction = f"DELETE FROM users WHERE user_id = {user_id}"
        
        cursor.execute(instruction)
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Usuario con ID {user_id} eliminado correctamente.")
        else:
            print(f"No se encontró ningún usuario con ID {user_id}.")
    
    except sql.OperationalError as e:
        print(f"Error en la operación: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    #createDB()     # Primero creamos la base de datos
    #createTable()
    #insertRow(70000,"Luisa Holguin Perez","Luisap@gmail.com","1234Luisa",3/12/2024)
    #insertRow(80000,"Hernando Falcao","hfalcao@gmail.com","1234Falcao",9/12/2024)

    #readRows()
    #updateRow(user_id=80000, full_name="Hernado Jose Falcao Perea")
    
    # Actualizar el correo y la contraseña del usuario con ID 70000
    #updateRow(user_id=70000, email="luisa_new@gmail.com", password_hash="newpassword1234")

    deleteRow(80000)  # Elimina el usuario con ID 80000

    # Leer filas para verificar los cambios
    #readRows()

