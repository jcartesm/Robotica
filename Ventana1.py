from turtle import pos
from sympy import false, true
from vpython import *
import math
import numpy as np
import serial as se

initialCords = vector(0, 6.5, 0)

scene.width = 800
scene.height = 400
scene.range = 1000
scene.title = "En la Busqueda del Tambor dorado\n"
scene.camera.pos = vector(0,500,2000)

def Ventana():
     Suelo = box(pos=vector(0, 0, 0), size=vector(
         1280, 3, 720), color=color.gray(0.5))

def Robot(x,y):
    Base = box(pos=vector(x,25,y),size=vector(100,30,80),color=color.red)
    
    antena1 =cylinder(pos=vector(x+35,23,y+15),radius=2,axis=vector(0,50,0),color = color.yellow)
    cabezaa1 = sphere(pos=vector(x+35,73,y+15),radius=5,color = color.yellow)
    
    antena2 =cylinder(pos=vector(x+35,23,y-15),radius=2,axis=vector(0,50,0),color = color.yellow)
    cabezaa2 = sphere(pos=vector(x+35,73,y-15),radius=5,color = color.yellow)
    
    ojo1 = box(pos=vector(x+40,25,y+15),size=vector(25,15,20),color=color.white)
    pupila1 = box(pos=vector(x+40,30,y+15),size=vector(25,5,20),color=color.black)
    color1 = cylinder(pos=vector(x+50,23,y+15),radius=5,axis=vector(5,00,0),color = color.black)
    
    ojo2 = box(pos=vector(x+40,25,y-15),size=vector(25,15,20),color=color.white)
    pupila2 = box(pos=vector(x+40,30,y-15),size=vector(25,5,20),color=color.black)
    color2 = cylinder(pos=vector(x+50,23,y-15),radius=5,axis=vector(5,00,0),color = color.black)
    # Ruedas del Robot
    Rueda1 = cylinder(pos=vector(x+40,20,y+40),radius=20,axis=vector(00,00,15),color = color.black) 
    Rueda2 = cylinder(pos=vector(x+40,20,y-55),radius=20,axis=vector(00,00,15),color = color.black)
    Rueda3 = cylinder(pos=vector(x-40,20,y+40),radius=20,axis=vector(00,00,15),color = color.black)
    Rueda4 = cylinder(pos=vector(x-40,20,y-55),radius=20,axis=vector(00,00,15),color = color.black)
    
    robotF = compound([Base,antena1,cabezaa1,antena2,cabezaa2,ojo1,pupila1,color1,
                       ojo2,pupila2,color2,Rueda1,Rueda2,Rueda3,Rueda4])
    robotF.pos.x=x
    robotF.pos.z=y

    return robotF
# def Ventana():
#     Suelo = box(pos=vector(0, 0, 0), size=vector(
#         1280, 3, 720), color=color.gray(0.5))


def logicaMov(ulPosX, ulPosZ, posDeseadaX, posDeseadaZ, nDesp):
    ts = 0.1
    tf = 10
    T = np.arange(0, tf+ts, ts)
    N = len(T)
    # Seteo de arreglos de ceros para las coordendas y angulos
    xc = np.zeros(len(T)+1)
    zc = np.zeros(len(T)+1)
    ph = np.zeros(len(T)+1)
    xp = np.zeros(len(T)+1)
    zp = np.zeros(len(T)+1)
    xr = np.zeros(len(T)+1)
    zr = np.zeros(len(T)+1)
    u = np.zeros(len(T)+1)
    w = np.zeros(len(T)+1)
    xre = np.zeros(len(T)+1)
    zre = np.zeros(len(T)+1)

    xc[0] = ulPosX
    zc[0] = ulPosZ
    ph[0] = math.sin(math.radians(4))

    xr[0] = xc[0] + nDesp*math.cos(ph[0])
    zr[0] = zc[0] + nDesp*math.sin(ph[0])
    xrD = posDeseadaX
    zrD = posDeseadaZ

    for i in range(N):
        xre[i] = xrD - xr[i]
        zre[i] = zrD - zr[i]

        # Intervalo de error
        e = np.array([[xre[i]],
                      [zre[i]]])

        # Matriz Jacobiana
        J = np.array([[math.cos(ph[i]), -nDesp*math.sin(ph[i])],  # omnidireccional -1*
                      [math.sin(ph[i]), nDesp*math.cos(ph[i])]])

        # Matriz de Ganancia
        K = np.array([[1, 0],
                      [0, 1]])

        # Ley de control del robot
        V = np.linalg.inv(J)*K*e

        # u=Velocidad del robot | w = velocidad angular
        u[i] = V[0][0]
        w[i] = V[1][1]

        # Aplicar las acciones del control al robot
        xp[i] = u[i]*math.cos(ph[i]) - nDesp*w[i]*math.sin(ph[i])
        zp[i] = u[i]*math.sin(ph[i]) + nDesp*w[i]*math.cos(ph[i])

        # Hallar posiciones del robot
        xr[i+1] = xr[i] + ts*xp[i]
        zr[i+1] = zr[i] + ts*zp[i]
        ph[i+1] = ph[i] + ts*w[i]

        # posicion final del robot
        xc[i+1] = xr[i+1] - nDesp*math.cos(ph[i+1])
        zc[i+1] = zr[i+1] - nDesp*math.sin(ph[i+1])

    return(xc, zc, ph, xrD, zrD)
# from base64 import decode

Ventana()
El_Bicho = Robot(0,0)
s = se.Serial('COM3', 9600, timeout=1)
destino = [0,0]
destiny = cylinder(pos=vector(0,0,0),radius=5,axis=vector(00,200,00),color = color.red, visible=False) 
stop = "0"

while True:
    Recibido = s.readline()
    Recibido = Recibido.decode()
    if Recibido != '':
        Recibido = Recibido.split(',')
        destino[0] = int(Recibido[0])
        destino[1] = int(Recibido[1])
        destiny.pos.x = destino[0]
        destiny.pos.z = destino[1]
        destiny.visible = True
        posx, posz, pi, xDestino, zDestino = logicaMov(El_Bicho.pos.x, El_Bicho.pos.z, destino[0], destino[1], 1)
        busqueda = 0
        while busqueda < len(posx):
            #if posx[busqueda] == xDestino and posz[busqueda] == zDestino:
                #El_Bicho.rotate(axis=vector(0, 1, 0), angle=pi[busqueda])
            El_Bicho.pos.x = posx[busqueda]
            El_Bicho.pos.z = posz[busqueda]
            El_Bicho.axis = vector(destino[0]-El_Bicho.pos.x,0,destino[1]-El_Bicho.pos.z)
            busqueda = busqueda+1
            rate(50)
        destiny.visible = False
        s.write(stop.encode())
