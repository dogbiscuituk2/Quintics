#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import BaseScene
from MF_Tools import *
from painter import *

class Poly_21_Quadratic(BaseScene):

    def __init__(self):
        BaseScene.__init__(self)

    def construct(self):

        self.set_pens(
            ('[a-e]', Pen.GREEN),
            ('h', Pen.ORANGE),
            ('[p-s]', Pen.YELLOW),
            ('x', Pen.RED),
            ('y', Pen.MAGENTA),
            ('z', Pen.CYAN))

        E1z = self.make_tex(r'y=\sum_{i=0}^{2}a_ix^i=0')
        E1y = MathTex(r'Degree=n=2').set_color(self.ink_fg)
        E1b = self.make_tex(r'y=ax^2+bx+c')
        E1c = self.make_tex(r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}')

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

if __name__ == "__main__":
    BaseScene.run(__file__)
