import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from funciones import *
from conexion1 import *

class FormularioClientes:
    
    global base
    base = None
    
    global groupBox
    groupBox = None
    
    global textBoxId
    textBoxId = None
    
    global textBoxNombre
    textBoxNombre = None
    
    global textBoxApellido
    textBoxApellido = None

    global textBoxDni
    textBoxDni = None
    
    global textBoxTelefono
    textBoxTelefono = None
    
    global textBoxProducto
    textBoxProducto = None
    
    global textBoxCantidad
    textBoxCantidad = None
    
    global comboBox
    comboBox = None
        
    global tree
    tree = None
    

def validar_nombre(nombre):
    if len(nombre) < 3:
        messagebox.showerror("Error", "El nombre debe tener al menos 3 letras.")
        return False
    return True

def validar_apellido(apellido):
    if len(apellido) < 4:
        messagebox.showerror("Error", "El apellido debe tener al menos 4 letras.")
        return False
    return True

def validar_dni(dni):
    if len(dni) !=8:
        messagebox.showerror("Error", "El dni debe tener 8 digitos.")
        return False
    return True

def validar_telefono(telefono):
    if len(telefono) !=10:
        messagebox.showerror("Error", "El telefono debe tener 10 digitos.")
        return False
    return True

def validar_producto(producto):
    if len(producto) < 4:
        messagebox.showerror("Error", "El producto debe tener al menos 4 letras.")
        return False
    return True

def validar_cantidad(cantidad):
    
        cantidad = int(cantidad)
        if cantidad <= 0:
            messagebox.showerror("Error", "La cantidad debe ser un número mayor que 0.")
            return False
        return True
    
