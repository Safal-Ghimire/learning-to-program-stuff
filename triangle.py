import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 700, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Triangle Rotation')

# Colors
bg_color = (0, 0, 0)  # Black
triangle_color = (153, 235, 255)  # Light blue
rotated_color = (255, 0, 0)  # Red

# Clock for controlling frame rate
clock = pygame.time.Clock()
running = True

def cordrand(case):
    """Generate random coordinates within screen bounds.
    case 1 for x-coordinate, case 0 for y-coordinate.
    """
    if case == 1:
        return random.randint(0, width)
    if case == 0:
        return random.randint(0, height)

def sidecords(center, length=25):
    """Generate the vertices of a triangle based on its center.
    Args:
    - center: Tuple (x, y) for the center of the triangle.
    - length: Length of the triangle's height.
    Returns:
    - List of three vertices [(x1, y1), (x2, y2), (x3, y3)].
    """
    x, y = center
    tip = (x, y - length)  # Tip of the triangle
    base_left = (x - length // 2, y + length // 2)
    base_right = (x + length // 2, y + length // 2)
    return [tip, base_left, base_right]

def rotate(vertex, angle, center):
    """Rotate a set of vertices around a center by a given angle.
    Args:
    - vertex: List of (x, y) points to rotate.
    - angle: Angle in radians to rotate.
    - center: Tuple (cx, cy) for the rotation center.
    Returns:
    - List of rotated vertices.
    """
    cx, cy = center
    rotated = []
    for x, y in vertex:
        # Translate to origin
        translated_x = x - cx
        translated_y = y - cy
        # Apply rotation matrix
        rotated_x = translated_x * math.cos(angle) - translated_y * math.sin(angle)
        rotated_y = translated_x * math.sin(angle) + translated_y * math.cos(angle)
        # Translate back
        final_x = rotated_x + cx
        final_y = rotated_y + cy
        rotated.append((final_x, final_y))
    return rotated

# Generate a random triangle
center = (cordrand(1), cordrand(0))
axis = random.uniform(0, 2 * math.pi)  # Random rotation angle in radians
triangle = sidecords(center)
rotated_triangle = rotate(triangle, axis, center)

# Print the axis angle and coordinates
print(f"Axis (radians): {axis}")
print(f"Original Triangle: {triangle}")
print(f"Rotated Triangle: {rotated_triangle}")

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(bg_color)

    # Draw the original triangle
    pygame.draw.polygon(screen, triangle_color, triangle, 0)

    # Draw the rotated triangle
    pygame.draw.polygon(screen, rotated_color, rotated_triangle, 0)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
