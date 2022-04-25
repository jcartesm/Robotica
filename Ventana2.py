import sys
from matplotlib.animation import MovieWriter
import pygame as pyg
from pygame.locals import *
import serial as sc


s = sc.Serial('COM2', 9600, timeout=0)
pyg.init()

size = (1280, 720)
blanco = 255,255,255

screen = pyg.display.set_mode(size)
screen.fill(blanco)
movimiento = 0


while True:
    pyg.display.update()
    rec = s.readline()
    rec = rec.decode()
    if rec != '':
        rec = int(rec)
        movimiento = rec
        
    for event in pyg.event.get():
        if movimiento == 0:
            if event.type == pyg.MOUSEBUTTONDOWN:
                movimiento = 1
                xFlag, yFlag = pyg.mouse.get_pos()
                x = xFlag - 640
                y = (yFlag - 360)*-1
                pos = str(x) + ',' + str(y)
                s.write(pos.encode())
                pyg.draw.circle( screen, (255,0,0), (xFlag , yFlag), 20 )
                print(x,y)
        if event.type == QUIT:
            pyg.quit()
            sys.exit()

pyg.quit()
