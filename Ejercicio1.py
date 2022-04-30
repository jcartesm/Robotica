#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from ast import Break
from operator import le
#from tkinter import font
from turtle import width
import matplotlib.pyplot as plt
import numpy as np
from visual import *
import random as ra
import math
import time as ti

#---------------------------------Ajuste del Escenario--------------------------------
# Esta función crea el escenario por donde se moveran los robot.
# Output:
#       - Un arreglo con las posiciones de las 4 metas donde se llevarán los tambores
def my_Escenario():    
    Ventana = display(title='En busqueda del Tambor Dorado', x=50, y=0, width=1280, height=720, center=(0,0,0))
    
    Superficie= box(pos=vector(0,0,0),size=vector(2000,2,1000), color = color.white)
    BordeCorto_1 = box(pos=vector(+1000,0,0),size=vector(40,40,1000), color = color.gray(0.5))
    BordeCorto_2 = box(pos=vector(-1000,0,0),size=vector(40,40,1000), color = color.gray(0.5))
    Bordelargo_1 = box(pos=vector(0,0,+500),size=vector(2000,40,40), color = color.gray(0.5))
    Bordelargo_2 = box(pos=vector(0,0,-500),size=vector(2000,40,40), color = color.gray(0.5))
    
    D_1 = box(pos=vector(-900,5,-400), size=vector(75,10,75), color = color.yellow)
    D_2 = box(pos=vector(-900,5,400), size=vector(75,10,75), color = color.yellow)
    D_3 = box(pos=vector(900,5,-400), size=vector(75,10,75), color = color.yellow)
    D_4 = box(pos=vector(900,5,400), size=vector(75,10,75), color = color.yellow)

    # arreglo de posiciones de espacio para dejar tambor 
    aD = [D_1.pos, D_2.pos, D_3.pos, D_4.pos]

    return aD
#---------------------------------Creacion de los Tambores--------------------------------
# Esta función genera tambores en posiciones aleatorias dentro de cada cuadrante
# de la superficie donde se movera el robot.
# Output:
#       - Los 4 Frames de los Tambores posicionados aleatoriamente

def my_Tambores():

    fTambor_1 = frame(pos=vector(ra.randint(0,700),0,ra.randint(-300,0)))
    fTambor_2 = frame(pos=vector(ra.randint(0,900),0,ra.randint(0,300)))
    fTambor_3 = frame(pos=vector(ra.randint(-900,0),0,ra.randint(-300,0)))
    fTambor_4 = frame(pos=vector(ra.randint(-700,0),0,ra.randint(0,300)))
    
    fTambor_1.Tambor  = cylinder(frame=fTambor_1, axis=vector(0,60,0), radius=30, color=color.blue) 
    fTambor_2.Tambor  = cylinder(frame=fTambor_2, axis=vector(0,60,0), radius=30, color=color.blue)
    fTambor_3.Tambor  = cylinder(frame=fTambor_3, axis=vector(0,60,0), radius=30, color=color.blue)
    fTambor_4.Tambor  = cylinder(frame=fTambor_4, axis=vector(0,60,0), radius=30, color=color.blue)  
    
    return fTambor_1, fTambor_2, fTambor_3, fTambor_4

#---------------------------------Creación de Robot's---------------------------------
# Esta función crea un Robot a partir de coordenadas donde sera posicionado en el comienzo
# de la ejecucion del programa.
# Imput:
#       - Una poscion en el Eje X donde se situará el Robot
#       - Una poscion en el Eje Z donde se situará el Robot (Eje Z funciona como el Eje Y)
# Output:
#       - El Frame del cuerpo del Robot
#       - El Frame de los brazos del Robot, para psoteriormente unirlos con el Frame del Barril

def RobotMaestro(x,y):
    
    # Frames Principales
    fCuerpo = frame(pos=(x,10,y))
    fBrazos = frame(frame=fCuerpo)

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


    return fCuerpo , fBrazos
    

