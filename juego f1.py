#imports (estos dos no se como aparecieron, llegaron solitos como veneco en lima)
from ast import Break
from operator import truediv
#random para los eventos aleatorios
import random
#time para añadir un delay entre lineas y no se ejecute todo de un trancazo
from time import sleep

#Variable juego para que se siga ejecutando hasta que termine la carrera
juego = True

#bucle principal, mientras juego sea True se seguira ejecutando el programa
while juego == True:
    print("Bienvenido a formula 1 2022")
    nombre_jugador = str(input("Bienvenido Jugador introduce tu nombre: "))
    apellido_jugador = str(input("Introduce tu apellido: "))
    vueltas = int(input("Introduce el número de vueltas a realizar: "))
    posicion = random.randint(1, 20)
    nombre = nombre_jugador + " " + apellido_jugador + " "
    #contador para el bucle que sirve para llevar el conteo de vueltas
    n = 1
    print("""Bienvenidos al gran premio de Italia en el circuito de Monza.
Hablemos de """ + nombre + "que hoy larga desde la plaza " + str(posicion) + ", esperemos que le vaya bien a lo largo de las " + str(vueltas) + " vueltas que se vivirán el dia de hoy")
    sleep(5)
    #secuencia del semaforo
    print("Empiezan a prenderse las luces en el semáforo")
    print("|O| | | | |")
    print("|O| | | | |")
    print("-------------")
    sleep(2)
    print("|O|O| | | |")
    print("|O|O| | | |")
    print("-------------")
    sleep(2)
    print("|O|O|O| | |")
    print("|O|O|O| | |")
    print("-------------")
    sleep(2)
    print("|O|O|O|O| |")
    print("|O|O|O|O| |")
    print("-------------")
    sleep(2)
    print("|O|O|O|O|O|")
    print("|O|O|O|O|O|")
    print("-------------")
    sleep(6)
    print("| | | | | |")
    print("| | | | | |")
    print("-------------")
    print("Se apaga el semáforo y arranca la carrera")
    
    #bucle secundario con los eventos, conteo de vueltas, posiciones.
    while n <= vueltas and n >= 1:
        
        #no pregunten por que puse dos veces la misma variable pudiendo haberme ahorrado y solo poner el random.randint o int(random.randint) asi como lo puse fue como funcionó
        evento_random = int
        evento_random = random.randint(1, 3)
        sleep(3)
        print("Posicion Actual: " + str(posicion))
        print("Vuelta " + str(n) + "/" + str(vueltas))

        #esta parte la estoy mejorando que es la de eventos, ya que en todas las vueltas deberia ocurrir algo, intente usando elif pero no me funcaba, solo funco con if puto python
        if evento_random == 1 and posicion < 1:
            print(nombre + " sube una posicion")
            posicion += 1
        if evento_random == 1 and posicion == 1:
            print(nombre + " mantiene la primera posición")
        if evento_random == 2 and posicion > 20:
            print(nombre + " pierde una plaza, ahora esta en la plaza numero " + str(posicion))
            posicion -= 1
        if evento_random == 2 and posicion == 20:
            print(nombre + " mantiene la ultima posicion")
        if evento_random == 3 and posicion <= 1:
            print(nombre + " ha sufrido un pinchazo y ha perdido algunas posiciones al parar en pits")
            posicion -= random.randint(1, 19)
        if evento_random == 3 and posicion == 20:
            print(nombre + " ha sufrido un pinchazo y se mantiene de ultimo")        

        #condicionales: Primer if: Si n es igual al numero de vueltas se acaba la carrera. Elif: si n es menor que var. vueltas (vueltas a realizar) se suma uno al contador 
        if n == vueltas:
            print("Y así termina la carrera de hoy " + nombre_jugador + " " + apellido_jugador + " terminó en la plaza número " + str(posicion))
            print("""Muchas gracias por jugar :)
            Sigueme en mis redes sociales (IG, twitter, twitch, YT) como @elsirguti""" )
            juego = False
            n = -1
        elif n < vueltas:
            n += 1