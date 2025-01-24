import pygame
import math
pygame.init()
#creating runtime variables
width = 700
height = 600
boid_color = (153, 235, 255)#bluish color
#boid_color = (0, 0, 0)#black

bg_color = (0,0,0) # black color

line_color=(255,0,0)

length = 15 # the length of triangle is length+length/2

no_ofboids =31

#below values are for sight:
sight=200
offset_factor=90


daxis=math.radians(3)#this is for adjusting the axis


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('flock simulation')
