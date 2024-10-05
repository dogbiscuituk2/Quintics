from manim import *

class Quintic01(Scene):
    def construct(self):

        def hide_chars(chars):
            for char in chars:
                #char.set_color(RED)
                char.set_opacity(0)

        def pause():
            self.wait(0)

        Y1 = MathTex('(ay^1=')

        Y2 = MathTex(
            '(ax^5=', 
            '(ax^4=', 
            '(bx^3=', 
            '(cx^2=', 
            '(dx^1=', 
            '(ex^0=').arrange(DOWN, aligned_edge = RIGHT)

        E1 = MathTex(
            'ax^5)+', 
            'ax^4)+', 
            'bx^3)+', 
            'cx^2)+', 
            'dx^1)+', 
            'ex^0)')

        E3 = MathTex(
            'az^5+', 
            '00z^4+', 
            '01^1pz^3+', 
            '01^1qz^2+', 
            '01^1rz+', 
            'hs^1)')

        E4 = MathTex(
            'a(z+h)^5', 
            'a(z+h)^4', 
            'b(z+h)^3', 
            'c(z+h)^2', 
            'd(z+h)^1', 
            'e)^1').arrange(DOWN, aligned_edge = LEFT)

        E5 = MathTex(
            'a(z^5 + 5hz^4 + 10h^2z^3 + 10h^3z^2 + 5h^4z + h^5)',
            'a(z^4 + 4hz^3 + 6h^2z^2 + 4h^3z + h^4)',
            'b(z^3 + 3hz^2 + 3h^2z + h^3)',
            'c(z^2 + 2hz + h^2)',
            'd(z + h)^1',
            'e)^1')

        E6 = VGroup(
            MathTex(
                'az^5+',
                '5hz^4+',
                '10h^2z^3+',
                '10h^3z^2+',
                '05h^4z+',
                'sh^5)'),
            MathTex(
                'az^4+',
                '04ahz^3+',
                '6ah^2z^2+',
                '4ah^3z+',
                'ah^4)'),
            MathTex(
                'bz^3+',
                '03bhz^2+',
                '3bh^2z+',
                'bh^3)'),
            MathTex(
                'cz^2+',
                '02chz+',
                'ch^2)'),
            MathTex(
                'dz+',
                'dh^1)'),
            MathTex(
                'eh^1)')
        )

        hide_chars([
            Y1[0][0], Y1[0][1], Y1[0][3],
            Y2[0][0], Y2[0][1], Y2[1][0], Y2[2][0], Y2[3][0], Y2[4][0], Y2[4][3], Y2[5][0], Y2[5][2], Y2[5][3],
            E1[0][0], E1[0][3], E1[1][3], E1[2][3], E1[3][3], E1[4][2], E1[4][3], E1[5][1], E1[5][2], E1[5][3],
            E3[0][0], E3[1][0], E3[2][0], E3[2][1], E3[2][2], E3[3][0], E3[3][1], E3[3][2], E3[4][0], E3[4][1], E3[4][2], E3[5][0], E3[5][2], E3[5][3],
            E4[0][0], E4[4][6], E4[5][1], E4[5][2],
            E5[0][0], E5[4][6], E5[5][1], E5[5][2],

            E6[0][0][0], E6[0][4][0], E6[0][5][0], E6[0][5][3], 
            E6[1][1][0], E6[1][4][3], 
            E6[2][1][0], E6[2][3][3], 
            E6[3][1][0], E6[3][2][3], 
            E6[4][1][2], E6[4][1][3], 
            E6[5][0][1], E6[5][0][2], E6[5][0][3],
        ])

        Y3 = Matrix([
            ['(ay^1)'],
            ['(ax^5)'],
            ['(ax^4)'],
            ['(bx^3)'],
            ['(cx^2)'],
            ['(dx^1)'],
            ['(ex^0)']], bracket_h_buff = 0)

        for i in range(7):
            hide_chars([Y3[0][i][0][0], Y3[0][i][0][4]])

        hide_chars([
            Y3[0][0][0][1], Y3[0][0][0][3],
            Y3[0][1][0][1],
            Y3[0][2][0][4],
            Y3[0][3][0][4],
            Y3[0][4][0][4],
            Y3[0][5][0][3],
            Y3[0][6][0][2], Y3[0][6][0][3]])

        M3 = Matrix([
            ['(z^5', '(0z^4', '(pz^3', '(qz^2', '(^1rz', '(s^1'],
            ['(z^5', '(5hz^4', '(10h^2z^3', '(10h^3z^2', '(5h^4z', '(h^5'],
            ['', '(az^4', '(4ahz^3', '(6ah^2z^2', '(4ah^3z', '(ah^4'],
            ['', '', '(bz^3', '(3bhz^2', '(3bh^2z', '(bh^3'],
            ['', '', '', '(cz^2', '(2chz', '(ch^2'],
            ['', '', '', '', '(dz', '(dh^1'],
            ['', '', '', '', '', '(eh^0']
        ], bracket_h_buff = 0, h_buff = 1.9)

        for i in range(6):
            hide_chars(M3[0][i][0][0])
            for j in range(i, 6):
                hide_chars(M3[0][6 * (i + 1) + j][0][0])

        hide_chars([
            M3[0][4][0][1],
            M3[0][5][0][2],
            M3[0][35][0][3],
            M3[0][41][0][2], M3[0][41][0][3]])

        Z1 = Matrix([
            ['(1^0'],
            ['(1^0'],
            ['(1^0'],
            ['(1^0'],
            ['(1^0'],
            ['(1^0']], bracket_h_buff = 0)

        for i in range(6):
            hide_chars([Z1[0][i][0][0], Z1[0][i][0][2]])

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
        self.play(TransformMatchingShapes(Y, Y3))
        self.play(FadeIn(EQ))
        self.play(TransformMatchingShapes(M, M3))
        self.play(FadeIn(Z1))

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
