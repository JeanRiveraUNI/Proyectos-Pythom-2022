import os
import cx_Oracle
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

# Conexión con la base de datos Oracle
os.environ["TNS_ADMIN"]="C:/Wallet_DB20220530152721"
conexion = cx_Oracle.connect("admin", ".Inacap2022.", "db20220530152721_high")
cursor = conexion.cursor()

# Ventana principal
ventana = tk.Tk()
ventana.title('Sistema de punto de venta')
ventana.geometry('400x200')
ventana.configure(bg='white')
#def iniciar_sesion():
    #if 'admin' and 'admin':
        #ventana_admin()
    #else:
        #messagebox.showerror("Error", "Usuario o clave incorrectos")
    #if 'cajero' and 'cajero':
        #ventana_cajero()
    #else:
        #messagebox.showerror("Error", "Usuario o clave incorrectos")

# Función para iniciar sesión
def iniciar_sesion():
    usuario = entry_usuario.get()
    clave = entry_clave.get()
    if usuario and clave:
        cursor.execute('SELECT usuario, clave FROM usuarios WHERE usuario = :p_usuario AND clave = :p_clave', {'p_usuario': usuario, 'p_clave': clave})
        resultado = cursor.fetchone()
        if resultado is None:
            messagebox.showerror("Error", "Usuario o clave incorrectos")
        else:
            ventana_admin()
    else:
        messagebox.showerror("Error", "Usuario o clave incorrectos")
    
#if 'admin' and 'admin':#ventana_admin()
    #else:
        #cursor.execute('SELECT usuario, clave FROM usuarios WHERE usuario = :p_usuario AND clave = :p_clave', {'p_usuario': usuario, 'p_clave': clave})
        #resultado = cursor.fetchone()
        #if resultado is None:
            #messagebox.showerror("Error", "Usuario o clave incorrectos")
        #else:
            #ventana_cajero()
#class aaa:
   # def __init__(self, ventana):
        #pass
    #def iniciar_sesion():
        #if values == ['Administrador']:
            #def iniciar_sesion_admin():
                #usuario = entry_admin.get()
                #clave = entry_clave_admin.get()
                #if usuario and clave:
                    #ventana_admin()
                    #else:
                        #messagebox.showerror("Error", "Usuario o clave incorrectos")
        #elif values == ['Cajero']:
            #class iniciar_sesion_cajero():
                #usuario = entry_cajero.get()
                #clave = entry_clave_cajero.get()
                #if usuario and clave:
                    #ventana_cajero()
                    #else:
                        #messagebox.showerror("Error", "Usuario o clave incorrectos")
    # Ventana para el administrador
def ventana_admin():
    ventana_admin = tk.Toplevel(ventana)
    ventana_admin.title('Ventana del administrador')
    ventana_admin.geometry('700x400')
    # Opción para mantener productos
    boton_mantenedor = tk.Button(ventana_admin, text='Mantenedor de productos', command=mantenedor_productos)
    boton_mantenedor.grid(column=0, row=0, padx=5, pady=5)
    # Opción para reporte de ventas
    boton_reporte = tk.Button(ventana_admin, text='Reporte de ventas', command=reporte_ventas)
    boton_reporte.grid(column=1, row=0, padx=5, pady=5)
    # Opción para nuevos usuarios
    boton_nuevo_usuario = tk.Button(ventana_admin, text='Crear nuevo usuario', command=nuevo_usuario)
    boton_nuevo_usuario.grid(column=2, row=0, padx=5, pady=5)

