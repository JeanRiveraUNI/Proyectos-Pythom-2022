import tkinter 
import os
import cx_Oracle

os.environ["TNS_ADMIN"]="C:/Wallet_DB20220530152721"
conexion = cx_Oracle.connect("admin", ".Inacap2022.", "db20220530152721_high")
cursor = conexion.cursor()

#Pantalla de Inicio
ventana = tkinter.Tk()
ventana.title("Punto de Venta")
ventana.geometry("400x300")
botonIdentificadorPerfil = tkinter.Button(ventana, text="Identificador de Perfil", command=identificadorPerfil)
botonIdentificadorPerfil.grid(row=0, column=0)
ventana.mainloop()
def login ():
    if(cajausername.get() == "admin" and cajacontraseña.get() == "admin"):
        print("Bienvenido Administrador")
    elif(cajausernameVendedor.get() == "vendedor" and cajacontraseñaVendedor.get() == "vendedor"):
        print("Bienvenido Vendedor")
    else:
        print("Usuario o Contraseña Incorrecta")
def mantenedorProductos():
    ventana2 = tkinter.Tk()
    ventana2.title("Mantenedor de Productos")
    ventana2.geometry("400x300")
    botonAgregar = tkinter.Button(ventana2, text="Agregar Producto", command=agregarProducto)
    botonAgregar.grid(row=0, column=0)
    botonEliminar = tkinter.Button(ventana2, text="Eliminar Producto", command=eliminarProducto)
    botonEliminar.grid(row=1, column=0)
    botonModificar = tkinter.Button(ventana2, text="Modificar Producto", command=modificarProducto)
    botonModificar.grid(row=2, column=0)
#Agregar Perfiles
#Agregar Perfil Administrador
def agregarPerfilAdministrador():
    agregarPerfilAdministrador = "INSERT INTO PERFIL VALUES('"+cajanombrePerfil.get()+"', '"+cajacodigoPerfil.get()+"', '"+cajadescripcionPerfil.get()+"')"
    cursor.execute(agregarPerfilAdministrador)
    conexion.commit()
    print("Perfil Agregado")
#Agregar Perfil Vendedor
def agregarPerfilVendedor():
    agregarPerfilVendedor = "INSERT INTO PERFIL VALUES('"+cajanombrePerfil.get()+"', '"+cajacodigoPerfil.get()+"', '"+cajadescripcionPerfil.get()+"')"
    cursor.execute(agregarPerfilVendedor)
    conexion.commit()
    print("Perfil Agregado")
#Eliminar Perfiles
#Eliminar Perfil Administrador
def eliminarPerfilAdministrador():
    eliminarPerfilAdministrador = "DELETE FROM PERFIL WHERE CODIGO_PERFIL = '"+cajacodigoPerfil.get()+"'"
    cursor.execute(eliminarPerfilAdministrador)
    conexion.commit()
    print("Perfil Eliminado")
#Eliminar Perfil Vendedor
def eliminarPerfilVendedor():
    eliminarPerfilVendedor = "DELETE FROM PERFIL WHERE CODIGO_PERFIL = '"+cajacodigoPerfil.get()+"'"
    cursor.execute(eliminarPerfilVendedor)
    conexion.commit()
    print("Perfil Eliminado")
#Mantenedor de Productos
def agregarProducto():
    agregarProducto = "INSERT INTO PRODUCTO VALUES('"+cajanombreProducto.get()+"', '"+cajacodigoProducto.get()+"', '"+cajaprecioProducto.get()+"', '"+cajacantidadProducto.get()+"')"
    cursor.execute(agregarProducto)
    conexion.commit()
    print("Producto Agregado")
def eliminarProducto():
    eliminarProducto = "DELETE FROM PRODUCTO WHERE CODIGO_PRODUCTO = '"+cajacodigoProducto.get()+"'"
    cursor.execute(eliminarProducto)
    conexion.commit()
    print("Producto Eliminado")
