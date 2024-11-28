from conexion1 import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

class Clientes:
    
    def mostrarClientes():
        try:
            cone = Conexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute('''SELECT c.idCliente, c.nombre, c.apellido, c.dni, c.telefono,
                            p.producto, p.cantidad
                            FROM clientes c
                            INNER JOIN productos p
                            ON c.idCliente = p.idVenta;''')
            
            miResultado = cursor.fetchall() #guarda el conjunto de datos
            print(cursor.rowcount, "Registro ingresado")
            cone.close()
            return miResultado
            
        except sqlite3.Error as error:
            print(f"Error al mostrar datos {error}")
    
    
    def ingresarDatos(id, nombre, apellido, dni, telefono, producto, cantidad):
        try:
            cone = Conexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
                     
            cursor.execute("INSERT INTO clientes ( idCliente, nombre, apellido, dni, telefono) VALUES (?, ?, ?, ?, ?)", (id, nombre, apellido, dni, telefono))
            cursor.execute("INSERT INTO ventas (idVenta, idCliente) VALUES (?, ?)", (id, id))
            cursor.execute("INSERT INTO productos (idVenta, producto, cantidad) VALUES (?, ?, ?)", (id, producto, cantidad))
            
            cone.commit()
            print(cursor.rowcount, "Registro ingresado")
            cone.close()
            
        except sqlite3.Error as error:
            print(f"Error al ingresar datos {error}")
    
    
    def modificarDatos(id, nombre, apellido, dni, telefono, producto, cantidad):
        try:
            cone = Conexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
                   
            cursor.execute('BEGIN TRANSACTION;')
                           
            cursor.execute('''UPDATE clientes 
                   SET nombre = ?,
                       apellido = ?,
                       dni = ?,
                       telefono = ?
                   WHERE idCliente = ?;''', (nombre, apellido, dni, telefono, id))

            cursor.execute('''UPDATE ventas
                   SET idVenta = ?
                   WHERE idCliente = ?;''', (id, id))

            cursor.execute('''UPDATE productos
                   SET producto = ?,
                       cantidad = ?
                   WHERE idVenta = ?;''',(producto, cantidad, id))

            cone.commit()
            print(cursor.rowcount, "Registro modificado")
            cone.close()
            
        except sqlite3.Error as error:
            print(f"Error al modificar datos {error}")
            cone.rollback()
            cone.close()
    
    def eliminarDatos(id):
        try:
            cone = Conexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
                   
            cursor.execute('BEGIN TRANSACTION;')
                           
            cursor.execute('DELETE FROM ventas where ventas.idVenta = ?;',(id,))

            cursor.execute('DELETE FROM productos where productos.idVenta = ?;',(id,))

            cursor.execute('DELETE from clientes where clientes.idCliente = ?;', (id,))

            cone.commit()
            print(cursor.rowcount, "Registro eliminado")
            cone.close()
            
        except sqlite3.Error as error:
            print(f"Error al eliminar datos {error}")
            cone.rollback()
            cone.close()

    def mostrarOrdenAlf(order_by):
        try:
            cone = Conexion.ConexionBaseDeDatos()
            cursor = cone.cursor()       
    
            if order_by =="Orden alfabetico":
                cursor.execute('''SELECT c.idCliente, c.nombre, c.apellido, c.dni, c.telefono, p.producto, p.cantidad
                        FROM clientes c
                        JOIN ventas v ON c.idCliente = v.idCliente
                        JOIN productos p ON v.idVenta = p.idVenta
                        ORDER BY c.nombre ASC;''')
            
            elif order_by =="Cantidad":
                 cursor.execute ('''SELECT c.idCliente, c.nombre, c.apellido, c.dni, c.telefono, p.producto, p.cantidad
                            FROM clientes c
                            JOIN ventas v ON c.idCliente = v.idCliente
                            JOIN productos p ON v.idVenta = p.idVenta
                            ORDER BY p.cantidad DESC;''')
                 
            elif order_by =="Orden ID":
                cursor.execute('''SELECT c.idCliente, c.nombre, c.apellido, c.dni, c.telefono,
                            p.producto, p.cantidad
                            FROM clientes c
                            INNER JOIN productos p
                            ON c.idCliente = p.idVenta;''')
            
            rows = cursor.fetchall()
            cone.close()
            return rows
        
        except sqlite3.Error as error:
            print(f"Error al mostrar orden{error}")