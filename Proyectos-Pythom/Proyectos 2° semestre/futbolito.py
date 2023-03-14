import datetime
player_1=[]
player_2=[]

def player ():
    print("ingrese el nombre del jugador 1")
    nombre_1=str(input())
    print("ingrese el nombre del jugador 2")
    nombre_2=str(input())
    print("Bien echo, los jugadores son: {nombre_1},{nombre_2}.")
    return player

def equipos():
    print("Selecione la liga de su equipo")
    ligas()
    return ligas

def ligas():
    print("1. La Liga española")
    def española():
        print("1. Real Mdrid")
        print("2. Barcelona")
        equipo=int(input())
    print("2. La liga italiana")
    def italiana():
        print("1. Juventus")
        print("2. Inter de Milan")
        equipo=int(input())
    print("3. La liga inglesa")
    def inglesa():
        print("1. Manchester United")
        print("2. Manchester City")
        equipo=int(input())
    liga=int(input())
    if liga == 1:
        española()
    if liga == 2:
        italiana()
    if liga == 3:
        inglesa()
    else:
        print("Ingrese una opcion valida")
        ligas()

def menu():
    print("Menu principal")
    print("1. Registrar jugadores")
    print("2. Jugar")
    print("3. Salir")
    opcion=int(input())
    return menu


print("Bienvenido al futbolito")
menu()
    