#---------------------------Implementacion del modelo cinematico-----------------------#
# Este funcion se implementa el modelo cinematico de la ley de control visto en clases:
# Imput:
#       - Ultima posicion en eje X del (UltPosX)
#       - Ultima posicion en eje Z del (UltPosZ) "esto es porque se trabaja con"
#         con un plano 3D y se reemplazo el Y por el Z.
#       - La posicion deseada a la que se quiere llegar (PosDeseada)
#       - El valor de la distancia desde el eje de las ruedas al punto de control (nDesp)
#       - un numero deciaml o entero para la matriz de ganancia (mg)
# Output:
#       - Posicion final en eje X (xc)
#       - Posicion final en eje Z (zc)
#       - Angulo phi (ph)
#       - Arreglo de errores eje Z (zre)
#       - Arreglo de errores eje X (xre)
#       - Arreglo de tiempo de ejecucion (T)
#       - Arreglo de velocidad (u)
#       - Arreglo de Velocidad Angular (w)

def LeyControl(UltPosX, UltPosZ, PosDeseada, nDesp, mg): 
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
        K = np.array([[mg, 0],
                      [0, mg]])

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
    
    return(xc, zc, ph, xre, zre, T, u, w)

#-------------------------------Variables Iniciales-------------------------------------#

nDesp=0.9
centroide = [0,0]
tPosInicial = (nDesp,0,0)

#---------------------Creacion del escenario y ploteo de tambores---------------------------#

posD = my_Escenario() 
ra.shuffle(posD)
Tambor1, Tambor2, Tambor3, Tambor4 = my_Tambores() 
Tambores = [Tambor1, Tambor2, Tambor3, Tambor4]
ra.shuffle(Tambores)

#---------------------Ceacion de Objetos Robot, del cual obtenemos el cuerpo y los brazoz---------------------------#

Robot_1 , Brazos_1 = RobotMaestro(0,0)
rPOSx = Robot_1.pos.x
rPOSz = Robot_1.pos.z
TagR1 = label(pos=(Robot_1.pos.x, 150, Robot_1.pos.z), text='Robot 1', font='sans', height=10, color=color.green)

Robot_2 , Brazos_2 = RobotMaestro(0,0)
rPOSx_2 = Robot_2.pos.x
rPOSz_2 = Robot_2.pos.z
TagR2 = label(pos=(Robot_2.pos.x, 150, Robot_2.pos.z), text='Robot 2', font='sans', height=10, color=color.green)

Robot_3 , Brazos_3 = RobotMaestro(0,0)
rPOSx_3 = Robot_3.pos.x
rPOSz_3 = Robot_3.pos.z
TagR3 = label(pos=(Robot_3.pos.x, 150, Robot_3.pos.z), text='Robot 3', font='sans', height=10, color=color.green)

Robot_4 , Brazos_4 = RobotMaestro(0,0)
rPOSx_4 = Robot_4.pos.x
rPOSz_4 = Robot_4.pos.z
TagR4 = label(pos=(Robot_4.pos.x, 150, Robot_4.pos.z), text='Robot 4', font='sans', height=10, color=color.green)


#----------------------------------------------------------------------------#
carga1 = 0

