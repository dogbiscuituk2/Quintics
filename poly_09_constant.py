from painter_old import *
from base_scene import BaseScene

class Poly_09_Constant(BaseScene):

    def construct(self):
        self.init()

        self.set_pens((
            #('[Oo|]', ghost),
            (r'\\frac', red),
            (r'\\sqrt', orange),
            (r'[a-e]|\\alpha|\\beta|\\gamma|\\delta|\\epsilon', green),
            ('h', orange),
            (r'[p-s]|\\pi|\\rho\|\\sigma', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))

        E1z = self.make_ssmt(r'y=\sum_{i=0}^{0}a_ix^i=a_0=0')
        E1y = MathTex(r'Degree=n=0').set_color(self.get_text_colour())
        E1y.next_to(E1z, DOWN)
        E1b = self.make_ssmt(r'a_n\neq{0}')
        E1b.next_to(E1y, DOWN)

        with self.say("The degree zero polynomial has no roots."):
            self.play(Create(E1z))

        with self.say("Notice that the equation, y equals zero, can have no solutions."):
            self.play(Create(E1y))

        with self.say("This is because a n is constrained to be both zero and nonzero.") as tracker:
            self.play(Create(E1b))
            boxes = [self.box(E1b), self.box(E1y[0][7:10]), self.box(E1z[0][13:17])]
            self.wait(tracker.duration + 2)
            self.play(FadeOut(E1z, E1y, E1b, *boxes))
            self.wait(2)
