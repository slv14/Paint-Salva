#pylint: disable = C0103

'''
El siguiente modulo es exclusivo
para dibujar tres tipos de triangulos:

1. Equilatero
2. Escaleno
3. Isosceles

Este modulo es llamado al modulo cmd_draw, el cual
se encarga de gestionar los comandos

'''
import pygame

WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0,0,0)
TRIANG_COLOR = (255,0,0)
punto_1 = (WIDTH // 2, HEIGHT // 2 - 100)
punto_2 = (WIDTH // 2 - 100, HEIGHT // 2 + 100)
punto_3 = (WIDTH // 2 + 100, HEIGHT // 2 + 100)

def triang(surface, color, punto_a, punto_b, punto_c):
    '''
    La funcion se encarga de dibujar tres lineas
    tomando tres puntos como referencia
    '''

    pygame.draw.line(surface, color, punto_a, punto_b, 1)
    pygame.draw.line(surface, color, punto_b, punto_c, 1)
    pygame.draw.line(surface, color, punto_c, punto_a, 1)
