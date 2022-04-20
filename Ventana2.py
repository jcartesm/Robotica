import serial as sc
import pygame as pyg

s = sc.Serial('COM2', 9600, timeout=0)
pyg.init()

window = (1280, 720)

screen = pyg.display.set_mode(window)

while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
        if event.type == pyg.MOUSEBUTTONDOWN:
            x, y = pyg.mouse.get_pos()
            x = x - 640
            y = (y - 360)*-1
            pos = (x, y)
            print(pos)
            #s.write(cords.encode())
