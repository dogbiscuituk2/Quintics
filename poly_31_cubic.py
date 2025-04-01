#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import BaseScene
from MF_Tools import *
from painter import *

class Poly_31_Cubic(BaseScene):

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

        E1z = self.make_tex(r'y=\sum_{i=0}^{3}a_ix^i=0')
        E1y = MathTex(r'Degree=n=3').set_color(self.ink_fg)
        E1b = self.make_tex(r'y=x^3+ax^2+bx+c')

        G = VGroup(E1z, E1y, E1b).arrange(DOWN)

        with self.say("The degree three polynomial, the cubic, has three roots."):
            self.play(Create(E1z))
            self.play(Create(E1y))
            self.play(Create(E1b))

            self.wait(2)
            self.play(FadeOut(G))

if __name__ == "__main__":
    BaseScene.run(__file__)
