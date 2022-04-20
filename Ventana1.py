#from vpython import *
# from doctest import master
# import tkinter as tk
# import numpy as np
# import matplotlib as plt

# # Ventana Frame
# ventana = tk.Tk()
# ventana.geometry('642x535')
# ventana.wm_title("Pruebas de Grafico 3d")
# ventana.minsize(width=642,height=535)

# frame = tk.Frame(ventana, bg='white', bd=3)
# frame.pack(expand=1,fill='both')

# #canvas = plt.backends.backends_tkagg.FigureCanvasTkAgg(fig, master = frame)

# ventana.mainloop()

from vpython import *
#---------------------------INICIALIZACION DE VARIABLES -------------------------#
coorIniciales = vector(0, 6.5, 0)
#--------------------------------------------------------------------------------#

def Ventana():
    Suelo = box(pos=vector(0, 0, 0), size=vector(
        1280, 3, 720), color=color.gray(0.5))


def Robot(tFXYZ):
    posRobot = box(pos=tFXYZ, size=vector(40, 15, 20), color=color.red)

#-------------------------------Inicializa elementos-----------------------------#
Ventana()
Robot(coorIniciales)

#--------------------------------------------------------------------------------#