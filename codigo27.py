from __future__ import division
from ast import Break
from turtle import width
import matplotlib.pyplot as plt
import numpy as np
from visual import *
import random as ra
import math
import time as ti
#---------------------------Creacion del mundo-----------------------------------------#
def my_Escenario():    
    Ventana = display(title='Robot Unidesplazado', x=50, y=0, width=1280, height=720, center=(0,0,0))
    
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

    return 

def my_Tambores(nTamCoords):
    fTambor = frame(pos=nTamCoords)
    fTambor.Tambor = cylinder(frame=fTambor, axis=(0,70,0), radius=40, color=color.cyan) 
    #if nTamCoords == tTamCoords1:
    #    lTambor = label(pos=cTambor.pos, text='Tambor 1')

    return fTambor

def my_Tambores():

    fTambor_1 = frame(pos=vector(700,0,-300))
    fTambor_2 = frame(pos=vector(700,0,300))
    fTambor_3 = frame(pos=vector(-700,0,-300))
    fTambor_4 = frame(pos=vector(-700,0,300))

    #Tambor_1  = cylinder( pos=vector(ra.randint(0,900),0,ra.randint(-400,0)), axis=vector(0,60,0), radius=30, color=color.blue) 
    #Tambor_2  = cylinder( pos=vector(ra.randint(0,900),0,ra.randint(0,400)), axis=vector(0,60,0), radius=30, color=color.blue)
    #Tambor_3  = cylinder( pos=vector(ra.randint(-900,0),0,ra.randint(-400,0)), axis=vector(0,60,0), radius=30, color=color.blue)
    #Tambor_4  = cylinder( pos=vector(ra.randint(-900,0),0,ra.randint(0,400)), axis=vector(0,60,0), radius=30, color=color.blue)
    
    fTambor_1.Tambor  = cylinder(frame=fTambor_1, axis=vector(0,60,0), radius=30, color=color.blue) 
    fTambor_2.Tambor  = cylinder(frame=fTambor_2, axis=vector(0,60,0), radius=30, color=color.blue)
    fTambor_3.Tambor  = cylinder(frame=fTambor_3, axis=vector(0,60,0), radius=30, color=color.blue)
    fTambor_4.Tambor  = cylinder(frame=fTambor_4, axis=vector(0,60,0), radius=30, color=color.blue)  
    
    return fTambor_1, fTambor_2, fTambor_3, fTambor_4
#---------------------------Definicion del Robot---------------------------------------#
def my_Robot(nCoords, nDesp):
    fBase = frame(pos=nCoords)
    fArms = frame(frame=fBase)
    #Definicion de frames central y compartimiento
    fBase.Base = box(frame=fBase, pos=(0-nDesp,30,00),size=(150,30,110),color=color.white)
    fBase.Lateral_1 = box(frame=fBase, pos=(-8,55,00), size=(50,20,110),color=color.red)
    fBase.Lateral_2 = box(frame=fBase, pos=(-60,55,50), size=(150,20,10),color=color.red)
    fBase.Lateral_3 = box(frame=fBase, pos=(-60,55,-50), size=(150,20,10),color=color.red)
    fBase.Lateral_4 = box(frame=fBase, pos=(-130,55,00), size=(10,20,110),color=color.red)
    #Definicion de ruedas
    fBase.Rueda_1 = cylinder(frame=fBase,pos=(50-nDesp,5,35),radius=15,axis=(00,00,20),color = color.blue) 
    fBase.Rueda_2 = cylinder(frame=fBase,pos=(50-nDesp,5,-55),radius=15,axis=(00,00,20),color = color.blue)
    fBase.Castor  = cylinder(frame=fBase,pos=(-110,5,-13),radius=15,axis=(00,00,20),color = color.blue)
    #Brazos

    fArms.Articulacion_1 = box(frame=fArms, pos=(50-nDesp, 40,60), size=(20,40,10), color=color.orange)
    fArms.Brazo_1 = box(frame=fArms, pos=(40, 25,60), size=(110,10,10), color=color.orange)
    fArms.Articulacion_2 = box(frame=fArms, pos=(+50-nDesp, 40,-60), size=(20,40,10), color=color.orange)
    fArms.Brazo_2 = box(frame=fArms, pos=(40, 25,-60), size=(110,10,10), color=color.orange)
    fBase.Label = label(frame=fBase,text='Punto de Control', space=10,height=15, border=4,yoffset=50,font='sans', pos=(nDesp,30,00))
    #fBase.axis = (ra.randint(-10,10), 00, ra.randint(-10,10))

    return fBase, fArms

