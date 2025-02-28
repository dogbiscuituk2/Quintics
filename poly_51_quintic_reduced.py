#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import BaseScene
from labels import *
import math
from MF_Tools import *
from painter import *

class Poly_51_Quintic_Reduced(BaseScene):

    def __init__(self):
        BaseScene.__init__(self)

    def construct(self):

        #self.options |= Opt.DEBUG_SILENT
        
        self.set_pens((
            #('o', Pen.BACKGROUND),
            ('[a-e]', Pen.GREEN),
            ('h', Pen.ORANGE),
            ('[p-s]', Pen.YELLOW),
            ('x', Pen.RED),
            ('y', Pen.MAGENTA),
            ('z', Pen.CYAN)))

        o = r'x^5&=\phantom{o}'
        a = 'ax^4&=a'
        b = 'bx^3&=b'
        c = 'cx^2&=c'
        d = 'dx&=d'
        e = 'e&=e'

        p = '(z+h)'
        trans = 'x&=z+h'
        monic = 'y&=x^5+ax^4+bx^3+cx^2+dx+e=0'
        reduced = 'y&=z^5+0z^4+pz^3+qz^2+rz+s'

        Equ = self.make_texes(
            trans,
            monic,
            reduced,
            f'{o}{p}^5',
            f'{a}{p}^4',
            f'{b}{p}^3',
            f'{c}{p}^2',
            f'{d}{p}',
            e)

        def make_trace(
            plot: ParametricFunction,
            plot_token: str,
            dots: VGroup,
            dots_token: str) -> VGroup:
            plot.color = self.get_token_ink(plot_token)
            dots.color = self.get_token_ink(dots_token)
            return VGroup(plot, dots)

        with self.say("The degree five polynomial, the quintic, has five roots."):
            self.play(Create(Equ[1]))

            roots = -5, -3, -2, +1, +4
            axes = self.make_axes(6, 4.25, [-7, 7, 1], [-600, 600, 100])
            border = SurroundingRectangle(
                axes,
                buff=0,
                corner_radius=0.1,
                color=self.ink_fg)
            dots = VGroup(*[
                Dot(axes.c2p(x, 0), radius=0.07)
                for x in roots])
            plot = axes.plot(
                lambda x: math.prod([(x - root) for root in roots]),
                [-5.825, 4.395, 0.02])
            x_trace = make_trace(plot, 'a', dots, 'x')
            z_trace = make_trace(plot.copy(), 'p', dots.copy(), 'z')
            graph = VGroup(axes, x_trace, z_trace, border)
            graph.shift(DOWN)

            self.play(FadeIn(border, axes))
            self.play(Create(plot), Create(dots), run_time=2)

        with self.say("We could solve it easily if we didn't have all these intermediate powers of x."):
            self.box_on(*Equ[1][0][5:19])

        with self.say("To make a start, we might first try to get rid of the quartic, x to the fourth, term."):
            self.box_on(*Equ[1][0][5:8])

        with self.say("In other words, transform it into so-called reduced form,"):
            brace = Brace(Group(Equ[1], Equ[2]), LEFT, color=self.ink_fg)
            self.play(FadeIn(brace), Create(Equ[2]))
            self.box_on(*Equ[2][0][5:8])

        with self.say("with this coefficient equal to zero."):
            self.play(Indicate(Equ[2][0][5], color=self.get_ink(Pen.WHITE), scale_factor=2, run_time=2))

        with self.say("This operation is technically known as a Tschirnhaus Transformation,"):
            image = ImageMobject("resources/Tschirnhaus_colour.jpg") # www.palette.fm - Polar Luster
            caption = MarkupText(
                'Ehrenfried Walther von Tschirnhaus (1651-1708)',
                color=self.ink_fg).scale(0.25).rotate(-PI/2)
            picture = Group(image, caption).arrange(RIGHT, buff=0.2)
            picture.to_corner(DR, buff=0.7).shift((picture.width+1)*RIGHT)
            self.add(picture)
            self.play(picture.animate.shift((picture.width+0.5)*LEFT), run_time=2)
            self.box_off()

        with self.say("the simplest example of which is a linear substitution, such as x = z + some constant h."):
            self.play(Create(Equ[0]))
            self.box_on(Equ[0])
            self.add(z_trace)

            scale = (axes.c2p(1, 0)[0] - axes.c2p(0, 0)[0]) * LEFT
            h = 0.0
            H = Variable(h, self.make_ssmt("h"), num_decimal_places=2)
            H.move_to(axes, UL).shift((RIGHT+DOWN)*0.5)
            H.label.set_color(self.get_token_ink('h'))
            H.value.set_color(self.ink_fg)
            self.play(Write(H))
            z_trace.add_updater(lambda trace:
                trace.move_to(x_trace).shift(scale * H.tracker.get_value()))
            for h in [-2.5, +1, -1]:
                self.play(H.tracker.animate.set_value(h), run_time=2)
                self.wait()

        with self.say("Let's use this to express all these x powers in terms of z."):
            E = Equ[1][0]
            S = E[2:4], E[5:8], E[9:12], E[13:16], E[17:19], E[20:21]
            self.play([
                TransformMatchingShapes(
                    S[i].copy(),
                    Equ[i+3][0][0:len(S[i])],
                    path_arc=-PI/2)
                for i in range(6)],
                run_time=2)
            self.play(FadeOut(graph, H))
            for i in range(5):
                self.play(
                    TransformMatchingShapes(
                        Equ[0][0][2:].copy(),
                        Equ[i+3][0][2:]))
            self.play(FadeIn(Equ[8][0][1:]))
            self.box_off()

        p2 = f'{p}{p}'
        p3 = f'{p2}{p}'
        p4 = f'{p3}{p}'
        p5 = f'{p4}{p}'

        def do_animations(phase: int, formulae: List[List[str]]) -> None:

            def box(i: int, bump: int) -> List[Group]:
                Hi = Equ[3][0]
                Lo = Equ[6-i][0]
                match phase:
                    case 1:
                        return [Equ[3][0][3:], Equ[4][0][4:], Equ[5][0][4:], Equ[6][0][4:]][0:4-i]
                    case 2:
                        k = 6*i+13+bump
                        return [Equ[3][0][3:k], Equ[4][0][4:k], Equ[5][0][4:k], Equ[6][0][4:k]][0:4-i]

            for i in range(4):
                self.box_on(*box(i, 0))
                animations = []
                for j in range(4-i):
                    Old = Equ[j+3]
                    New = self.make_tex(formulae[j][i])
                    New.move_to(Old, aligned_edge=LEFT)
                    animations.append(TransformMatchingShapes(Old, New))
                    Equ[j+3] = New
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
                S = Equ[j+4]
                T = self.make_tex(formulae[j])
                T.move_to(S, aligned_edge=LEFT)
                self.box_on(S)
                self.play(TransformMatchingShapes(S, T), self.box_move(T))
                Equ[j+4] = T
            self.box_off()
            self.play(FadeOut(Equ[0], brace, Equ[1]))
            Equations2 = VGroup(*Equ[2:])
            self.play(Equations2.animate.move_to(ORIGIN))

        with self.say("Now recall that this first z equation is just the sum of the six below it."):
            self.box_on(Equ[2])
            self.wait(2)
            self.box_on(*[Equ[i] for i in range(3, 9)])
            self.wait(2)
            self.box_off()
            
        def get_element(row: int, col: int):
            return M1[0][row * 6 + col][0]

        def set_element(row: int, col: int, value: VMobject):
            M1[0][row * 6 + col] = value

        Y = self.make_matrix((['y'], ['x^5'], ['ax^4'], ['bx^3'], ['cx^2'], ['dx'], ['e']), margin = 0)
        EQ = self.make_tex('=')
        M1 = self.make_matrix((
            ('z^5', '0z^4', 'pz^3', 'qz^2', 'rz', 's'),
            ('z^5', '5hz^4', '10h^2z^3', '10h^3z^2', '5h^4z', 'h^5'),
            ('', 'az^4', '4ahz^3', '6ah^2z^2', '4ah^3z', 'ah^4'),
            ('', '', 'bz^3', '3bhz^2', '3bh^2z', 'bh^3'),
            ('', '', '', 'cz^2', '2chz', 'ch^2'),
            ('', '', '', '', 'dz', 'dh'),
            ('', '', '', '', '', 'e')),
            padding = 1.75)
        Z = self.make_matrix((('1'), ('1'), ('1'), ('1'), ('1'), ('1')), margin = 0.25)
        EQ.move_to(M1, LEFT)
        Y.move_to(EQ, LEFT)
        VGroup(Y, EQ, M1, Z).arrange(RIGHT)

        opera = [ # index of '=', '+' operators
            [1, 4, 8, 12, 16, 19],
            [2, 5, 10, 17, 24, 29],
            [3, 7, 13, 20, 26],
            [3, 7, 13, 19],
            [3, 7, 12],
            [2, 5],
            [1]]
        stage = [[], [], [], []]
        Y0 = Y[0]
        for row in range(7):
            equ = Equations2[row][0]
            opus = opera[row]
            p = opus[0]
            q = p + 1
            stage[0].append(TransformMatchingShapes(equ[0:p], Y0[row]))
            if row != 3:
                stage[1].append(FadeOut(equ[p:q]))
            stage[1].append(TransformMatchingShapes(equ[p:q], EQ) if row == 3 else FadeOut(equ[p:q]))
            for col in range(len(opus)):
                lop = opus[col]
                if col > 0:
                    stage[2].append(FadeOut(equ[lop:lop+1]))
                start = lop + 1
                if col < len(opus)-1:
                    if row < 2 and col == 0:
                        lop += 1
                    S = equ[start:opus[col+1]]
                else:
                    S = equ[lop+1:]
                T = get_element(row, col + (0 if row < 2 else row-1))
                stage[3].append(TransformMatchingShapes(S, T))

        with self.say("All seven of these equations are identities, true for every choice of x and corresponding z."):
            self.play(*stage[0])
            self.play(FadeIn(Y[1:3]))
            self.play(*stage[1])
            self.play(*stage[2])
            self.play(*stage[3], run_time=2)
            self.play(FadeIn(M1[1:3], Z))

        Z0 = Z[0]
        for col in range(5):
            idx = -2 if col < 4 else -1
            T = Z0[col]
            transforms = []
            for row in range(col + 2):
                R = get_element(row, col)
                S = R[idx:]
                if row == 0:
                    U = S.copy()
                    U.move_to(T)
                    transforms.append(Transform(T, U))
                transforms.append(Transform(S.copy(), U))
                transforms.append(FadeOut(S, run_time=0.01)) ###############
            self.play(transforms)
            if col == 0:
                transforms = []
                for row in range(2):
                    V = Z0[5].copy()
                    V.move_to(get_element(row, 0))
                    set_element(row, 0, V)
                    transforms.append(FadeIn(V))
                self.play(transforms)

        def make_lines() -> VGroup:

            def make_line(m: Matrix) -> Line:
                y = (
                    m[0][0].get_corner(DOWN)[1] + 
                    m.get_rows()[1][0].get_corner(UP)[1]) / 2
                return Line(
                    (m[1].get_center()[0], y, 0),
                    (m[2].get_center()[0], y, 0),
                    color = self.ink_fg)

            return VGroup(make_line(Y), make_line(M1))

        Lines = make_lines()
        self.play(Create(Lines))

        self.wait(10)
        return


        Z2 = [] # Will hold the powers of z which fly into column vector Z1
        M2 = [] # Will hold the replacement terms for the main matrix

        def get_element(row: int, col: int):
            return M1[0][row * 6 + col]
        
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

        def rewrite(S: MathTex, T: MathTex) -> Transform:
            M2.append(T)
            lhs = S.tex_string.replace('^', '')
            i = lhs.find('z')
            maps = [([1], [1])]
            if i == 1:
                maps = [([1,2], ShrinkToCenter), (GrowFromCenter, [1])]
            elif i > 1:
                maps = [([i] if len(lhs) <= i + 1 else [i, i + 1], ShrinkToCenter)]
            return TransformByGlyphMap(S, T.move_to(S.get_center()), *maps)
        
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
            self.play(FadeOut(Y, EQ, M1, M2[0], M2[1], Z[0][5], Z[1], Z[2], *Z2))
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
