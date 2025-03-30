#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import Animate, BaseScene
from painter import *

#region data

e1 = (
    r'y &= \sum_{i=0}^{n>0} a_i x^i, \quad a_n=1',
    r'&= x^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + \ldots + a_2 x^2 + a_1 x + a_0',
    r'&= (x-x_1)(x-x_2) \ldots (x-x_n)',
    r'&= \prod_{j=1}^{n} (x-x_j)',
#),(
#    r'S_{m>0} &= \sum_{j=1}^{n} x_j^m = x_1^m + x_2^m + \ldots + x_n^m',
#),(
#    r'S_m &= -ma_{n-m}-\sum_{j=1}^{m-1} a_{j+n-m} S_j, \quad a_{j<0}=0',
)

#endregion

#region code

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

        E1 = self.make_texes(*e1)

        with self.say("Let y be a monic polynomial of degree n greater than zero, with coefficients a i. "):
            self.play(Create(E1[0]))
            self.play(Create(E1[1]))

        with self.say("It has n roots, denoted by x 1, x 2, and so on, up to x n, "):
            self.play(Create(E1[2]))

        with self.say("so it can also be expressed as the product of n linear factors. "):
            self.play(Create(E1[3]))

        #with self.say("and let S m be the sum of the m-th powers of these roots."):
        #    self.play(Create(E1[2]))

        #with self.say("We need to prove this recurrence relation between the power sums,"):
        #    p = 25
        #    self.box_on(E1[3][0][:p])
        #    self.play(Create(E1[3][0][:p]))

        #with self.say("where all coefficients with a negative index are taken to be zero."):
        #    self.box_on(E1[3][0][p+1:])
        #    self.play(FadeIn(E1[3][0][p:]))

        #self.box_off()

        self.wait(10)
        return

#endregion

if __name__ == "__main__":
    BaseScene.run(__file__)
