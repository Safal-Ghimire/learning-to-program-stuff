import pygame
from common import *
from boidclass import boid
from function import under_sight

"""-all the commmon variables are in common.
   - the boid class is in boidclass.py .
   
   creating the window:

    -done in common.py"""

clock = pygame.time.Clock()
running = True



#------------------------------------------------------------------------------------------------------------------------
""" to do: 
      -add cohesion
      -add seperation"""
#------------------------------------------------------------------------------------------------------------------------

bird = []
boids_undersight=[]
for i in range(no_ofboids):    #creating the boid instances

  bird.append(boid()) 



#mainj session loop
while running:
  #event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill(bg_color)
  #updating the boid instance





  for instance in  bird:
    boids_undersight=under_sight(bird,instance,sight,offset_factor)
    if(instance==bird[1]):
      bird[1].show_boids_under_sight(boids_undersight)
      for check in boids_undersight:
        print(check.center,'\n')
      print("set")
  
    
    instance.update_posn()
    
    instance.change_axis(boids_undersight)

    instance.update()
    boids_undersight=[]
    


  

  #updating the screen
  pygame.display.flip()

  clock.tick(70) #this is fps
pygame.quit