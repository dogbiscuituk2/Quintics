#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import Animate, BaseScene
from painter import *
from equations.poly_91 import *

class Poly_91_Newton(BaseScene):

    def __init__(self):
        BaseScene.__init__(self)

    def construct(self):

        self.set_pens((
            #('o', Pen.BACKGROUND),
            ('[a-e]', Pen.GREEN),
            ('h', Pen.ORANGE),
            ('[p-s]', Pen.YELLOW),
            ('x', Pen.RED),
            ('y', Pen.MAGENTA),
            ('z', Pen.CYAN)))

        E = self.make_texes(e1, e2, e4, e5)

        with self.say("Let y be a polynomial, of degree n greater than zero, with coefficients a i,"):
            self.play(Create(E[0]))

        with self.say("and roots denoted by x j, for j between 1 and n,"):
            self.play(Create(E[1]))

        with self.say("and let S m be the sum of the m-th powers of these roots."):
            self.play(Create(E[2]))

        with self.say("We need to prove this recurrence relation between the power sums,"):
            p = 27
            self.box_on(E[3][0][:p])
            self.play(Create(E[3][0][:p]))

        with self.say("where all coefficients with a negative index are taken to be zero."):
            self.box_on(E[3][0][p+1:])
            self.play(FadeIn(E[3][0][p:]))

        self.box_off()

        self.wait(10)
        return

if __name__ == "__main__":
    BaseScene.run(__file__)
