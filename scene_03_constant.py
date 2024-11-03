from manim import *
from MF_Tools import *
from scene_00_base import Scene_00_Base
from texpaint import *

class Scene_03_Constant(Scene_00_Base):

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

        E1 = self.make_tex(r'y=\sum_{i=0}^{0}a_ix^i=a_0=0')
        E1a = MathTex(r'Degree=n=0').set_color(self.get_text_colour())
        E1a.next_to(E1, DOWN)
        E1b = self.make_tex(r'a_n\neq{0}')
        E1b.next_to(E1a, DOWN)

        with self.say("The constant, or degree zero polynomial, has no roots."):
            self.play(Create(E1))

        with self.say("Notice that the equation, y equals zero, can have no solutions."):
            self.play(Create(E1a))

        with self.say("This is because a n is constrained to be both zero and nonzero.") as tracker:
            self.play(Create(E1b))
            boxes = [self.box(E1b), self.box(E1a[0][7:10]), self.box(E1[0][13:17])]
            self.wait(tracker.duration + 2)
            self.play(FadeOut(E1, E1a, E1b, *boxes))
            self.wait(2)

