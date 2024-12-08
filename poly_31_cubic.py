from MF_Tools import *
from painter_old import *
from base_scene import BaseScene

class Poly_31_Cubic(BaseScene):

    def construct(self):
        self.init()

        self.set_colour_map((
            ('[a-e]', green),
            ('h', orange),
            ('[p-s]', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))

        E1z = self.make_tex(r'y=\sum_{i=0}^{3}a_ix^i=0')
        E1y = MathTex(r'Degree=n=3').set_color(self.get_text_colour())
        E1b = self.make_tex(r'y=x^3+ax^2+bx+c')

        G = VGroup(E1z, E1y, E1b).arrange(DOWN)

        with self.say("The degree three polynomial, the cubic, has three roots."):
            self.play(Create(E1z))
            self.play(Create(E1y))
            self.play(Create(E1b))

            self.wait(2)
            self.play(FadeOut(G))
