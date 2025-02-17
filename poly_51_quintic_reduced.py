#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import BaseScene
import math
from MF_Tools import *
from painter import *

class Poly_51_Quintic_Reduced(BaseScene):

    def __init__(self):
        BaseScene.__init__(self)

    def construct(self):
        
        self.set_pens((
            ('o', Pen.BACKGROUND),
            ('[a-e]', Pen.GREEN),
            ('h', Pen.ORANGE),
            ('[p-s]', Pen.YELLOW),
            ('x', Pen.RED),
            ('y', Pen.MAGENTA),
            ('z', Pen.CYAN)))

        o = 'ox^5&=o'
        a = 'ax^4&=a'
        b = 'bx^3&=b'
        c = 'cx^2&=c'
        d = 'odx&=d'
        e = 'ooe&=e'

        p = '(z+h)'
        trans = 'xo&=oz+h'
        monic = 'yo&=ox^5+ax^4+bx^3+cx^2+dx+e=0'
        reduced = 'yo&=oz^5+0z^4+pz^3+qz^2+rz+s=0'

        Equations = self.make_texes(
            trans,
            monic,
            reduced,
            f'{o}{p}^5',
            f'{a}{p}^4',
            f'{b}{p}^3',
            f'{c}{p}^2',
            f'{d}{p}',
            e).shift(UP*0.5)

        with self.say("The degree five polynomial, the quintic, has five roots."):
            self.play(Create(Equations[1]))

            roots = -5, -3, -2, +1, +4
            axes = self.make_axes(4.5, 4.5, [-7, 7, 1], [-600, 600, 100])
            border = SurroundingRectangle(axes, buff=0, corner_radius=0.1, color=self.ink_fg)
            dots = VGroup(*[
                Dot(axes.coords_to_point(x, 0), radius=0.07)
                for x in roots])
            plot = axes.plot(
                lambda x: math.prod([(x - root) for root in roots]),
                [-5.825, 4.395, 0.02])
            x_trace = VGroup(plot, dots)
            x_trace.color = self.get_token_ink('x')
            z_trace = x_trace.copy()
            z_trace.color = self.get_token_ink('z')
            graph = VGroup(axes, x_trace, z_trace, border)
            graph.shift(DOWN*0.75)
            self.play(FadeIn(border, axes))
            self.play(Create(x_trace[0]), Create(dots), run_time=2)

        with self.say("We could solve it easily if we didn't have all these intermediate powers of x."):
            self.box_on(*Equations[1][0][7:21])

        with self.say("To make a start, we might first try to get rid of the quartic, x to the fourth, term."):
            self.box_on(*Equations[1][0][7:10])

        with self.say("In other words, transform it into so-called reduced form,"):
            brace = Brace(Group(Equations[1], Equations[2]), LEFT, color=self.ink_fg)
            self.play(FadeIn(brace), Create(Equations[2]))
            self.box_on(*Equations[2][0][7:10])

        with self.say("with this coefficient equal to zero."):
            self.play(Indicate(Equations[2][0][7], color=self.get_ink(Pen.WHITE), scale_factor=2, run_time=2))

        with self.say("This operation is technically known as a Tschirnhaus Transformation,"):
            image = ImageMobject("resources/Tschirnhaus.jpg")
            caption = MarkupText(
                    'Ehrenfried Walther von Tschirnhaus (1651-1708)',
                    color=self.ink_fg
                ).scale(0.25).rotate(-PI/2)
            picture = Group(image, caption).arrange(RIGHT, buff=0.1)
            picture.to_corner(DR, buff=0.5)
            self.play(FadeIn(picture))
            self.box_off()

        with self.say("the simplest example of which is a linear substitution, such as x = z + some constant h."):
            self.play(Create(Equations[0]))
            self.box_on(Equations[0])
            for dx in (2.5, -3.5, 2.0):
                self.play(z_trace.animate.shift(0.34*dx*RIGHT), run_time=1)

        with self.say("Let's use this to express all these x powers in terms of z."):
            E = Equations[1][0]
            S = E[4:6], E[7:10], E[11:14], E[15:18], E[19:21], E[22:23]
            self.play([
                TransformMatchingShapes(
                    S[i].copy(),
                    Equations[i+3][0][0:3],
                    path_arc=-PI/2)
                for i in range(6)],
                run_time=2)
            self.play(FadeOut(graph))
            for i in range(5):
                self.play(
                    TransformMatchingShapes(
                        Equations[0][0][3:].copy(),
                        Equations[i+3][0][3:]))
            self.play(FadeIn(Equations[8][0][3:]))
            self.box_off()

        p2 = f'{p}{p}'
        p3 = f'{p2}{p}'
        p4 = f'{p3}{p}'
        p5 = f'{p4}{p}'

        def do_animations(phase: int, formulae: List[List[str]]) -> None:

            def box(i: int, bump: int) -> Tuple[Group]:
                Hi = Equations[3][0]
                Lo = Equations[6-i][0]
                match phase:
                    case 1:
                        return Hi[4:], Lo[4:]
                    case 2:
                        k = 6*i+15+bump
                        return Hi[4:k], Lo[4:k]

            for i in range(4):
                self.box_on(*box(i, 0))
                animations = []
                for j in range(4-i):
                    Old = Equations[j+3]
                    New = self.make_tex(formulae[j][i])
                    New.move_to(Old, aligned_edge=LEFT)
                    animations.append(TransformMatchingShapes(Old, New))
                    Equations[j+3] = New
                animations.append(self.box_move(*box(i, 1)))
                self.play(*animations)
            self.box_off()

        with self.say("Expand these powers."):
            self.play(FadeOut(picture))
            do_animations(
                1,
                [
                    [f'{o}{p2}^4', f'{o}{p3}^3', f'{o}{p4}^2', f'{o}{p5}'],
                    [f'{a}{p2}^3', f'{a}{p3}^2', f'{a}{p4}'],
                    [f'{b}{p2}^2', f'{b}{p3}'],
                    [f'{c}{p2}']
                ])

        q2 = '(z^2+2hz+h^2)'
        q3 = '(z^3+3hz^2+3h^2z+h^3)'
        q4 = '(z^4+4hz^3+6h^2z^2+4h^3z+h^4)'
        q5 = 'z^5+5hz^4+10h^2z^3+10h^3z^2+5h^4z+h^5'

        with self.say("Multiply out the binomials."):
            do_animations(
                2,
                [
                    [f'{o}{q2}{p3}', f'{o}{q3}{p2}', f'{o}{q4}{p}', f'{o}{q5}'],
                    [f'{a}{q2}{p2}', f'{a}{q3}{p}', f'{a}{q4}'],
                    [f'{b}{q2}{p}', f'{b}{q3}'],
                    [f'{c}{q2}']
                ])

        with self.say("Distribute the original coefficients."):
            formulae = [
                    f'{a}z^4+4ahz^3+6ah^2z^2+4ah^3z+ah^4',
                    f'{b}z^3+3bhz^2+3bh^2z+bh^3',
                    f'{c}z^2+2chz+ch^2',
                    f'{d}z+dh']
            for j in range(4):
                S = Equations[j+4]
                T = self.make_tex(formulae[j])
                T.move_to(S, aligned_edge=LEFT)
                self.play(TransformMatchingShapes(S, T))
                Equations[j+4] = T
            self.play(FadeOut(Equations[0], brace, Equations[1], Equations[2][0][-2:]))

        self.wait(10)
        return


        def expand(i: int, immediate: bool = False) -> None:

            def move_box(grow: int=0) -> Animation:
                return self.box_move(*[EQU[j+3][1][0][k] for k in range(1, 6*(i-3)+grow) for j in range(0, 9-i)])

            if i in range(5, 9):
                self.play(move_box())
            fz = Fz[i]
            animations = []
            for j in range(1 if immediate else 0, len(fz)):
                source = EQU[j+3][1]
                target = fz[j]
                target.move_to(source, aligned_edge=LEFT)
                animation = TransformMatchingShapes(source, target)
                if immediate:
                    self.play(animation)
                else:
                    animations.append(animation)
                EQU[j+3][1] = target
            if not immediate:
                if i in range(5, 9):
                    animations.append(move_box(1))
                self.play(animations)

       
        Y = self.make_matrix((['y^1'], ['x^5'], ['ax^4'], ['bx^3'], ['cx^2'], ['dx^1'], ['eo^0']), margin = 0)
        EQ = self.make_tex('=')
        M = self.make_matrix((
            ('z^5', '0z^4', 'pz^3', 'qz^2', 'rz', 's'),
            ('z^5', '5hz^4', '10h^2z^3', '10h^3z^2', '5h^4z', 'h^5'),
            ('', 'az^4', '4ahz^3', '6ah^2z^2', '4ah^3z', 'ah^4'),
            ('', '', 'bz^3', '3bhz^2', '3bh^2z', 'bh^3'),
            ('', '', '', 'cz^2', '2chz', 'ch^2'),
            ('', '', '', '', 'dz', 'dh'),
            ('', '', '', '', '', 'e')),
            padding = 1.75)
        Z = self.make_matrix((('1'), ('1'), ('1'), ('1'), ('1'), ('1')), margin = 0)
        VGroup(Y, EQ, M, Z).arrange(RIGHT, aligned_edge=DOWN)
        EQ.move_to(EQ.get_center() + 2.8 * UP)
        Z.move_to(Z.get_center() + 0.4 * UP)

        with self.say("Expand these powers."):
            self.play(FadeOut(picture))
            for i in range(1, 5):
                expand(i)

        self.wait(10)
        return

        with self.say("Multiply out the binomials."):
            for i in range(5, 9):
                expand(i)
            self.box_off()

        with self.say("Distribute the original coefficients."):
            expand(9, immediate=True)

        with self.say("Now recall that this first z equation is just the sum of the six below it."):
            self.box_on(EQU[2])
            self.wait(2)
            self.box_on(*[EQU[i] for i in range(3, 9)])
            self.wait(2)
            self.box_off()

        with self.say("All seven of these equations are identities, true for every choice of x and corresponding z."):
            self.play(FadeOut(*EQU[0], *EQU[1], brace))
            self.play(TransformMatchingShapes(VGroup(*[EQU[i][0] for i in range(2, 9)]), Y), Create(EQ))
            self.play(TransformMatchingShapes(VGroup(*[EQU[i][1] for i in range(2, 9)]), M), Create(Z))

        Z2 = [] # Will hold the powers of z which fly into column vector Z1
        M2 = [] # Will hold the replacement terms for the main matrix

        def get_element(row: int, col: int):
            return M[0][row * 6 + col]
        
        def indicate(items: List[VMobject], size: float = 1.2) -> None:
            self.play(Indicate(VGroup(*items), color = self.get_colour(Pen.WHITE), scale_factor = size))

        def new_target(row: int, col: int):
            p = ('z^5', 'z^4', 'z^3', 'z^2', 'z', '1')
            mathTex: MathTex = self.make_tex(p[col])
            mathTex.move_to(get_element(row, col), RIGHT)
            Z2.append(mathTex)
            mathTex.generate_target()
            mathTex.target.move_to(Z[0][col], DOWN)
            return mathTex

        def rewrite(src: MathTex, tgt: MathTex) -> Transform:
            M2.append(tgt)
            s = src.tex_string.replace('^', '')
            i = s.find('z')
            maps = [([1], [1])]
            if i == 1:
                maps = [([1,2], ShrinkToCenter), (GrowFromCenter, [1])]
            elif i > 1:
                maps = [([i] if len(s) <= i + 1 else [i, i + 1], ShrinkToCenter)]
            return TransformByGlyphMap(src, tgt.move_to(src.get_center()), *maps)
        
        m2 = (
            ('1', '0', 'p', 'q', 'r', 's'),
            ('1', '5h', '10h^2', '10h^3', '5h^4', 'h^5'),
            ('', 'a', '4ah', '6ah^2', '4ah^3', 'ah^4'),
            ('', '', 'b', '3bh', '3bh^2', 'bh^3'),
            ('', '', '', 'c', '2ch', 'ch^2'),
            ('', '', '', '', 'd', 'dh'),
            ('', '', '', '', '', 'e'))

        with self.say("If we now consider the case z equals one, then all of these z powers vanish from the matrix."):
            for col in range(6):
                transforms: List[Transform] = []
                rows = range(col + 2)
                transforms = [MoveToTarget(new_target(row, col)) for row in rows]
                transforms.append(FadeOut(Z[0][col]))
                for row in rows:
                    transforms.append(rewrite(get_element(row, col), self.make_tex(m2[row][col])))
                if col < 5:
                    indicate([get_element(row, col) for row in rows])
                self.play(*transforms)
            #for row in range(7):
            #    M2.append(self.make_tex(m2[row][5]))

        self.wait(10)

        F1 = self.make_tex('y=x^5+ax^4+bx^3+cx^2+dx+e')
        F2 = self.make_tex('y=z^5+0z^4+pz^3+qz^2+rz+s')
        F3 = self.make_tex('z=x-h')
        F4 = self.make_tex('z=x+a/5')

        def setup(*args: str) -> MathTex:
            return VGroup(*[self.make_tex(arg) for arg in args]).arrange(DOWN, aligned_edge = LEFT).move_to(2 * LEFT + DOWN)

        F5 = setup('0=5h+a', 'p=10h^2+4ah+b'  , 'q=10h^3+6ah^2+3bh+c', 'r=5h^4+4ah^3+3bh^2+2ch+d'   , 's=h^5+a^4+bh^3+ch^2+dh+e')
        F6 = setup('a=-5h' , 'p=10h^2-20h^2+b', 'q=10h^3-30h^3+3bh+c', 'r=5h^4-20h^4+3bh^2+2ch+d'   , 's=h^5-5h^5+bh^3+ch^2+dh+e')
        F7 = setup('h=-a/5', 'p=-10h^2+b'     , 'q=-20h^3+3bh+c'     , 'r=-15h^4+3bh^2+2ch+d'       , 's=-4h^5+bh^3+ch^2+dh+e')
        F8 = setup('h=-a/5', 'p=b-10h^2'      , 'q=c+3bh-20h^3'      , 'r=d+2ch+3bh^2-15h^4'        , 's=e+dh+ch^2+bh^3-4h^5')
        F9 = setup('h=-a/5', 'p=b-2a^2/5'     , 'q=c-3ab/5+4a^3/25'  , 'r=d-2ac/5+3a^2b/25-3a^4/125', 's=e-ad/5+a^2c/25-a^3b/125-4a^5/3125')
        
        with self.say("Now we can read the matrix column by column, to get expressions for the new coefficients in terms of the old."):
            self.play(FadeOut(Y, EQ, M, M2[0], M2[1], Z[0][5], Z[1], Z[2], *Z2))
            for f_2 in (F5, F6, F7, F8):
                VGroup(F1, F2, F3, f_2).arrange(DOWN, aligned_edge = LEFT)
            VGroup(F1, F2, F4, F8).arrange(DOWN, aligned_edge = LEFT)

            M6 = [
                VGroup(*[M2[i] for i in range(2, 5)]),
                VGroup(*[M2[i] for i in range(5, 9)]),
                VGroup(*[M2[i] for i in range(9, 14)]),
                VGroup(*[M2[i] for i in range(14, 20)]),
                VGroup(*[M2[i] for i in range(20, 27)])]
            for i in range(5):
                self.play(TransformMatchingShapes(M6[i], F5[i], path_arc=PI/2))
        
        with self.say(
            """
            This h substitution avoids a lot of ugly fractions with powers of five denominators in the results. 
            Apply the substitution, collect like powers of h, and reorder for clarity. 
            """):
            indicate(F5[0])
            self.play(TransformMatchingShapes(F5[0], F6[0]))
            indicate(F6[0])
            for i in range(1, 5):
                #indicate(F5[i][[9, 9, 8, 6][i - 1]], size = 2)
                self.play(TransformMatchingShapes(F5[i], F6[i]))
                self.play(TransformMatchingShapes(F6[i], F7[i]))
                self.play(TransformMatchingShapes(F7[i], F8[i], path_arc=PI/2))
            indicate(F6[0])
            self.play(TransformMatchingShapes(F6[0], F7[0]))
            indicate(F7[0])

        with self.say("Finally we have succeeded in eliminating the quartic term."):
            self.play(FadeIn(F1))
            self.play(FadeIn(F2))
            self.play(FadeIn(F3))
            indicate([F3])
            self.play(TransformMatchingShapes(F3, F4))
            indicate([F4])
            self.wait(5)

        with self.say("Here are those ugly power of five denominators, if you prefer:"):
            for i in range(1, 5):
                F9[i].move_to(F8[i], aligned_edge=LEFT)
                self.play(TransformMatchingShapes(F8[i], F9[i]))
        self.wait(3)
        with self.say("Maybe not."):
            for i in range(1, 5):
                self.play(TransformMatchingShapes(F9[i], F8[i]))
        self.wait(3)
        self.play(FadeOut(F1), FadeOut(F2), FadeOut(F4), FadeOut(F7[0]), FadeOut(F8))

if __name__ == "__main__":
    BaseScene.run(__file__)
