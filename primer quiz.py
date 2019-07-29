'''Primer quiz: El robot se mueve toma la manzana 
deja un banano y y se devuelvea home
Autor: Nikolas Eraso'''

#Mover hasta manzana
print("hola soy reeborg")
print("voy a hacer una mision")
repeat 4:
    move()
    
#pause()
#Tomar manzana y dejar banano
take("apple")
put("banana")
#pause()
#Devolverse a home
repeat 2:
    turn_left()
#pause()
repeat 4:
    move()
#FIN
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
