__author__ = 'TOSS'
import pygame

class Particle:
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 255)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

background_colour = (255, 255, 255)
(width, height) = (700, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tutorial with Particle Class")
screen.fill(background_colour)
#
# draw a circle
# pygame.draw.circle(screen,(0,0,255,255), (150,50), 125, 1)

particle1 = Particle((150,50), 23)
particle1.display()

pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False