from manim import *
from MF_Tools import *
from scene_00_base import Scene_00_Base
from texpaint import *

class Scene_06_Cubic(Scene_00_Base): 

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

        E1 = self.make_tex(r'y=\sum_{i=0}^{3}a_ix^i=0')
        E1a = MathTex(r'Degree=n=3').set_color(self.get_colour(Grey))
        E1b = self.make_tex(r'y=x^3+ax^2+bx+c')

        VGroup(E1, E1a, E1b).arrange(DOWN)

        with self.say("The cubic, or degree three polynomial, has three roots."):
            self.play(Create(E1))
            self.play(Create(E1a))

            self.wait(2)
