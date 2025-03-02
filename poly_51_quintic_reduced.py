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

        o = r'\phantom{o}' # hard space
        u = f'x^5&={o}'
        a = 'ax^4&=a'
        b = 'bx^3&=b'
        c = 'cx^2&=c'
        d = f'dx{o}&=d'
        e = f'e{o}{o}&=e'
        p = '(z+h)'

        Equ = self.make_texes(
            f'x{o}&={o}z+h',
            f'y{o}&={o}x^5+ax^4+bx^3+cx^2+dx+e=0',
            f'y{o}&={o}z^5+0z^4+pz^3+qz^2+rz+s',
            f'{u}{p}^5',
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
                self.play(H.tracker.animate.set_value(h), run_time=1.25)
                self.wait(0.25)

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
                    [f'{u}{p2}^4', f'{u}{p3}^3', f'{u}{p4}^2', f'{u}{p5}'],
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
                    [f'{u}{q2}{p3}', f'{u}{q3}{p2}', f'{u}{q4}{p}', f'{u}{q5}'],
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
            
        def get_element(matrix: Matrix, row: int, col: int):
            return matrix[0][row * 6 + col][0]

        def set_element(matrix: Matrix, row: int, col: int, value: VMobject):
            matrix[0][row * 6 + col] = value

        Y1 = self.make_matrix((['y'], ['x^5'], ['ax^4'], ['bx^3'], ['cx^2'], ['dx'], ['e']), margin = 0)
        E1 = self.make_tex('=')
        M1 = self.make_matrix((
            ('z^5', '0z^4', 'pz^3', 'qz^2', 'rz', 's'),
            ('z^5', '5hz^4', '10h^2z^3', '10h^3z^2', '5h^4z', 'h^5'),
            ('', 'az^4', '4ahz^3', '6ah^2z^2', '4ah^3z', 'ah^4'),
            ('', '', 'bz^3', '3bhz^2', '3bh^2z', 'bh^3'),
            ('', '', '', 'cz^2', '2chz', 'ch^2'),
            ('', '', '', '', 'dz', 'dh'),
            ('', '', '', '', '', 'e')),
            padding = 1.75)
        Z1 = self.make_matrix([('1') for _ in range(6)], margin = 0.25)
        E1.move_to(M1, LEFT)
        Y1.move_to(E1, LEFT)
        VGroup(Y1, E1, M1, Z1).arrange(RIGHT)

        opera = [ # index of '=', '+' operators
            [1, 4, 8, 12, 16, 19],
            [2, 5, 10, 17, 24, 29],
            [3, 7, 13, 20, 26],
            [3, 7, 13, 19],
            [3, 7, 12],
            [2, 5],
            [1]]
        stage = [[], [], [], []]
        Y0 = Y1[0]
        for new_row in range(7):
            eq1 = Equations2[new_row][0]
            opus = opera[new_row]
            p = opus[0]
            q = p + 1
            stage[0].append(TransformMatchingShapes(eq1[0:p], Y0[new_row]))
            if new_row != 3:
                stage[1].append(FadeOut(eq1[p:q]))
            stage[1].append(TransformMatchingShapes(eq1[p:q], E1) if new_row == 3 else FadeOut(eq1[p:q]))
            for new_col in range(len(opus)):
                lop = opus[new_col]
                if new_col > 0:
                    stage[2].append(FadeOut(eq1[lop:lop+1]))
                start = lop + 1
                if new_col < len(opus)-1:
                    if new_row < 2 and new_col == 0:
                        lop += 1
                    S = eq1[start:opus[new_col+1]]
                else:
                    S = eq1[lop+1:]
                T = get_element(M1, new_row, new_col + (0 if new_row < 2 else new_row-1))
                stage[3].append(TransformMatchingShapes(S, T))

        with self.say("All seven of these equations are identities, true for every choice of x and corresponding z."):
            self.play(*stage[0]) # Show the Y1 column verctor.
            self.play(FadeIn(Y1.get_brackets())) # Show Y1's brackets.
            self.play(*stage[1]) # Coalesce the '=' signs.
            self.play(*stage[2]) # Hide the '+' signs.
            self.play(*stage[3], run_time=2) # Adjust the layout of matrix M1.
            self.play(FadeIn(M1.get_brackets(), Z1)) # Show M1's brackets & Z1.

        transforms = []
        def fly(source: Mobject, target: Mobject, arc: float) -> None:
            transforms.append(ReplacementTransform(source, target, path_arc=arc, run_time=2))

        Z0 = Z1[0]
        for new_col in range(5):
            idx = -2 if new_col < 4 else -1
            T = Z0[new_col]
            transforms = []
            for new_row in range(new_col + 2):
                R = get_element(M1, new_row, new_col)
                S = R[idx:]
                if new_row == 0:
                    U = S.copy()
                    U.move_to(T)
                    fly(T, U, -PI/2)
                fly(S.copy(), U, -PI/2)
                transforms.append(FadeOut(S, run_time=0.01))
            self.play(transforms) # Move the powers of z from M1 into Z1.
            if new_col == 0:
                transforms = []
                for new_row in range(2):
                    V = Z0[5].copy()
                    V.move_to(get_element(M1, new_row, 0), aligned_edge=DOWN)
                    M1[0][6*new_row] = V
                    transforms.append(FadeIn(V))
                self.play(transforms) # Set '1's in the first column of M1.

        def make_lines() -> VGroup:

            def make_line(m: Matrix) -> Line:
                y = (
                    m[0][0].get_corner(DOWN)[1] + 
                    m.get_rows()[1][0].get_corner(UP)[1]) / 2
                return Line(
                    (m[1].get_center()[0], y, 0),
                    (m[2].get_center()[0], y, 0),
                    color = self.ink_fg)

            return VGroup(make_line(Y1), make_line(M1))

        with self.say("So every value above the line is equal to the sum of the values below it."):
            Lines = make_lines()
            self.play(Create(Lines))

        Y2 = self.make_matrix((['0'], ['p'], ['q'], ['r'], ['s']), margin = 0)
        E2 = self.make_tex('=')
        M2 = self.make_matrix((
            ('a', '5h', '', '', '', ''),
            ('b', '4ah', '10h^2', '', '', ''),
            ('c', '3bh', '6ah^2', '10h^3', '', ''),
            ('d', '2ch', '3bh^2', '4ah^3', '5h^4', ''),
            ('e', 'dh', 'ch^2', 'bh^3', 'ah^4', 'h^5')),
            padding = 1.75)
        Z2 = self.make_matrix([('1') for _ in range(5)], margin = 0.25)
        E2.move_to(M2, LEFT)
        Y2.move_to(E2, LEFT)
        VGroup(Y2, E2, M2, Z2).arrange(RIGHT)

        transforms = []
        for new_row in range(5):
            old_col = new_row+1
            fly(get_element(M1, 0, old_col)[0], Y2[0][new_row], 0.7*PI)
            for new_col in range(new_row+2):
                old_row = new_row+2-new_col
                S = get_element(M1, old_row, old_col)
                match old_col:
                    case 5:
                        pass
                    case 4:
                        S = S[0:-1]
                    case _:
                        S = S[0:-2]
                T = get_element(M2, new_row, new_col)
                fly(S, T, -PI/4)

        with self.say("Reading the matrix column by column, we can express the new coefficients in terms of the old."):
            self.play(FadeOut(Y1, E1, M1.get_brackets(), M1[0][0], M1[0][6], Lines, Z1))
            self.play(transforms)
            self.play(FadeIn(Y2.get_brackets(), E2, M2.get_brackets(), Z2))
            self.wait(2)

        formulae = [
            [f'0{o}&={o}a+5h', f'p{o}&={o}b+4ah+10h^2', f'q{o}&={o}c+3bh+6ah^2+10h^3', f'r{o}&={o}d+2ch+3bh^2+4ah^3+5h^4', f's{o}&={o}e+dh+ch^2+bh^3+a^4+h^5'],
            [f'a=-5h' , 'p=10h^2-20h^2+b', f'q=10h^3-30h^3+3bh+c', f'r=5h^4-20h^4+3bh^2+2ch+d'   , f's=h^5-5h^5+bh^3+ch^2+dh+e'],
            [f'h=-a/5', 'p=-10h^2+b'     , f'q=-20h^3+3bh+c'     , f'r=-15h^4+3bh^2+2ch+d'       , f's=-4h^5+bh^3+ch^2+dh+e'],
            [f'h=-a/5', 'p=b-10h^2'      , f'q=c+3bh-20h^3'      , f'r=d+2ch+3bh^2-15h^4'        , f's=e+dh+ch^2+bh^3-4h^5'],
            [f'h=-a/5', 'p=b-2a^2/5'     , f'q=c-3ab/5+4a^3/25'  , f'r=d-2ac/5+3a^2b/25-3a^4/125', f's=e-ad/5+a^2c/25-a^3b/125-4a^5/3125']]

        for row in range(5):
            equ = self.make_tex(formulae[0][row])
            equ.move_to(Equ[row+3], aligned_edge = LEFT)
            Equ[row+3] = equ
        Equ[3:8].arrange(DOWN, aligned_edge = LEFT)

        self.play(Create(equ))

        #self.play(Create(Equ[0]))
        #self.play(Create(Equ[1]))
        #self.play(Create(Equ[2]))
        self.play(Create(Equ[3]))
        self.play(Create(Equ[4]))
        self.play(Create(Equ[5]))
        self.play(Create(Equ[6]))
        self.play(Create(Equ[7]))
        
        self.wait(10)
        return



        self.play(FadeIn(Y2, E2, M2, Z2))


        for new_col in range(5):
            Equ[new_col+3] = self.make_tex(formulae[0][new_col])
            Equ.arrange(DOWN, aligned_edge = LEFT)

        for new_row in range(8):
            self.play(Create(Equ[new_row]))







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
            self.play(FadeOut(Y1, E1, M1, M2[0], M2[1], Z1[0][5], Z1[1], Z1[2], *Z2))
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
