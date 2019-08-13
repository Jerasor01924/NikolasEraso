'''Descripción: Función para moverse
Autores: Laura Molina y Nikolas Eraso
Pre: El robot empieza en (1,1) mirando al norte y 1<x<y<10
Pos: Termina en (1,1)'''

def funcion_prueba(x,y):
    #think(1)
    posicionx=1
    posiciony=1
    while front_is_clear():
        #Ciclo para moverse hasta la posicion y
        while not posiciony==y:
            move()
            posiciony=posiciony+1
            if posiciony==y:
                repeat 3 :
                    turn_left()
                break
        #Ciclo para moverse hasta la posicion x
        while not posicionx==x: 
            move()
            posicionx=posicionx+1
            if posicionx==x:
                break
        #Ciclo para una vez halladas las posiciones colocar las estrellas    
        while posicionx==x and posiciony==y:
            if carries_object("star"):
                put("star")
            else:
                print("La posicion es: ",posicionx,posiciony)
                repeat 2:
                    turn_left()
                break
        #Ciclo para devolverse una vez no tenga estrellas
        while not carries_object("star"):
            #Ciclo para dolverse en x
            while posicionx!=1: 
                move()
                posicionx=posicionx-1
                if posicionx==1:
                    break
            #Ciclo para girar si hay una estrella
            while wall_in_front():
                turn_left()
            #Ciclo para devolverse en y
            while posiciony!=1:
                move()
                posiciony=posiciony-1
                if posiciony==1:
                    break
            if posicionx==1 and posiciony==1:
                print("el robot regreso a casa: ",posicionx,posiciony)
            break
    distancia=int(((x-1)**2+(y-1)**2)**0.5)
    print("la distancia recorrida es: ",distancia)
funcion_prueba(5,5)

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
