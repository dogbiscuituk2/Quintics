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
        
        e0 = (
            ' x· &= ·z+h',
            ' y· &= ·x⁵+ax⁴+bx³+cx²+dx+e=0',
            ' y· &= ·z⁵+0z⁴+pz³+qz²+rz+s',
            ' x⁵ &= ·(z+h)⁵',
            'ax⁴ &= a(z+h)⁴',
            'bx³ &= b(z+h)³',
            'cx² &= c(z+h)²',
            'dx· &= d(z+h)',
            'e·· &= e',
        )

        e1 = ((
            'x⁵ &= ·(z+h)(z+h)⁴',
            'x⁵ &= ·(z+h)(z+h)(z+h)³',
            'x⁵ &= ·(z+h)(z+h)(z+h)(z+h)²',
            'x⁵ &= ·(z+h)(z+h)(z+h)(z+h)(z+h)',
        ),(
            'ax⁴ &= a(z+h)(z+h)³',
            'ax⁴ &= a(z+h)(z+h)(z+h)²',
            'ax⁴ &= a(z+h)(z+h)(z+h)(z+h)',
        ),(
            'bx³ &= b(z+h)(z+h)²',
            'bx³ &= b(z+h)(z+h)(z+h)',
        ),(
            'cx² &= c(z+h)(z+h)',
        ))

        e2 = ((
            'x⁵ &= ·(z²+2hz+h²)(z+h)(z+h)(z+h)',
            'x⁵ &= ·(z³+3hz²+3h²z+h³)(z+h)(z+h)',
            'x⁵ &= ·(z⁴+4hz³+6h²z²+4h³z+h⁴)(z+h)',
            'x⁵ &= ·z⁵+5hz⁴+10h²z³+10h³z²+5h⁴z+h⁵',
        ),(
            'ax⁴ &= a(z²+2hz+h²)(z+h)(z+h)',
            'ax⁴ &= a(z³+3hz²+3h²z+h³)(z+h)',
            'ax⁴ &= a(z⁴+4hz³+6h²z²+4h³z+h⁴)',
        ),( 
            'bx³ &= b(z²+2hz+h²)(z+h)',
            'bx³ &= b(z³+3hz²+3h²z+h³)',
        ),( 
            'cx² &= c(z²+2hz+h²)',
        ))

        e3 = (
            'ax⁴ &= az⁴+4ahz³+6ah²z²+4ah³z+ah⁴',
            'bx³ &= bz³+3bhz²+3bh²z+bh³',
            'cx² &= cz²+2chz+ch²',
            'dx· &= dz+dh',
        )

        y0 = ('y', 'x⁵', 'ax⁴', 'bx³', 'cx²', 'dx', 'e')

        m0 = (
            ('z⁵',  '0z⁴',    'pz³',    'qz²',    'rz',  's' ),
            ('z⁵', '5hz⁴', '10h²z³', '10h³z²',  '5h⁴z',  'h⁵'),
            (  '',  'az⁴', '4ah³z³', '6ah²z²', '4ah³z', 'ah⁴'),
            (  '',     '',    'bz³',  '3bhz²', '3bh²z', 'bh³'),
            (  '',     '',       '',    'cz²',  '2chz', 'ch²'),
            (  '',     '',       '',       '',    'dz', 'dh' ),
            (  '',     '',       '',       '',      '', 'e'  ),
        )

        z0 = [('1') for _ in range(6)]

        y1 = ('0', 'p', 'q', 'r', 's')

        m1 = (
            ('a',  '5h',     '',     '',    '',   ''),
            ('b', '4ah', '10h²',     '',    '',   ''),
            ('c', '3bh', '6ah²', '10h³',    '',   ''),
            ('d', '2ch', '3bh²', '4ah³', '5h⁴',   ''),
            ('e',  'dh',  'ch²',  'bh³', 'ah⁴', 'h⁵'),
        )

        z1 = [('1') for _ in range(6)]

        e4 = ((                         # e4[0]
            '0 = a+5h',
            'p = b+4ah+10h²',
            'q = c+3bh+6ah²+10h³',
            'r = d+2ch+3bh²+4ah³+5h⁴',
            's = e+dh+ch²+bh³+ah⁴+h⁵',
        ),(                             # e4[1]
            'a =-5h',
            'p = b-20h²+10h²',
            'q = c+3bh-30h³+10h³',
            'r = d+2ch+3bh²-20h⁴+5h⁴',
            's = e+dh+ch²+bh³-5h⁵+h⁵',
        ),(                             # e4[2]
            'h =-a/5',
            'p = b-10h²',
            'q = c+3bh-20h³',
            'r = d+2ch+3bh²-15h⁴',
            's = e+dh+ch²+bh³-4h⁵',
        ),(                             # e4[3]
            'h =-a/5',
            'p = b-2a²/5',
            'q = c-3ab/5+4a³/25',
            'r = d-2ac/5+3a²b/25-3a⁴/125',
            's = e-ad/5+a²c/25-a³b/125-4a⁵/3125',
        ))

        def make_trace(
            plot: ParametricFunction,
            plot_token: str,
            dots: VGroup,
            dots_token: str) -> VGroup:
            plot.color = self.get_token_ink(plot_token)
            dots.color = self.get_token_ink(dots_token)
            return VGroup(plot, dots)
        
        E0 = self.make_texes(*e0)

        with self.say("The degree five polynomial, the quintic, has five roots."):
            self.play(Create(E0[1]))

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
            self.box_on(*E0[1][0][5:19])

        with self.say("To make a start, we might first try to get rid of the quartic, x to the fourth, term."):
            self.box_on(*E0[1][0][5:8])

        with self.say("In other words, transform it into so-called reduced form,"):
            brace = Brace(Group(E0[1], E0[2]), LEFT, color=self.ink_fg)
            self.play(FadeIn(brace), Create(E0[2]))
            self.box_on(*E0[2][0][5:8])

        with self.say("with this coefficient equal to zero."):
            self.play(Indicate(E0[2][0][5], color=self.get_ink(Pen.WHITE), scale_factor=2, run_time=2))

        with self.say("This operation is technically known as a Tschirnhaus Transformation,"):
            image = ImageMobject("resources/Tschirnhaus_colour.jpg") # www.palette.fm - Polar Luster
            caption = MarkupText(
                'Ehrenfried Walther von Tschirnhaus (1651-1708)',
                color=self.ink_fg).scale(0.25).rotate(-PI/2)
            picture = Group(image, caption).arrange(RIGHT, buff=0.2)
            picture.to_corner(DR, buff=0.7).shift((picture.width+1)*RIGHT)
            self.add(picture)
            self.play(picture.animate.shift((picture.width+0.5)*LEFT), run_time=2)

        with self.say("the simplest example of which is a linear substitution, such as x = z + some constant h."):
            self.play(Create(E0[0]))
            self.box_on(E0[0])
            self.add(z_trace)

            scale = (axes.c2p(1, 0)[0] - axes.c2p(0, 0)[0]) * LEFT
            h = 0.0
            H = Variable(h, self.make_smt("h"), num_decimal_places=2)
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
            T = E0[1][0] # y = x⁵ + ax⁴ + bx³ + cx² + dx + e
            S = T[2:4], T[5:8], T[9:12], T[13:16], T[17:19], T[20:21]
            self.play([
                TransformMatchingShapes(
                    S[i].copy(),
                    E0[i+3][0][0:len(S[i])],
                    path_arc=-PI/2)
                for i in range(6)],
                run_time=2)
            self.play(FadeOut(graph, H))
            for i in range(5):
                self.play(
                    TransformMatchingShapes(
                        E0[0][0][2:].copy(),
                        E0[i+3][0][2:]))
            self.play(FadeIn(E0[8][0][1:]))

        def do_animations(phase: int, formulae: List[List[str]]) -> None:

            def box(i: int, bump: int) -> List[Group]:
                match phase:
                    case 1:
                        return [E0[3][0][3:], E0[4][0][4:], E0[5][0][4:], E0[6][0][4:]][0:4-i]
                    case 2:
                        k = 6*i+13+bump
                        return [E0[3][0][3:k], E0[4][0][4:k], E0[5][0][4:k], E0[6][0][4:k]][0:4-i]

            for i in range(4):
                self.box_on(*box(i, 0))
                animations = []
                for j in range(4-i):
                    Old = E0[j+3]
                    New = self.make_tex(formulae[j][i])
                    New.move_to(Old, aligned_edge=LEFT)
                    animations.append(TransformMatchingShapes(Old, New))
                    E0[j+3] = New
                animations.append(self.box_move(*box(i, 1)))
                self.play(*animations)

        with self.say("Expand these powers."):
            self.play(FadeOut(picture))
            do_animations(1, e1)

        with self.say("Multiply out the binomials."):
            do_animations(2, e2)

        with self.say("Distribute the original coefficients."):
            for j in range(4):
                S = E0[j+4]
                T = self.make_tex(e3[j])
                T.move_to(S, aligned_edge=LEFT)
                self.box_on(S)
                self.play(TransformMatchingShapes(S, T), self.box_move(T))
                E0[j+4] = T
            self.box_off()
            self.play(FadeOut(E0[0], brace, E0[1]))
            Equations2 = VGroup(*E0[2:])
            self.play(Equations2.animate.move_to(ORIGIN))

        with self.say("Now recall that this first z equation is just the sum of the six below it."):
            self.box_on(E0[2])
            self.wait(2)
            self.box_on(*[E0[i] for i in range(3, 9)])
            self.wait(2)
            self.box_off()
            
        def get_element(matrix: Matrix, row: int, col: int):
            return matrix[0][row * 6 + col][0]
        
        Y0 = self.make_matrix([[y] for y in y0], margin = 0)
        Q0 = self.make_tex('=')
        M0 = self.make_matrix(m0, padding = 1.75)
        Z0 = self.make_matrix(z0, margin = 0.25)
        Q0.move_to(M0, LEFT)
        Y0.move_to(Q0, LEFT)
        VGroup(Y0, Q0, M0, Z0).arrange(RIGHT)

        opera = [ # index of '=', '+' operator glyphs
            get_glyph_starts(Equations2[new_row][0], '[+=]')
            for new_row in range(7)
        ]

        stage = [[], [], [], []]
        Y = Y0[0]
        for new_row in range(7):
            eq1 = Equations2[new_row][0]
            opus = opera[new_row]
            p1 = opus[0]
            q = p1 + 1
            stage[0].append(TransformMatchingShapes(eq1[0:p1], Y[new_row]))
            if new_row != 3:
                stage[1].append(FadeOut(eq1[p1:q]))
            stage[1].append(TransformMatchingShapes(eq1[p1:q], Q0) if new_row == 3 else FadeOut(eq1[p1:q]))
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
                T = get_element(M0, new_row, new_col + (0 if new_row < 2 else new_row-1))
                stage[3].append(TransformMatchingShapes(S, T))

        with self.say("All seven of these equations are identities, true for every choice of x and corresponding z."):
            self.play(*stage[0]) # Show the column vector.
            self.play(FadeIn(Y0.get_brackets())) # Show its brackets.
            self.play(*stage[1]) # Coalesce the '=' signs.
            self.play(*stage[2]) # Hide the '+' signs.
            self.play(*stage[3], run_time=2) # Adjust the matrix layout.
            self.play(FadeIn(M0.get_brackets(), Z0)) # Show matrix brackets & Z0.

        def fly(source: Mobject, target: Mobject, arc: float) -> None:
            return ReplacementTransform(source, target, path_arc=arc, run_time=1.5)

        transforms = []
        Z = Z0[0]
        for new_col in range(5):
            idx = -2 if new_col < 4 else -1
            T = Z[new_col]
            transforms = []
            for new_row in range(new_col + 2):
                R = get_element(M0, new_row, new_col)
                S = R[idx:]
                if new_row == 0:
                    U = S.copy()
                    U.move_to(T)
                    transforms.append(fly(T, U, -PI/2))
                transforms.append(fly(S.copy(), U, -PI/2))
                transforms.append(FadeOut(S, run_time=0.01))
            self.play(transforms) # Move the powers of z from M1 into Z1.
            if new_col == 0:
                transforms = []
                for new_row in range(2):
                    V = Z[5].copy()
                    V.move_to(get_element(M0, new_row, 0), aligned_edge=DOWN)
                    M0[0][6*new_row] = V
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

            return VGroup(make_line(Y0), make_line(M0))

        with self.say("So every value above the line is equal to the sum of the values below it."):
            Lines = make_lines()
            self.play(Create(Lines))

        Y1 = self.make_matrix([[y] for y in y1], margin = 0)
        Q1 = self.make_tex('=')
        M1 = self.make_matrix(m1, padding = 1.75)
        Z1 = self.make_matrix(z1, margin = 0.25)
        Q1.move_to(M1, LEFT)
        Y1.move_to(Q1, LEFT)
        VGroup(Y1, Q1, M1, Z1).arrange(RIGHT)

        transforms1 = []
        transforms2 = []
        for new_row in range(5):
            old_col = new_row+1
            transforms1.append(fly(get_element(M0, 0, old_col)[0], Y1[0][new_row], -PI/4))
            for new_col in range(new_row+2):
                old_row = new_row+2-new_col
                S = get_element(M0, old_row, old_col)
                match old_col:
                    case 5:
                        pass
                    case 4:
                        S = S[0:-1]
                    case _:
                        S = S[0:-2]
                T = get_element(M1, new_row, new_col)
                transforms2.append(fly(S, T, -PI/4))

        with self.say("Reading the matrix column by column, we can express the new coefficients in terms of the old."):
            self.play(FadeOut(Y0, Q0, M0.get_brackets(), M0[0][0], M0[0][6], Lines, Z0))
            self.play(transforms1)
            self.play(transforms2)
            junk = (Y1.get_brackets(), Q1, M1.get_brackets(), Z1)
            self.play(FadeIn(*junk))
            self.wait(2)
            self.play(FadeOut(*junk))

        for row in range(5):
            equ = self.make_tex(e4[0][row])
            equ.move_to(E0[row+3], aligned_edge=LEFT)
            E0[row+3] = equ
        E0[3:8].arrange(DOWN, aligned_edge=LEFT)
        terms = []
        signs = []
        for row in range(5):
            T = split_smt(E0[row+3][0])
            terms.append(TransformMatchingShapes(Y1[0][row], T[0]))
            for col in range(row+2):
                signs.append(T[2*col+1])
                terms.append(TransformMatchingShapes(get_element(M1, row, col), T[2*(col+1)]))
        self.play(terms)
        self.play(FadeIn(*signs))

        with self.say(
            """
            This h substitution avoids a lot of ugly fractions with powers of five denominators in the results. 
            Apply the substitution, and collect like powers of h. 
            """):

            S = E0[3]                                                   # 0 = a + 5h
            T = self.make_tex(e4[1][0]).move_to(S, aligned_edge=LEFT)   # a = -5h
            self.box_on(S)
            self.play(
                TransformByGlyphMap(S, T, ([0], FadeOut), ([2], [0])),
                self.box_move(T))

            S = E0[4]                                                   # p = b + 4ah + 10h²
            T = self.make_tex(e4[1][1]).move_to(S, aligned_edge=LEFT)   # p = b - 20h² + 10h²
            U = S[0][3:7]
            V = T[0][3:8]
            self.box_on(U)
            self.play(
                TransformByGlyphMap(S, T, (FadeIn, [7])),
                self.box_move(V))

            S = T                                                       # p = b - 20h² + 10h²
            T = self.make_tex(e4[2][1]).move_to(S, aligned_edge=LEFT)   # p = b - 10h²
            U = S[0][3:13]
            V = T[0][3:8]
            self.box_on(U)
            self.play(
                TransformByGlyphMap(S, T, (ir(8,12), FadeOut)),
                self.box_move(V))

            S = E0[5]                                                   # q = c + 3bh + 6ah² + 10h³
            T = self.make_tex(e4[1][2]).move_to(S, aligned_edge=LEFT)   # q = c + 3bh - 30h³ + 10h³
            U = S[0][7:12]
            V = T[0][7:12]
            self.box_on(U)
            self.play(
                TransformByGlyphMap(S, T, (ir(0,16), ir(0,16))),
                self.box_move(V))

            S = T                                                       # q = c + 3bh - 30h³ + 10h³
            T = self.make_tex(e4[2][2]).move_to(S, aligned_edge=LEFT)   # q = c + 3bh - 20h³
            U = S[0][7:17]
            V = T[0][7:12]
            self.box_on(U)
            self.play(
                TransformByGlyphMap(S, T, (ir(12,16), FadeOut)),
                self.box_move(V))

            S = E0[6]                                                   # r = d + 2ch + 3bh² + 4ah³ + 5h⁴
            T = self.make_tex(e4[1][3]).move_to(S, aligned_edge=LEFT)   # r = d + 2ch + 3bh² - 20h⁴ + 5h⁴
            U = S[0][12:17]
            V = T[0][12:17]
            self.box_on(U)
            self.play(
                TransformByGlyphMap(S, T, (ir(0,20), ir(0,20))),
                self.box_move(V))

            S = T                                                       # r = d + 2ch + 3bh² - 20h⁴ + 5h⁴
            T = self.make_tex(e4[2][3]).move_to(S, aligned_edge=LEFT)   # r = d + 2ch + 3bh² - 15h⁴
            U = S[0][12:21]
            V = T[0][12:17]
            self.box_on(U)
            self.play(
                TransformByGlyphMap(S, T, (ir(17,20), FadeOut)),
                self.box_move(V))

            S = E0[7]                                                   # s = e + dh + ch² + bh³ + ah⁴ + h⁵
            T = self.make_tex(e4[1][4]).move_to(S, aligned_edge=LEFT)   # s = e + dh + ch² + bh³ - 5h⁵ + h⁵
            U = S[0][14:18]
            V = T[0][14:18]
            self.box_on(U)
            self.play(
                TransformByGlyphMap(S, T, (ir(0,20), ir(0,20))),
                self.box_move(V))

            S = T                                                       # s = e + dh + ch² + bh³ - 5h⁵ + h⁵
            T = self.make_tex(e4[2][4]).move_to(S, aligned_edge=LEFT)   # s = e + dh + ch² + bh³ - 4h⁵
            U = S[0][14:21]
            V = T[0][14:18]
            self.box_on(U)
            self.play(
                TransformByGlyphMap(S, T, (ir(18,20), FadeOut)),
                self.box_move(V))

        self.wait(10)
        return

        F1 = self.make_tex('y=x⁵+ax⁴+bx³+cx²+dx+e')
        F2 = self.make_tex('y=z⁵+0z⁴+pz³+qz²+rz+s')
        F3 = self.make_tex('z=x-h')
        F4 = self.make_tex('z=x+a/5')

        def setup(*args: str) -> MathTex:
            return VGroup(*[self.make_tex(arg) for arg in args]).arrange(DOWN, aligned_edge = LEFT).move_to(2 * LEFT + DOWN)

        F5 = setup('0=5h+a', 'p=10h²+4ah+b'  , 'q=10h³+6ah²+3bh+c', 'r=5h⁴+4ah³+3bh²+2ch+d'   , 's=h⁵+a⁴+bh³+ch²+dh+e')
        F6 = setup('a=-5h' , 'p=10h²-20h²+b', 'q=10h³-30h³+3bh+c', 'r=5h⁴-20h⁴+3bh²+2ch+d'   , 's=h⁵-5h⁵+bh³+ch²+dh+e')
        F7 = setup('h=-a/5', 'p=-10h²+b'     , 'q=-20h³+3bh+c'     , 'r=-15h⁴+3bh²+2ch+d'       , 's=-4h⁵+bh³+ch²+dh+e')
        F8 = setup('h=-a/5', 'p=b-10h²'      , 'q=c+3bh-20h³'      , 'r=d+2ch+3bh²-15h⁴'        , 's=e+dh+ch²+bh³-4h⁵')
        F9 = setup('h=-a/5', 'p=b-2a²/5'     , 'q=c-3ab/5+4a³/25'  , 'r=d-2ac/5+3a²b/25-3a⁴/125', 's=e-ad/5+a²c/25-a³b/125-4a⁵/3125')
        
        with self.say("Now we can read the matrix column by column, to get expressions for the new coefficients in terms of the old."):
            self.play(FadeOut(Y0, E1, M0, M1[0], M1[1], Z0[0][5], Z0[1], Z0[2], *Z1))
            for f_2 in (F5, F6, F7, F8):
                VGroup(F1, F2, F3, f_2).arrange(DOWN, aligned_edge = LEFT)
            VGroup(F1, F2, F4, F8).arrange(DOWN, aligned_edge = LEFT)

            M6 = [
                VGroup(*[M1[i] for i in range(2, 5)]),
                VGroup(*[M1[i] for i in range(5, 9)]),
                VGroup(*[M1[i] for i in range(9, 14)]),
                VGroup(*[M1[i] for i in range(14, 20)]),
                VGroup(*[M1[i] for i in range(20, 27)])]
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
