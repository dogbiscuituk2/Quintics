from manim import *
from MF_Tools import *
from scene_00_base import Scene_00_Base
from texpaint import *

class Scene_05_Quadratic(Scene_00_Base):

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

        E1 = self.make_tex(r'y=\sum_{i=0}^{2}a_ix^i=0')
        E1a = MathTex(r'Degree=n=2').set_color(self.get_text_colour())
        E1b = self.make_tex(r'y=ax^2+bx+c')
        E1c = self.make_tex(r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}')

        VGroup(E1, E1a, E1b, E1c).arrange(DOWN)

        with self.say("The quadratic, or degree two polynomial, has two roots."):
            self.play(Create(E1))
            self.play(Create(E1a))

        with self.say("It's usually solved directly, using this formula, without conversion to the monic form."):
            self.play(Create(E1b))
            self.play(Create(E1c))

            self.wait(2)
            self.play(FadeOut(E1, E1a))
            self.wait(2)

