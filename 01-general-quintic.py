from manim import *
from manim_voiceover import VoiceoverScene
#from MF_Tools import *

from common import *

class Quintic01(VoiceoverScene):
    def construct(self):

        init(self)
        set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))
        
        print(f"Manim Community version {version('manim')}")
        print(f"MF Tools version {version('MF_Tools')}")
        print(f"Manum Voiceover version {version('manim_voiceover')}")

        print()
        print(version("manim_voiceover"))
        #print(version("MF_Tools"))
        
        #g1 = make_sum("x_0^i")
        #g2 = make_sum("x_0^i", "i=0")
        #g3 = make_sum("x_0^i", "i=0", "j+1")
        #g = VGroup(g1, g2, g3).arrange(RIGHT, aligned_edge= LEFT, buff=1)

        #self.play(Create(g))
        self.wait(5)
