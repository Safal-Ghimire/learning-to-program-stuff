import pygame
import math
import random
from common import *


def sidecords(center,angle): # returns the cordinates of triangle based on the axis by first creating it and rotating it
    """
    Generate the vertices of a triangle resembling a paper plane.
    Args:
    - center: A tuple (x, y) representing the center of the triangle.
    - length: The length of the triangle's base to its tip.
    Returns:
    - A list of three vertices [(x1, y1), (x2, y2), (x3, y3)].
    """               
    #setting the length to 25 px
    x, y = center
    # Tip of the triangle
    tip = (x, y - length)
    # Base left is length/2 from the centr
    base_left = (x - length // 2, y + length // 2)
    # Base right is legth/2 from the centr
    base_right = (x + length // 2, y + length // 2)

    return rotate([tip, base_left, base_right],angle,center)
  


def rotate(vertex,angle,center):
  cx,cy=center
  #rotating the vertices of the triangle
  rotated = []
  for x, y in vertex:
     # Apply rotation matrix
     # Translate point to origin becaude rotation matrix works for the position vector 
    translated_x = x - cx
    translated_y = y - cy

        # Apply rotation matrix
    rotated_x = translated_x * math.cos(angle) - translated_y * math.sin(angle)
    rotated_y = translated_x * math.sin(angle) + translated_y * math.cos(angle)

    # Translate back to the original position
    final_x = rotated_x + cx
    final_y = rotated_y + cy
    rotated.append((final_x, final_y))

  return rotated




def draw_boid(vertex):
    #drawing the triangles
    
    pygame.draw.polygon(screen,boid_color,vertex,0)



def cordrand(case):#case 1 for absissa abd 0 for ordinate
  if case == 1:
    return random.randint(0,700) #for x cordinate
  if case == 0:
    return random.randint(0,600) #for y cordinate
  


# keeping boids in the screen
def correct_bound(center):

  # ! length+length/2 is  px is total length of the triangle

  #checking is the boid is out of window
  if(center[0] <- (length+length/2)):#for x axis to the left
    center[0] = width+(length)
  if(center[0] > width+(length+length/2)):#for x axis to the right
    center[0] =- length
  if(center[1] <- (length+length/2)):#for y axis to top
    center[1] = height+length
  if(center[1] > height+(length+length/2)):#for y axis to top
    center[1] =- length

  return center


def under_sight(boids, main_instance, sight, offset_factor):
    """
    identify boids within the visual range (a circle minus a restricted arc at the back).

    
        boids: the entire boid class
        main_instance: the main boid for checking
        sight: Visual range (radius of the circle).
        offset_factor: Offset angle (in degrees) for the restricted arc at the back.

    Returns:
        List of boid instances that are within the sight range and outside the restricted arc.
    """
    center = main_instance.center
    axis = main_instance.axis
    one_side_ofvertex = main_instance.side_cords[0]
    passboid = []
    try:

      m1 = ( one_side_ofvertex[1] - center[1]) / (one_side_ofvertex[0] - center[0])
    except ZeroDivisionError:
          m1 = float('inf')
    for instance in boids:
        
        x, y = instance.center[0], instance.center[1]
        dx = x - center[0]
        dy = y - center[1]
        try:
          m2 = dy / dx
        except ZeroDivisionError:
          m2 = float('inf')
          

        # calculate the distance from the main boid
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance <= sight:  # within the circle but may or may not be in the arc at the back of boid
            # calculate angle to the other boid relative to the main boid's axis
            angle = math.degrees(math.atan2(m1 + m2, 1 - m1 * m2))
            angle = angle % 360  # normalizing angle to [0, 360)
            if angle < 180-offset_factor:
               passboid.append(instance)
           
            

    return passboid



# geting the density of the boids in the sight range and steer to high density region
def most_populated_region(pass_boids, center,visual_range):
  horizontal_offset = center[0]
  vertical_offset = center[1]
  averaga_vertical_component = 0
  average_horizontal_component = 0
  for instance in pass_boids:
     pass






