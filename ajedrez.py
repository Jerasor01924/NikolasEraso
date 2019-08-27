'''Descripción: Reeborg se mueve horizontal o verticalmente en linea recta
en un campo de 8*8 de ajedrez, desde cualquier posición, 
según una direccion y el número de pasos a avanzar

Pre: 
Reeborg debe mirar al norte y esta en la posicion (2,1)
Reeborg recibe el parametro de direccion siendo 
direccion = 1 = --|
direccion = 2 =   -
                 |
                 |
direccion = 3= -
                |
                |

Pos: Reeborg llega la posición deseada y retorna verdadera
Reeborg se retorna a la posición de inicio y 
retorna false
Reeborg mira al norte
Si puede moverse retorna verdadero.

Fecha:
26/08/2019
autores:
Julian Ortiz
Juan Pablo 
Nikolas Eraso

'''

def girar_derecha() :
    repeat 3:
        turn_left()
def girar_180():
    turn_left()
    turn_left()    
def mueve_caballo(direccion):
    contador = 0
    while front_is_clear():
        if direccion==1:
            girar_derecha()
            move()
            move()
            turn_left()
            move()
            if object_here():
                print("No puedo moverme por que esta ocupado")
                girar_180()
                move()
                girar_derecha()
                move()
                move()
                return False
        elif direccion==2:
            move()
            move()
            girar_derecha()
            move()
            if object_here():
                print("No puedo moverme por que esta ocupado")
                girar_180()
                move()
                turn_left()
                move()
                move()
                girar_180()
                return False
        
        elif direccion==3:
            move()
            move()
            turn_left()
            move()
            if object_here():
                print("No puedo moverme por que esta ocupado")
                girar_180()
                move()
                girar_derecha()
                move()
                move()
                return False
        return True
        
        
        
    

mueve_caballo(3)

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
