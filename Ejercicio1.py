from cProfile import run
import random as ra,  matplotlib as plt
from vpython import *
from vpython import frame
from matplotlib.pyplot import axis
import numpy as np
import math
import sys
import time

from Ventana1 import Robot


########################################################################################
#                              AJUSTES DE LA ESCENA                                    #
########################################################################################

scene.width = 1450
scene.height = 600
scene.range = 1000
scene.title = "En la Busqueda del Tambor dorado\n"
scene.camera.pos = vector(0,500,2000)


########################################################################################
#                                   FUNCIONES                                          #
########################################################################################

# Coordenadas Aleatorias dado intervalos para x e y
def RandomCoord(x1,x2,y1,y2):
    x = ra.randint(x1,x2)
    y = ra.randint(y1,y2)
    return x,y

# Creación del suelo donde se moverá el robot
def my_Escenario():     
    # pos = coordenada ( x, y (es profundidad, como una eje z), z )   ;   size = ( ancho , alto , largo )
    Superficie= box(pos=vector(0,0,0),size=vector(2000,2,1000), color = color.white)
    BordeCorto_1 = box(pos=vector(+1000,0,0),size=vector(40,40,1000), color = color.gray(0.5))
    BordeCorto_2 = box(pos=vector(-1000,0,0),size=vector(40,40,1000), color = color.gray(0.5))
    Bordelargo_1 = box(pos=vector(0,0,+500),size=vector(2000,40,40), color = color.gray(0.5))
    Bordelargo_2 = box(pos=vector(0,0,-500),size=vector(2000,40,40), color = color.gray(0.5))
    #D_1 = box(pos=vector(ra.randint(0,900),5,ra.randint(-400,0)), size=vector(75,10,75), color = color.yellow)
    #D_2 = box(pos=vector(ra.randint(0,900),5,ra.randint(0,400)), size=vector(75,10,75), color = color.yellow)
    #D_3 = box(pos=vector(ra.randint(-900,0),5,ra.randint(-400,0)), size=vector(75,10,75), color = color.yellow)
    #D_4 = box(pos=vector(ra.randint(-900,0),5,ra.randint(0,400)), size=vector(75,10,75), color = color.yellow)
    
    D_1 = box(pos=vector(-900,5,-400), size=vector(75,10,75), color = color.yellow)
    D_2 = box(pos=vector(-900,5,400), size=vector(75,10,75), color = color.yellow)
    D_3 = box(pos=vector(900,5,-400), size=vector(75,10,75), color = color.yellow)
    D_4 = box(pos=vector(900,5,400), size=vector(75,10,75), color = color.yellow)

    # arreglo de posiciones de espacio para dejar tambor 
    aD = [D_1.pos, D_2.pos, D_3.pos, D_4.pos]
    
    # Proyecto ultra secreto P.E. utilizando el prototipo N.E.
    # c1 = sphere(pos=vector(5,150,-500),radius=50, color = color.orange)
    # c2 = sphere(pos=vector(-5,150,-500),radius=50, color = color.orange)
    # pe = cylinder(pos=vector(0,0,-500),radius=50,axis=vector(00,150,0), color = color.orange)
    # c3 = sphere(pos=vector(-50,0,-500),radius=50, color = color.orange)
    # c4 = sphere(pos=vector(50,0,-500),radius=50, color = color.orange)

    return aD

# Creacion de tambores, x { -1000 ..... 1000} y x { -500 ..... 500}
def my_Tambores():

    #Tambor_1  = cylinder( pos=vector(ra.randint(0,900),0,ra.randint(-400,0)), axis=vector(0,60,0), radius=30, color=color.blue) 
    #Tambor_2  = cylinder( pos=vector(ra.randint(0,900),0,ra.randint(0,400)), axis=vector(0,60,0), radius=30, color=color.blue)
    #Tambor_3  = cylinder( pos=vector(ra.randint(-900,0),0,ra.randint(-400,0)), axis=vector(0,60,0), radius=30, color=color.blue)
    #Tambor_4  = cylinder( pos=vector(ra.randint(-900,0),0,ra.randint(0,400)), axis=vector(0,60,0), radius=30, color=color.blue)
    
    Tambor_1  = cylinder( pos=vector(700,0,-300), axis=vector(0,60,0), radius=30, color=color.blue) 
    Tambor_2  = cylinder( pos=vector(700,0,300), axis=vector(0,60,0), radius=30, color=color.blue)
    Tambor_3  = cylinder( pos=vector(-700,0,-300), axis=vector(0,60,0), radius=30, color=color.blue)
    Tambor_4  = cylinder( pos=vector(-700,0,300), axis=vector(0,60,0), radius=30, color=color.blue)  
    
    return Tambor_1, Tambor_2, Tambor_3, Tambor_4 
#---------------------------Definicion del Robot---------------------------------------# 

