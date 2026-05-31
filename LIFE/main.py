# Ok it is little complex for my python knowladge. I will come back to this later. You can find the files req. in your github repo.

import pygame

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
herbivore_pos = pygame.Vector2(100, 100)


class herbivore():
    def draw(self):
        pygame.draw.circle(screen, "orange", herbivore_pos,40)











while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    

    pygame.display.flip()



pygame.quit()










