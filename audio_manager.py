import pygame

# Things to set up audio for terminal

def init_mixer():
    pygame.mixer.init(buffer=2048)
    pygame.mixer.set_num_channels(20)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load("audio/mother.wav")

def load_sounds():
    sound1 = pygame.mixer.Sound("audio/typewriter-key-even.wav")
    sound1.set_volume(0.1)
    return sound1

init_mixer()
sound1 = load_sounds()
