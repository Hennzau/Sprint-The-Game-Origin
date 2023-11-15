import pygame


def sound_collision():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('Collision.wav')
    my_sound.play()
