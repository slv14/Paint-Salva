import pygame

# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
width = 800 
height = 600
surface = pygame.display.set_mode((width, height))
background_color = (0,0,0)
surface.fill(background_color)
# Establecer el color de un píxel en la posición (100, 200) a rojo (255, 0, 0)
color = (255,120, 10)
def linea_x():
    for i in range(0,100):
        surface.set_at((100 + i, 200), color)
    ## Mostrar la superficie en la pantalla
    pygame.display.flip()

def linea_y():
    for i in range(0,100):
        surface.set_at((100, 200 + i), color)
    pygame.display.flip(
)
myfile = open("comandos.cmd.txt", "r")
for cmd in myfile:
    cmd = cmd.strip()
    if cmd == "linea -x":
        linea_x()
    if cmd == "linea -y":
        linea_y()
    print(f" -(cmd)-")
myfile.close()


# Esperar a que el usuario cierre la ventana
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()