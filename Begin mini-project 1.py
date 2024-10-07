import pygame
import math
import datetime

pygame.init()
display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()
FPS = 50

def print_text(text, position): 
   # Creates a font for displaying text on the clock
    font = pygame.font.SysFont("Castellar", 40, True, False)
    # Renders the text with the specified font and color
    surface = font.render(text, True, (0, 0, 0))  
    # Places the text on the desired position on the screen
    display.blit(surface, position)

def convert_degress_to_pygame(R, theta):
     # Calculates the y-coordinate using cosinus 
    y = math.cos(2 * math.pi * theta / 360) * R
     # Calculates the x-coordinate using sinus 
    x = math.sin(2 * math.pi * theta / 360) * R
    return x + 400, 400 - y  

def game():
     # Handles events like closing the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
         # Gets the current time   
        current_time = datetime.datetime.now()
        seconds = current_time.second
        minute = current_time.minute
        hour = current_time.hour % 12  

        display.fill((211, 202, 230))  # Background
        pygame.draw.circle(display, (91, 63, 191), (400, 400), 400, 5)  # Black circle outline

        # Draw numbers 1-12
        for number in range(1, 13):
            print_text(str(number), convert_degress_to_pygame(350, number * 30))

        # Second hand 
        R = 380
        theta = seconds * 6  # 6 degrees per second
        pygame.draw.line(display, (157, 141, 214), (400, 400), convert_degress_to_pygame(R, theta), 2)  # Red, thin

        # Minute hand 
        R = 350
        theta = (minute + seconds / 60) * 6  # 6 degrees per minute
        pygame.draw.line(display, (19, 29, 138), (400, 400), convert_degress_to_pygame(R, theta), 6)  # Black, medium

        # Hour hand 
        R = 250
        theta = (hour + minute / 60) * 30  # 30 degrees per hour
        pygame.draw.line(display, (55, 24, 122), (400, 400), convert_degress_to_pygame(R, theta), 8)  # Black, thick

        pygame.display.update()
        clock.tick(FPS)

# Run the game
game()
pygame.quit()