# Función para el mantenedor de productos
def mantenedor_productos():
    ventana_mantenedor = tk.Toplevel(ventana)
    ventana_mantenedor.title('Mantenedor de productos')
    ventana_mantenedor.geometry('400x200')
    # Etiquetas
    etiqueta_codigo = tk.Label(ventana_mantenedor, text='Código de producto')
    etiqueta_codigo.grid(column=0, row=0, padx=5, pady=5)
    etiqueta_nombre = tk.Label(ventana_mantenedor, text='Nombre de producto')
    etiqueta_nombre.grid(column=0, row=1, padx=5, pady=5)
    etiqueta_precio = tk.Label(ventana_mantenedor, text='Precio de producto')
    etiqueta_precio.grid(column=0, row=2, padx=5, pady=5)
    etiqueta_cantidad = tk.Label(ventana_mantenedor, text='Cantidad de producto')
    etiqueta_cantidad.grid(column=0, row=3, padx=5, pady=5)
    # Entradas de texto
    entry_codigo = tk.Entry(ventana_mantenedor)
    entry_codigo.grid(column=1, row=0, padx=5, pady=5)
    entry_nombre = tk.Entry(ventana_mantenedor)
    entry_nombre.grid(column=1, row=1, padx=5, pady=5)
    entry_precio = tk.Entry(ventana_mantenedor)
    entry_precio.grid(column=1, row=2, padx=5, pady=5)
    entry_cantidad = tk.Entry(ventana_mantenedor)
    entry_cantidad.grid(column=1, row=3, padx=5, pady=5)

# Función para el reporte de ventas
def reporte_ventas():
    ventana_reporte = tk.Toplevel(ventana)
    ventana_reporte.title('Reporte de ventas')
    ventana_reporte.geometry('400x200')
    # Combobox con las opciones de reporte
    valores = ['Diario', 'Mensual']
    combobox_valores = ttk.Combobox(ventana_reporte, values=valores,)
    combobox_valores.grid(column=0, row=0, padx=5, pady=5)
    # Botón para generar el reporte
    boton_generar = tk.Button(ventana_reporte, text='Generar reporte', command=generar_reporte)
    boton_generar.grid(column=1, row=0, padx=5, pady=5)

# Función para generar el reporte
def generar_reporte():
    valor_seleccionado = combobox_valores.get()
    if valor_seleccionado == 'Diario':
        cursor.execute('SELECT * FROM ventas WHERE fecha_venta = :p_fecha_venta', {'p_fecha_venta': fecha_actual})
    elif valor_seleccionado == 'Mensual':
        cursor.execute('SELECT * FROM ventas WHERE fecha_venta BETWEEN :p_fecha_inicio AND :p_fecha_fin', {'p_fecha_inicio': mes_inicio, 'p_fecha_fin': mes_fin})
    else:
        messagebox.showerror("Error", "Debe seleccionar una opción de reporte")
# Función para crear un nuevo usuario
def nuevo_usuario():
    ventana_usuario = tk.Toplevel(ventana)
    ventana_usuario.title('Nuevo usuario')
    ventana_usuario.geometry('400x200')
    # Etiquetas
    etiqueta_usuario = tk.Label(ventana_usuario, text='Nombre de usuario')
    etiqueta_usuario.grid(column=0, row=0, padx=5, pady=5)
    etiqueta_clave = tk.Label(ventana_usuario, text='Clave de usuario')
    etiqueta_clave.grid(column=0, row=1, padx=5, pady=5)
    etiqueta_perfil = tk.Label(ventana_usuario, text='Perfil de usuario')
    etiqueta_perfil.grid(column=0, row=2, padx=5, pady=5)
    # Entradas de texto
    entry_usuario = tk.Entry(ventana_usuario)
    entry_usuario.grid(column=1, row=0, padx=5, pady=5)
    entry_clave = tk.Entry(ventana_usuario)
    entry_clave.grid(column=1, row=1, padx=5, pady=5)
    # Combobox con los perfiles de usuario
    valores = ['Cajero', 'Administrador']
    combobox_valores = ttk.Combobox(ventana_usuario, values=valores)
    combobox_valores.grid(column=1, row=2, padx=5, pady=5)
    # Botón para guardar el usuario
    boton_guardar = tk.Button(ventana_usuario, text='Guardar', command=guardar_usuario)
    boton_guardar.grid(column=1, row=3, padx=5, pady=5)

# Función para guardar el usuario
def guardar_usuario():
    usuario = entry_usuario.get()
    clave = entry_clave.get()
    perfil = combobox_valores.get()
    if usuario == '' or clave == '' or perfil == '':
        messagebox.showerror("Error", "Debe ingresar todos los datos del usuario")
    else:
        cursor.execute('INSERT INTO usuarios VALUES (:p_usuario, :p_clave, :p_perfil)', {'p_usuario': usuario, 'p_clave': clave, 'p_perfil': perfil})
        conexion.commit()
        entry_usuario.delete(0, 'end')
        entry_clave.delete(0, 'end')
        messagebox.showinfo("Información", "Usuario guardado exitosamente")

