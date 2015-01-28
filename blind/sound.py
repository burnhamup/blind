import os

from pygame import mixer


class Sound(object):
    def __init__(self):
        mixer.pre_init()
        mixer.init()
        self.footstep_channel = mixer.find_channel(True)
        self.footstep_sound = mixer.Sound(os.path.join('sound', 'footsteps.ogg'))

    def get_footstep_channel(self):
        return self.footstep_channel

    def play_footstep(self):
        if not self.get_footstep_channel().get_busy():
            self.get_footstep_channel().play(self.footstep_sound, loops=-1)

    def stop_footstep(self):
        self.get_footstep_channel().stop()


