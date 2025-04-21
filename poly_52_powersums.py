#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import BaseScene
from MF_Tools import *
from painter import *

#region data

e1 = (
    r'y &= \sum_{i=0}^{n>0} aᵢxⁱ = 0',
    r'y &= aₙxⁿ + aₙ₋₁xⁿ⁻¹ + aₙ₋₂xⁿ⁻² + \dots + a₁x + a₀ = 0',
    r'y &= \prod_{j=1}^{n}(x-xⱼ) = 0',
    r'y &= (x-x₁)(x-x₂)(x-x₃) \dots (x-xₙ₋₁)(x-xₙ) = 0',
    r'y &= xⁿ - (\sum_{j=1}^{n}xⱼ)xⁿ⁻¹ + \dots + (-1)ⁿ(\prod_{j=1}^{n}xⱼ) = 0',
)

e2 = (
   r'y &= xⁿ + aₙ₋₁xⁿ⁻¹ + aₙ₋₂xⁿ⁻² + \dots + a₁x + a₀ = 0',
)

e3 = (
    r'S_{m>0} &= \sum_{j=1}^{n} xⱼ^m = x₁^m + x₂^m + x₃^m + \dots + xₙ₋₁^m + xₙ^m',
    r'S_m &= -(\sum_{j=1}^{m-1} aₙ₋ₘ₊ⱼSⱼ) - maₙ₋ₘ, \quad a_{j<0} = 0',
     'S₁ &= -aₙ₋₁',
     'S₂ &= -aₙ₋₁S₁ - 2aₙ₋₂',
     'S₃ &= -aₙ₋₁S₂ - aₙ₋₂S₁ - 3aₙ₋₃',
     'S₄ &= -aₙ₋₁S₃ - aₙ₋₂S₂ - aₙ₋₃S₁ - 4aₙ₋₄',
     'S₅ &= -aₙ₋₁S₄ - aₙ₋₂S₃ - aₙ₋₃S₂ - aₙ₋₄S₁ - 5aₙ₋₅',
)

e4 = (
    r'S_m &= -(\sum_{j=1}^{m-1} a₅₋ₘ₊ⱼSⱼ) - ma_{5-m}, \quad a_{j<0} = 0',
    'S₁ &= -a₄',
    'S₂ &= -a₄S₁ - 2a₃',
    'S₃ &= -a₄S₂ - a₃S₁ - 3a₂',
    'S₄ &= -a₄S₃ - a₃S₂ - a₂S₁ - 4a₁',
    'S₅ &= -a₄S₄ - a₃S₃ - a₂S₂ - a₁S₁ - 5a₀',
    'S₆ &= -a₄S₅ - a₃S₄ - a₂S₃ - a₁S₂ - a₀S₁',
    'S₇ &= -a₄S₆ - a₃S₅ - a₂S₄ - a₁S₃ - a₀S₂',
    'S₈ &= -a₄S₇ - a₃S₆ - a₂S₅ - a₁S₄ - a₀S₃',
    'S₉ &= -a₄S₈ - a₃S₇ - a₂S₆ - a₁S₅ - a₀S₄',
    'S₁₀ &= -a₄S₉ - a₃S₈ - a₂S₇ - a₁S₆ - a₀S₅',
)

e6 = (
    'S₁ &= -a',
    'S₂ &= -aS₁ - 2b',
    'S₃ &= -aS₂ - bS₁ - 3c',
    'S₄ &= -aS₃ - bS₂ - cS₁ - 4d',
    'S₅ &= -aS₄ - bS₃ - cS₂ - dS₁ - 5e',
    'S₆ &= -aS₅ - bS₄ - cS₃ - dS₂ - eS₁',
    'S₇ &= -aS₆ - bS₅ - cS₄ - dS₃ - eS₂',
    'S₈ &= -aS₇ - bS₆ - cS₅ - dS₄ - eS₃',
    'S₉ &= -aS₈ - bS₇ - cS₆ - dS₅ - eS₄',
    'S₁₀ &= -aS₉ - bS₈ - cS₇ - dS₆ - eS₅',
)

e7 = (
    'S₁ &= -a',
    'S₂ &= a²-2b',
    'S₃ &= -a³+3(ab-c)',
    'S₄ &= a⁴-4(a²b-ac+d)+2b²',
    'S₅ &= -a⁵+5(a³b-a²c+ad-e+bc-ab²)',
    'S₆ &= a⁶-6(a⁴b-a³c+a²d-ae+2abc-bd)+9a²b²-2b³+3c²',
    'S₇ &= -aS₆ - bS₅ - cS₄ - dS₃ - eS₂',
    'S₈ &= -aS₇ - bS₆ - cS₅ - dS₄ - eS₃',
    'S₉ &= -aS₈ - bS₇ - cS₆ - dS₅ - eS₄',
    'S₁₀ &= -aS₉ - bS₈ - cS₇ - dS₆ - eS₅',
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
        E7 = self.make_texes(*e7)
        
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
            return TransformByGlyphMap(
                E5[row],
                E6[row],
                (list(glyphs), ShrinkToCenter),
                remove_individually=True)

        with self.say("and the coefficients with the original single letter ones, a b c d e."):
            self.play(FadeOut(E3[0]))
            self.play(TransformMatchingShapes(E4, E5))
            self.wait(5)
            self.play(
                foo(0,5),
                foo(1,5,11),
                foo(2,5,10,16),
                foo(3,5,10,15,21),
                foo(4,5,10,15,20,26),
                *[foo(row,5,10,15,20,25) for row in range(5,9)],
                foo(9,6,11,16,21,26)
                )
            
        with self.say("We could now substitute all the recurring S values, "):
            for row in range(len(E7)):
                self.play(TransformMatchingShapes(E6[row], E7[row]))
            pass

        self.wait(10)

#endregion

if __name__ == "__main__":
    BaseScene.run(__file__)
