import pygame
import sys

screen_width_pixel = 800  # Width of the screen in pixels
screen_height_pixel = 600  # Height of the screen in pixels

x = screen_width_pixel // 2  # Initial X coordinate of the object in pixels
y = screen_height_pixel // 2  # Initial Y coordinate of the object in pixels
width = 50  # Width of the object in pixels
height = 50  # Height of the object in pixels
angle = 0  # Initial angle of the object's rotation in degrees
rotation_speed_deg = 2  # Rotation speed of the object in degrees per frame
movement_speed_pixel = 5  # Movement speed of the object in pixels per frame

total_distance_x_pixel = 0  # Total distance moved along the X-axis in pixels
total_distance_y_pixel = 0  # Total distance moved along the Y-axis in pixels

step_size_input = input("Enter the step size for movement (default is 5): ")  # Take input from the use
step_size = float(step_size_input) if step_size_input else 5 # If there is no input arrange it to 5 pixel

rotation_angle_deg = 0  # Total rotation angle in degrees

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((screen_width_pixel, screen_height_pixel))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 24) # Define font

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get input from the user
    try:
        distance_x = float(input("How many units do you want to move to the right? "))  # Distance to move along the X-axis in pixels
        total_distance_x_pixel += distance_x  # Add the distance to the total distance when each input is taken
        distance_y = -float(input("How many units do you want to move downwards? "))  # Distance to move along the Y-axis in pixels (negative for upward movement)
        total_distance_y_pixel += distance_y  # Add the distance to the total distance when each input is taken
        rotation_angle_deg += float(input("How many degrees do you want to rotate? "))  # Update rotation angle in degrees
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Move the object according to specified steps
    while abs(total_distance_x_pixel) >= step_size or abs(total_distance_y_pixel) >= step_size:
        # Movement along the X axis
        if total_distance_x_pixel > 0:
            remaining_distance_x = min(step_size, total_distance_x_pixel)
            x += remaining_distance_x
            total_distance_x_pixel -= remaining_distance_x
        elif total_distance_x_pixel < 0:
            remaining_distance_x = min(step_size, abs(total_distance_x_pixel))
            x -= remaining_distance_x
            total_distance_x_pixel += remaining_distance_x

        # Movement along the Y axis
        if total_distance_y_pixel > 0:
            remaining_distance_y = min(step_size, total_distance_y_pixel)
            y -= remaining_distance_y
            total_distance_y_pixel -= remaining_distance_y
        elif total_distance_y_pixel < 0:
            remaining_distance_y = min(step_size, abs(total_distance_y_pixel))
            y += remaining_distance_y
            total_distance_y_pixel += remaining_distance_y

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the object
        rotated_image = pygame.Surface((width, height))
        rotated_image.fill((255, 255, 255))
        rotated_image.set_colorkey((0, 0, 0))
        rotated_rect = rotated_image.get_rect(center=(x, y))
        rotated_image = pygame.transform.rotate(rotated_image, angle + rotation_angle_deg)
        screen.blit(rotated_image, rotated_rect)
        displayed_rotational_angle = (angle + rotation_angle_deg) % 360

        # Create text information
        text_distance = font.render(f"Remaining Distance (X): {total_distance_x_pixel} pixels", True, (255, 255, 255))
        text_distance_rect = text_distance.get_rect(topleft=(10, 10))
        text_rotation = font.render(f"Rotation Angle: {displayed_rotational_angle} degrees", True, (255, 255, 255))
        text_rotation_rect = text_rotation.get_rect(topleft=(10, 30))

        # Draw text to the screen
        screen.blit(text_distance, text_distance_rect)
        screen.blit(text_rotation, text_rotation_rect)

        # Update the screen
        pygame.display.flip()

        # FPS limit
        clock.tick(60)

# Close Pygame
pygame.quit()
sys.exit()