if (abs(Brazos_1.pos.x) <= abs(Tambor1.pos.x)):

    posX1, posZ1, phi1, eX, eZ, temp, vel_1, velA_1 = LeyControl(rPOSx, rPOSz, Tambores[0].pos, nDesp, 1.7)
    posX_2, posZ_2, phi_2, eX_2,eZ_2, temp_2, vel_2, velA_2 = LeyControl(rPOSx_2, rPOSz_2, Tambores[1].pos, nDesp, 1.7)
    posX_3, posZ_3, phi_3, eX_3, eZ_3, temp_3, vel_3, velA_3 = LeyControl(rPOSx_3, rPOSz_3, Tambores[2].pos, nDesp, 1.7)
    posX_4, posZ_4, phi_4, eX_4, eZ_4, temp_4, vel_4, velA_4 = LeyControl(rPOSx_4, rPOSz_4, Tambores[3].pos, nDesp, 1.7)

    BusQ = 0

    while (BusQ < len(posX1) ):
        if posX1[BusQ] >= 1100 or posX1[BusQ] <= -1100 or posZ1[BusQ] >= 600 or posZ1[BusQ] <= -600:
            BusQ=len(posX1)
        else:
            Robot_1.pos.x = posX1[BusQ]
            Robot_1.pos.z = posZ1[BusQ]
            Robot_1.axis = vector(Tambores[0].pos)
            TagR1.pos = (Robot_1.pos.x, 150, Robot_1.pos.z)
            UltPosX = posX1[BusQ]
            UltPosZ = posZ1[BusQ]

            Robot_2.pos.x = posX_2[BusQ]
            Robot_2.pos.z = posZ_2[BusQ]
            Robot_2.axis = vector(Tambores[1].pos)
            TagR2.pos = (Robot_2.pos.x, 150, Robot_2.pos.z)
            UltPosX_2 = posX_2[BusQ]
            UltPosZ_2 = posZ_2[BusQ]

            Robot_3.pos.x = posX_3[BusQ]
            Robot_3.pos.z = posZ_3[BusQ]
            Robot_3.axis = vector(Tambores[2].pos)
            TagR3.pos = (Robot_3.pos.x, 150, Robot_3.pos.z)
            UltPosX_3 = posX_3[BusQ]
            UltPosZ_3 = posZ_3[BusQ]

            Robot_4.pos.x = posX_4[BusQ]
            Robot_4.pos.z = posZ_4[BusQ]
            Robot_4.axis = vector(Tambores[3].pos)
            TagR4.pos = (Robot_4.pos.x, 150, Robot_4.pos.z)
            UltPosX_4 = posX_4[BusQ]
            UltPosZ_4 = posZ_4[BusQ]            
            
            rate(1)
        BusQ = BusQ + 1
    carga1 = 1

    
    # Levanta el tambor si llega al destino
if carga1 == 1:
    
    Tambores[0].frame = Brazos_1
    Tambores[0].pos = (40,0,0)

    Tambores[1].frame = Brazos_2
    Tambores[1].pos = (40,0,0)

    Tambores[2].frame = Brazos_3
    Tambores[2].pos = (40,0,0)

    Tambores[3].frame = Brazos_4
    Tambores[3].pos = (40,0,0)    

    # Animacion de la rotacion de los brazos 
    rot = 0
    while rot < 4:
        Brazos_1.rotate(angle=(0.45*math.pi)/2, axis=(0,0,1), origin=(-30,30,0))
        Brazos_2.rotate(angle=(0.45*math.pi)/2, axis=(0,0,1), origin=(-30,30,0))
        Brazos_3.rotate(angle=(0.45*math.pi)/2, axis=(0,0,1), origin=(-30,30,0))
        Brazos_4.rotate(angle=(0.45*math.pi)/2, axis=(0,0,1), origin=(-30,30,0))    
        rot = rot + 1
        rate(20)

    carga1 = 2
if carga1 == 2:

    posX1, posZ1, phi1, eXp, eZp, temp_p, velP_1, velPA_1  = LeyControl(Robot_1.pos.x, Robot_1.pos.z, posD[0], nDesp, 1.7)
    posX_2, posZ_2, phi_2, eXp_2, eZp_2, temp_2_p, velP_2, velPA_2  = LeyControl(Robot_2.pos.x, Robot_2.pos.z, posD[1], nDesp, 1.7)
    posX_3, posZ_3, phi_3, eXp_3, eZp_3, temp_3_p, velP_3, velPA_3  = LeyControl(Robot_3.pos.x, Robot_3.pos.z, posD[2], nDesp, 1.7)
    posX_4, posZ_4, phi_4, eXp_4, eZp_4, temp_4_p, velP_4, velPA_4  = LeyControl(Robot_4.pos.x, Robot_4.pos.z, posD[3], nDesp, 1.7)    

    BusQ = 0
 
    while (BusQ < len(posX1)):
        if posX1[BusQ] >= 1100 or posX1[BusQ] <= -1100 or posZ1[BusQ] >= 600 or posZ1[BusQ] <= -600:
            BusQ=len(posX1)
        else:
            Robot_1.pos.x = posX1[BusQ]
            Robot_1.pos.z = posZ1[BusQ]
            Robot_1.axis = vector(posD[0])
            TagR1.pos = (Robot_1.pos.x, 150, Robot_1.pos.z)
            UltPosX = posX1[BusQ]
            UltPosZ = posZ1[BusQ]

            Robot_2.pos.x = posX_2[BusQ]
            Robot_2.pos.z = posZ_2[BusQ]
            Robot_2.axis = vector(posD[1])
            TagR2.pos = (Robot_2.pos.x, 150, Robot_2.pos.z)
            UltPosX_2 = posX_2[BusQ]
            UltPosZ_2 = posZ_2[BusQ]

            Robot_3.pos.x = posX_3[BusQ]
            Robot_3.pos.z = posZ_3[BusQ]
            Robot_3.axis = vector(posD[2])
            TagR3.pos = (Robot_3.pos.x, 150, Robot_3.pos.z)
            UltPosX_3 = posX_3[BusQ]
            UltPosZ_3 = posZ_3[BusQ]

            Robot_4.pos.x = posX_4[BusQ]
            Robot_4.pos.z = posZ_4[BusQ]
            Robot_4.axis = vector(posD[3])
            TagR4.pos = (Robot_4.pos.x, 150, Robot_4.pos.z)
            UltPosX_4 = posX_4[BusQ]
            UltPosZ_4 = posZ_4[BusQ]            


            BusQ = BusQ + 1

  
            rate(1) 
    
    # Animacion de la rotacion de los brazos  
    rot = 0    
    while rot < 4:
        Brazos_1.rotate(angle=-(0.45*math.pi)/2, axis=(0,0,1), origin=(-30,30,0))
        Brazos_2.rotate(angle=-(0.45*math.pi)/2, axis=(0,0,1), origin=(-30,30,0))
        Brazos_3.rotate(angle=-(0.45*math.pi)/2, axis=(0,0,1), origin=(-30,30,0))    
        Brazos_4.rotate(angle=-(0.45*math.pi)/2, axis=(0,0,1), origin=(-30,30,0)) 
        rot = rot + 1
        rate(20)
    carga1 = 3



