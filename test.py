import pygame
import math
length=25

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


pygame.init()
#creating runtime variables


    #drawing the triangles
boid_color = (153, 235, 255)#bluish color
    






width = 700
height = 600
boid_color = (153, 235, 255)#bluish color
#boid_color = (0, 0, 0)#black

bg_color = (0,0,0) # black color

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('flock simulation')

clock = pygame.time.Clock()
running = True

center=(200,200)
angle=0
out=sidecords(center,angle)
print(out)
center2=(300,300)
out2=sidecords(center2,math.radians(90))

while running:
  #event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  
  screen.fill(bg_color)
  pygame.draw.polygon(screen,boid_color,out,0)
  pygame.draw.polygon(screen,boid_color,out2,0)

  

 #updating the screen
  pygame.display.flip()

  clock.tick(10) #this is fps
pygame.quit