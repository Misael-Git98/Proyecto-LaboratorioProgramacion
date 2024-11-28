import sqlite3

class Conexion:
    
    def ConexionBaseDeDatos():
        try:
            conexion = sqlite3.connect('baseDeDatos.db')
            print("Conexion correcta")
            return conexion
        except sqlite3.Error as error:
            print(f"Error en la conexion a Base de Datos: {error}")
            return None
        
Conexion.ConexionBaseDeDatos()