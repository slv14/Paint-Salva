#pylint: disable = E1101
'''
En este modulo se desarrollan
los comandos que se implementaran
para dibujar las figuras predeterminadas

'''

import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Dibuja():
    '''
    Esta clase se encarga
    de trazar lineas en una pantalla
    de 800x600
    '''
    def __init__(self):
        self.width = 800
        self.height = 600
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.default_bg_color = BLACK
        self.grosor_linea = 1
        self.trazo = []
        self.line_color = (255,120,10)

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Paint de Salva")
        self.screen.fill(self.default_bg_color)
        pygame.display.flip()

    def linea_x(self):
        '''
        Traza una linea horizontal
        eje x
        '''
        for i in range(0,100):
            self.surface.set_at((100 + i, 200), self.line_color)
        pygame.display.flip()

    def linea_y(self):
        '''
        Traza una linea vertical
        eje y
        '''
        for i in range(0,100):
            self.surface.set_at((100, 200 + i), self.line_color)
        pygame.display.flip()

linea1 = Dibuja()
linea1.linea_y()

RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    pygame.display.update()

pygame.quit()
