import pygame
from dj.dj import Dj

class Ui:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("This is my Dj Game!")
        
    def show_ui(self):
       dj = Dj("Kyle", 22, "Male", "Ireland", 500, True)
       running = True

       while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            pygame.display.update()

    pygame.quit()

