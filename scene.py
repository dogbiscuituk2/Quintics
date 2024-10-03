from manim import *

class Equation(Scene):
    def construct(self):
        t1 = Tex(r"$x_{1, 2} =$", r"$\frac{-b \pm \sqrt{D}}{2a}$", font_size = 96)
        t2 = Tex(r"$x_{1, 2} =$", r"$\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$", font_size = 96)
        g = VGroup(t1, t2).arrange(DOWN, aligned_edge = LEFT, buff = 1)
        self.play(Write(t1))
        self.wait(0.5)
        self.play(TransformFromCopy(t1[0], t2[0]))
        self.play(TransformFromCopy(t1[1], t2[1]))
        self.wait()

class Quintic01(Scene):
    def construct(self):

        def hide_chars(chars):
            for char in chars:
                char.set_color(BLACK)

        pause = 1;

        Y1 = MathTex(r'(ay^1\ ')
        E1 = MathTex(r'=\ 1x^5)', r'+\ ax^4)', r'+\ bx^3)', r'+\ cx^2)', r'+\ dx^1)', r'+\ ex^0)')
        E3 = MathTex(r'=\ 1z^5)', r'+\ 0z^4)', r'+\ pz^3)', r'+\ qz^2)', r'+\ rz^1)', r'+\ sz^0)')
        Y2 = MathTex(r'(1x^5', r'(ax^4', r'(bx^3', r'(cx^2', r'(dx^1', r'(ex^0').arrange(DOWN, aligned_edge = LEFT)
        E4 = MathTex(r'=\ 1(z+h)^5', r'=\ a(z+h)^4', r'=\ b(z+h)^3', r'=\ c(z+h)^2', r'=\ d(z+h)^1', r'=\ e)').arrange(DOWN, aligned_edge = LEFT)

        E5 = MathTex(
            r'=\ 1(z^5 + 5hz^4 + 10h^2z^3 + 10h^3z^2 + 5h^4z + h^5)',
            r'=\ a(z^4 + 4hz^3 + 6h^2z^2 + 4h^3z + h^4)',
            r'=\ b(z^3 + 3hz^2 + 3h^2z + h^3)',
            r'=\ c(z^2 + 2hz + h^2)',
            r'=\ d(z + h)',
            r'=\ e'
        )

        E6 = MathTex(
            r'=\ 1z^5 + 5hz^4 + 10h^2z^3 + 10h^3z^2 + 5h^4z + h^5',
            r'=\ az^4 + 4ahz^3 + 6ah^2z^2 + 4ah^3z + ah^4',
            r'=\ bz^3 + 3bhz^2 + 3bh^2z + bh^3',
            r'=\ cz^2 + 2chz + ch^2)',
            r'=\ dz + dh',
            r'=\ e'
        )

        hide_chars([
            Y1[0][0], Y1[0][1], Y1[0][3],
            E1[0][1], E1[0][4], E1[1][4], E1[2][4], E1[3][4], E1[4][3], E1[4][4], E1[5][2], E1[5][3], E1[5][4],
            E3[0][1], E3[0][4], E3[1][4], E3[2][4], E3[3][4], E3[4][3], E3[4][4], E3[5][2], E3[5][3], E3[5][4],
            Y2[0][0], Y2[0][1], Y2[1][0], Y2[2][0], Y2[3][0], Y2[4][0], Y2[4][3], Y2[5][0], Y2[5][2], Y2[5][3],
            E4[0][1], E4[4][7], E4[5][2]
            ])

        E2 = E1.copy().arrange(DOWN, aligned_edge = LEFT)
        G1 = VGroup(E1, E2).arrange(DOWN, aligned_edge = LEFT)
        G2 = VGroup(Y1, Y2).arrange(DOWN, aligned_edge = LEFT)
        G3 = VGroup(G2, G1).arrange(RIGHT, aligned_edge = UP);

        self.play(FadeIn(Y1))
        self.play(Create(E1))
        self.wait(pause)

        self.play(TransformFromCopy(E1, E2, path_arc = 2))
        self.wait(pause)

        E3.move_to(E1, aligned_edge = LEFT)
        self.play(Transform(E1, E3))
        self.wait(pause)

        self.play(TransformMatchingShapes(E2, Y2))
        self.wait(pause)

        E4.move_to(E2, aligned_edge = LEFT)
        self.play(Create(E4))
        self.wait(pause)

        for index in range(6):
            E5[index].move_to(E4[index], aligned_edge = LEFT)
            self.play(TransformMatchingShapes(E4[index], E5[index]))
            self.wait(pause)

        for index in range(6):
            E6[index].move_to(E5[index], aligned_edge = LEFT)
            self.play(TransformMatchingShapes(E5[index], E6[index]))
            self.wait(pause)


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

class Quintic03(Scene):
    def construct(self):

        e1 = 'y = x^5 + ax^4 + bx^3 + cx^2 + dx + e'
        E1 = MathTex(e1)
        e2 = 'y = z^5 + 0z^4 + pz^3 + qz^2 + rz + s'
        E2 = MathTex(e2)
        G = VGroup(E1, E2).arrange_submobjects(DOWN, aligned_edge = LEFT);
        self.play(Create(G))
        self.wait(3)
        X5 = VGroup(E1[0][2], E1[0][3], E1[0][6], E1[0][7])
        Z5 = VGroup(E2[0][2], E2[0][3])
        self.play(Transform(X5, Z5))
        self.wait(3)
