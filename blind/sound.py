import os

from pygame import mixer
from blind.hero import Hero


class Sound(object):
    def __init__(self):
        mixer.pre_init()
        mixer.init()
        self.footstep_channel = mixer.Channel(0)
        self.ping_channel = mixer.Channel(1)
        self.footstep_sound = mixer.Sound(os.path.join('sound', 'footsteps.ogg'))
        self.ping_sound = mixer.Sound(os.path.join('sound','metal.ogg'))

    def get_footstep_channel(self):
        return self.footstep_channel

    def play_footstep(self):
        if not self.get_footstep_channel().get_busy():
            self.get_footstep_channel().play(self.footstep_sound, loops=-1)

    def stop_footstep(self):
        self.get_footstep_channel().stop()

    def play_ping(self, direction):
        if self.ping_channel.get_busy():
            return
        if direction == Hero.LEFT:
            self.ping_channel.set_volume(1,0)
        elif direction == Hero.RIGHT:
            self.ping_channel.set_volume(0,1)
        elif direction == Hero.UP:
            self.ping_channel.set_volume(1,1)
        elif direction == Hero.DOWN:
            self.ping_channel.set_volume(.3)
        self.ping_channel.play(self.ping_sound)




