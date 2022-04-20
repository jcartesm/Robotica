import random as ra,  matplotlib as plt
from vpython import *
from vpython import frame
from matplotlib.pyplot import axis
from numpy import size

#import math as mt




########################################################################################
#                                   FUNCIONES                                          #
########################################################################################

# Coordenadas Aleatorias dado intervalos para x e y
def RandomCoord(x1,x2,y1,y2):
    x = ra.randint(x1,x2)
    y = ra.randint(y1,y2)
    cord = [x , y]
    return cord

# Creación del suelo donde se moverá el robot
def my_Escenario():     
    # pos = coordenada ( x, y (es profundidad, como una eje z), z )   ;   size = ( ancho , alto , largo )
    Superficie= box(pos=vector(0,0,0),size=vector(2000,5,1000), color = color.white)
    BordeCorto_1 = box(pos=vector(+1000,0,0),size=vector(40,40,1000), color = color.gray(0.5))
    BordeCorto_2 = box(pos=vector(-1000,0,0),size=vector(40,40,1000), color = color.gray(0.5))
    Bordelargo_1 = box(pos=vector(0,0,+500),size=vector(2000,40,40), color = color.gray(0.5))
    Bordelargo_2 = box(pos=vector(0,0,-500),size=vector(2000,40,40), color = color.gray(0.5))
    D_1 = box(pos=vector(900,5,-400), size=vector(75,10,75), color = color.yellow)
    D_2 = box(pos=vector(900,5,400), size=vector(75,10,75), color = color.yellow)
    D_3 = box(pos=vector(-900,5,-400), size=vector(75,10,75), color = color.yellow)
    D_4 = box(pos=vector(-900,5,400), size=vector(75,10,75), color = color.yellow)
    
    # Figura protocolar del prototipo P.E.N.E.
    # c1 = sphere(pos=vector(5,150,-500),radius=50, color = color.orange)
    # c2 = sphere(pos=vector(-5,150,-500),radius=50, color = color.orange)
    # pe = cylinder(pos=vector(0,0,-500),radius=50,axis=vector(00,150,0), color = color.orange)
    # c3 = sphere(pos=vector(-50,0,-500),radius=50, color = color.orange)
    # c4 = sphere(pos=vector(50,0,-500),radius=50, color = color.orange)

    return

# Creacion de tambores, x { -1000 ..... 1000} y x { -500 ..... 500}
def my_Tambores(x1,x2,y1,y2):
    posicion = RandomCoord(x1,x2,y1,y2)
    Tambor_1  = cylinder( pos=vector(posicion[0],0,posicion[1]), axis=vector(0,60,0), radius=30, color=color.blue) 
#---------------------------Definicion del Robot---------------------------------------#
def my_Robot(nDesp):
    
    #Definicion de frames central y compartimiento
    Base = box(pos=vector(00-nDesp,40,00),size=vector(150,30,110),color=color.red)
    
    #Lado de adelante
    Lado1 = box(pos=vector(10,65,00), size=vector(50,20,75),color=color.red)
    
    Lado2 = box(pos=vector(-40,65,50), size=vector(150,20,10),color=color.red)
    
    Lado3 = box(pos=vector(-40,65,-50), size=vector(150,20,10),color=color.red)
    #Lado de atras
    Lado4 = box(pos=vector(-110,65,00), size=vector(10,20,75),color=color.red)
    
    #Definicion de ruedas
    Rueda1 = cylinder(pos=vector(50-nDesp,15,35),radius=15,axis=vector(00,00,20),color = color.black) 
    Rueda2 = cylinder(pos=vector(+50-nDesp,15,-55),radius=15,axis=vector(00,00,20),color = color.black)
    RuedaCastor  = cylinder(pos=vector(-100,15,-13),radius=15,axis=vector(00,00,20),color = color.black)
    
    #Brazo derecho
    AnteBrazoR = box(pos=vector(50-nDesp, 50,60), size=vector(20,40,10), color=color.blue)
    BrazoR = box(pos=vector(70, 35,60), size=vector(110,10,10), color=color.blue)
    
    #Brazo izquierdo
    AnteBrazoL = box(pos=vector(+50-nDesp, 50,-60), size=vector(20,40,10), color=color.orange)
    BrazoL = box(pos=vector(70, 35,-60), size=vector(110,10,10), color=color.blue)
    
    Brazos = compound([AnteBrazoL, AnteBrazoR, BrazoL, BrazoR])
    robot1 = compound([Base, Lado1, Lado2, Lado3, Lado4, Rueda1, Rueda2, RuedaCastor])

    return    


def robotPrueba(x,y):
    
    centro = cylinder( pos=vector(x-40,0,y), axis=vector(0,200,0), radius=3, color=color.yellow) 
    #Definicion de frames central y compartimiento
    Base = box(pos=vector(x-40,25,y),size=vector(100,15,80),color=color.red)
    
    #                                  size (largo , alto , ancho)
    #Lado de adelante
    Lado1 = box(pos=vector(x+10,31,y), size=vector(50,28,80),color=color.red)
    # Lado derecho
    Lado2 = box(pos=vector(x-40,35,y+35), size=vector(100,20,10),color=color.red)
    # Lado izquierdo
    Lado3 = box(pos=vector(x-40,35,y-35), size=vector(100,20,10),color=color.red)
    #Lado de atras
    Lado4 = box(pos=vector(x-85,35,y), size=vector(10,20,78),color=color.red)
    
    #Definicion de ruedas
    Rueda1 = cylinder(pos=vector(x,15,y+22),radius=15,axis=vector(00,00,15),color = color.black) 
    Rueda2 = cylinder(pos=vector(x,15,y-36),radius=15,axis=vector(00,00,15),color = color.black)
    RuedaCastor  = cylinder(pos=vector(-75,15,y-8),radius=15,axis=vector(00,00,15),color = color.black)
    #                                        , y (+)derecha (-)izquierda
    # pos ( +adelante- -atras, arriba, a los lados hacia afuera o hacia dentro)
    #Brazo derecho
    AnteBrazoR = box(pos=vector(x+15, 31,y+40), size=vector(25,15,10), color=color.blue)
    BrazoR = box(pos=vector(x+52, 27,y+40), size=vector(100,10,8), color=color.blue)
    
    #Brazo izquierdo
    AnteBrazoL = box(pos=vector(x+15, 31,y-40), size=vector(25,15,10), color=color.blue)
    BrazoL = box(pos=vector(x+52, 27,y-40), size=vector(100,10,8), color=color.blue)
    
    Brazos = compound([AnteBrazoL, AnteBrazoR, BrazoL, BrazoR])
    robot1 = compound([Base, Lado1, Lado2, Lado3, Lado4, Rueda1, Rueda2, RuedaCastor])

    return  


#-------------------------------Variables Iniciales-------------------------------------#

nDesp=40
centroide = [0,0]
tPosInicial = (nDesp,0,0)

my_Escenario() 
my_Tambores(500,502,12,14)
#my_Robot(nDesp)
robotPrueba(centroide[0],centroide[1])