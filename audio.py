from pygame import mixer

def play_sound(fileName):
    mixer.init()  # Initializing the mixer
    mixer.music.load(fileName)  # Loading the sound file
    mixer.music.play()

def play_sound_nonzero(fileName):
    mixer.music.load(fileName)
    mixer.music.play()

def play_sound_zero(fileName):
    mixer.music.load(fileName)
    mixer.music.play()

def play_sound_infinite(fileName):
    mixer.init()
    mixer.music.load(fileName)
    mixer.music.play(-1)  # Play the sound in an infinite loop
