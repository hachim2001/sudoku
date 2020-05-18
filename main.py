import pygame
from pygame.math import Vector2
from pygame import draw
scrn = (500,500)
size = 50
fps = 60
colr = pygame.color.Color("white")


board = [
    [0, 8, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 4, 3, 0, 0, 9, 8, 0],
    [3, 0, 1, 0, 0, 8, 7, 0, 0],
    [0, 1, 0, 5, 4, 0, 0, 6, 0],
    [0, 0, 0, 2, 9, 0, 4, 1, 0],
    [0, 4, 3, 0, 0, 6, 0, 9, 0],
    [0, 0, 8, 0, 0, 5, 0, 3, 0],
    [0, 6, 7, 0, 3, 9, 5, 0, 8],
    [1, 0, 5, 0, 8, 0, 0, 0, 0]
  ];

class tab:
    def __init__(self,tab):
        self.tab = tab

def draw_borders():
    for i in range(10):
        
        if i%3 == 0:
            sz = 8
        else:
            sz = 1
        pygame.draw.line(surface,colr, Vector2(0,i*size), Vector2(9*size,i*size), sz)
        pygame.draw.line(surface,colr, Vector2(i*size,0), Vector2(i*size,9*size), sz)

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.Font("freesansbold.ttf",32)
    surface = pygame.display.set_mode(scrn, 0)
    for i in range(9):
        for j in range(9):
            t = font.render(str(board[i][j]),True,colr)
            r = t.get_rect()
            r.center = (i*size+size/2,j*size+size/2)
            surface.blit(t, r, area=None, special_flags = 0)
            
    sz = 1
    draw_borders()
    game = True
    while game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
                break
            if pygame.mouse.get_pressed()[0]:
                print("hi")
        pygame.display.update()
        clock.tick(fps)

