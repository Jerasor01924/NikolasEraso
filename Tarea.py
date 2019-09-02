'''Descripcion: Funcion para recorrer la columna en la
que se indique el parémetro
Autor: Nikolas Eraso
Fecha: 30/08/2019
Pre: Parametro col>1
Reeborg inicia en (1,1) mirando al este
Si puede moverse retorna True
Si no puede se mueve hasta donde pide la variable 
y se devulve y retorna False
Pos:Reeborg termina en (discriminante,10) si se puede
si no se devulve a (1,1).'''

def girar_derecha():
    repeat 3:
        turn_left()
        
def volver_a_casa_con_rastro(encontro_columna,col):
    if wall_in_front():
        turn_left()
        turn_left()
        if (col%2)==0:
            put("strawberry")
        else:
            put("apple")
    while not wall_in_front() and (col%2)==0:
        move()
        put("strawberry")
        if wall_in_front():
            girar_derecha()
            encontro_columna=False
        while encontro_columna==False:
            move()
            put("strawberry")
            if wall_in_front():
                break
    if wall_in_front():
        turn_left()
        turn_left()
    
    while not wall_in_front() and (col%2)!=0:
        move()
        put("apple")
        if wall_in_front():
            girar_derecha()
            encontro_columna=False
        while encontro_columna==False and front_is_clear():
            move()
            put("apple")
            if wall_in_front():
                break
    if wall_in_front():
        turn_left()
        turn_left()
    
    
def recorrer_columna(col):
    think(1)
    contadorx=1
    encontro_columna=False
    
    while front_is_clear() and contadorx<=col:         
        if contadorx==col:
            encontro_columna=True
            turn_left()
            break
        move()
        contadorx=contadorx+1        
    
    if encontro_columna:
        while front_is_clear(): 
            move()
        volver_a_casa_con_rastro(encontro_columna,col)    
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
recorrer_columna(3)
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
