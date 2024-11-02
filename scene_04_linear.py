from manim import *
from MF_Tools import *
from scene_00_base import Scene_00_Base
from texpaint import *

class Scene_04_Linear(Scene_00_Base): 

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

        E1 = self.make_tex(r'y=\sum_{i=0}^{1}a_ix^i=0')
        E1a = MathTex(r'Degree=n=1').set_color(self.get_colour(Grey))
        E1a.next_to(E1, DOWN)
        E1b = self.make_tex(r'a_1x+a_0=0').next_to(E1a, DOWN)
        E1c = self.make_tex(r'a_1x=-a_0').next_to(E1a, DOWN)
        E1d = self.make_tex(r'x=-a_0/a_1').next_to(E1a, DOWN)
        E1e = self.make_tex(r'x_1=-a_0/a_1').next_to(E1a, DOWN)

        with self.say(
            """
            The linear, or degree one polynomial, has a single root because  
            the equation y equals zero has one solution.
            """):
            self.play(Create(E1))
            self.play(Create(E1a))

        with self.say("Solving it is easy."):
            self.play(Create(E1b))
            self.wait(1)
            arc = {"path_arc": PI}
            self.play(TransformByGlyphMap(
                E1b, E1c,
                ([4], [5], arc),
                ([5], [6], arc),
                ([6], [7], arc),
                ([7], [4], arc),
                ([8], ShrinkToCenter)))
            self.wait(1)
            self.play(TransformByGlyphMap(
                E1c, E1d,
                ([1], [7], arc),
                ([2], [8], arc),
                ([3], [1], arc),
                ([4], [2], arc),
                ([5], [3], arc),
                ([6], [4], arc),
                ([7], [5], arc),
                (FadeIn, [6])))
            self.wait(1)
            self.play(TransformByGlyphMap(E1d, E1e, (GrowFromCenter, [2])))
            self.wait(2)
            self.play(FadeOut(E1, E1a, E1e))
            self.wait(2)

