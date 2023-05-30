#pylint: disable = C0103

'''
El siguiente modulo es exclusivo
para dibujar un circulo, este modulo
es llamado al modulo cmd_draw, el cual
se encarga de gestionar los comandos

'''

import math
import pygame

WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0,0,0)
CIRCLE_DEFAULT_COLOR = (255,255,255)
ORIGEN = (WIDTH // 2, HEIGHT // 2)
RADIO = 50
PUNTOS = 100

def circle(surface, color, origen, radio):
    '''
    Esta funcion se encarga de dibujar un circulo
    con bases matematicas(geometria)
    '''
    x,y = origen
    increase_ang = 2*math.pi / PUNTOS
    coordenadas = []
    for i in range(PUNTOS):
        ang = i * increase_ang
        coord_x = int(x + radio * math.cos(ang))
        coord_y = int(y + radio * math.sin(ang))
        coordenadas.append((coord_x,coord_y))

    for i, punto in enumerate(coordenadas):
        pygame.draw.line(surface, color,punto, coordenadas[(+1) % len(coordenadas)], 1)
