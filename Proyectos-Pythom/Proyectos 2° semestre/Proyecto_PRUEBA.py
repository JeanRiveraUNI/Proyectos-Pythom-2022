print('Bienvenido a JUBER ')
print('precione 1 para registrar un nuevo vehiculo')
print('precione 2 para inciar una carrera')
print('precione 3 para salir')
menu=int()
while menu==1:
    def objeto_auto():
        marca=str(input('introduzca la marca del vehiculo:'))
        patente=float(input('ingrese la pantete del vehiculo:'))
        conductor=str(input('introduzca el nombre del conductor:'))
        color=str(input('introduzca el color del vehiculo:'))
        uber=[conductor,marca,patente,color]
        return uber

#---------------------------------------------------------------------------------------------------------
#def imprimir_auto(lista):
    #for i in lista:
        #print('Elementos en lista:{0}'.format(i))
#lista_de_auto=(objeto_auto())
#crear mas autos
#lista_de_auto.extend(objeto_auto())
#print(lista_de_auto)
#----------------------------------------------------------------------------------------------------------
