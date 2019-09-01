'''Descripcion: Funcion para recorrer la columna en la
que se indique el parémetro
Autor: Nikolas Eraso
Fecha: 30/08/2019

Pre: Parametro discriminante>1
Reeborg inicia en (1,1) mirando al este
Si puede moverse retorna True
Si no puede se mueve hasta donde pide la variable 
y se devulve y retorna False
Pos:Reeborg termina en (discriminante,10) si se puede
si no se devulve a (1,1).'''

def girar_derecha():
    repeat 3:
        turn_left()
        
def devolverse_home(encontro_columna,discriminante):
    if wall_in_front():
        turn_left()
        turn_left()
        if (discriminante%2)==0:
            put("apple")
        else:
            put("star")
    while not wall_in_front() and (discriminante%2)==0:
        move()
        put("apple")
        if wall_in_front():
            girar_derecha()
            encontro_columna=False
        while encontro_columna==False:
            move()
            if wall_in_front():
                break
    if wall_in_front():
        turn_left()
        turn_left()
    
    while not wall_in_front() and (discriminante%2)!=0:
        move()
        put("star")
        if wall_in_front():
            girar_derecha()
            encontro_columna=False
        while encontro_columna==False and front_is_clear():
            move()
            if wall_in_front():
                break
    if wall_in_front():
        turn_left()
        turn_left()
    
    
def recorrer_columna(discriminante):
    think(1)
    contadorx=1
    encontro_columna=False
    
    while front_is_clear() and contadorx<=discriminante:         
        if contadorx==discriminante:
            encontro_columna=True
            turn_left()
            break
        move()
        contadorx=contadorx+1        
    
    if encontro_columna:
        while front_is_clear(): 
            move()
        devolverse_home(encontro_columna,discriminante)    
    else:
        volver()
    
    return (encontro_columna)
               
    
'''
Pre: Reeborg mira al Este y tiene un pared en frente
'''
def volver():     
    
    repeat 2:
        turn_left()
        
    while not wall_in_front():
        move()

    repeat 2:
        turn_left()
    
    return False
        

recorrer_columna(1)
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