def Formulario():
    
    global textBoxId
    global textBoxNombre
    global textBoxApellido
    global textBoxDni
    global textBoxTelefono
    global textBoxProducto
    global textBoxCantidad
    global comboBox
    global base
    global tree
    global groupBox
    
    try:
        base = Tk()
        base.geometry("1320x300")
        base.title("Registro de clientes")
        
        groupBox = LabelFrame(base, text="Datos del cliente", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)
        
        LabelId = Label(groupBox, text="ID:", width=13, font=("Arial Baltic", 12)).grid(row=0, column=0)
        textBoxId = Entry(groupBox)
        textBoxId.grid(row=0, column=1)
        
        LabelNombre = Label(groupBox, text="Nombre:", width=13, font=("Arial Baltic", 12)).grid(row=1, column=0)
        textBoxNombre = Entry(groupBox)
        textBoxNombre.grid(row=1, column=1)
    
        LabelApellido = Label(groupBox, text="Apellido:", width=13, font=("Arial Baltic", 12)).grid(row=2, column=0)
        textBoxApellido= Entry(groupBox)
        textBoxApellido.grid(row=2, column=1)

        LabelDni = Label(groupBox, text="DNI:", width=13, font=("Arial Baltic", 12)).grid(row=3, column=0)
        textBoxDni = Entry(groupBox)
        textBoxDni.grid(row=3, column=1)
    
        LabelTelefono = Label(groupBox, text="Telefono:", width=13, font=("Arial Baltic", 12)).grid(row=4, column=0)
        textBoxTelefono = Entry(groupBox)
        textBoxTelefono.grid(row=4, column=1)
    
        LabelProducto= Label(groupBox, text="Producto:", width=13, font=("Arial Baltic", 12)).grid(row=5, column=0)
        textBoxProducto = Entry(groupBox)
        textBoxProducto.grid(row=5, column=1)        
        
        LabelCantidad = Label(groupBox, text="Cantidad:", width=13, font=("Arial Baltic", 12)).grid(row=6, column=0)
        textBoxCantidad = Entry(groupBox)
        textBoxCantidad.grid(row=6, column=1)           
        
        Button(groupBox, text="Guardar", width=10, command=guardarRegistros).grid(row=7, column=0)
    
        Button(groupBox, text="Modificar", width=10, command=modificarRegistros).grid(row=7, column=1)
    
        Button(groupBox, text="Eliminar", width=10, command=eliminarRegistros).grid(row=7, column=2)
        
        groupBox = tk.LabelFrame(base, text="Lista de datos", padx=5, pady=5)
        groupBox.grid(row=0, column=1, padx=10, pady=10)
        
        labelBox = tk.Label (groupBox, text="Ordenar por:", width=13, font=("Arial Baltic", 12))
        labelBox.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        comboBox = ttk.Combobox(groupBox, values=["Orden ID", "Orden alfabetico", "Cantidad"], state="readonly")
        comboBox.grid(row=0, column=0, padx=10, pady=10)
        comboBox.current(0)
                       
        tree = ttk.Treeview(groupBox, column = ("ID", "Nombre", "Apellido", "DNI", "Telefono", "Producto", "Cantidad"), show="headings", height=6)
        tree.grid(row=1, column=0, padx=10, pady=10)
        
        tree.column("# 1", anchor=CENTER, width=50)
        tree.heading("# 1", text="ID")
        tree.column("# 2", anchor=CENTER, width=140)
        tree.heading("# 2", text="Nombre")
        tree.column("# 3", anchor=CENTER, width=140)
        tree.heading("# 3", text="Apellido")
        tree.column("# 4", anchor=CENTER, width=140)
        tree.heading("# 4", text="DNI")
        tree.column("# 5", anchor=CENTER, width=140)
        tree.heading("# 5", text="Telefono")
        tree.column("# 6", anchor=CENTER, width=140)
        tree.heading("# 6", text="Producto")
        tree.column("# 7", anchor=CENTER, width=140)
        tree.heading("# 7", text="Cantidad")
        
        comboBox.bind("<<ComboboxSelected>>", actualizarTreeview)
        
        #Mostrar los datos en el Treeview
        for row in Clientes.mostrarClientes():
            tree.insert("", END, values=row)
            
        tree.bind("<<TreeviewSelect>>", seleccionarRegistro) 
    
        vsb = Scrollbar(groupBox, orient="vertical", command=tree.yview)
        vsb.grid(row=1, column=1, sticky='ns')
        tree.configure(yscrollcommand=vsb.set)
        
        base.mainloop()
            
    except ValueError as error:
        print(f"Error al mostrar la interfaz {error}")
    
 
def guardarRegistros():
    
    global textBoxId, textBoxNombre, textBoxApellido, textBoxDni, textBoxTelefono, textBoxProducto, textBoxCantidad
    
    try:
        if not (textBoxId and textBoxNombre and textBoxApellido and textBoxDni and textBoxTelefono and textBoxProducto and textBoxCantidad):
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            
            return
        
        id = textBoxId.get()
        nombre = textBoxNombre.get()
        apellido = textBoxApellido.get()
        dni = textBoxDni.get()
        telefono = textBoxTelefono.get()
        producto = textBoxProducto.get()
        cantidad = textBoxCantidad.get()
        
        if not validar_nombre(nombre):
            return     
        
        if not validar_apellido(apellido):
            return
        
        if not validar_dni(dni):
            return

        if not validar_telefono(telefono):
            return
        
        if not validar_cantidad(cantidad):
            return

        if not validar_producto(producto):
            return     

        
        Clientes.ingresarDatos(id, nombre, apellido, dni, telefono, producto, cantidad)
        messagebox.showinfo ("Informacion", "Los datos han sido guardados")
        
        actualizarRegistros()
        
        textBoxId.delete(0,END)
        textBoxNombre.delete(0, END)
        textBoxApellido.delete(0, END)
        textBoxDni.delete(0, END)
        textBoxTelefono.delete(0, END)
        textBoxProducto.delete(0, END)
        textBoxCantidad.delete(0, END)
        
    except ValueError as error:
        print (f"Error al ingresar datos {error}")  


