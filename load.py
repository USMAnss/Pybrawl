import pygame

#Used pygame guide basic guide for increasing performance:
#http://www.pygame.org/docs/tut/newbieguide.html
def load_image(path):
    return pygame.image.load(path).convert_alpha()

def load_sound(path):
    return pygame.mixer.Sound(path)