def robotPrueba(x,y):
    
    # Frames Principales
    fCuerpo = frame(pos=(x,10,y))
    fBrazos = frame(frame=fCuerpo)
    
    #centro = cylinder( pos=vector(x,0,y), axis=vector(0,200,0), radius=3, color=color.yellow) 
    #Definicion de frames central y compartimiento
    fCuerpo.Base = box(frame=fCuerpo, pos=vector(x-90,25,y),size=vector(100,15,80),color=color.red)
    
    # Cuerpo del Robot
    #                                  size (largo , alto , ancho)
    #Lado de adelante
    fCuerpo.Lado1 = box(frame=fCuerpo, pos=vector(x-40,31,y), size=vector(50,28,80),color=color.red)
    # Lado derecho
    fCuerpo.Lado2 = box(frame=fCuerpo, pos=vector(x-90,35,y+35), size=vector(100,20,10),color=color.red)
    # Lado izquierdo
    fCuerpo.Lado3 = box(frame=fCuerpo, pos=vector(x-90,35,y-35), size=vector(100,20,10),color=color.red)
    #Lado de atras
    fCuerpo.Lado4 = box(frame=fCuerpo, pos=vector(x-135,35,y), size=vector(10,20,78),color=color.red)
    
    # Ruedas del Robot
    Rueda1 = cylinder(frame=fCuerpo, pos=vector(x-40,15,y+22),radius=15,axis=vector(00,00,15),color = color.black) 
    Rueda2 = cylinder(frame=fCuerpo, pos=vector(x-40,15,y-36),radius=15,axis=vector(00,00,15),color = color.black)
    RuedaCastor  = cylinder(frame=fCuerpo, pos=vector(x-125,15,y-8),radius=15,axis=vector(00,00,15),color = color.black)
    #                                        , y (+)derecha (-)izquierda
    
    # BRAZOS
    # pos ( +adelante- -atras, arriba, a los lados hacia afuera o hacia dentro)
    #Brazo derecho
    fBrazos.AnteBrazoR = box(frame=fBrazos, pos=vector(x-35, 31,y+40), size=vector(25,15,10), color=color.blue)
    fBrazos.BrazoR = box(frame=fBrazos, pos=vector(x+2, 27,y+40), size=vector(100,10,8), color=color.blue)
    
    #Brazo izquierdo
    fBrazos.AnteBrazoL = box(frame=fBrazos, pos=vector(x-35, 31,y-40), size=vector(25,15,10), color=color.blue)
    fBrazos.BrazoL = box(frame=fBrazos, pos=vector(x+2, 27,y-40), size=vector(100,10,8), color=color.blue)

    #cLabel = label(text='Punto de Control', space=10,height=15, border=4,yoffset=30,font='sans', pos=cRobot.pos)
    #robotF.axis = vector(100, 0, 100)
    #Brazos.axis = robotF.axis

    return fCuerpo , fBrazos

#---------------------------Implementacion del modelo cinematico-----------------------#
def LeyControl(UltPosX, UltPosZ, PosDeseada, nDesp): 
    ts = 0.1; tf = 30 ; T = np.arange(0,tf+ts,ts) ; N = len(T)
    # Seteo de arreglos de ceros para las coordendas y angulos
    xc  = np.zeros(len(T)+1) ; zc  = np.zeros(len(T)+1)
    ph  = np.zeros(len(T)+1) 
    xp  = np.zeros(len(T)+1) ; zp  = np.zeros(len(T)+1)
    xr  = np.zeros(len(T)+1) ; zr  = np.zeros(len(T)+1)
    u   = np.zeros(len(T)+1) ; w   = np.zeros(len(T)+1)
    xre = np.zeros(len(T)+1) ; zre = np.zeros(len(T)+1)

    xc[0] = UltPosX ; zc[0]=UltPosZ
    ph[0] = math.sin(math.radians(4))

    xr[0] = xc[0] + nDesp*math.cos(ph[0])
    zr[0] = zc[0] + nDesp*math.sin(ph[0])
    xrD = PosDeseada[0] ; zrD = PosDeseada[2]

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
        K = np.array([[1.5, 0],
                      [0, 1.5]])

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
    
    return(xc, zc, ph)

