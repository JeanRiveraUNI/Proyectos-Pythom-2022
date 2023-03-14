#Ejercicio 2
import math
lamina1=0
lamina2=0
#funcion
def area1():
    largo=0
    alto=0
    input(print('Ingrese el largo de la primera lamina: {largo}'))
    input(print('Ingrese el alto de la primera lamina: {alto}'))
    lamina1=largo*alto
def area2():
    largo=0
    alto=0
    input(print('Ingrese el largo de la primera lamina: {largo}'))
    input(print('Ingrese el alto de la primera lamina: {alto}'))
    lamina2=largo*alto
def metros():
    lamina1*lamina2
class condensador():
    def elementos():
        vacio=1.0000
        aire=1.0005
        gasolina=2.35
        aceite=2.8
        vidrio=4.7
        mica=5.6
        glicerina=45
        agua=80.5
        cuazo=4.5
        caucho=2.1
        cera=1.8
        cristal=5,8
        resina=2.5
        vaselina=2.2
        papel=1.5
        celuloide=4.1
        papel_parefinado=3.7
        plexiglas=3.4
#bucle
while bucle==True:
    print('Bienvenido')
    print(area1)
    print(area2)
    f=input(print('Ingrese el elemto: {self.elmentos}'))
    m=lamina1*lamina2
    eo=8,85*10^-12*f/m
    print('El resueltado es: {eo}')
    bucle=False

import cx_Oracle
import os

os.environ['TNS_ADMIN'] = 'Z:/Wallet_DB20220530152721'
conn = cx_Oracle.connect('admin', 'CLAVEBDD', 'db20220530152721_high')
c = conn.cursor()
c.execute('select * from usuarios')
for row in c:
    print(row)