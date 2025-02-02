from MF_Tools import *
from painter_old import *
from base_scene import BaseScene

class Poly_11_Linear(BaseScene):

    def construct(self):
        self.init()

        self.set_pens((
            ('[a-e]', green),
            ('h', orange),
            ('[p-s]', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))

        E1z = self.make_ssmt(r'y=\sum_{i=0}^{1}a_ix^i=0')
        E1y = MathTex(r'Degree=n=1').set_color(self.get_text_colour())
        E1y.next_to(E1z, DOWN)
        E1b = self.make_ssmt(r'a_1x+a_0=0').next_to(E1y, DOWN)
        E1c = self.make_ssmt(r'a_1x=-a_0').next_to(E1y, DOWN)
        E1d = self.make_ssmt(r'x=-a_0/a_1').next_to(E1y, DOWN)
        E1e = self.make_ssmt(r'x_1=-a_0/a_1').next_to(E1y, DOWN)

        with self.say(
            """
            The degree one polynomial has a single root because  
            the equation y equals zero has one solution.
            """):
            self.play(Create(E1z))
            self.play(Create(E1y))

        with self.say("Solving it is easy."):
            self.play(Create(E1b))
            self.wait(1)
            arc = {"path_arc": PI}
            self.play(TransformByGlyphMap(
                E1b, E1c,
                #([4], [5], arc),
                #([5], [6], arc),
                #([6], [7], arc),
                ([7], [4], arc),
                ([8], ShrinkToCenter)))
            self.wait(1)
            self.play(TransformByGlyphMap(
                E1c, E1d,
                #([1], [7], arc),
                #([2], [8], arc),
                ([3], [1], arc),
                ([4], [2], arc),
                ([5], [3], arc),
                ([6], [4], arc),
                ([7], [5], arc),
                (FadeIn, [6])))
            self.wait(1)
            self.play(TransformByGlyphMap(E1d, E1e, (GrowFromCenter, [2])))
            self.wait(2)
            self.play(FadeOut(E1z, E1y, E1e))
            self.wait(2)