def robotPrueba(x,y):
    
    centro = cylinder( pos=vector(x,0,y), axis=vector(0,200,0), radius=3, color=color.yellow) 
    #Definicion de frames central y compartimiento
    Base = box(pos=vector(x-90,25,y),size=vector(100,15,80),color=color.red)
    
    #                                  size (largo , alto , ancho)
    #Lado de adelante
    Lado1 = box(pos=vector(x-40,31,y), size=vector(50,28,80),color=color.red)
    # Lado derecho
    Lado2 = box(pos=vector(x-90,35,y+35), size=vector(100,20,10),color=color.red)
    # Lado izquierdo
    Lado3 = box(pos=vector(x-90,35,y-35), size=vector(100,20,10),color=color.red)
    #Lado de atras
    Lado4 = box(pos=vector(x-135,35,y), size=vector(10,20,78),color=color.red)
    
    #Definicion de ruedas
    Rueda1 = cylinder(pos=vector(x-40,15,y+22),radius=15,axis=vector(00,00,15),color = color.black) 
    Rueda2 = cylinder(pos=vector(x-40,15,y-36),radius=15,axis=vector(00,00,15),color = color.black)
    RuedaCastor  = cylinder(pos=vector(x-125,15,y-8),radius=15,axis=vector(00,00,15),color = color.black)
    #                                        , y (+)derecha (-)izquierda
    # pos ( +adelante- -atras, arriba, a los lados hacia afuera o hacia dentro)
    #Brazo derecho
    AnteBrazoR = box(pos=vector(x-35, 31,y+40), size=vector(25,15,10), color=color.blue)
    BrazoR = box(pos=vector(x+2, 27,y+40), size=vector(100,10,8), color=color.blue)
    
    #Brazo izquierdo
    AnteBrazoL = box(pos=vector(x-35, 31,y-40), size=vector(25,15,10), color=color.blue)
    BrazoL = box(pos=vector(x+2, 27,y-40), size=vector(100,10,8), color=color.blue)
    
    Brazos = compound([AnteBrazoL, AnteBrazoR, BrazoL, BrazoR])
    robotC = compound([Base, Lado1, Lado2, Lado3, Lado4, Rueda1, Rueda2, RuedaCastor])#, pos=vector(x,20,y))
    robotF = compound([robotC, Brazos], origin=Brazos.origin)
    robotF.pos.x = x
    robotF.pos.y = y
    #cLabel = label(text='Punto de Control', space=10,height=15, border=4,yoffset=30,font='sans', pos=cRobot.pos)
    robotF.axis = vector(ra.randint(-10,10), 00, ra.randint(-10,10))

    return robotF


def LeyControl(ulPosX, ulPosZ, posDeseadaX, posDeseadaZ, nDesp): 
    ts = 0.1; tf = 10 ; T = np.arange(0,tf+ts,ts) ; N = len(T)
    # Seteo de arreglos de ceros para las coordendas y angulos
    xc  = np.zeros(len(T)+1) ; zc  = np.zeros(len(T)+1)
    ph  = np.zeros(len(T)+1) 
    xp  = np.zeros(len(T)+1) ; zp  = np.zeros(len(T)+1)
    xr  = np.zeros(len(T)+1) ; zr  = np.zeros(len(T)+1)
    u   = np.zeros(len(T)+1) ; w   = np.zeros(len(T)+1)
    xre = np.zeros(len(T)+1) ; zre = np.zeros(len(T)+1)

    xc[0] = ulPosX ; zc[0]=ulPosZ
    ph[0] = math.sin(math.radians(4))

    xr[0] = xc[0] + nDesp*math.cos(ph[0])
    zr[0] = zc[0] + nDesp*math.sin(ph[0])
    xrD = posDeseadaX ; zrD = posDeseadaZ

    for i in range(N):
        xre[i] = xrD - xr[i]
        zre[i] = zrD - zr[i]
        
        #Intervalo de error 
        e = np.array([[xre[i]],
                      [zre[i]]])
        
        #Matriz Jacobiana
        J = np.array([[math.cos(ph[i]), -nDesp*math.sin(ph[i])],
                      [math.sin(ph[i]), nDesp*math.cos(ph[i])]])

        #Matriz de Ganancia
        K = np.array([[1, 0],
                      [0, 1]])

        #Ley de control del robot
        V = np.linalg.inv(J)*K*e

        #u=Velocidad del robot | w = velocidad angular
        u[i] = V[0][0]
        w[i] = V[1][1]

        #Aplicar las acciones del control al robot
        xp[i] = u[i]*math.cos(ph[i]) - nDesp*w[i]*math.sin(ph[i])
        zp[i] = u[i]*math.sin(ph[i]) + nDesp*w[i]*math.cos(ph[i]) 

        #Hallar posiciones del robot
        xr[i+1] = xr[i] + ts*xp[i]
        zr[i+1] = zr[i] + ts*zp[i]
        ph[i+1] = ph[i] + ts*w[i]

        #posicion final del robot
        xc[i+1] = xr[i+1] - nDesp*math.cos(ph[i+1])
        zc[i+1] = zr[i+1] - nDesp*math.sin(ph[i+1])
    
    return(xc, zc, ph, xrD, zrD,u)

#-------------------------------Variables Iniciales-------------------------------------#

