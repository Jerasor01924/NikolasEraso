'''Descripción: Funcion para moverse por todo el mapa
Autor: Nikolas Eraso
Fecha: 11/08/2019
Pre: El robot empieza en (1,1) mirando al este
Pos: El robot termina en (5,5) mirando al norte'''

def moverse():
    energy=7
    print("Hola iniciaré el recorrido con :",energy,"de energía")
    while energy>0:
        energy = avanzar(energy)
        if energy == 0:
            break
        energy =subir(energy)
        if energy == -100 or energy == 0:
            break
        energy = avanzar(energy)
        if energy == 0:
            print("La energia final es: ",energy)
            break
        girarDerecha()
        if wall_in_front():
            print("La energia final es: ",energy)
            break
        move()
        girarDerecha()

'''Funcion para girar a la derecha
Pre: el robot tiene una pared en frente
Pos: el robot termina mirando hacia el este o el 
oeste dependiendo de la pared'''
def girarDerecha():
    repeat 3:
        turn_left()
        
'''Funcion para avanzar y validar los objetos en el mapa
Pre: El frente del robot debe estar despejado y
debe tener energia
Pos: El robot ha tomado las manzanas y ha recogido '''
def avanzar(energy):
    while not wall_in_front():
        if energy==0:
            print("Sin energia")
            return energy
        move()
        energy = energy-1
        print("He caminado un paso mi energía es de: ",energy)
        if object_here("apple"):
            take()
            if carries_object("apple"):
                energy = energy+7
                print("He pasado por una manzana mi energía es de: ",energy)
            elif energy>=21:
                print("No puedo comer más manzanas")
        elif object_here("tulip"):
            energy = energy-2
            print("He pasado por un Tulipan mi energía actual es: ",energy)
        elif object_here("triangle"):
            take()
            energy = energy-1
            print("He pasado por un triangulo, mi energía es de: ",energy)
        elif object_here("token"):
            if energy>21:
                energy = 0
                print("Perdi las manzanas")
    return energy
def subir(energy):
    if energy==0:
        print("Sin energia")
        return energy
    turn_left()
    if wall_in_front():
        print("La energia final es: ",energy)
        energy = -100
    else:
        move()
        energy = energy-1
        print("He caminado un paso mi energía es de: ",energy)
        if object_here("apple"):
            take()
            if carries_object("apple"):
                energy = energy+7
                print("He pasado por una manzana mi energía es de: ",energy)
            elif energy>=21:
                print("No puedo comer más manzanas")
        elif object_here("tulip"):
            energy = energy-2
            print("He pasado por un Tulipan mi energía actual es: ",energy)
        elif object_here("triangle"):
            take()
            energy=int(energy-1)
            print("He pasado por un triangulo, mi energía es de: ",energy)
        elif object_here("token"):
            if energy>21:
                energy = 0
                print("Perdi las manzanas")
        turn_left()
    return energy
    
moverse()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
