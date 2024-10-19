from manim import *
from manim_voiceover import VoiceoverScene

from common import *

class Quintic02(VoiceoverScene):
    def construct(self):

        init(self)
        set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        with self.voiceover(text="This is the General Form of a quintic polynomial equation in one variable, x.") as tracker:
            say(tracker)
            self.play(Create(EQU[1]))
            dump()