################### GRAFICAS ####################

# 
# Tratamiento de los arreglos haciendolos positivos para obtener graficas descenentes y 
# observar de mejor manera la disminucion del error

ts = 0.1; tf = 60 ; tempo = np.arange(0,tf+ts,ts)
for i in range(len(eX)):
    eZ[i] = abs(eZ[i])
    eX[i] = abs(eX[i])
    eXp[i] = abs(eXp[i])
    eZp[i] = abs(eZp[i])         
    eZ_2[i] = abs(eZ_2[i])
    eX_2[i] = abs(eX_2[i])
    eZp_2[i] = abs(eZp_2[i])
    eXp_2[i] = abs(eXp_2[i]) 
    eX_3[i] = abs(eX_3[i])
    eZ_3[i] = abs(eZ_3[i])
    eZp_3[i] = abs(eZp_3[i])
    eXp_3[i] = abs(eXp_3[i])   
    eZ_4[i] = abs(eZ_4[i])
    eX_4[i] = abs(eX_4[i])
    eZp_4[i] = abs(eZp_4[i])
    eXp_4[i] = abs(eXp_4[i])   
    vel_1[i] = abs(vel_1[i])
    vel_2[i] = abs(vel_2[i])
    vel_3[i] = abs(vel_3[i])
    vel_4[i] = abs(vel_4[i])
    velA_1[i] = abs(velA_1[i])
    velA_2[i] = abs(velA_2[i])
    velA_3[i] = abs(velA_3[i])
    velA_4[i] = abs(velA_4[i])


arrXF_1 = np.append(eX,eXp)
arrZF_1 = np.append(eZ,eZp)
arrX_1 = np.delete(arrXF_1, [588,599,600])
arrZ_1 = np.delete(arrZF_1, [588,599,600])

arrXF_2 = np.append(eX_2,eXp_2)
arrZF_2 = np.append(eZ_2,eZp_2)
arrX_2 = np.delete(arrXF_2, [588,599,600])
arrZ_2 = np.delete(arrZF_2, [588,599,600])

arrXF_3 = np.append(eX_3,eXp_3)
arrZF_3 = np.append(eZ_3,eZp_3)
arrX_3 = np.delete(arrXF_3, [588,599,600])
arrZ_3 = np.delete(arrZF_3, [588,599,600])

arrXF_4 = np.append(eX_4,eXp_4)
arrZF_4 = np.append(eZ_4,eZp_4)
arrX_4 = np.delete(arrXF_4, [588,599,600])
arrZ_4 = np.delete(arrZF_4, [588,599,600])

