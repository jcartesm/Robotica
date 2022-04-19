import serial as sc
import pygame as pyg

s = sc.Serial('COM2', 9600, timeout=0)
pyg.init()

window = (1200, 600)

screen = pyg.display.set_mode(window)

while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
        if event.type == pyg.MOUSEBUTTONDOWN:
            cords = pyg.mouse.get_pos()
            cords = str(cords)
            print(cords)
            s.write(cords.encode())
            # print(cords)

# while True:
#