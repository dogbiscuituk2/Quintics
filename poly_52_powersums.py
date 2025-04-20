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
    r'S_m &= -(\sum_{j=1}^{m-1} a_{n-m+j} S_j) - ma_{n-m}, \quad a_{j<0} = 0',
     'S_1 &= -a_{n-1}',
     'S_2 &= -a_{n-1} S_1 - 2a_{n-2}',
     'S_3 &= -a_{n-1} S_2 - a_{n-2} S_1 - 3a_{n-3}',
     'S_4 &= -a_{n-1} S_3 - a_{n-2} S_2 - a_{n-3} S_1 - 4a_{n-4}',
     'S_5 &= -a_{n-1} S_4 - a_{n-2} S_3 - a_{n-3} S_2 - a_{n-4} S_1 - 5a_{n-5}',
)

e4 = (
    r'S_m &= -(\sum_{j=1}^{m-1} a_{5-m+j} S_j) - ma_{5-m}, \quad a_{j<0} = 0',
    'S_1 &= -a_4',
    'S_2 &= -a_4 S_1 - 2a_3',
    'S_3 &= -a_4 S_2 - a_3 S_1 - 3a_2',
    'S_4 &= -a_4 S_3 - a_3 S_2 - a_2 S_1 - 4a_1',
    'S_5 &= -a_4 S_4 - a_3 S_3 - a_2 S_2 - a_1 S_1 - 5a_0',
    'S_6 &= -a_4 S_5 - a_3 S_4 - a_2 S_3 - a_1 S_2 - a_0 S_1',
    'S_7 &= -a_4 S_6 - a_3 S_5 - a_2 S_4 - a_1 S_3 - a_0 S_2',
    'S_8 &= -a_4 S_7 - a_3 S_6 - a_2 S_5 - a_1 S_4 - a_0 S_3',
    'S_9 &= -a_4 S_8 - a_3 S_7 - a_2 S_6 - a_1 S_5 - a_0 S_4',
    'S_{10} &= -a_4 S_9 - a_3 S_8 - a_2 S_7 - a_1 S_6 - a_0 S_5',
)

e6 = (
    'S_1 &= -a',
    'S_2 &= -a S_1 - 2b',
    'S_3 &= -a S_2 - b S_1 - 3c',
    'S_4 &= -a S_3 - b S_2 - c S_1 - 4d',
    'S_5 &= -a S_4 - b S_3 - c S_2 - d S_1 - 5e',
    'S_6 &= -a S_5 - b S_4 - c S_3 - d S_2 - e S_1',
    'S_7 &= -a S_6 - b S_5 - c S_4 - d S_3 - e S_2',
    'S_8 &= -a S_7 - b S_6 - c S_5 - d S_4 - e S_3',
    'S_9 &= -a S_8 - b S_7 - c S_6 - d S_5 - e S_4',
    'S_{10} &= -a S_9 - b S_8 - c S_7 - d S_6 - e S_5',
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
        E4 = self.make_texes(*e4[:9])
        E5 = self.make_texes(*e4[1:])
        E6 = self.make_texes(*e6)
        
        with self.say("This is the general polynomial of degree n, in one variable, x."):
            self.play(Create(E1[0]))

        with self.say("Let's unpack it."):
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
            self.play(Create(E3[2:6]))

        with self.say("Since we are dealing with the quintic, let's now replace n with 5, "):
            self.play(Create(E3[6:]))
            self.play([ReplacementTransform(E3[row], E4[row]) for row in range(6)])
            self.play(Create(E4[6:9]))

        def foo(row: int, *glyphs: int) -> None:
            return TransformByGlyphMap(E5[row], E6[row], (list(glyphs), FadeOut))

        with self.say("and the coefficients with the original single letter ones, a b c d e."):
            self.play(FadeOut(E3[0]))
            self.play(TransformMatchingShapes(E4, E5))
            self.wait(5)
            self.play(
                foo(0,5),
                *[foo(row,*([6,9,14,19,24][:row+1])) for row in range(1,5)],
                *[foo(row,5,10,15,20,25) for row in range(5,9)],
                foo(9,6,11,16,21,26)
                )

        self.wait(10)

#endregion

if __name__ == "__main__":
    BaseScene.run(__file__)