def actualizarRegistros():
    global tree
    
    try:
        tree.delete(*tree.get_children())
        
        datos = Clientes.mostrarClientes()
        
        for row in Clientes.mostrarClientes():
            tree.insert("", END, values=row)
    
    except ValueError as error:
        print (f"Error al actualizar datos {error}")  

def seleccionarRegistro(event):
    
    try:
        seleccion = tree.focus()
        
        if seleccion:
            values = tree.item(seleccion)["values"]
            
            textBoxId.delete(0, END[0])
            textBoxId.insert(0, values[0])
            
            textBoxNombre.delete(0, END)
            textBoxNombre.insert(0, values[1])
            
            textBoxApellido.delete(0, END)
            textBoxApellido.insert(0, values[2])
            
            textBoxDni.delete(0, END)
            textBoxDni.insert(0, values[3])
            
            textBoxTelefono.delete(0, END)
            textBoxTelefono.insert(0, values[5])
            
            textBoxProducto.delete(0, END)
            textBoxProducto.insert(0, values[4])
            
            textBoxCantidad.delete(0, END)
            textBoxCantidad.insert(0, values[6])

    except ValueError as error:
         print(f"Error al seleccionar registros {error}")

    
def modificarRegistros():
    
    global textBoxId, textBoxNombre, textBoxApellido, textBoxDni, textBoxTelefono, textBoxProducto, textBoxCantidad
    
    try:
        if not (textBoxId and textBoxNombre and textBoxApellido and textBoxDni and textBoxTelefono and textBoxProducto and textBoxCantidad):
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            
            return
        
        id = textBoxId.get()
        nombre = textBoxNombre.get()
        apellido = textBoxApellido.get()
        dni = textBoxDni.get()
        telefono = textBoxTelefono.get()
        producto = textBoxProducto.get()
        cantidad = textBoxCantidad.get()
        
        if not validar_nombre(nombre):
            return     
        
        if not validar_apellido(apellido):
            return
        
        if not validar_dni(dni):
            return

        if not validar_telefono(telefono):
            return
        
        if not validar_cantidad(cantidad):
            return

        if not validar_producto(producto):
            return     
        

        Clientes.modificarDatos(id, nombre, apellido, dni, telefono, producto, cantidad)
        messagebox.showinfo ("Informacion", "Los datos han sido actualizados")
        
        actualizarRegistros()
        
        textBoxId.delete(0,END)
        textBoxNombre.delete(0, END)
        textBoxApellido.delete(0, END)
        textBoxDni.delete(0, END)
        textBoxTelefono.delete(0, END)
        textBoxProducto.delete(0, END)
        textBoxCantidad.delete(0, END)
        
    except ValueError as error:
        print (f"Error al modificar datos {error}")  


def eliminarRegistros():
    
    global textBoxId, textBoxNombre, textBoxApellido, textBoxDni, textBoxTelefono, textBoxProducto, textBoxCantidad
    
    try:
        if not textBoxId:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            
            return
        
        id = textBoxId.get()
      
        Clientes.eliminarDatos(id)
        messagebox.showinfo ("Informacion", "Los datos han sido eliminados")
        
        actualizarRegistros()
        
        textBoxId.delete(0,END)
        textBoxNombre.delete(0, END)
        textBoxApellido.delete(0, END)
        textBoxDni.delete(0, END)
        textBoxTelefono.delete(0, END)
        textBoxProducto.delete(0, END)
        textBoxCantidad.delete(0, END)
        
    except ValueError as error:
        print (f"Error al eliminar datos {error}") 


def actualizarTreeview(event):
    global tree
    
    try:
        order_by = comboBox.get()
            
        for row in tree.get_children():
            tree.delete(row)
            
        rows = Clientes.mostrarOrdenAlf(order_by)
        
        for row in rows:
            tree.insert("", "end", values=row)
    
    except ValueError as error:
        print (f"Error al actualizar Treeview {error}") 

    Formulario()