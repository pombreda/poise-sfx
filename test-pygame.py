import sys
import pygame
from pygame.locals import *

pygame.init()

pygame.font.init()

screen = pygame.display.set_mode((640, 480))

background = pygame.Surface(screen.get_size())

if pygame.font:
    textpos.centery = background.get_rect().centery
    
    
import numpy
a = numpy.zeros([48000,2],numpy.float)
snd = pygame.sndarray.make_sound(a)
snd.play()
    
clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
            
    screen.blit(background, (0, 0))