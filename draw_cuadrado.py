#pylint: disable = C0103

'''
El siguiente modulo es exclusivo
para dibujar un triangulo, este modulo
es llamado al modulo cmd_draw, el cual
se encarga de gestionar los comandos

'''

import pygame

WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0,0,0)
COLOR_CUADRADO = (255,0,0)
esquina_izq = (WIDTH // 2 - 50, HEIGHT // 2 - 50)
L = 100 # LADO

def cuadrado(surface, color, esquina, lado):
    '''
    En la siguiente funcion:
    el parametro esquina va
    a representar las coordenadas
    x,y. Despues vamos a ir guardando
    los vertices en tuplas de la siguiente
    forma:

    '''

    x,y = esquina
    puntos = [
        (x,y),
        (x + lado, y),
        (x + lado, y + lado),
        (x,y + lado),
    ]

    for i in range(4): # 4 lados
        pygame.draw.line(surface,color,puntos[i],puntos[(i+1)%4], 1)
