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

        e1a = r" =  x^5"
        e1b = r" + ax^4"
        e1c = r" + bx^3"
        e1d = r" + cx^2"
        e1e = r" + dx"
        e1f = r" + e"

        e1 = rf"y {e1a}{e1b}{e1c}{e1d}{e1e}{e1f}"
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
        E1a = MathTex(e1a)
        E1b = MathTex(e1b)
        E1c = MathTex(e1c)
        E1d = MathTex(e1d)
        E1e = MathTex(e1e)
        E1f = MathTex(e1f)

#E1 = MathTex(e1)

        E1a = MathTex(e1a)
        E1b = MathTex(e1b)
        E1c = MathTex(e1c)
        E1d = MathTex(e1d)
        E1e = MathTex(e1e)
        E1f = MathTex(e1f)
        
        E1 = MathTex(e1)
        E2 = MathTex(e2)
        E3 = MathTex(e3)
        E4 = MathTex(e4)

        g = Group(E1, E2, E3, E1a, E1b, E1c, E1d, E1e, E1f).arrange(DOWN, aligned_edge = LEFT)

        self.play(Create(E1))
        self.wait(3)
        self.play(TransformFromCopy(E1, E2))
        self.wait(3)
        self.play(TransformFromCopy(E1, E3))
        self.wait(3)
        self.play(Create(E1a))
        self.play(Create(E1b))
        self.play(Create(E1c))
        self.play(Create(E1d))
        self.play(Create(E1e))
        self.play(Create(E1f))
        self.wait(3)
        self.play(Create(E4))
        self.wait(3)

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

        #self.add(index_labels(E8[2]))
        #self.add(E8)
        
        #for p in E8[2]:
        #    p.set_color(BLUE)
        #    self.wait(1)

        self.play(ReplacementTransform(E4, E8))
        self.wait(5)
        self.play(ReplacementTransform(E8, E9))
        self.wait(5)
