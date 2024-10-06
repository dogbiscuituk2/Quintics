from manim import *

class Quintic01(Scene):
    def construct(self):

        def get_count(s):
            return s.count()

        def hide_chars(*args):
            for arg in args:
                #arg.set_color(RED)
                arg.set_opacity(0)

        def make_tex(*args):
            s = [f'({arg}' for arg in args]
            tex = MathTex(*s)
            for t in tex:
                t[0].set_color(RED)
                #t[0].set_opacity(0)
            return tex

        def pause():
            self.wait(0)

        Y1 = make_tex(r'y^1\ =')
        hide_chars(Y1[0][2])
        Y2 = make_tex(r'x^5\ =', r'ax^4\ =', r'bx^3\ =', r'cx^2\ =', r'dx\ =', r'e\ =').arrange(DOWN, aligned_edge = RIGHT)
        E1 = make_tex('x^5+', 'ax^4+', 'bx^3+', 'cx^2+', 'dx+', 'e')
        E3 = make_tex('z^5+', '0z^4+', 'pz^3+', 'qz^2+', 'rz+', 's')
        E4 = make_tex('(z+h)^5', 'a(z+h)^4', 'b(z+h)^3', 'c(z+h)^2', 'd(z+h)', 'e').arrange(DOWN, aligned_edge = LEFT)
        E5 = make_tex(
            'a(z^5 + 5hz^4 + 10h^2z^3 + 10h^3z^2 + 5h^4z + h^5)',
            'a(z^4 + 4hz^3 + 6h^2z^2 + 4h^3z + h^4)',
            'b(z^3 + 3hz^2 + 3h^2z + h^3)',
            'c(z^2 + 2hz + h^2)',
            'd(z + h)',
            'e')
        E6 = VGroup(
            make_tex('z^5+', '5hz^4+', '10h^2z^3+', '10h^3z^2+', '5h^4z+', 'sh^5'),
            make_tex('az^4+', '4ahz^3+', '6ah^2z^2+', '4ah^3z+', 'ah^4'),
            make_tex('bz^3+', '3bhz^2+', '3bh^2z+', 'bh^3'),
            make_tex('cz^2+', '2chz+', 'ch^2'),
            make_tex('dz+', 'dh'),
            make_tex('e')
        )

        Y3 = Matrix([
            ['(ay^1)'],
            ['(ax^5)'],
            ['(ax^4)'],
            ['(bx^3)'],
            ['(cx^2)'],
            ['(dx^1)'],
            ['(ex^0)']], bracket_h_buff = 0)

        for i in range(7):
            hide_chars(Y3[0][i][0][0], Y3[0][i][0][4])

        hide_chars(
            Y3[0][0][0][1], Y3[0][0][0][3],
            Y3[0][1][0][1],
            Y3[0][2][0][4],
            Y3[0][3][0][4],
            Y3[0][4][0][4],
            Y3[0][5][0][3],
            Y3[0][6][0][2], Y3[0][6][0][3])

        M3 = Matrix([
            ['(z^5', '(0z^4', '(pz^3', '(qz^2', '(^1rz', '(s^1'],
            ['(z^5', '(5hz^4', '(10h^2z^3', '(10h^3z^2', '(5h^4z', '(h^5'],
            ['', '(az^4', '(4ahz^3', '(6ah^2z^2', '(4ah^3z', '(ah^4'],
            ['', '', '(bz^3', '(3bhz^2', '(3bh^2z', '(bh^3'],
            ['', '', '', '(cz^2', '(2chz', '(ch^2'],
            ['', '', '', '', '(dz', '(dh^1'],
            ['', '', '', '', '', '(eh^0']
        ], bracket_h_buff = 0.1, h_buff = 1.8)

        for i in range(6):
            hide_chars(M3[0][i][0][0])
            for j in range(i, 6):
                hide_chars(M3[0][6 * (i + 1) + j][0][0])

        hide_chars(
            M3[0][4][0][1],
            M3[0][5][0][2],
            M3[0][35][0][3],
            M3[0][41][0][2], M3[0][41][0][3])

        Z1 = Matrix([
            ['(1^0'],
            ['(1^0'],
            ['(1^0'],
            ['(1^0'],
            ['(1^0'],
            ['(1^0']], bracket_h_buff = 0)

        for i in range(6):
            hide_chars(Z1[0][i][0][0], Z1[0][i][0][2])

        E2 = E1.copy().arrange(DOWN, aligned_edge = LEFT)
        G1 = VGroup(E1, E2).arrange(DOWN, aligned_edge = LEFT)
        Y = VGroup(Y1, Y2).arrange(DOWN, aligned_edge = RIGHT)
        G3 = VGroup(Y, G1).arrange(RIGHT, aligned_edge = UP);

        self.play(FadeIn(Y1))
        self.play(Create(E1))
        pause()

        self.play(TransformFromCopy(E1, E2, path_arc = 2))
        pause()

        self.play(TransformMatchingShapes(E2, Y2))
        pause()

        E4.move_to(E2, aligned_edge = LEFT)
        self.play(Create(E4))
        pause()

        for index in range(6):
            E5[index].move_to(E4[index], aligned_edge = LEFT)
            if index < 5:
                self.play(Indicate(E4[index]))
            self.play(TransformMatchingShapes(E4[index], E5[index]))
            E6[index].move_to(E5[index], aligned_edge = LEFT)
            self.play(TransformMatchingShapes(E5[index], E6[index]))
        pause()

        E3.move_to(E1, aligned_edge = LEFT)
        self.play(Indicate(E1))
        self.play(ReplacementTransform(E1, E3))
        pause()

        EQ = MathTex('=')

        M = VGroup(E3, E6)
        E7 = E6.copy().arrange(DOWN, aligned_edge = RIGHT)
        E8 = VGroup(E3.copy(), E7).arrange(DOWN, aligned_edge = RIGHT)
        E8.move_to(M)
        self.play(Transform(E3, E8[0]))
        for index in range(6):
            self.play(Transform(E6[index], E7[index]))
        pause()

