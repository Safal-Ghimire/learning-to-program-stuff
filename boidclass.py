import math
import random
from function import *


class boid:
  def __init__(self):
    self.x,self.y = (cordrand(1),cordrand(0))
    self.speed = 5
    self.center = [self.x,self.y]
    self.axis = math.radians(random.randint(0,360))#this is in radian
    self.side_cords = sidecords(self.center,self.axis)# side cords are vertex of the trianglr and is already rotated
    self.dangle = 0 #small change in angle


  def update_posn(self):
  
    self.center[0] += self.speed*math.sin(self.axis)
    self.center[1] -= self.speed*math.cos(self.axis) # it is minus because of the cordiante systemof pygame
    self.side_cords = sidecords(self.center,self.axis)# side cords are vertex of the triangle and is already rotated
    

    # updating position when boids go out of bound
    self.center = correct_bound(self.center)
    

    
     
  
  
  def update(self):
    # Only rotate relative to the current axis; dangle adjusts the axis over time
    
    # Recalculate the rotated side cords from the base triangle
    
    # Draw the boid
    draw_boid(self.side_cords)


    # calculating the average axis of boids withing sight accounting the visual range pixels and changing the axis

  def change_axis(self,boids_undersight):
    average_axis = self.axis
    i = 0
    for instance in boids_undersight:
      if instance == self:
        pass
      average_axis += instance.axis
      i+=1
      if i!=0:
        average_axis = average_axis/i


    if average_axis > self.axis: 
      self.axis +=daxis
      
    if average_axis < self.axis:
      self.axis -= daxis
      
    if average_axis == 0:
      pass

    self.axis = self.axis % 360 #re normalizing to [0,360]

  def show_boids_under_sight(self,boids_under_sight):
    for instance in boids_under_sight:
      pygame.draw.line(screen,line_color,self.center,instance.center,width = 1)

    pygame.draw.circle(screen,line_color,self.center,sight,width=1)
    