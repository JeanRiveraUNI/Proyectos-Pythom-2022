import tkinter

def mifuncion():
    print(caja.get())
ventana = tkinter.Tk()
ventana.title("Hola Mundo")
ventana.geometry("400x300")
etiqueta = tkinter.Label(ventana, text="Hola Mundo")
etiqueta.grid(column=0, row=0)
caja = tkinter.Entry(ventana)
caja.grid(column=1, row=0)
aceptar = tkinter.Button(ventana, text="Aceptar", command=mifuncion)
aceptar.grid(column=2, row=0)
radio = tkinter.Radiobutton(ventana, text="Opcion 1")
radio.grid(column=0, row=1)
check = tkinter.Checkbutton(ventana, text="Opcion 2")
check.grid(column=1, row=1)
listas = tkinter.Listbox(ventana)
listas.insert(1, "Opcion 1")
listas.insert(2, "Opcion 2")
texto = tkinter.Text(ventana, height=10, width=30)
texto.insert(tkinter.END, "Hola Mundo")
texto.grid(column=0, row=2)
ventana.mainloop()

#Para un usuario, crea un formulario que pida 
#nombre, apellido, edad, sexo, correo, contraseña, username, hobbies.
#Al presionar el botón, almacena los datos en un diccionario, y posteriormente, genera la consulta 
#para insertar los datos en una tabla de una base de datos.