################################################################################

        VGroup(Y3, EQ, M3, Z1).arrange(RIGHT, aligned_edge = UP)
        EQ.move_to(EQ.get_center() + 2.9 * DOWN)
        Z1.move_to(Z1.get_center() + 0.5 * DOWN)
        self.play(TransformMatchingShapes(Y, Y3))
        self.play(FadeIn(EQ))
        self.play(TransformMatchingShapes(M, M3))
        self.play(FadeIn(Z1))
        pause()

        def replace(S, t):
            return TransformMatchingShapes(S, MathTex(t).move_to(S.get_center()))

        self.play(
            Indicate(M3[0][0]),
            Indicate(M3[0][6]))
        self.play(
            replace(M3[0][0], '1'),
            replace(M3[0][6], '1'),
            replace(Z1[0][0], 'z^5'))

        self.play(
            Indicate(M3[0][1]),
            Indicate(M3[0][7]),
            Indicate(M3[0][13]))
        self.play(
            replace(M3[0][1], '0'),
            replace(M3[0][7], '5h'),
            replace(M3[0][13], 'a'),
            replace(Z1[0][1], 'z^4'))

        self.play(
            Indicate(M3[0][2]),
            Indicate(M3[0][8]),
            Indicate(M3[0][14]),
            Indicate(M3[0][20]))
        self.play(
            replace(M3[0][2], 'p'),
            replace(M3[0][8], '10h^2'),
            replace(M3[0][14], '4ah'),
            replace(M3[0][20], 'b'),
            replace(Z1[0][2], 'z^3'))

        self.play(
            Indicate(M3[0][3]),
            Indicate(M3[0][9]),
            Indicate(M3[0][15]),
            Indicate(M3[0][21]),
            Indicate(M3[0][27]))
        self.play(
            replace(M3[0][3], 'q'),
            replace(M3[0][9], '10h^3'),
            replace(M3[0][15], '6ah^2'),
            replace(M3[0][21], '3bh'),
            replace(M3[0][27], 'c'),
            replace(Z1[0][3], 'z^2'))

        self.play(
            Indicate(M3[0][4]),
            Indicate(M3[0][10]),
            Indicate(M3[0][16]),
            Indicate(M3[0][22]),
            Indicate(M3[0][28]),
            Indicate(M3[0][34]))
        self.play(
            replace(M3[0][4], 'r'),
            replace(M3[0][10], '5h^4'),
            replace(M3[0][16], '4ah^3'),
            replace(M3[0][22], '3bh^2'),
            replace(M3[0][28], '2ch'),
            replace(M3[0][34], 'd'),
            replace(Z1[0][4], 'z'))

        self.wait(10)


