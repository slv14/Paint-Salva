#pylint: disable = C0103

'''
Este modulo contiene la clase dibuja
la cual contiene todos los metodos
encargados de crear figuras y dibujar
rectas
'''

import math
import pygame

BLACK = (0, 0, 0)

class Dibuja:
    '''
    Esta clase contiene todos los metodos:

    1. Dibujar recta de punto A - punto B
    2. Dibujar circulo
    3. Dibujar cuadrado
    4. Dibujar rectangulo
    5. Dibujar los 3 tipos de triangulo
    '''
    def __init__(self):
        self.width = 800
        self.height = 600
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.default_bg_color = BLACK
        self.grosor_linea = 1
        self.trazo_actual = []
        self.historial_trazos = []
        self.line_color = (255, 120, 10)
        self.colores = []

    def draw_pendiente(self, point_a, point_b):
        '''
        
        '''
        dx = point_b[0] - point_a[0]
        dy = point_b[1] - point_a[1]
        steps = max(abs(dx), abs(dy))
        x_increment = dx / steps if steps != 0 else 0
        y_increment = dy / steps if steps != 0 else 0

        x = point_a[0]
        y = point_a[1]
        steps = int(max(abs(dx), abs(dy)))
        for _ in range(steps):
            x += x_increment
            y += y_increment
            self.trazo_actual.append((int(x), int(y)))

        pygame.draw.lines(self.surface, self.line_color,
                          False, self.trazo_actual, self.grosor_linea)
        pygame.display.flip()

    def borrar_ultimo_trazo(self):
        '''
        El metodo llama a la propiedad
        historial de  trazos y los elimina
        con pop
        '''
        if self.historial_trazos:
            self.surface.fill(self.default_bg_color)
            self.historial_trazos.pop()
            for trazo in self.historial_trazos:
                pygame.draw.lines(self.surface, self.line_color, False, trazo, self.grosor_linea)
            pygame.display.flip()

    def aumentar_grosor(self, increase):
        '''
        El metodo toma todas las propiedades
        correspondientes del trazo y lo que hace
        es aumentar el grosor del mismo
        '''
        self.grosor_linea += increase
        self.surface.fill(self.default_bg_color)
        for trazo in self.historial_trazos:
            pygame.draw.lines(self.surface, self.line_color, False, trazo, self.grosor_linea)
        pygame.display.flip()

    def dibujar_cuadrado(self, x, y, lado):
        punto1 = (x, y)
        punto2 = (x + lado, y)
        punto3 = (x + lado, y + lado)
        punto4 = (x, y + lado)

        pygame.draw.lines(self.surface, self.line_color, False, [punto1, punto2], self.grosor_linea)
        pygame.draw.lines(self.surface, self.line_color, False, [punto2, punto3], self.grosor_linea)
        pygame.draw.lines(self.surface, self.line_color, False, [punto3, punto4], self.grosor_linea)
        pygame.draw.lines(self.surface, self.line_color, False, [punto4, punto1], self.grosor_linea)

        pygame.display.flip()

    def dibujar_circulo(self, centro_x, centro_y, radio):
        puntos_circulo = []
        angulo = 0
        # Ajusta la precisión del círculo cambiando el número de puntos
        incremento_angulo = 2 * math.pi / 100

        while angulo < 2 * math.pi:
            xc = centro_x + radio * math.cos(angulo)
            yc = centro_y + radio * math.sin(angulo)
            puntos_circulo.append((int(xc), int(yc)))
            angulo += incremento_angulo

        self.trazo_actual = puntos_circulo.copy()
        self.historial_trazos.append(puntos_circulo)

        pygame.draw.lines(self.surface, self.line_color, False, puntos_circulo, self.grosor_linea)
        pygame.display.flip()

    def dibujar_rectangulo(self, x, y, ancho, alto):
        '''
        El metodo toma cuatro puntos
        los cuatro deben contener
        a las coordenadas dentro,
        dos de esos puntos deben almacenar
        el ancho, mientras que en los lados
        debe ser almacenada la informacion
        mediante la variable alto
        '''
        punto1 = (x, y)
        punto2 = (x + ancho, y)
        punto3 = (x + ancho, y + alto)
        punto4 = (x, y + alto)

        pygame.draw.lines(self.surface, self.line_color, False, [punto1, punto2], self.grosor_linea)
        pygame.draw.lines(self.surface, self.line_color, False, [punto2, punto3], self.grosor_linea)
        pygame.draw.lines(self.surface, self.line_color, False, [punto3, punto4], self.grosor_linea)
        pygame.draw.lines(self.surface, self.line_color, False, [punto4, punto1], self.grosor_linea)

        pygame.display.flip()


    def dibujar_triangulo_equilatero(self, x, y, lado):
        '''
        Metodo que dibuja un triangulo
        de acuerdo a las coordenadas que
        se le asignen, la altura y el lado
        '''
        altura = (3 ** 0.5) * lado / 2
        punto1 = (x, y)
        punto2 = (x + lado, y)
        punto3 = (x + lado / 2, y - altura)

        self.trazo_actual = [punto1, punto2, punto3, punto1]
        self.historial_trazos.append(self.trazo_actual)

        pygame.draw.lines(self.surface,
                          self.line_color, False, self.trazo_actual, self.grosor_linea)
        pygame.display.flip()

    def dibujar_triangulo_escaleno(self, x1, y1, x2, y2, x3, y3):
        '''
        Este triangulo toma distintas coordenadas
        y lo que hace es almacenarlas en un historial
        para posteriormente irlas dibujando
        '''
        self.draw_pendiente((x1, y1), (x2, y2))
        self.historial_trazos.append(self.trazo_actual.copy())
        self.trazo_actual.clear()

        self.draw_pendiente((x2, y2), (x3, y3))
        self.historial_trazos.append(self.trazo_actual.copy())
        self.trazo_actual.clear()

        self.draw_pendiente((x3, y3), (x1, y1))
        self.historial_trazos.append(self.trazo_actual.copy())
        self.trazo_actual.clear()

        pygame.display.flip()

    def dibujar_triangulo_isosceles(self, x1, y1, x2, y2, base):
        '''
        
        '''
        # Dibuja los lados iguales
        self.draw_pendiente((x1, y1), (x2, y2))
        self.historial_trazos.append(self.trazo_actual.copy())
        self.trazo_actual.clear()

        self.draw_pendiente((x2, y2), (x1 + base, y2))
        self.historial_trazos.append(self.trazo_actual.copy())
        self.trazo_actual.clear()

        # Dibuja el tercer lado
        self.draw_pendiente((x1, y1), (x1 + base, y2))
        self.historial_trazos.append(self.trazo_actual.copy())
        self.trazo_actual.clear()

        pygame.display.flip()
