import datetime
from math import radians, sin , cos , acos
pago=0
dist=0
a=0
print("Menu Pincipal: \n 1-Registrarse \n 2-Comenzar una carrera \n 3-Salir \n")
i=1
auto="Apagado"
velocidad=0
opc = int(input("Ingrese una opcion: "))
while opc != 3:
    if opc == 1 and a==0:
        nombre=input("Ingrese su nombre y apellido: ")
        rut=input("Ingrese su rut: ")
        modelo=input("Ingrese el modelo de su auto: ")
        patente=input("Ingrese la patente de su auto: ")
        a=1
    else:
        print("Debe registrarse primero")
    if opc== 2 and a==1:
        print("Menu principal")
        print ("1. Ingresar ubicacion GPS Latitud e ingresar ubicacion gps longitud \n 2. Ver horario \n 3. Encender el vehiculo \n 4. Apagar el vehiculo \n 5. Acelerar \n 6. Girar \n 7. Mostrar todos los datos \n 8. Salir \n")
        opc2 = int(input("Ingrese una opcion: "))
        while opc2 != 9:
            if opc2 == 1:
                print("Ingrese las coordenadas de dos puntos para calcular la distancia entre ellos")
                lugar1 = input("¿En que lugar comienza el recorrido?: ")
                slat = radians(float(input("Latitud del primer lugar: ")))
                slon = radians(float(input("Longitud del primer lugar: ")))
                lugar2 = input("¿En donde terminar el recorrido?: ")
                elat = radians(float(input("Latitud del segundo lugar: ")))
                elon = radians(float(input("longitud del segundo lugar:")))
                dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
                r = round(dist, 2)
                print("La distancia entre: " ,lugar1, "y" ,lugar2, "es" , r, "Km")
                precio = int(input("¿Valor del kilometro por hora? en pesos chilenos: "))
                pago=dist*precio
                p = round(pago, 2)
                print("El pago es: ", p, "pesos")
            elif opc2 == 2:
                import datetime
                print(datetime.datetime.now())
            elif opc2 == 3:
                auto="Encendido"
                print("El auto esta encendido")
            elif opc2 == 4:
                if velocidad !=0:
                    print("No se puede apagar el vehiculo")
                else:
                    auto="Apagado"    
                print("Auto apagado")
            elif opc2 == 5 and auto=="Encendido":
                n = int(input("Cantidad de veces que desea acelerar: "))
                while n > 0:
                    velocidad += 10
                    print("Usted está viajando a", velocidad ,"Km/h")
                    n -= 1
            elif opc2 == 6:
                f = int(input("Ingrese el angulo de giro: "))
                if f > 0 and f < 360:
                    print("El auto gira a", f, "grados")
                else:
                    print("El angulo de giro debe estar entre 0 y 360")
            elif opc2 == 7:
                if dist != 0 and pago !=0:
                    print("Nombre: ", nombre, "\n Rut: ", rut, "\n Modelo: ", modelo, "\n Patente: ", patente,"\n Comenzo en: " ,lugar1, "\n Termino en: " ,lugar2, "\n Distancia Recorrida: ", r,"km" "\n Velocidad: ", velocidad,"km/h" "\n Pago: ", p , "\n El vehiculo ha girado : " ,f, "grados")
                    print(datetime.datetime.now())
                else :
                    print("Debe ingresar las coordenadas")
            elif opc2 == 8:
                print("Gracias por usar el programa")
                exit()
            else:
                print("Opcion no valida")
            opc2 = int(input("Ingrese una opcion: "))    
    else:
        opc = int(input("Ingrese una opcion: \n 1-Registrarse \n 2-Comenzar una carrera \n 3-Salir \n"))
print("Ha salido del programa")