from pygame import mixer


class SoundManager:

    def __init__(self):
        mixer.music.load('sounds/main_menu.mp3')
        mixer.music.play(-1)
        self.setVolume(0.5)

    def loadMusic(self, mp3Dir):
        mixer.music.load(mp3Dir)
        mixer.music.play(-1)

    def setVolume(self, vol):
        mixer.music.set_volume(vol)