class Quintic02(Scene):
    def construct(self):

        e1z = r"= x^5"
        e1a = r"+ ax^4"
        e1b = r"+ bx^3"
        e1c = r"cx^2"
        e2d = r"+ dx"
        e2e = r"+ e"

        e1 = r"y = x^5 + ax^4 + bx^3 + cx^2 + dx + e"

        E1 = VGroup(MathTex(e1))

        self.play(Create(E1))
        self.wait(3)

        
        e2 = r"y = (z+h)^5 + a(z+h)^4 + b(z+h)^3 + c(z+h)^2 + d(z+h) + e"
        e3 = r"y = z^5 + 0z^4 + pz^3 + qz^2 + rz + s"

        e4 = r"""
             x^5 & =  (z+h)^5 =  z^5 +  5hz^4 + 10h^2z^3 + 10h^3z^2 + 5h^4z + h^5 \\
            ax^4 & = a(z+h)^4 = az^4 + 4ahz^3 + 6ah^2z^2 + 4ah^3z   + ah^4 \\
            bx^3 & = b(z+h)^3 = bz^3 + 3bhz^2 + 3bh^2z   +  bh^3 \\
            cx^2 & = c(z+h)^2 = cz^2 + 2chz   +  ch^2 \\
            dx   & = d(z+h)   = dz   +  dh \\
            e    & = e
        """
        E1 = MathTex(e1)
        E2 = MathTex(e2)
        E3 = MathTex(e3)
        E4 = MathTex(e4)

        Y = r"\begin{pmatrix} y \\ \hline x^5 \\ ax^4 \\ bx^3 \\ cx^2 \\ dx \\ e \end{pmatrix}"
        
        M1 = r"""\begin{pmatrix} 
            z^5 & 0z^4 & pz^3 & qz^2 & rz & s \\
            \hline 
            z^5 & 5hz^4 & 10h^2z^3 & 10h^3z^2 &  5h^4z &  h^5 \\ 
             .  &  az^4 &   4ahz^3 & 6ah^2z^2 & 4ah^3z & ah^4 \\ 
             .  &     . &     bz^3 &   3bhz^2 & 3bh^2z & bh^3 \\ 
             .  &     . &        . &     cz^2 &   2chz & ch^2 \\ 
             .  &     . &        . &        . &     dz & dh   \\ 
             .  &     . &        . &        . &      . & e
        \end{pmatrix}"""
        
        M2 = r"""\begin{pmatrix} 
            1 & 0 & p & q & r & s \\
            \hline 
            1 & 5h & 10h^2 & 10h^3 &  5h^4 &  h^5 \\ 
            . &  a &   4ah & 6ah^2 & 4ah^3 & ah^4 \\ 
            . &  . &     b &   3bh & 3bh^2 & bh^3 \\ 
            . &  . &     . &     c &   2ch & ch^2 \\ 
            . &  . &     . &     . &     d & dh   \\ 
            . &  . &     . &     . &     . & e  
        \end{pmatrix}"""

        Z1 = r"\begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}"
        Z2 = r"\begin{pmatrix} z^5 \\ z^4 \\ z^3 \\ z^2 \\ z \\ 1 \end{pmatrix}"
        
        E8 = MathTex(Y, r"=", M1, Z1)
        E9 = MathTex(Y, r"=", M2, Z2)
        
        g = Group(E1, E2, E3, E8).arrange(DOWN, aligned_edge = LEFT)

        self.play(Create(E1))
        self.wait(3)

        #self.play(TransformFromCopy(E1, E2))
        #self.wait(3)
        #self.play(TransformFromCopy(E1, E3))
        #self.wait(3)
        #self.play(Create(E4))
        #self.wait(3)

        #self.play(Create(E8))
        #self.wait(3)

        #self.play(ReplacementTransform(E4, E8))
        #self.wait(5)
        #self.play(ReplacementTransform(E8, E9))
        #self.wait(5)