# Ventana para el cajero
def ventana_cajero():
    ventana_cajero = tk.Toplevel(ventana)
    ventana_cajero.title('Ventana del cajero')
    ventana_cajero.geometry('400x200')
    # Etiqueta
    etiqueta_codigo = tk.Label(ventana_cajero, text='Código de producto')
    etiqueta_codigo.grid(column=0, row=0, padx=5, pady=5)
    # Entrada de texto
    entry_codigo = tk.Entry(ventana_cajero)
    entry_codigo.grid(column=1, row=0, padx=5, pady=5)
    # Botón para vender el producto
    boton_vender = tk.Button(ventana_cajero, text='Vender producto', command=vender_producto)
    boton_vender.grid(column=1, row=1, padx=5, pady=5)

# Función para vender un producto
def vender_producto():
    codigo = entry_codigo.get()
    if codigo == '':
        messagebox.showerror("Error", "Debe ingresar el código de producto")
    else:
        cursor.execute('SELECT * FROM productos WHERE codigo = :p_codigo', {'p_codigo': codigo})
        resultado = cursor.fetchone()
        if resultado is None:
            messagebox.showerror("Error", "Producto no encontrado")
        else:
            nombre = resultado[1]
            precio = resultado[2]
            cantidad = resultado[3]
            if cantidad == 0:
                messagebox.showerror("Error", "No hay unidades disponibles para el producto")
            else:
                # Actualizar la cantidad de productos
                cantidad_actualizada = cantidad - 1
                cursor.execute('UPDATE productos SET cantidad = :p_cantidad WHERE codigo = :p_codigo', {'p_cantidad': cantidad_actualizada, 'p_codigo': codigo})
                conexion.commit()
                # Ingresar la venta
                cursor.execute('INSERT INTO ventas VALUES (:p_fecha_venta, :p_codigo, :p_nombre, :p_precio)', {'p_fecha_venta': fecha_actual, 'p_codigo': codigo, 'p_nombre': nombre, 'p_precio': precio})
                conexion.commit()
                entry_codigo.delete(0, 'end')
                messagebox.showinfo("Información", "Producto vendido exitosamente")

# Variables 
fecha_actual = ''
mes_inicio = ''
mes_fin = ''
# Etiquetas
etiqueta_fecha = tk.Label(ventana, text='Fecha')
etiqueta_fecha.grid(column=0, row=0, padx=5, pady=5)
etiqueta_mes_inicio = tk.Label(ventana, text='Mes inicio')
etiqueta_mes_inicio.grid(column=0, row=1, padx=5, pady=5)

etiqueta_mes_fin = tk.Label(ventana, text='Seleccione Perfil')
etiqueta_mes_fin.grid(column=0, row=2, padx=5, pady=5)
etiqueta_usuario = tk.Label(ventana, text='Nombre de usuario')
etiqueta_usuario.grid(column=0, row=0, padx=5, pady=5)
etiqueta_clave = tk.Label(ventana, text='Clave de usuario')
etiqueta_clave.grid(column=0, row=1, padx=5, pady=5)
# Entradas de texto
entry_usuario = tk.Entry(ventana)
entry_usuario.grid(column=1, row=0, padx=5, pady=5)
entry_clave = tk.Entry(ventana)
entry_clave.grid(column=1, row=1, padx=5, pady=5)

# entry_codigo
entry_codigo = tk.Entry(ventana)
entry_codigo.grid(column=1, row=0, padx=5, pady=5)
# Combobox
combobox_valores = ttk.Combobox(ventana, values=['Administrador', 'Cajero'])
combobox_valores.grid(column=1, row=2, padx=5, pady=5)
# Botón para iniciar sesión
boton_iniciar_sesion = tk.Button(ventana, text='Iniciar sesión', command=iniciar_sesion)
boton_iniciar_sesion.grid(column=1, row=3, padx=5, pady=5)
ventana.mainloop()