from MF_Tools import *
from painter_old import *
from base_scene import BaseScene

class Poly_21_Quadratic(BaseScene):

    def construct(self):
        self.init()

        self.set_pens((
            ('[a-e]', green),
            ('h', orange),
            ('[p-s]', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))

        E1z = self.make_ssmt(r'y=\sum_{i=0}^{2}a_ix^i=0')
        E1y = MathTex(r'Degree=n=2').set_color(self.get_text_colour())
        E1b = self.make_ssmt(r'y=ax^2+bx+c')
        E1c = self.make_ssmt(r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}')

        VGroup(E1z, E1y, E1b, E1c).arrange(DOWN)

        with self.say("The degree two polynomial, the quadratic, has two roots."):
            self.play(Create(E1z))
            self.play(Create(E1y))

        with self.say("It's usually solved directly, using this formula, without conversion to the monic form."):
            self.play(Create(E1b))
            self.play(Create(E1c))

            self.wait(2)
            self.play(FadeOut(E1z, E1y, E1b, E1c))
            self.wait(2)
