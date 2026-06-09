# normal pygame for some reason doesn't download on my laptop, so Arsen helped me download pygame_ce. I also used Gemini for things like making sure the visuals appear as they're supposed to
#I know the submission is a little late but I was really overwhelmed last week with uni, hope its okay :)
#Sources: Song: excerpt of Simple and Clean by Hikaru Utada, bitcrushed for retro effect with: Melobytes.com
# Images: Bubbles: https://abrakadabra.fun/15522-puzyrki-png.html, Goldfish: https://de.pinterest.com/pin/599682506656773679/
#Background: https://de.pinterest.com/pin/298574650269480482/
import pygame
import random
import math
import sys

pygame.init()
pygame.mixer.init()

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#clock
clock = pygame.time.Clock()

#pictures and music
raw_background = pygame.image.load("background.jpg").convert()
background_img = pygame.transform.scale(raw_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
bubble_img = pygame.image.load("bubble.png").convert_alpha()
fish_img = pygame.image.load("fish.png").convert_alpha()

#loading music
pygame.mixer.music.load("Crushed_song.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


#bubbles
class Bubble:
    def __init__(self, image):
        self.original_image = image
        scale_factor = random.uniform(0.04, 0.16)
        width = int(self.original_image.get_width() * scale_factor)
        height = int(self.original_image.get_height() * scale_factor)
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - width)
        self.rect.y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 200)
        self.speed_y = random.uniform(-3, -1)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.rect.y = SCREEN_HEIGHT
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.speed_y = random.uniform(-5, -1)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# fishes
class Fish:
    def __init__(self, image):
        self.original_image = image

        #making pictures smaller
        base_width = 100
        aspect_ratio = self.original_image.get_height() / self.original_image.get_width()
        base_height = int(base_width * aspect_ratio)

        #random size
        scale_factor = random.uniform(0.6, 1.3)
        width = int(base_width * scale_factor)
        height = int(base_height * scale_factor)

        self.direction = random.choice([-1, 1])

        #scaling picture
        scaled_image = pygame.transform.scale(self.original_image, (width, height))

        if self.direction == -1:
            self.image = pygame.transform.flip(scaled_image, True, False)
        else:
            self.image = scaled_image

        self.rect = self.image.get_rect()

        if self.direction == 1:
            self.rect.x = random.randint(-200, -50)
        else:
            self.rect.x = random.randint(SCREEN_WIDTH + 50, SCREEN_WIDTH + 200)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - height - 50)

        self.speed_x = random.uniform(1.5, 3.5) * self.direction
        self.angle = random.uniform(0, math.pi * 2)
        self.angular_speed = random.uniform(0.001, 0.02)
        self.wave_amplitude = random.uniform(1, 3)

    def update(self):
        self.rect.x += self.speed_x
        self.angle += self.angular_speed
        self.rect.y += math.sin(self.angle) * self.wave_amplitude

        if self.direction == 1 and self.rect.left > SCREEN_WIDTH:
            self.rect.x = -self.rect.width
            self.rect.y = random.randint(50, SCREEN_HEIGHT - self.rect.height - 50)
        elif self.direction == -1 and self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH
            self.rect.y = random.randint(50, SCREEN_HEIGHT - self.rect.height - 50)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# instances
spawned_objects = []
for i in range(8):
    spawned_objects.append(Bubble(bubble_img))
for i in range(7):
    spawned_objects.append(Fish(fish_img))

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_img, (0, 0))

    for obj in spawned_objects:
        obj.update()
        obj.draw(screen)

    pygame.display.flip()
    clock.tick(60)

# Stopping music when stopping animation
pygame.mixer.music.stop()
pygame.quit()
sys.exit()