import pygame


def sound_collision():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('assets/sounds/Collision.wav')
    my_sound.set_volume(0.25)
    my_sound.play()


def sound_victory():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('assets/sounds/Victory_new.wav')
    my_sound.set_volume(0.75)
    my_sound.play()


def sound_swipe():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('assets/sounds/Swipe_new.wav')
    my_sound.set_volume(0.03)
    my_sound.play()
    pass


def sound_background():
    pass

def sound_button(bool):
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('assets/sounds/Boup.wav')
    my_sound.set_volume(0.05)
    if not bool:
        my_sound.play()
    pass

def sound_game_launched():
    pass