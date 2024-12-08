from MF_Tools import *
from painter_old import *
from base_scene import BaseScene

class Poly_41_Quartic(BaseScene):

    def construct(self):
        self.init()

        self.set_colour_map((
            ('[a-e]', green),
            ('h', orange),
            ('[p-s]', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))

        E1z = self.make_tex(r'y=\sum_{i=0}^{4}a_ix^i=0')
        E1y = MathTex(r'Degree=n=4').set_color(self.get_text_colour())
        E1b = self.make_tex(r'y=x^4+ax^3+bx^2+cx+d')

        G = VGroup(E1z, E1y, E1b).arrange(DOWN)

        with self.say("The degree four polynomial, the quartic, has four roots."):
            self.play(Create(E1z))
            self.play(Create(E1y))
            self.play(Create(E1b))

            self.wait(2)
            self.play(FadeOut(G))
