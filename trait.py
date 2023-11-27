# Fonction trait(x1,y1,x2,y2) :
# x1, y1 : coordonn´ees du d´ebut du trait
# x2, y2 : coordonn´ees de la fin du trait
from turtle import *

def trait(x1,y1,x2,y2,w) :
    up()
    goto(x1,y1)
    width(w)
    down()
    goto(x2,y2)
