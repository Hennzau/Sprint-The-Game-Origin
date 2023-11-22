### Imports
import pygame


# Here we define all functions related to sound and manage their volumes (except for the soundtrack)

def sound_collision():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('assets/sounds/Collision.wav')
    my_sound.set_volume(0.045)
    my_sound.play()


def sound_victory():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('assets/sounds/Victory_new.wav')
    my_sound.set_volume(0.08)
    my_sound.play()


def sound_swipe():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('assets/sounds/Swipe_new.wav')
    my_sound.set_volume(0.015)
    my_sound.play()
    pass


def sound_button():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('assets/sounds/Boup.wav')
    my_sound.set_volume(0.1)
    my_sound.play()


def sound_game_launched():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('assets/sounds/Game launched.wav')
    my_sound.set_volume(0.075)
    my_sound.play()

def sound_color_switch():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('assets/sounds/Color swticher.wav')
    my_sound.set_volume(0.025)
    my_sound.play()
