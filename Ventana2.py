# Librerias utilizadas
import sys
import pygame as pyg
from pygame.locals import *
import serial

# Se establece el puerto que se utilizara para la
# comunicacion serial
s = serial.Serial('COM2', 9600, timeout=0)
pyg.init()

#-------------------- AJUSTES DE LA PANTALLA --------------------
size = (640, 360)
blanco = 255,255,255
screen = pyg.display.set_mode(size)
screen.fill(blanco)
movimiento = 0

#-------------------------  FUNCIONAMIENTO  -------------------------
#
# El siguiente while se mantendra activo siempre y funciona de la siguiente
# manera:
# 
### Lectura:
# --Se mantendrá constantemente leyendo el puerto, y si lee algo que no sea
# --'', guardará el valor en la variable movimiento (valor esperado: 0) y
# --limpiará la pantalla de pygame.
#
### Asignando Destino:
# --Si la variable 'movimiento' = 0, habilitará el click para asignar
# --coordenadas de destinos para el robot, dichas coordenadas se ajustan
# --a las dimensiones del escenario, luego se pasaran a str para poder
# --enviarlas por serial a la otra ventana, ademas de crear un circulo rojo
# --donde se hizo clock, y finaliza cambiando el valor de a variable a 1,
# --impidiendo de esta forma realizar otro click

while True:
    pyg.display.update()
    rec = s.readline()
    rec = rec.decode()
    if rec != '':
        # Convierte lo recibido a int
        rec = int(rec)
        movimiento = int(rec)
        # Limpia la pantalla
        screen.fill(blanco)
        pyg.display.update()

    for event in pyg.event.get():
        if movimiento == 0:
            if event.type == pyg.MOUSEBUTTONDOWN:
                # Guarda las Posiciones del click
                xFlag, yFlag = pyg.mouse.get_pos()
                
                # Ajusta las coordeandas para
                # el escenario
                x = (xFlag*2) - size[0]#640
                y = ((yFlag*2) - size[1])#360
                pos = str(x) + ',' + str(y)
                s.write(pos.encode())
                
                # Dibuja el circulo en el click
                pyg.draw.circle( screen, (255,0,0), (xFlag , yFlag), 10 )
                print(x,y)
                movimiento = 1
        if event.type == QUIT:
            pyg.quit()
            sys.exit()


