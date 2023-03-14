#funcion
from tkinter import E
velocidad=0
encendido=False
opcion=99
distancia=0
rotacion_x=0
rotacion_y=0
def menu():
    global encendido
    entendido=not(encendido)
    print("velocidad encendido" if encendido else "velocidad apagado ")
def acelerar():
    global velocidad
    if velocidad>=0 and encendido:
        velocidad+=10
        print("el vehiculo esta acelerando: {velocidad}.km/h")        
    else:
        print("El vehiculo esta apagado o esta en reversa")
    print("velocidad actual"+(str(velocidad)))
def frenar ():
    global velocidad
    if velocidad>0 and encendido:
        velocidad-=10
    else:
        print("el vehiculo esta frenando: {velocidad}.Km/h")
def girar_a_la_derecha():
    if girar_a_la_derecha==True:
        print("giro a la derecha")
        def rotacion_x():
            rotacion_x=rotacion_x+10
            print("rotacion en eye x"+(str(rotacion_x)))
    else :
        print("giro no realizado")
def girar_a_la_izquierda():
    if girar_a_la_izquierda==true:
        print("giro a la izquierda")
        def rotacion_y():
            rotacion_y=rotacion_x+10
            print("rotacion en eye y"+(str(rotacion_y)))
    else:
        print("giro no realizado")
        

