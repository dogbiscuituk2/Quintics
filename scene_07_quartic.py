from manim import *
from MF_Tools import *
from scene_00_base import Scene_00_Base
from texpaint import *

class Scene_07_Quartic(Scene_00_Base):

    def __init__(self):
        super().__init__()

    def construct(self):
        self.init()
        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        E1 = self.make_tex(r'y=\sum_{i=0}^{4}a_ix^i=0')
        E1a = MathTex(r'Degree=n=4').set_color(self.get_text_colour())
        E1b = self.make_tex(r'y=x^4+ax^3+bx^2+cx+d')

        VGroup(E1, E1a, E1b).arrange(DOWN)

        with self.say("The quartic, or degree four polynomial, has four roots."):
            self.play(Create(E1))
            self.play(Create(E1a))

            self.wait(2)