def modificarProducto():
    modificarProducto = "UPDATE PRODUCTO SET NOMBRE_PRODUCTO = '"+cajanombreProducto.get()+"', PRECIO_PRODUCTO = '"+cajaprecioProducto.get()+"', CANTIDAD_PRODUCTO = '"+cajacantidadProducto.get()+"' WHERE CODIGO_PRODUCTO = '"+cajacodigoProducto.get()+"'"
    cursor.execute(modificarProducto)
    conexion.commit()
    print("Producto Modificado")
def salir():
    botonSalir = tkinter.Button(ventana2, text="Salir", command=ventana2.destroy)
    botonSalir.grid(row=3, column=0)
salir()

#indentificador de Perfil
identificadorPerfil = (usernameAdmin, usernameVendedor) = (cajausername.get(), cajausernameVendedor.get())
if(usernameAdmin == "admin"):
    print("Bienvenido Administrador")
    ventana2 = tkinter.Tk()
    ventana2.title("Panel de Administrador")
    ventana2.geometry("400x300")
    botonAgregarPerfilAdministrador = tkinter.Button(ventana2, text="Agregar Perfil Administrador", command=agregarPerfilAdministrador)
    botonAgregarPerfilAdministrador.grid(row=0, column=0)
    botonAgregarPerfilVendedor = tkinter.Button(ventana2, text="Agregar Perfil Vendedor", command=agregarPerfilVendedor)
    botonAgregarPerfilVendedor.grid(row=1, column=0)
    botonEliminarPerfilAdministrador = tkinter.Button(ventana2, text="Eliminar Perfil Administrador", command=eliminarPerfilAdministrador)
    botonEliminarPerfilAdministrador.grid(row=2, column=0)
    botonEliminarPerfilVendedor = tkinter.Button(ventana2, text="Eliminar Perfil Vendedor", command=eliminarPerfilVendedor)
    botonEliminarPerfilVendedor.grid(row=3, column=0)
elif(usernameVendedor == "vendedor"):
    print("Bienvenido Vendedor")
    ventana2 = tkinter.Tk()
    ventana2.title("Mantenedor de Perfiles")
    ventana2.geometry("400x300")


#Datos Administrador
usernameAdmin = tkinter.Label(text="Ingrese su Username: ")
cajausername = tkinter.Entry()
cajausername.grid(row=0, column=1)
usernameAdmin.grid(row=0, column=0)
contraseña = tkinter.Label(text="Ingrese su Contraseña: ")
cajacontraseña = tkinter.Entry()
cajacontraseña.grid(row=1, column=1)
contraseña.grid(row=1, column=0)
#Datos Vendedor
usernameVendedor = tkinter.Label(text="Ingrese su Username: ")
cajausernameVendedor = tkinter.Entry()
cajausernameVendedor.grid(row=2, column=1)
usernameVendedor.grid(row=2, column=0)
contraseñaVendedor = tkinter.Label(text="Ingrese su Contraseña: ")
cajacontraseñaVendedor = tkinter.Entry()
cajacontraseñaVendedor.grid(row=3, column=1)
contraseñaVendedor.grid(row=3, column=0)
#Datos Producto
nombreProducto = tkinter.Label(text="Ingrese el Nombre del Producto: ")
cajanombreProducto = tkinter.Entry()
cajanombreProducto.grid(row=4, column=1)
nombreProducto.grid(row=4, column=0)
codigoProducto = tkinter.Label(text="Ingrese el Codigo del Producto: ")
cajacodigoProducto = tkinter.Entry()
cajacodigoProducto.grid(row=5, column=1)
codigoProducto.grid(row=5, column=0)
precioProducto = tkinter.Label(text="Ingrese el Precio del Producto: ")
cajaprecioProducto = tkinter.Entry()
cajaprecioProducto.grid(row=6, column=1)
precioProducto.grid(row=6, column=0)
cantidadProducto = tkinter.Label(text="Ingrese la Cantidad del Producto: ")
cajacantidadProducto = tkinter.Entry()
cajacantidadProducto.grid(row=7, column=1)
cantidadProducto.grid(row=7, column=0)