def Run():
    Tambor1.pos.x = Tambor1.pos.x + 5
    Tambor1.pos.y = Tambor1.pos.y + 10



#bRun = button(text="<b>RUN</b>", background=color.green,  
       #textcolor=color.white,pos=(scene.title_anchor), bind=Run)
#bExit = button(text="<b>EXIT</b>", background=color.red,     # bind = Funcion al clickear
       #textcolor=color.white,pos=(scene.title_anchor), bind=sys.exit)

nDesp=40
centroide = [0,0]
tPosInicial = (nDesp,0,0)

posD = my_Escenario() 
Tambor1, Tambor2, Tambor3, Tambor4 = my_Tambores() 

tPosInicial1 = vector(ra.randint(-830,830),40,ra.randint(-430,430)) 
#tPosInicial2 = vector(ra.randint(-830,830),40,ra.randint(-430,430))
#tPosInicial3 = vector(ra.randint(-830,830),40,ra.randint(-430,430))
#tPosInicial4 = vector(ra.randint(-830,830),40,ra.randint(-430,430))

Robot1 = robotPrueba(0,0) ; ultPosX = Robot1.pos.x ; ultPosZ = Robot1.pos.z
Robot2 = robotPrueba(0,0) ; ultPosX_2 = Robot2.pos.x ; ultPosZ_2 = Robot2.pos.z
#Robot3 = my_Robot(tPosInicial3,nDesp)
#Robot4 = my_Robot(tPosInicial4,nDesp)

#----------------------------------------------------------------------------#

while True:
    xPosRobot, yPosRobot, phi1, xTambor, yTambor,velo = LeyControl(ultPosX, ultPosZ, Tambor1.pos.x, Tambor1.pos.z, nDesp)
    xPosRobot_2, yPosRobot_2, phi2, xTambor_2, yTambor_2, velo2 = LeyControl(ultPosX_2, ultPosZ_2, Tambor2.pos.x, Tambor2.pos.z, nDesp)
    print(len(xPosRobot))
    print(velo)
    Busqueda = 0
    Bus2 = 0
    while (Busqueda < len(xPosRobot) and Bus2 < len(xPosRobot_2)):
        if xPosRobot[Busqueda] >= 950 or xPosRobot[Busqueda] <= -950 or yPosRobot[Busqueda] >= 450 or yPosRobot[Busqueda] <= -450:
            Busqueda=len(xPosRobot)
        elif xPosRobot_2[Bus2] >= 950 or xPosRobot_2[Bus2] <= -950 or yPosRobot_2[Bus2] >= 450 or yPosRobot_2[Bus2] <= -450:
            Bus2=len(xPosRobot_2)
        else:
            #if (phi1[cc]<0):
            #    Robot1.rotate(axis=vector(0,1,0),angle=phi1[cc])
            #else:
            #    Robot1.rotate(axis=vector(0,1,0), angle=phi1[cc])
            Robot1.pos.x = xPosRobot[Busqueda]
            Robot1.pos.z = yPosRobot[Busqueda]
            ultPosZ = yPosRobot[Busqueda]
            ultPosX = xPosRobot[Busqueda]
            Busqueda = Busqueda+1

            Robot2.pos.x = xPosRobot_2[Bus2]
            Robot2.pos.z = yPosRobot_2[Bus2]
            ultPosZ_2 = yPosRobot_2[Bus2]
            ultPosX_2 = xPosRobot_2[Bus2]
            Bus2 = Bus2+1
            time.sleep(0.015)
        # if Busqueda == len(xPosRobot):
        #     RobotT1 = compound([Robot1,Tambor1])
        #     RobotT1.rotate(axis=vector(0,1,0),angle=135)
    #######################################################
    # Robot1c = compound([Robot1,Tambor1]) ; ultPosXc = Robot1c.pos.x ; ultPosZc = Robot1c.pos.z
    # xPosRobotc, yPosRobotc, phi1, xDestiny, yDestiny = LeyControl(ultPosXc, ultPosZc, -900, -400, nDesp)
    # cc = 0
    # while (cc < len(xPosRobotc)):
    #     if xPosRobotc[cc] >= 950 or xPosRobotc[cc] <= -950 or yPosRobotc[cc] >= 450 or yPosRobotc[cc] <= -450:
    #         cc=len(xPosRobotc)
    #     else:
    #         #if (phi1[cc]<0):
    #         #    Robot1.rotate(axis=vector(0,1,0),angle=phi1[cc])
    #         #else:
    #         #    Robot1.rotate(axis=vector(0,1,0), angle=phi1[cc])
    #         if xPosRobotc[cc] == xDestiny and yPosRobotc == yDestiny:
    #             Robot1c.rotate(axis=vector(0,1,0),angle=phi1[cc])
    #         Robot1c.pos.x = xPosRobotc[cc]
    #         Robot1c.pos.z = yPosRobotc[cc]
    #         ultPosZ = yPosRobotc[cc]
    #         ultPosX = xPosRobotc[cc]
    #         cc = cc+1
    
    rate(100)
