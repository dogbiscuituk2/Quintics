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

class Quintic00(Scene):
    def construct(self):

        def hide_chars2(tex):
            x = tex.get_part_by_tex('%')
            print(x)
            print(type(x))
            print(x.get_tex_string())

        Y1 = MathTex(
            r'(ay^1\ %123')
        
        hide_chars2(Y1)


class Quintic01(Scene):
    def construct(self):

        def hide_chars(chars):
            for char in chars:
                #char.set_color(RED)
                char.set_opacity(0)

        def pause():
            self.wait(0)

        Y1 = MathTex(
            r'(ay^1=')
        
        Y2 = MathTex(
            r'(ax^5=', 
            r'(ax^4=', 
            r'(bx^3=', 
            r'(cx^2=', 
            r'(dx^1=', 
            r'(ex^0='
            ).arrange(DOWN, aligned_edge = LEFT)

        E1 = MathTex(
            r'ax^5)+', 
            r'ax^4)+', 
            r'bx^3)+', 
            r'cx^2)+', 
            r'dx^1)+', 
            r'ex^0)')

        E3 = MathTex(
            r'az^5)+', 
            r'0z^4)+', 
            r'pz^3)+', 
            r'qz^2)+', 
            r'rz^1)+', 
            r'sz^0)')

        E4 = MathTex(
            r'a(z+h)^5', 
            r'a(z+h)^4', 
            r'b(z+h)^3', 
            r'c(z+h)^2', 
            r'd(z+h)^1', 
            r'e)^1'
            ).arrange(DOWN, aligned_edge = LEFT)

        E5 = MathTex(
            r'a(z^5 + 5hz^4 + 10h^2z^3 + 10h^3z^2 + 5h^4z + h^5)',
            r'a(z^4 + 4hz^3 + 6h^2z^2 + 4h^3z + h^4)',
            r'b(z^3 + 3hz^2 + 3h^2z + h^3)',
            r'c(z^2 + 2hz + h^2)',
            r'd(z + h)^1',
            r'e)^1'
        )

        E6 = VGroup(
            MathTex(
                r'az^5+',
                r'5hz^4+',
                r'10h^2z^3+',
                r'10h^3z^2+',
                r'5h^4z+',
                r'h^5)'),
            MathTex(
                r'az^4+',
                r'4ahz^3+',
                r'6ah^2z^2+',
                r'4ah^3z+',
                r'ah^4)'),
            MathTex(
                r'bz^3+',
                r'3bhz^2+',
                r'3bh^2z+',
                r'bh^3)'),
            MathTex(
                r'cz^2+',
                r'2chz+',
                r'ch^2)'),
            MathTex(
                r'dz+',
                r'dh)^1'),
            MathTex(
                r'e)^1')
        )

        hide_chars([
            Y1[0][0], Y1[0][1], Y1[0][3],
            Y2[0][0], Y2[0][1], Y2[1][0], Y2[2][0], Y2[3][0], Y2[4][0], Y2[4][3], Y2[5][0], Y2[5][2], Y2[5][3],
            E1[0][0], E1[0][3], E1[1][3], E1[2][3], E1[3][3], E1[4][2], E1[4][3], E1[5][1], E1[5][2], E1[5][3],
            E3[0][0], E3[0][3], E3[1][3], E3[2][3], E3[3][3], E3[4][2], E3[4][3], E3[5][1], E3[5][2], E3[5][3],
            E4[0][0], E4[4][6], E4[5][1], E4[5][2],
            E5[0][0], E5[4][6], E5[5][1], E5[5][2],
            E6[0][0][0], E6[0][5][2], E6[1][4][3], E6[2][3][3], E6[3][2][3], E6[4][1][2], E6[4][1][3], E6[5][0][1], E6[5][0][2],
            ])

        E2 = E1.copy().arrange(DOWN, aligned_edge = LEFT)
        G1 = VGroup(E1, E2).arrange(DOWN, aligned_edge = LEFT)
        Y = VGroup(Y1, Y2).arrange(DOWN, aligned_edge = LEFT)
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
        self.play(Transform(E1, E3))
        pause()

        self.play(Indicate(Y))
        self.play(Indicate(E3))
        self.play(Indicate(E6))

        #E7 = E6.copy()
        #E7.arrange(DOWN, aligned_edge = RIGHT)
        #E8 = VGroup(E3, E7).arrange(RIGHT, aligned_edge = UP)
        #self.play(Transform(E6, E7))

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
