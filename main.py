#pylint: disable = E1101
#pylint: disable = C0103

'''
Modulo main:

se encarga de ejecutar
todos los comandos
disponibles, contiene
un menu, el cual muestra
los comandos que el usuario
puede usar (que iran en un .txt)

'''

import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Dibuja:
    '''
    La clase contiene 3 metodos:

    1. Dibujar recta(desde un punto A -> punto B)
    mediante el uso de la ecuacion pendiente

    2. Undo(borrar el ultimo trazo)

    3. Aumentar el grosor de linea
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

    def draw_pendiente(self, point_a, point_b):
        '''
            Pendiente por comentar       
        '''
        dx = point_b[0] - point_a[0]
        dy = point_b[1] - point_a[1]
        steps = max(abs(dx), abs(dy))
        x_increment = dx / steps if steps != 0 else 0
        y_increment = dy / steps if steps != 0 else 0

        x = point_a[0]
        y = point_a[1]
        for _ in range(steps):
            x += x_increment
            y += y_increment
            self.trazo_actual.append((int(x), int(y)))

        pygame.draw.lines(self.surface, self.line_color,
                          False, self.trazo_actual, self.grosor_linea)
        pygame.display.flip()

    def borrar_ultimo_trazo(self):
        '''
        Este metodo lo primero que hace
        es verificar si hay algun trazo
        en el historial(puesto que es un
        arreglo y lo declaramos vacio en el init)

        Despues rellena la pantalla con el color
        ya predeterminado en el init nuevamente
        '''
        if self.historial_trazos:
            self.surface.fill(self.default_bg_color)
            self.historial_trazos.pop()
            for trazo in self.historial_trazos:
                pygame.draw.lines(self.surface, self.line_color, False, trazo, self.grosor_linea)
            pygame.display.flip()

    def aumentar_grosor(self, increase):
        '''
        Lo que hace este metodo
        es llamar a la propiedad
        grosor_linea y asignarle como
        parametro increase, increase
        es un parametro que sera
        dado desde el archivo de txt
        '''
        self.grosor_linea += increase
        self.surface.fill(self.default_bg_color)
        for trazo in self.historial_trazos: # busca los trazos restantes en el historial
            pygame.draw.lines(self.surface, self.line_color, False, trazo, self.grosor_linea)
        pygame.display.flip()

linea1 = Dibuja()
linea2 = Dibuja()
linea3 = Dibuja()

myfile = open("comandos.cmd.txt", "r", encoding="utf8")
for cmd in myfile:
    cmd = cmd.strip()
    if cmd.startswith("draw_pendiente"):
        j, a, b = cmd.split()
        x1, y1 = map(int, a.split(","))
        x2, y2 = map(int, b.split(","))

        # Dibujo de objetos:
        linea1.draw_pendiente((x1, y1), (x2, y2))
        linea1.historial_trazos.append(linea1.trazo_actual.copy())
        linea1.trazo_actual.clear()
        linea2.draw_pendiente((x1, y1), (x2, y2))
        linea2.historial_trazos.append(linea2.trazo_actual.copy())
        linea2.trazo_actual.clear()

        linea3.draw_pendiente((x1, y1), (x2, y2))
        linea3.historial_trazos.append(linea3.trazo_actual.copy())
        linea3.trazo_actual.clear()

    elif cmd == "borrar_ultimo_trazo":
        linea1.borrar_ultimo_trazo()

    elif cmd.startswith("aumentar_grosor"):
        j, inc = cmd.split()
        incremento = int(inc)
        linea1.aumentar_grosor(incremento)
    print(f" -{cmd}-")
myfile.close()


# Para que corra el programa
RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    pygame.display.update()

pygame.quit()
