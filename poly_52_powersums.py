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
    r'S_{m>0} &= \sum_{j=1}^{n} x_j^m = x_1^m + x_2^m + x_3^m + \dots + x_{n-1}^m + x_n^m',
    r'S_m &= -ma_{n-m} - \sum_{j=1}^{m-1} a_{n-m+j} S_j, \quad a_{j<0} = 0',
     'S_1 &= -a_{n-1}',
     'S_2 &= -2a_{n-2} - a_{n-1} S_1',
     'S_3 &= -3a_{n-3} - a_{n-2} S_1 - a_{n-1} S_2',
     'S_4 &= -4a_{n-4} - a_{n-3} S_1 - a_{n-2} S_2 - a_{n-1} S_3',
     'S_5 &= -5a_{n-5} - a_{n-4} S_1 - a_{n-3} S_2 - a_{n-2} S_3 - a_{n-1} S_4',
)

e4 = (
    r'S_m &= -ma_{5-m} - \sum_{j=1}^{m-1} a_{5-m+j} S_j, \quad a_{j<0} = 0',
     'S_1 &= -a_4',
     'S_2 &= -2a_3 - a_4 S_1',
     'S_3 &= -3a_2 - a_3 S_1 - a_4 S_2',
     'S_4 &= -4a_1 - a_2 S_1 - a_3 S_2 - a_4 S_3',
     'S_5 &= -5a_0 - a_1 S_1 - a_2 S_2 - a_3 S_3 - a_4 S_4',
     'S_6 &= -a_0 S_1 - a_1 S_2 - a_2 S_3 - a_3 S_4 - a_4 S_5',
     'S_7 &= -a_0 S_2 - a_1 S_3 - a_2 S_4 - a_3 S_5 - a_4 S_6',
     'S_8 &= -a_0 S_3 - a_1 S_4 - a_2 S_5 - a_3 S_6 - a_4 S_7',
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
        E2 = self.make_texes(e2[0], e1[4], *e3[:3])
        E3 = self.make_texes(*e3[1:])
        E4 = self.make_texes(*e4)
        
        with self.say("This is the general polynomial of degree n, in one variable, x."):
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
            self.play(FadeOut(E1[0], E1[2:4]))
            self.play(
                ReplacementTransform(E1[1], E2[0]),
                ReplacementTransform(E1[4], E2[1]))

        with self.say("For example, the coefficient of x to the power n minus one"):
            self.box_on(E1[1][0][5:9])

        with self.say("is equal to minus the sum of the roots, "):
            self.box_on(E1[4][0][4:14])

        with self.say("and the constant term"):
            self.box_on(E1[1][0][-4:-2])

        with self.say("is equal to their product, "):
            self.box_on(E1[4][0][28:37])

        with self.say("negated if n is odd."):
            self.box_on(E1[4][0][23:37])
            self.wait(2)

        with self.say("Let S m be the sum of the m-th powers of all n roots."):
            self.box_off()
            self.play(Create(E2[2]))

        with self.say("Then we have this handy recurrence relation to compute these sums."):
            self.play(Create(E2[3]))

        with self.say("We've already seen the formula for S 1"):
            self.box_on(E1[4][0][4:14])
            self.play(Create(E2[4]))
            self.box_on(E1[1][0][5:9])
            self.wait()
            self.box_off()

        with self.say("Here are a few more power sums in the series."):
            self.play(FadeOut(E2[:3]))
            self.play(
                ReplacementTransform(E2[3], E3[0]),
                ReplacementTransform(E2[4], E3[1]))
            self.play(Create(E3[2:]))

        with self.say("Since we are dealing with the quintic, let's now replace n with 5."):
            self.play(
                *[ReplacementTransform(E3[row], E4[row]) for row in range(6)],
                FadeIn(E4[6:]))

        self.wait(10)

#endregion

if __name__ == "__main__":
    BaseScene.run(__file__)
