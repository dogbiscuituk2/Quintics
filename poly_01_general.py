from MF_Tools import *
from painter import *
from poly_00_base import Poly_00_Base

class Poly_01_General(Poly_00_Base):

    def construct(self):
        self.init()

        self.set_colour_map((
            ('abcde', green),
            ('h', orange),
            ('pqrs', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))
        
        with self.say("This is a general polynomial equation in one variable, x."):
            F1 = self.make_tex(r'y=\sum_{i=0}^{n}a_ix^i')
            self.play(Create(F1))

        with self.say("It has degree n, where n is the highest power of x present."):
            self.flash(F1[0][10])
            F2 = MathTex(r'Degree=n').set_color(self.get_text_colour())
            F2.next_to(F1, DOWN)
            self.play(Create(F2))
            self.flash(F1[0][3])

        with self.say("Note that this means a n is nonzero."):
            F3 = self.make_tex(r'a_n\neq{0}')
            F3.next_to(F2, DOWN)
            self.play(Create(F3))

        with self.say("Let's unpack this sum."):
            F4 = self.make_tex(r'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0')
            arc = {"path_arc": PI}
            self.play(
                TransformByGlyphMap(
                    F1, F4,
                    ([3,4,5,6,7], ShrinkToCenter),
                    ([8], [3,8,17,30,34], arc),
                    ([9], [4,9,10,11,18,19,20,31,35], arc),
                    ([10], [5,12,21,32], arc),
                    ([11], [6,13,14,15,22,23,24], arc),
                    (GrowFromCenter, [7,16,25,26,27,28,29,33])), run_time=2)
            
        with self.say("It has n roots, or values of x, for which y is zero."):            
            F5 = self.make_tex(r'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0=0')
            self.play(TransformByGlyphMap(F4, F5, ([], [36, 37])))

        with self.say("To find these values, start by dividing throughout by a n."):

            self.flash(F5[0][37]) # The zero on the RHS

            F6a = self.make_tex(r'\frac{y}{a_n}=\frac{a_n}{a_n}x^n+\frac{a_{n-1}}{a_n}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(
                F5,
                F6a,
                (GrowFromCenter, [2,8,18,30,44,51]),
                (FadeIn, [3,4,9,10,19,20,31,32,45,46,52,53]),
                introduce_individually=True))

            F6b = MathTex(r'\intertext{Let }').set_color(self.get_text_colour())
            F6c = self.make_tex(r'b_i=a_i/a_n:')
            F6d = VGroup(F6b, F6c).arrange(RIGHT, aligned_edge=UP)
            F6d.next_to(F6a, UP, aligned_edge=LEFT)
            self.play(FadeOut(F2), FadeOut(F3), Create(F6d))

            F6e = self.make_tex( \
                r'\frac{a_n}{a_n}x^n+\frac{a_{n-1}}{a_n}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+' \
                    r'\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(F6a, F6e, ([*ir(1,5)], ShrinkToCenter)), run_time=1.5)

            F6f = self.make_tex( \
                r'x^n+\frac{a_{n-1}}{a_n}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+' \
                    r'\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(F6e, F6f, ([*ir(1,5)], ShrinkToCenter)), run_time=1.5)

            F6g = self.make_tex( \
                r'x^n+b_{n-1}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+' \
                    r'\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(F6f, F6g, ([8,9,10], ShrinkToCenter)), run_time=1.5)

            F6h = self.make_tex(r'x^n+b_{n-1}x^{n-1}+b_{n-2}x^{n-2}+...+b_1x+b_0=0')
            self.play(
                TransformByGlyphMap(
                    F6g,
                    F6h,
                    ([17,18,19,31,32,33,38,39,40], ShrinkToCenter),
                    remove_individually=True),
                run_time=1.5)

        with self.say("This is called the monic form, where the coefficient of the highest power of x is equal to one."):
            self.flash(F6c[0][7:9])

        with self.say("In fact this is often called the general form, as it has all the same roots as the original."):
            self.flash(VGroup(*F6a[0][3:5]))
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
                    ([2,3,4,5,6], ShrinkToCenter),
                    ([7], [2,8,14,23,31], arc),
                    ([8], [3,9,15,24,32], arc),
                    ([9], [4,10,16,22,33], arc),
                    ([10], [5,11,17,26,34], arc),
                    ([11], [6,12,18,27,28,29,35], arc),
                    ([12], [7,13,19,30,36], arc),
                    (GrowFromCenter, [20,21,25])), run_time=2)
            
        with self.say("x 1, x 2, and so on, up to x n."):
            for g in ((5,7), (11,13), (17,19), (26,30), (34,36)):
                self.flash(VGroup(*F8[0][g[0]:g[1]]), run_time=1)
            self.wait(2)
            self.play(FadeOut(F6h), FadeOut(F8))
            self.wait(2)