#-------------------------------Variables Iniciales-------------------------------------#

#---------------------Llamado de Robots y Tambores---------------------------#
#my_Escenario() 

nDesp=1
centroide = [0,0]
tPosInicial = (nDesp,0,0)

posD = my_Escenario() 
Tambor1, Tambor2, Tambor3, Tambor4 = my_Tambores() 

tPosInicial1 = vector(ra.randint(-830,830),40,ra.randint(-430,430)) 
#tPosInicial2 = vector(ra.randint(-830,830),40,ra.randint(-430,430))
#tPosInicial3 = vector(ra.randint(-830,830),40,ra.randint(-430,430))
#tPosInicial4 = vector(ra.randint(-830,830),40,ra.randint(-430,430))

Robot1 , Brazos1 = robotPrueba(0,0)
rPOSx = Robot1.pos.x
rPOSz = Robot1.pos.z
#Robot2 = robotPrueba(0,0) ; ultPosX_2 = Robot2.pos.x ; ultPosZ_2 = Robot2.pos.z
#Robot3 = my_Robot(tPosInicial3,nDesp)
#Robot4 = my_Robot(tPosInicial4,nDesp)

#----------------------------------------------------------------------------#

while True:
    posX1, posZ1, phi1 = LeyControl(rPOSx, rPOSz, Tambor1.pos, nDesp)
    Busqueda = 0
    while (Busqueda < len(posX1)):
        if posX1[Busqueda] >= 1100 or posX1[Busqueda] <= -1100 or posZ1[Busqueda] >= 600 or posZ1[Busqueda] <= -600:
            Busqueda=len(posX1)
        else:
            Robot1.pos.x = posX1[Busqueda]
            Robot1.pos.z = posZ1[Busqueda]
            UltPosX = posX1[Busqueda]
            UltPosZ = posZ1[Busqueda]
            Busqueda = Busqueda+1
        if Robot1.pos.x == Tambor1.pos[0]:
            print("hoaaa")
        #ti.sleep(0.2)  <- ESTA COSA MATA MI PC XD, PERO HACE QUE EL PROGRAMA NO ME RESPONDA :C **WARNING**
            
    rate(120)


# UltimaPos1 = (ra.randint(-930,930),12,ra.randint(-450,450)) ; UltPosX = UltimaPos1[0] ; UltPosZ = UltimaPos1[2]
# #tPosInicial2 = vector(ra.randint(-830,830),40,ra.randint(-430,430))
# #tPosInicial3 = vector(ra.randint(-830,830),40,ra.randint(-430,430))
# #tPosInicial4 = vector(ra.randint(-830,830),40,ra.randint(-430,430))

# TamCoords1 = (ra.randint(-930,930),12,ra.randint(-450,450)) 
# #tTamCoords2 = vector(ra.randint(-930,930),45,ra.randint(-450,450))
# #tTamCoords3 = vector(ra.randint(-930,930),45,ra.randint(-450,450))
# #tTamCoords4 = vector(ra.randint(-930,930),45,ra.randint(-450,450))

# Robot1, Brazos1 = my_Robot(UltimaPos1,nDesp)  #ultPosX = Robot1.pos.x ; ultPosZ = Robot1.pos.z
# #Robot2 = my_Robot(tPosInicial2,nDesp)
# #Robot3 = my_Robot(tPosInicial3,nDesp)
# #Robot4 = my_Robot(tPosInicial4,nDesp)

# Tambor1 = my_Tambores(TamCoords1) 
# #Tambor2 = my_Tambores(tTamCoords2)
# #Tambor3 = my_Tambores(tTamCoords3)
# #Tambor4 = my_Tambores(tTamCoords4)
#----------------------------------------------------------------------------#

# while True:
#     posX1, posZ1, phi1 = logicaMov(UltPosX, UltPosZ, TamCoords1, nDesp)
#     cc = 0
#     while (cc < len(posX1)):
#         if posX1[cc] >= 1100 or posX1[cc] <= -1100 or posZ1[cc] >= 600 or posZ1[cc] <= -600:
#             cc=len(posX1)
#         else:
#             Robot1.pos.x = posX1[cc]
#             Robot1.pos.z = posZ1[cc]
#             UltPosX = posX1[cc]
#             UltPosZ = posZ1[cc]
#             cc = cc+1
#         #if Robot1.pos.x == TamCoords1[0]:
#         #    print("hoaaa")
            
#     rate(120)

