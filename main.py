#pylint: disable = E1101
#pylint: disable = C0103
#pylint: disable = W0621
#pylint: disable = W0401
#pylint: disable = W0614

'''
Modulo main:

se encarga de ejecutar
todos los comandos
disponibles, contiene
un menu, el cual muestra
los comandos que el usuario
puede usar (que iran en un .txt)

'''

from dibuja import *
from help import *

def mostrar_colores():
    '''
    Lo que esta funcion es mostrar en la terminal
    los colores disponibles para su seleccion 
    '''
    lista_colores = {'ROJO': (255, 0, 0),
                     'VERDE': (0, 255, 0), 
                     'AZUL': (0, 0, 255),
                     'AMARILLO': (255, 241, 61), 
                     'ROSA': (253, 64, 222), 
                     'NARANJA': (234, 141, 59), 
                     'BLANCO': (255, 255, 255), 
                     'NEGRO': (0, 0, 0)}
    print("Colores disponibles: ")
    for color in lista_colores:
        print(color)

linea = Dibuja()
figura = Dibuja()

myfile = open("comandos.cmd.txt", "r", encoding="utf8")
for cmd in myfile:
    cmd = cmd.strip()
    if cmd.startswith("/help"):
        imprimir_help()
    if cmd.startswith("color ls"):
        mostrar_colores()
    # Cuadrado
    if cmd.startswith("dibujar_cuadrado"):
        _, x, y, lado = cmd.split()
        x = int(x)
        y = int(y)
        lado = int(lado)

        figura.dibujar_cuadrado(x, y, lado)

    # Pendiente
    if cmd.startswith("draw_pendiente"):
        j, a, b = cmd.split()
        x1, y1 = map(int, a.split(","))
        x2, y2 = map(int, b.split(","))

        linea.draw_pendiente((x1, y1), (x2, y2))
        linea.historial_trazos.append(linea.trazo_actual.copy())
        linea.trazo_actual.clear()

    # Undo
    if cmd == "borrar_ultimo_trazo":
        linea.borrar_ultimo_trazo()

    # Circulo
    if cmd.startswith("dibujar_circulo"):
        _, centro_x, centro_y, radio = cmd.split()
        centro_x = int(centro_x)
        centro_y = int(centro_y)
        radio = int(radio)

        figura.dibujar_circulo(centro_x, centro_y, radio)

    # Grosor
    if cmd.startswith("aumentar_grosor"):
        j, inc = cmd.split()
        incremento = int(inc)
        linea.aumentar_grosor(incremento)

    # Rectangulo
    if cmd.startswith("dibujar_rectangulo"):
        _, x, y, ancho, alto = cmd.split()
        x = int(x)
        y = int(y)
        ancho = int(ancho)
        alto = int(alto)

        figura.dibujar_rectangulo(x, y, ancho, alto)

    # Triangulo 1
    if cmd.startswith("dibujar_triangulo_equilatero"):
        _, x, y, lado = cmd.split()
        x = int(x)
        y = int(y)
        lado = int(lado)
        figura.dibujar_triangulo_equilatero(x, y, lado)

    # Triangulo 2
    if cmd.startswith("dibujar_triangulo_escaleno"):
        _, x1, y1, x2, y2, x3, y3 = cmd.split()
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        x3 = int(x3)
        y3 = int(y3)

        figura.dibujar_triangulo_escaleno(x1, y1, x2, y2, x3, y3)

    # Triangulo 3
    if cmd.startswith("dibujar_triangulo_isosceles"):
        _, x1, y1, x2, y2, base = cmd.split()
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        base = int(base)

        figura.dibujar_triangulo_isosceles(x1, y1, x2, y2, base)

myfile.close()

RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    pygame.display.update()

pygame.quit()
