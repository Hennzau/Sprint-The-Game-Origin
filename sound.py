import pygame


def sound_collision():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('Collision.wav')
    my_sound.play()


def sound_victory():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('Victory.wav')
    my_sound.play()


def sound_swipe():
    pass


def sound_background():
    pass
