#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import BaseScene
from MF_Tools import *
from painter import *

class Poly_08_General(BaseScene):

    def __init__(self):
        BaseScene.__init__(self)

    def construct(self):

        self.set_pens((
            ('[a-e]]', Pen.GREEN),
            ('h', Pen.ORANGE),
            ('[p-s]', Pen.YELLOW),
            ('x', Pen.RED),
            ('y', Pen.MAGENTA),
            ('z', Pen.CYAN)))
        
        with self.say("This is a general polynomial equation in one variable, x."):
            F1 = self.make_tex(r'y=\sum_{i=0}^{n}a_ix^i')
            self.play(Create(F1))

        with self.say("It has degree n, where n is the highest power of x present."):
            self.flash(F1[0][9])
            F2 = MathTex(r'Degree=n').set_color(self.ink_fg)
            F2.next_to(F1, DOWN)
            self.play(Create(F2))
            self.flash(F1[0][2])

        with self.say("Note that this means a n is nonzero."):
            F3 = self.make_tex(r'a_n\neq{0}')
            F3.next_to(F2, DOWN)
            self.play(Create(F3))

        with self.say("Let's unpack this sum."):
            f4 = r'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0'
            F4 = self.make_tex(f4)
            arc = {"path_arc": PI}
            self.play(
                TransformByGlyphMap(F1, F4,
                    ([2,3,4,5,6], ShrinkToCenter),
                    ([7], [2,7,16,29,33], arc),
                    ([8], [3,8,9,10,17,18,19,30,34], arc),
                    ([9], [4,11,20,31], arc),
                    ([10], [5,12,13,14,21,22,23], arc),
                    (GrowFromCenter, [6,15,24,25,26,27,28,32])), 
                    run_time=2)

        with self.say("It has n roots, or values of x, for which y is zero."):            
            f5 = f'{f4}=0'
            F5 = self.make_tex(f5)
            self.play(TransformByGlyphMap(F4, F5, ([], [35, 36])))

        with self.say("To find these values, start by dividing by a n."):
            self.flash(F5[0][36]) # The zero on the RHS
            F6a = self.make_tex(
                r'\frac{y}{a_n}=\frac{a_n}{a_n}x^n+\frac{a_{n-1}}{a_n}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(
                F5,
                F6a,
                (GrowFromCenter, [1,7,17,29,43,50]),
                (FadeIn, [2,3,8,9,18,19,30,31,44,45,51,52]),
                introduce_individually=True))
            
            F6b = MathTex(r'\intertext{Let }').set_color(self.ink_fg)
            F6c = self.make_tex(r'b_i=a_i/a_n:')
            F6d = VGroup(F6b, F6c).arrange(RIGHT, aligned_edge=UP)
            F6d.next_to(F6a, UP, aligned_edge=LEFT)
            self.play(FadeOut(F2), FadeOut(F3), Create(F6d))

            F6e = self.make_tex( \
                r'\frac{a_n}{a_n}x^n+\frac{a_{n-1}}{a_n}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+' \
                    r'\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(F6a, F6e, ([*ir(0,4)], ShrinkToCenter)), run_time=1.5)

            F6f = self.make_tex( \
                r'x^n+\frac{a_{n-1}}{a_n}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+' \
                    r'\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(F6e, F6f, ([*ir(0,4)], ShrinkToCenter)), run_time=1.5)

            F6g = self.make_tex( \
                r'x^n+b_{n-1}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+' \
                    r'\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(F6f, F6g, ([7,8,9], ShrinkToCenter)), run_time=1.5)

            F6h = self.make_tex(r'x^n+b_{n-1}x^{n-1}+b_{n-2}x^{n-2}+...+b_1x+b_0=0')
            self.play(
                TransformByGlyphMap(
                    F6g,
                    F6h,
                    ([16,17,18,30,31,32,37,38,39], ShrinkToCenter),
                    remove_individually=True),
                run_time=1.5)

        with self.say("This is called the monic form, where the coefficient of the highest power of x is equal to one."):
            self.flash(F6c[0][6:8])

        with self.say("In fact this is often called the general form, as it has all the same roots as the original."):
            self.flash(VGroup(*F6a[0][2:4]))
            self.play(FadeOut(F6d))

        with self.say("If we know these roots, we can express the polynomial as a product of n linear factors."):
            F7 = self.make_tex(r'=\prod_{j=1}^{n}(x-x_j)')
            F7.next_to(F6a, DOWN)
            self.play(Create(F7))

        with self.say("Each factor corresponds to a root value of the polynomial."):
            F8 = self.make_tex(r'=(x-x_1)(x-x_2)(x-x_3)...(x-x_{n-1})(x-x_n)')
            F8.next_to(F6a, DOWN)
            arc = {"path_arc": PI}
            self.play(
                TransformByGlyphMap(
                    F7, F8,
                    ([1,2,3,4,5], ShrinkToCenter),
                    ([6], [1,7,13,22,30], arc),
                    ([7], [2,8,14,23,31], arc),
                    ([8], [3,9,15,21,32], arc),
                    ([9], [4,10,16,25,33], arc),
                    ([10], [5,11,17,26,27,28,34], arc),
                    ([11], [6,12,18,29,35], arc),
                    (GrowFromCenter, [19,20,24])), run_time=2)

        with self.say("x 1, x 2, and so on, up to x n."):
            for g in ((4,6), (10,12), (16,18), (25,29), (33,35)):
                self.flash(VGroup(*F8[0][g[0]:g[1]]), run_time=1)
            self.wait(2)
            self.play(FadeOut(F6h), FadeOut(F8))
            self.wait(2)

if __name__ == "__main__":
    import os
    module_name = os.path.abspath(__file__).split(os.sep)[-1]
    # py -m: run library module as a script (terminates option list)
    # manim -a: all scenes, -p: preview, -ql: 480p15, -qm: 720p30,
    # -qh: 1080p60, -qp: 1440p60, -qk: 2160p60.
    command_line = f'py -m manim render -a -p -ql {module_name}'
    print(command_line)
    os.system(command_line)