arPX_1 = np.delete(posX1, 300)
arPX_2 = np.delete(posX_2, 300)
arPX_3 = np.delete(posX_3, 300)
arPX_4 = np.delete(posX_4, 300)

arPZ_1 = np.delete(posZ1, 300)
arPZ_2 = np.delete(posZ_2, 300)
arPZ_3 = np.delete(posZ_3, 300)
arPZ_4 = np.delete(posZ_4, 300)

arV_1 = np.delete(vel_1, 300)
arV_2 = np.delete(vel_2, 300)
arV_3 = np.delete(vel_3, 300)
arV_4 = np.delete(vel_4, 300)

arVA_1 = np.delete(velA_1, 300)
arVA_2 = np.delete(velA_2, 300)
arVA_3 = np.delete(velA_3, 300)
arVA_4 = np.delete(velA_4, 300)

# 
#   Aqui creamos las figuras y le asignamos una variable a los subplots para luego plotear
#   de acuerdo a esta variable en cada sector designado como matriz

fig_E, ax_E = plt.subplots(nrows=2, ncols=2, figsize=(9,9))
plt.suptitle("ERRORES DE LOS 4 ROBOTS")

fig_V, ax_V = plt.subplots(nrows=2, ncols=2, figsize=(9,9))
plt.suptitle("VELOCIDAD")

fig_P, ax_P = plt.subplots(nrows=2, ncols=2, figsize=(9,9))
plt.suptitle("POSICION")

fig_acele, ax_acele = plt.subplots(nrows=2, ncols=2, figsize=(9,9))
plt.suptitle("ACELERACION")

fig_VA, ax_VA = plt.subplots(nrows=2, ncols=2, figsize=(9,9))
plt.suptitle("VELOCIDAD ANGULAR")

fig_PA, ax_PA = plt.subplots(nrows=2, ncols=2, figsize=(9,9))
plt.suptitle("POSICION ANGULAR")

################### VENTANA DE ERROR #################### 

#   En este apartado de grafica el error obtenido de la funcion de ley de control
#   en donde se ve reflejado como este va disminuyendo mientras se acerca a su  
#   destino

ax_E[0, 0].plot(tempo,arrX_1,'b',linewidth = 2, label='error X')
ax_E[0, 0].plot(tempo,arrZ_1,'r',linewidth = 2,  label='error Z')
ax_E[0, 0].legend(loc='upper right')
ax_E[0, 0].set_xlabel('Tiempo [s]')
ax_E[0, 0].set_ylabel('Error [m]')
ax_E[0, 0].set_title("Robot I")
ax_E[0, 0].grid()

ax_E[0, 1].plot(tempo,arrX_2,'b',linewidth = 2, label='error X')
ax_E[0, 1].plot(tempo,arrZ_2,'r',linewidth = 2,  label='error Z')
ax_E[0, 1].legend(loc='upper right')
ax_E[0, 1].set_xlabel('Tiempo [s]')
ax_E[0, 1].set_ylabel('Error [m]')
ax_E[0, 1].set_title("Robot II")
ax_E[0, 1].grid()

ax_E[1, 0].plot(tempo,arrX_3,'b',linewidth = 2, label='error X')
ax_E[1, 0].plot(tempo,arrZ_3,'r',linewidth = 2,  label='error Z')
ax_E[1, 0].legend(loc='upper right')
ax_E[1, 0].set_xlabel('Tiempo [s]')
ax_E[1, 0].set_ylabel('Error [m]')
ax_E[1, 0].set_title("Robot III")
ax_E[1, 0].grid()

ax_E[1, 1].plot(tempo,arrX_4,'b',linewidth = 2, label='error X')
ax_E[1, 1].plot(tempo,arrZ_4,'r',linewidth = 2,  label='error Z')
ax_E[1, 1].legend(loc='upper right')
ax_E[1, 1].set_xlabel('Tiempo [s]')
ax_E[1, 1].set_ylabel('Error [m]')
ax_E[1, 1].set_title("Robot IV")
ax_E[1, 1].grid()

################### VELOCIDAD, ACELERACION, POSISION #################### 

#   En este apartado se grafica la velociad, posicion y aceleracion durante el tiempo 
#   de los 4 robots en la simulacion
# 

