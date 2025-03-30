#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import Animate, BaseScene
from labels import *
import math
from MF_Tools import *
from painter import *

#region data

e1 = (
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

e2 = ((
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

e3 = ((
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

e4 = (
    'ax⁴ &= az⁴+4ahz³+6ah²z²+4ah³z+ah⁴',
    'bx³ &= bz³+3bhz²+3bh²z+bh³',
    'cx² &= cz²+2chz+ch²',
    'dx· &= dz+dh',
)

y1 = ('y', 'x⁵', 'ax⁴', 'bx³', 'cx²', 'dx', 'e')

m1 = (
    ('z⁵',  '0z⁴',    'pz³',    'qz²',    'rz',  's' ),
    ('z⁵', '5hz⁴', '10h²z³', '10h³z²',  '5h⁴z',  'h⁵'),
    (  '',  'az⁴', '4ah³z³', '6ah²z²', '4ah³z', 'ah⁴'),
    (  '',     '',    'bz³',  '3bhz²', '3bh²z', 'bh³'),
    (  '',     '',       '',    'cz²',  '2chz', 'ch²'),
    (  '',     '',       '',       '',    'dz', 'dh' ),
    (  '',     '',       '',       '',      '', 'e'  ),
)

z1 = [('1') for _ in range(6)]

y2 = ('0', 'p', 'q', 'r', 's')

m2 = (
    ('a',  '5h',     '',     '',    '',   ''),
    ('b', '4ah', '10h²',     '',    '',   ''),
    ('c', '3bh', '6ah²', '10h³',    '',   ''),
    ('d', '2ch', '3bh²', '4ah³', '5h⁴',   ''),
    ('e',  'dh',  'ch²',  'bh³', 'ah⁴', 'h⁵'),
)

z2 = [('1') for _ in range(6)]

e5 = ((                         # e4[0]
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

e6 = (
    'x = z+h',
    'y = x⁵+ax⁴+bx³+cx²+dx+e=0',
    'y = z⁵+0z⁴+pz³+qz²+rz+s',
)

e7 = ((
    'x &= z+h',
    'x &= z-1',
),(
    'y &= (x+5)(x+3)(x+2)(x-1)(x-4)',
    'y &= (x²+8x+15)(x+2)(x-1)(x-4)',
    'y &= (x³+10x²+31x+30)(x-1)(x-4)',
    'y &= (x⁴+9x³+21x²-x-30)(x-4)',
    'y &= x⁵+5x⁴-15x³-85x²-26x+120',
),(
    'a &= 5, ·b = -15, ·c = -85, ·d = -26, ·e = 120',
    'y &= (x+5)(x+3)(x+2)(x-1)(x-4)',
    'y &= (z-1+5)(x+3)(x+2)(x-1)(x-4)',
    'y &= (z-1+5)(z-1+3)(x+2)(x-1)(x-4)',
    'y &= (z-1+5)(z-1+3)(z-1+2)(x-1)(x-4)',
    'y &= (z-1+5)(z-1+3)(z-1+2)(z-1-1)(x-4)',
    'y &= (z-1+5)(z-1+3)(z-1+2)(z-1-1)(z-1-4)',
    'y &= (z-1+5)(z-1+3)(z-1+2)(z-1-1)(z-5)',
    'y &= (z-1+5)(z-1+3)(z-1+2)(z-2)(z-5)',
    'y &= (z-1+5)(z-1+3)(z+1)(z-2)(z-5)',
    'y &= (z-1+5)(z+2)(z+1)(z-2)(z-5)',
    'y &= (z+4)(z+2)(z+1)(z-2)(z-5)',
    'y &= z⁵-25z³-20z²+84z+80',
),(
    'h &= -a/5',
    'h &= -1',
),(
    'p &= b-10h²',
    'p &= -25',
),(
    'q &= c+3bh-20h³',
    'q &= -20',
),(
    'r &= d+2ch+3bh²-15h⁴',
    'r &= 84',
),(
    's &= e+dh+ch²+bh³-4h⁵',
    's &= 80',
))

#endregion

#region code

class Poly_51_Reduced(BaseScene):

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

        def autopilot(S: MathTex, t: str, a: int, b: int, c: int, *glyph_map: tuple) -> MathTex:
            """
            TransformByGlyphMap one MathTex into another, boxing the changed region.
            """
            T = self.make_tex(t).move_to(S, aligned_edge=LEFT)
            if b == 0:
                b = len(S[0])
            if c == 0:
                c = len(T[0])
            self.box_on(S[0][a:b])
            self.play(
                TransformByGlyphMap(S, T, *glyph_map)
                if len(glyph_map) > 0
                else TransformMatchingShapes(S, T),
                self.box_move(T[0][a:c]))
            return T

        def make_trace(
            plot: ParametricFunction,
            plot_token: str,
            dots: VGroup,
            dots_token: str) -> VGroup:
            plot.color = self.get_token_ink(plot_token)
            dots.color = self.get_token_ink(dots_token)
            return VGroup(plot, dots)
        
        E = self.make_texes(*e1)

        with self.say("The degree five polynomial, the quintic, has five roots."):
            self.play(Create(E[1]))

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
            self.box_on(*E[1][0][5:19])

        with self.say("To make a start, we might first try to get rid of the quartic, x to the fourth, term."):
            self.box_on(*E[1][0][5:8])

        with self.say("In other words, transform it into so-called reduced form,"):
            brace = Brace(Group(E[1], E[2]), LEFT, color=self.ink_fg)
            self.play(FadeIn(brace), Create(E[2]))
            self.box_on(*E[2][0][5:8])

        with self.say("with this coefficient equal to zero."):
            self.play(Indicate(E[2][0][5], color=self.get_ink(Pen.WHITE), scale_factor=2, run_time=2))

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
            self.play(Create(E[0]))
            self.box_on(E[0])
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
            T = E[1][0] # y = x⁵ + ax⁴ + bx³ + cx² + dx + e
            S = T[2:4], T[5:8], T[9:12], T[13:16], T[17:19], T[20:21]
            self.play([
                TransformMatchingShapes(
                    S[i].copy(),
                    E[i+3][0][0:len(S[i])],
                    path_arc=-PI/2)
                for i in range(6)],
                run_time=2)
            self.play(FadeOut(graph, H))
            for i in range(5):
                self.play(
                    TransformMatchingShapes(
                        E[0][0][2:].copy(),
                        E[i+3][0][2:]))
            self.play(FadeIn(E[8][0][1:]))

        def do_animations(phase: int, formulae: List[List[str]]) -> None:

            def box(i: int, bump: int) -> List[Group]:
                match phase:
                    case 1:
                        return [E[3][0][3:], E[4][0][4:], E[5][0][4:], E[6][0][4:]][0:4-i]
                    case 2:
                        k = 6*i+13+bump
                        return [E[3][0][3:k], E[4][0][4:k], E[5][0][4:k], E[6][0][4:k]][0:4-i]

            for i in range(4):
                self.box_on(*box(i, 0))
                animations = []
                for j in range(4-i):
                    Old = E[j+3]
                    New = self.make_tex(formulae[j][i])
                    New.move_to(Old, aligned_edge=LEFT)
                    animations.append(TransformMatchingShapes(Old, New))
                    E[j+3] = New
                animations.append(self.box_move(*box(i, 1)))
                self.play(*animations)

        with self.say("Expand these powers."):
            self.play(FadeOut(picture))
            do_animations(1, e2)

        with self.say("Multiply out the binomials."):
            do_animations(2, e3)

        with self.say("Distribute the original coefficients."):
            for j in range(4):
                S = E[j+4]
                T = self.make_tex(e4[j])
                T.move_to(S, aligned_edge=LEFT)
                self.box_on(S)
                self.play(TransformMatchingShapes(S, T), self.box_move(T))
                E[j+4] = T
            self.box_off()
            self.play(FadeOut(E[0], brace, E[1]))
            Equations2 = VGroup(*E[2:])
            self.play(Equations2.animate.move_to(ORIGIN))

        with self.say("Now recall that this first z equation is just the sum of the six below it."):
            self.box_on(E[2])
            self.wait(2)
            self.box_on(*[E[i] for i in range(3, 9)])
            self.wait(2)
            self.box_off()
            
        def get_element(matrix: Matrix, row: int, col: int):
            return matrix[0][row * 6 + col][0]
        
        Y1 = self.make_matrix([[y] for y in y1], margin = 0)
        Q1 = self.make_tex('=')
        M1 = self.make_matrix(m1, padding = 1.75)
        Z1 = self.make_matrix(z1, margin = 0.25)
        Q1.move_to(M1, LEFT)
        Y1.move_to(Q1, LEFT)
        VGroup(Y1, Q1, M1, Z1).arrange(RIGHT)

        opera = [ # index of '=', '+' operator glyphs
            get_glyph_starts(Equations2[new_row][0], '[+=]')
            for new_row in range(7)
        ]

        stage = [[], [], [], []]
        Y = Y1[0]
        for new_row in range(7):
            eq1 = Equations2[new_row][0]
            opus = opera[new_row]
            p1 = opus[0]
            q = p1 + 1
            stage[0].append(TransformMatchingShapes(eq1[0:p1], Y[new_row]))
            if new_row != 3:
                stage[1].append(FadeOut(eq1[p1:q]))
            stage[1].append(TransformMatchingShapes(eq1[p1:q], Q1) if new_row == 3 else FadeOut(eq1[p1:q]))
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
            self.play(*stage[0]) # Show the column vector.
            self.play(FadeIn(Y1.get_brackets())) # Show its brackets.
            self.play(*stage[1]) # Coalesce the '=' signs.
            self.play(*stage[2]) # Hide the '+' signs.
            self.play(*stage[3], run_time=2) # Adjust the matrix layout.
            self.play(FadeIn(M1.get_brackets(), Z1)) # Show matrix brackets & Z0.

        def fly(source: Mobject, target: Mobject, arc: float) -> None:
            return ReplacementTransform(source, target, path_arc=arc, run_time=1.5)

        transforms = []
        Z = Z1[0]
        for new_col in range(5):
            idx = -2 if new_col < 4 else -1
            T = Z[new_col]
            transforms = []
            for new_row in range(new_col + 2):
                R = get_element(M1, new_row, new_col)
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

        Y2 = self.make_matrix([[y] for y in y2], margin = 0)
        Q2 = self.make_tex('=')
        M2 = self.make_matrix(m2, padding = 1.75)
        Z2 = self.make_matrix(z2, margin = 0.25)
        Q2.move_to(M2, LEFT)
        Y2.move_to(Q2, LEFT)
        VGroup(Y2, Q2, M2, Z2).arrange(RIGHT)

        transforms1 = []
        transforms2 = []
        for new_row in range(5):
            old_col = new_row+1
            transforms1.append(fly(get_element(M1, 0, old_col)[0], Y2[0][new_row], -PI/4))
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
                transforms2.append(fly(S, T, -PI/4))

        with self.say("Reading the matrix column by column, we can express the new coefficients in terms of the old."):
            self.play(FadeOut(Y1, Q1, M1.get_brackets(), M1[0][0], M1[0][6], Lines, Z1))
            self.play(transforms1)
            self.play(transforms2)
            junk = (Y2.get_brackets(), Q2, M2.get_brackets(), Z2)
            self.play(FadeIn(*junk))
            self.wait(2)
            self.play(FadeOut(*junk))

        for row in range(5):
            equ = self.make_tex(e5[0][row])
            equ.move_to(E[row+3], aligned_edge=LEFT)
            E[row+3] = equ
        E[3:8].arrange(DOWN, aligned_edge=LEFT)
        terms = []
        signs = []
        for row in range(5):
            T = split_smt(E[row+3][0])
            terms.append(TransformMatchingShapes(Y2[0][row], T[0]))
            for col in range(row+2):
                signs.append(T[2*col+1])
                terms.append(TransformMatchingShapes(get_element(M2, row, col), T[2*(col+1)]))
        self.play(terms)
        self.play(FadeIn(*signs))

        with self.say(
            """
            This h substitution avoids a lot of ugly fractions with powers of five denominators in the results. 
            Apply the substitution, collecting like powers of h. 
            """):

            def do(
                    s: int,
                    phase: int,
                    row: int,
                    a: int,
                    b: int,
                    c: int,
                    *glyph_map: tuple) -> None:
                E[s] = autopilot(E[s], e5[phase][row], a, b, c, *glyph_map)

            do(3,1,0,0,6,5,([0],FadeOut),([2],[0])) # 0=a+5h                -> a=-5h
            do(4,1,1,3,7,8,(FadeIn,[7]))            # p=b+4ah+10h²          -> p=b-20h²+10h²
            do(4,2,1,3,13,8,(ir(8,12),FadeOut))     # p=b-20h²+10h²         -> p=b-10h²
            do(5,1,2,7,12,12,(ir(0,16),ir(0,16)))   # q=c+3bh+6ah²+10h³     -> q=c+3bh-30h³+10h³
            do(5,2,2,7,17,12,(ir(12,16),FadeOut))   # q=c+3bh-30h³+10h³     -> q=c+3bh-20h³
            do(6,1,3,12,17,17,(ir(0,20),ir(0,20)))  # r=d+2ch+3bh²+4ah³+5h⁴ -> r=d+2ch+3bh²-20h⁴+5h⁴
            do(6,2,3,12,21,17,(ir(17,20),FadeOut))  # r=d+2ch+3bh²-20h⁴+5h⁴ -> r=d+2ch+3bh²-15h⁴
            do(7,1,4,14,18,18,(ir(0,20),ir(0,20)))  # s=e+dh+ch²+bh³+ah⁴+h⁵ -> s=e+dh+ch²+bh³-5h⁵+h⁵
            do(7,2,4,14,21,18,(ir(18,20),FadeOut))  # s=e+dh+ch²+bh³-5h⁵+h⁵ -> s=e+dh+ch²+bh³-4h⁵
            do(3,2,0,0,5,6,([0],[3]),([3],[5]),([4],[0]),(FadeIn,[4]))       # a=-5h -> h=-a/5
            self.wait(2)

        with self.say("Here are those ugly power of five denominators, if you prefer:"):
            for row in range(4):
                S = E[row+4]
                T = self.make_tex(e5[3][row+1]).move_to(S, aligned_edge=LEFT)
                self.box_on(S)                
                self.play(
                    TransformMatchingShapes(S, T),
                    self.box_move(T))
                E[row+4] = T
            self.box_off()
            self.play(FadeOut(E[3]))
            self.wait(2)

        with self.say("Or maybe not!"):
            animations = [FadeIn(E[3])]
            for row in range(4):
                S = E[row+4]
                T = self.make_tex(e5[2][row+1]).move_to(S, aligned_edge=LEFT)
                animations.append(TransformMatchingShapes(S, T))
                E[row+4] = T
            self.play(*animations)
            self.wait(2)

        with self.say("So we have finally managed to transform the original monic quintic into reduced form, "):
            F = VGroup(*[self.make_tex(e6[row]) for row in range(3)], *E[3:8].copy())
            F.arrange(DOWN, aligned_edge=LEFT)
            self.play(ReplacementTransform(E[3:8], F[3:8]))
            self.play(FadeIn(F[0:3]))
            self.box_on(F[1])
            self.wait()
            self.box_on(F[2])
            self.wait()

        with self.say("with these values for the new coefficients."):
            self.box_on(*F[4:8])
            self.wait(5)
            self.box_off()
            self.wait(2)

        with self.say("Later, we'll see how to get rid of the next intermediate term, the cubic."):
            self.box_on(F[2][0][9:12])
            self.play(FadeOut(F[0:2], F[3:]), run_time=5)
            self.box_off()
            self.play(FadeOut(F[2]), run_time=2)

        E = self.make_texes(*[e[0] for e in e7])
        E.shift(0.5*UP + 1.5*LEFT)

        with self.say("Let's test this reduced form using a numerical example."):
            self.play(Create(E[1]))

        with self.say("This is the same quintic we saw earlier."):
            graph.shift(3.5*RIGHT)
            self.play(FadeIn(border, axes))
            self.play(Create(plot), Create(dots), run_time=2)

        with self.say("Multiply out all these factors to find its coefficients, "):
            S = E[1]
            t = e7[1]                         # y &= (x+5)(x+3)(x+2)(x-1)(x-4)
            S = autopilot(S, t[1], 2, 12, 12) # y &= (x²+8x+15)(x+2)(x-1)(x-4)
            S = autopilot(S, t[2], 2, 17, 18) # y &= (x³+10x²+31x+30)(x-1)(x-4)
            S = autopilot(S, t[3], 2, 23, 20) # y &= (x⁴+9x³+21x²-x-30)(x-4)
            S = autopilot(S, t[4], 2, 28, 29) # y &= x⁵+5x⁴-15x³-85x²-26x+120'
            E[1] = S
            self.box_off()
            self.play(Create(E[2][0]))

        with self.say("then use these to calculate the new coefficients for the reduced equation."):
            for row in range(3,8):
                self.play(Create(E[row]))
                E[row] = autopilot(E[row], e7[row][1], 2, 0, 0)
            self.box_off()

        with self.say("Stick a pin in that, and let's go back briefly to the product of factors form."):
            E[1] = autopilot(E[1], e7[1][0], 2, 0, 0)
            self.box_off()

        with self.say("The new graph has the same shape as before, just shifted one unit to the right."):
            self.play(FadeOut(E[2]))
            self.play(Create(E[0]))
            self.play(Create(z_trace))
            E[0] = autopilot(E[0], e7[0][1], 2, 0, 0)
            self.play(FadeOut(E[3]))
            self.box_off()
            
        with self.say("So its roots are easily found, by similarly shifting the original roots."):
            n = len(E[1])-1
            E[2] = self.make_tex(e7[2][1]).move_to(E[2], aligned_edge=LEFT)
            self.play(TransformByGlyphMap(E[1].copy(), E[2], [(0,n),(0,n)]))

        with self.say("If our method is sound, then expanding this product should give the same coefficients as before."):
            for row in range(2, 7):
                p = 2+7*(row-2)
                E[2] = autopilot(E[2], e7[2][row], p, p+5, p+7, [FadeIn,(p+2,p+3)])
            for row in range(7, 12):
                p = 2+7*(11-row)
                E[2] = autopilot(E[2], e7[2][row], p, p+7, p+5, [(p+2,p+3),FadeOut])

        with self.say("Here goes..."):
            E[2] = autopilot(E[2], e7[2][12], 2, 0, 0)
        
        with self.say("And it does!"):
            self.box_on(E[4][0][2:], E[7][0][2:])
            self.play(FadeOut(E[0:2]))
            self.box_off()

            transforms = []
            for row in range(4,8):
                S = E[row][0][2:]
                p = [4, 9, 15, 19][row - 4]
                q = p + len(S)
                T = E[2][0][p:q]
                transforms.append(Transform(S.copy(), T, path_arc=PI/2))
            self.play(*transforms, run_time=1.5)

        self.wait(10)
        return

#endregion

if __name__ == "__main__":
    BaseScene.run(__file__)
