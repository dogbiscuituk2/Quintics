#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import BaseScene
from MF_Tools import *
from painter import *

#region data

e1 = (
    r'y &= \sum_{i=0}^{n>0} a_i x^i = 0',
    r'y &= a_nx^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + \dots + a_1x + a_0 = 0',
    r'y &= \prod_{j=1}^{n}(x - x_j) = 0',
    r'y &= (x - x_1)(x - x_2)(x - x_3) \dots (x - x_{n-1})(x - x_n) = 0',
    r'y &= x^n - (\sum_{j=1}^{n}x_j)x^{n-1} + \dots + (-1)^n(\prod_{j=1}^{n}x_j) = 0',
)

e2 = (
   r'y &= x^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + \dots + a_1x + a_0 = 0',
)

e3 = (
    r'S_m &= \sum_{j=1}^{n} x_j^m = x_1^m + x_2^m + x_3^m + \dots + x_{n-1}^m + x_n^m',
    r'S_m &= -ma_{n-m} - \sum_{j=1}^{m-1} a_{j+n-m} S_j, \quad a_{j<0} = 0',
)

#endregion

#region Code

class Poly_52_PowerSums(BaseScene):

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
        
        E1 = self.make_texes(*e1)
        
        with self.say("This is a general polynomial equation of degree n, in one variable, x."):
            self.play(Create(E1[0]))

        with self.say("Let's unpack this sum."):
            arc = {"path_arc": -PI/2}
            self.play(
                TransformByGlyphMap(
                    E1[0].copy(),
                    E1[1],
                    (ir(2,8), ShrinkToCenter),
                    ([9], [2,7,16,29,33], arc),
                    ([10], [3,8,9,10,17,18,19,30,34], arc),
                    ([11], [4,11,20,31], arc),
                    ([12], [5,12,13,14,21,22,23], arc),
                    (GrowFromCenter, [6,15,*ir(24,28),32]),
                ),
                run_time=2)
            
            
        with self.say("We can always scale things so this leading term has a coefficient of one."):
            E1[1] = self.autopilot(E1[1], e2[0], 2, 6, 4, ([2,3], FadeOut))

        with self.say("This polynomial has n roots, values of x for which y is zero."):
            self.box_off()
            self.play(Create(E1[2]))
    
        with self.say("So we can also express it as a product of n linear factors, one for each root."):
            arc = {"path_arc": -PI/2}
            self.play(
                TransformByGlyphMap(
                    E1[2].copy(),
                    E1[3],
                    (ir(2,6), ShrinkToCenter),          # \prod
                    ([ 7], [2,8,14,23,31], arc),        # (
                    ([ 8], [3,9,15,24,32], arc),        # x
                    ([ 9], [4,10,16,25,33], arc),       # -
                    ([10], [5,11,17,26,34], arc),       # x
                    ([11], [6,12,18,27,28,29,35], arc), # j
                    ([12], [7,13,19,30,36], arc),       # )
                    (GrowFromCenter, ir(20,22)),        # \dots
                ),
                run_time=2)
            
        with self.say("Multiplying out, we get the coefficients expressed in terms of these roots."):
            self.play(Create(E1[4]))

        with self.say("Vieta's formulae."):
            self.play(FadeOut(E1[0], E1[2], E1[3]))
            G = VGroup(E1[1].copy(), E1[4].copy()).arrange(DOWN, aligned_edge=LEFT)
            self.play(
                Transform(E1[1], G[0]),
                Transform(E1[4], G[1]))

        with self.say("For example, the coefficient of x to the power n minus one"):
            self.box_on(E1[1][0][5:9])

        with self.say("is equal to minus the sum of the roots"):
            self.box_on(E1[4][0][4:14])

        with self.say("and the constant term"):
            self.box_on(E1[1][0][-4:-2])

        with self.say("is equal to their product, "):
            self.box_on(E1[4][0][28:37])

        with self.say("negated if n is odd."):
            self.box_on(E1[4][0][23:37])
            self.wait(2)
            
        self.box_off()

        self.wait(10)

#endregion

if __name__ == "__main__":
    BaseScene.run(__file__)
