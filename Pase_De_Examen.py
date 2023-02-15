from random import randint 
from os import system

#FUNCIÓN RECIBE ELEMENTOS Y DETERMINA GANADOR
def juego(a,b):

    if a == b:
        print(f'PLAYER 1: {b}')
        print(f'PLAYER 2: {a}')
        variable = 'TIE'
        return[variable]

    elif a == 'PIEDRA' and b == 'PAPEL' or a == 'PIEDRA' and  b == 'SPOCK':
        print(f'PLAYER 1: {b}')
        print(f'PLAYER 2: {a}')
        variable = 'GANADOR PLAYER 1'
        return[variable]

    elif a == 'PAPEL' and b == 'TIJERA' or a == 'PAPEL' and  b == 'LAGARTO':
        print(f'PLAYER 1: {b}')
        print(f'PLAYER 2: {a}')
        variable = 'GANADOR PLAYER 1'
        return[variable]

    elif a == 'TIJERA' and b == 'PIEDRA' or a == 'TIJERA' and  b == 'SPOCK':
        print(f'PLAYER 1: {b}')
        print(f'PLAYER 2: {a}')
        variable = 'GANADOR PLAYER 1'
        return[variable]

    elif a == 'SPOCK' and b == 'PAPEL' or a == 'SPOCK' and  b == 'LAGARTO':
        print(f'PLAYER 1: {b}')
        print(f'PLAYER 2: {a}')
        variable = 'GANADOR PLAYER 1'
        return[variable]

    elif a == 'LAGARTO' and b == 'TIJERA' or a == 'LAGARTO' and b == 'PIEDRA':
        print(f'PLAYER 1: {b}')
        print(f'PLAYER 2: {a}')
        variable = 'GANADOR PLAYER 1'
        return[variable]
    
    else:
        print(f'PLAYER 1: {b}')
        print(f'PLAYER 2: {a}')
        variable = 'GANADOR PLAYER 2'
        return[variable]


#CREACIÓN DE VARIABLES QUE USAREMOS PARA SUMAR PUNTOS
contador = 0
contador_2 = 0
condition = True

while condition == True:

    system('cls')
    print('\t\t\tHOLA BIENVENIDO\n')

    #LISTA DE ELEMENTOS DISPONIBLES
    elements = ['PIEDRA', 'PAPEL', 'TIJERA', 'LAGARTO', 'SPOCK']
    print('1) Piedra 🪨. ', '2) Papel 🧻. ', '3) Tijera ✂️. ', '4) Lagarto 🦎. ', '5) Spock 🖖. \n')

    #SE CREA UN NÚMERO ALEATORIO Y UNA VARIABLE DONDE GUARDARA ESTE DATO EN CASO DE JUGAR UN SOLO JUGADOR
    aleatorio = randint(0,4)
    jugador_pc = elements[aleatorio]
    desicion = input('¿Desea jugar con otro jugador? ').upper()

    #DOS JUGADORES
    if desicion == 'SI':
        jugador_one = input('Player 1 ingrese el nombre del elemento: ').upper()
        system('cls')
        print('\t\t\tHOLA BIENVENIDO\n')
        print('1) Piedra 🪨. ', '2) Papel 🧻. ', '3) Tijera ✂️. ', '4) Lagarto 🦎. ', '5) Spock 🖖. \n')
        jugador_two = input('Player 2 ingrese el nombre del elemento: ').upper()
        input('PRESIONE UNA TECLA PARA CONTINUAR...')
        system('cls')

        #DETERMINA SI INGRESO UN ELEMENTO VALIDO DE SER ASI SE EJECUTA ESTE BLOQUE
        if jugador_one in elements and jugador_two in elements:
            lista = juego(jugador_two,jugador_one)
            print(lista)

            if 'GANADOR PLAYER 1' in lista:
                contador +=1
                print(f'PLAYER 1 VICTORIAS {contador} VS PLAYER 2 VICTORIAS {contador_2}')
                input('PRESIONE UNA TECLA PARA JUGAR...')

            elif 'GANADOR PLAYER 2' in lista:
                contador_2 += 1
                print(f'PLAYER 1 VICTORIAS {contador} VS PLAYER 2 VICTORIAS {contador_2}')
                input('PRESIONE UNA TECLA PARA JUGAR...')
            
            else:
                print(f'PLAYER 1 VICTORIAS {contador} VS PLAYER 2 VICTORIAS {contador_2}')
                input('PRESIONE UNA TECLA PARA JUGAR...')

        #SE DETERMINO QUE NO ESCOGIO UN ELEMENTO VALIDO POR LO TANTO TERMINA
        else:
            print('Vuelve a intentarlo')


    #UN SOLO JUGADOR
    else:
        jugador_one = input('Player 1 ingrese el nombre del elemento: ').upper()

        #DETERMINA SI EL ELEMENTO INGRESADO ESTA EN LA LISTA DE SER ASI SE EJECUTA ESTE BLOQUE
        if jugador_one in elements:
            lista = juego(jugador_pc,jugador_one)
            print(lista)

            if 'GANADOR PLAYER 1' in lista:
                contador += 1
                print(f'PLAYER 1 VICTORIAS {contador} VS PLAYER 2 VICTORIAS {contador_2}')
                input('PRESIONE UNA TECLA PARA JUGAR...')

            elif 'GANADOR PLAYER 2' in lista:
                contador_2 += 1
                print(f'PLAYER 1 VICTORIAS {contador} VS PLAYER 2 VICTORIAS {contador_2}')
                input('PRESIONE UNA TECLA PARA JUGAR...')
            
            else:
                print(f'PLAYER 1 VICTORIAS {contador} VS PLAYER 2 VICTORIAS {contador_2}')
                input('PRESIONE UNA TECLA PARA JUGAR...') 


        #SE DETERMINO QUE INGRESO UN ELEMENTO INVALIDO      
        else:
            print('Vuelve a intentarlo')