#########################################################################
ax_V[0, 0].plot(temp,arV_1,'b',linewidth = 2, label='Velocidad')
ax_V[0, 0].legend(loc='upper right')
ax_V[0, 0].set_xlabel('Tiempo [s]')
ax_V[0, 0].set_ylabel('Distancia [m]')
ax_V[0, 0].set_title("Robot I")
ax_V[0, 0].grid()

ax_V[0, 1].plot(temp,arV_2,'b',linewidth = 2, label='Velocidad')
ax_V[0, 1].legend(loc='upper right')
ax_V[0, 1].set_xlabel('Tiempo [s]')
ax_V[0, 1].set_ylabel('Distancia [m]')
ax_V[0, 1].set_title("Robot II")
ax_V[0, 1].grid()

ax_V[1, 0].plot(temp,arV_3,'b',linewidth = 2, label='Velocidad')
ax_V[1, 0].legend(loc='upper right')
ax_V[1, 0].set_xlabel('Tiempo [s]')
ax_V[1, 0].set_ylabel('Distancia [m]')
ax_V[1, 0].set_title("Robot III")
ax_V[1, 0].grid()

ax_V[1, 1].plot(temp,arV_4,'b',linewidth = 2, label='Velocidad')
ax_V[1, 1].legend(loc='upper right')
ax_V[1, 1].set_xlabel('Tiempo [s]')
ax_V[1, 1].set_ylabel('Distancia [m]')
ax_V[1, 1].set_title("Robot IV")
ax_V[1, 1].grid()

#####################################################################

ax_P[0, 0].plot(temp,arPX_1,'b',linewidth = 2, label='Posicion X')
ax_P[0, 0].plot(temp,arPZ_1,'r',linewidth = 2, label='Posicion Z')
ax_P[0, 0].legend(loc='upper right')
ax_P[0, 0].set_xlabel('Tiempo [s]')
ax_P[0, 0].set_ylabel('Posicion [m]')
ax_P[0, 0].set_title("Robot I")
ax_P[0, 0].grid()

ax_P[0, 1].plot(temp,arPX_2,'b',linewidth = 2, label='Posicion X')
ax_P[0, 1].plot(temp,arPZ_2,'r',linewidth = 2, label='Posicion Z')
ax_P[0, 1].legend(loc='upper right')
ax_P[0, 1].set_xlabel('Tiempo [s]')
ax_P[0, 1].set_ylabel('Posicion [m]')
ax_P[0, 1].set_title("Robot II")
ax_P[0, 1].grid()

ax_P[1, 0].plot(temp,arPX_3,'b',linewidth = 2, label='Posicion X')
ax_P[1, 0].plot(temp,arPZ_3,'r',linewidth = 2, label='Posicion Z')
ax_P[1, 0].legend(loc='upper right')
ax_P[1, 0].set_xlabel('Tiempo [s]')
ax_P[1, 0].set_ylabel('Posicion [m]')
ax_P[1, 0].set_title("Robot III")
ax_P[1, 0].grid()

ax_P[1, 1].plot(temp,arPX_4,'b',linewidth = 2, label='Posicion X')
ax_P[1, 1].plot(temp,arPZ_4,'r',linewidth = 2, label='Posicion Z')
ax_P[1, 1].legend(loc='upper right')
ax_P[1, 1].set_xlabel('Tiempo [s]')
ax_P[1, 1].set_ylabel('Posicion [m]')
ax_P[1, 1].set_title("Robot IV")
ax_P[1, 1].grid()

#####################################################################

# ax_acele[0, 0].plot(temp,arV_1,'b',linewidth = 2, label='Aceleracion')
ax_acele[0, 0].legend(loc='upper right')
ax_acele[0, 0].set_xlabel('Tiempo [s**2]')
ax_acele[0, 0].set_ylabel('Distancia [m]')
ax_acele[0, 0].set_title("Robot I")
ax_acele[0, 0].grid()

# ax_acele[0, 1].plot(temp,arV_2,'b',linewidth = 2, label='Aceleracion')
ax_acele[0, 1].legend(loc='upper right')
ax_acele[0, 1].set_xlabel('Tiempo [s**2]')
ax_acele[0, 1].set_ylabel('Distancia [m]')
ax_acele[0, 1].set_title("Robot II")
ax_acele[0, 1].grid()

# ax_acele[1, 0].plot(temp,arV_3,'b',linewidth = 2, label='Aceleracion')
ax_acele[1, 0].legend(loc='upper right')
ax_acele[1, 0].set_xlabel('Tiempo [s**2]')
ax_acele[1, 0].set_ylabel('Distancia [m]')
ax_acele[1, 0].set_title("Robot III")
ax_acele[1, 0].grid()

# ax_acele[1, 1].plot(temp,arV_4,'b',linewidth = 2, label='Aceleracion')
ax_acele[1, 1].legend(loc='upper right')
ax_acele[1, 1].set_xlabel('Tiempo [s**2]')
ax_acele[1, 1].set_ylabel('Distancia [m]')
ax_acele[1, 1].set_title("Robot IV")
ax_acele[1, 1].grid()

################### VELOCIDAD Y POSICION ANGULAR #################### 

#  En este apartado se emplea los subplots generados de la tercera figura para graficar la velocidad angular de cada robot
#  medida en radianes/segundos 
# 
# 

ax_VA[0, 0].plot(temp,arVA_1,'b',linewidth = 2, label='Velocidad Angular')
ax_VA[0, 0].legend(loc='upper right')
ax_VA[0, 0].set_xlabel('Tiempo [s]')
ax_VA[0, 0].set_ylabel('w [rad]')
ax_VA[0, 0].set_title("Robot I")
ax_VA[0, 0].grid()

ax_VA[0, 1].plot(temp,arVA_2,'b',linewidth = 2, label='Velocidad Angular')
ax_VA[0, 1].legend(loc='upper right')
ax_VA[0, 1].set_xlabel('Tiempo [s]')
ax_VA[0, 1].set_ylabel('w [Rad]')
ax_VA[0, 1].set_title("Robot II")
ax_VA[0, 1].grid()

ax_VA[1, 0].plot(temp,arVA_3,'b',linewidth = 2, label='Velocidad Angular')
ax_VA[1, 0].legend(loc='upper right')
ax_VA[1, 0].set_xlabel('Tiempo [s]')
ax_VA[1, 0].set_ylabel('w [rad]')
ax_VA[1, 0].set_title("Robot III")
ax_VA[1, 0].grid()

ax_VA[1, 1].plot(temp,arVA_4,'b',linewidth = 2, label='Velocidad Angular')
ax_VA[1, 1].legend(loc='upper right')
ax_VA[1, 1].set_xlabel('Tiempo [s]')
ax_VA[1, 1].set_ylabel('w [rad]')
ax_VA[1, 1].set_title("Robot IV")
ax_VA[1, 1].grid()

########################################################################

# ax_PA[0, 0].plot(temp,arVA_1,'b',linewidth = 2, label='Posicion')
ax_PA[0, 0].legend(loc='upper right')
ax_PA[0, 0].set_xlabel('Tiempo [s]')
ax_PA[0, 0].set_ylabel('Pw')
ax_PA[0, 0].set_title("Robot I")
ax_PA[0, 0].grid()

# ax_PA[0, 1].plot(temp,arVA_2,'b',linewidth = 2, label='Posicion')
ax_PA[0, 1].legend(loc='upper right')
ax_PA[0, 1].set_xlabel('Tiempo [s]')
ax_PA[0, 1].set_ylabel('Pw')
ax_PA[0, 1].set_title("Robot II")
ax_PA[0, 1].grid()

# ax_PA[1, 0].plot(temp,arVA_3,'b',linewidth = 2, label='Posicion')
ax_PA[1, 0].legend(loc='upper right')
ax_PA[1, 0].set_xlabel('Tiempo [s]')
ax_PA[1, 0].set_ylabel('Pw')
ax_PA[1, 0].set_title("Robot III")
ax_PA[1, 0].grid()

# ax_PA[1, 1].plot(temp,arVA_4,'b',linewidth = 2, label='Posicion')
ax_PA[1, 1].legend(loc='upper right')
ax_PA[1, 1].set_xlabel('Tiempo [s]')
ax_PA[1, 1].set_ylabel('Pw')
ax_PA[1, 1].set_title("Robot IV")
ax_PA[1, 1].grid()



plt.show()


