from painter import *
from poly_00_base import Poly_00_Base

class Poly_09_Constant(Poly_00_Base):

    def construct(self):
        self.init()

        self.set_colour_map((
            #('[Oo|]', ghost),
            (r'\\frac', red),
            (r'\\sqrt', orange),
            (r'[a-e]|\\alpha|\\beta|\\gamma|\\delta|\\epsilon', green),
            ('h', orange),
            (r'[p-s]|\\pi|\\rho\|\\sigma', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))
        
        t0 = r'\alpha\beta\gamma\delta\epsilon\zeta\eta\theta\iota\kappa\lambda\mu\nu\xi o\pi\rho\sigma\tau\upsilon\phi\chi\psi\omega'
        t1 = r'AB\Gamma\Delta EZH\Theta IK\Lambda MN\Xi O\Pi P\Sigma T\Upsilon\Phi X\Psi\Omega'
        t2 = r'''\leftarrow\rightarrow\uparrow\downarrow\leftrightarrow
            \updownarrow\leftharpoonup\rightharpoonup\leftharpoondown
            \rightharpoondown\nwarrow\swarrow\searrow\nearrow
            \Leftarrow\Rightarrow\Uparrow\Downarrow\Leftrightarrow
            \Updownarrow\rightleftharpoons\mapsto\longmapsto'''
        t3 = r'\sum_{a=0}^\infty 2^{-a}=1'
        t4 = r'\prod_{p=1}^5 p=120'
        t5 = r'\frac{x+y}{\sqrt{z+1}}'
        t6 = r'123'

        T0 = self.make_tex(t0)
        T1 = self.make_tex(t1)
        T2 = self.make_tex(t2)
        T3 = self.make_tex(t3)
        T4 = self.make_tex(t4)
        T5 = self.make_tex(t5)
        T6 = self.make_tex(t6)

        G1 = VGroup(T3, T4, T5, T6).arrange(RIGHT)
        T = VGroup(T0, T1, T2, G1).arrange(DOWN, aligned_edge=LEFT)
        self.play(Create(T))
        self.wait(10)

        return
        
        a0 = ['x&=z+h']
        a1 = ['y&=x^5+ax^4+bx^3+cx^2+dx+e']
        a2 = ['y&=z^5+0z^4+pz^3+qz^2+rz+s']
        a3 = ['x^5&=(z+h)^5']
        a4 = ['ax^4&=a(z+h)^4']
        a5 = ['bx^3&=b(z+h)^3']
        a6 = ['cx^2&=c(z+h)^2', 'cx^2&=c(z+h)(z+h)', 'cx^2&=c(z^2+2hz+h^2)', 'cx^2&=cz^2+2chz+ch^2)']
        a7 = ['dx&=d(z+h)', 'dx&=dz+dh']
        a8 = ['e&=e']
        
        b0 = 'x&=z+h'
        b1 = 'y&=x^5+ax^4+bx^3+cx^2+dx+e'
        b2 = 'y&=z^5+0z^4+pz^3+qz^2+rz+s'
        b3 = 'x^5&=(z+h)(z+h)^4'
        b4 = 'ax^4&=(z+h)(z+h)^3'
        b5 = 'bx^3&=(z+h)(z+h)^2'
        b6 = 'cx^2&=(z+h)(z+h)'
        b7 = 'dx&=(z+h)'
        b8 = 'e&=e'
        
        #n0 = r'x&=z+h+\alpha+\sqrt{\beta}+\sqrt[3]{\gamma}+\sqrt[123]{\delta}+o+O+|+o+O+|'
        #n1 = r'y&=x^5+ax^4+bx^3+cx^2+dx+e+\pi+\rho+\sigma'

        n0 = 'x&=z+h'
        n1 = 'y&=x^5+ax^4+bx^3+cx^2+dx+e'
        n2 = 'y&=z^5+0z^4+pz^3+qz^2+rz+s'
        n3 = 'x^5&=z^5+5hz^4+10h^2z^3+10h^3z^2+5h^4z+h^5'
        n4 = 'ax^4&=az^4+4ahz^3+6ah^2z^2+4ah^3z+ah^4'
        n5 = 'bx^3&=bz^3+3bhz^2+3bh^2z+bh^3'
        n6 = 'cx^2&=cz^2+2chz+ch^2'
        n7 = 'dx&=dz+dh'
        a8 = 'e&=e'

        def make_texx(*args) -> MathTex:
            tex = MathTex(r'\\'.join(args))
            self.paint(tex)
            return tex

        #tex = MathTex(fr'{a0}\\{a1}\\{a2}\\{a3}\\{a4}\\{a5}\\{a6}\\{a7}\\{a8}\\')
        tex = make_texx(n0, n1, n2, n3, n4, n5, n6, n7, a8)
        
        #print(tex.tex_string);
        self.painter.paint(tex)
        
        self.play(Create(tex))
        self.wait(10)
        self.play(Uncreate(tex))

        E1z = self.make_tex(r'y=\sum_{i=0}^{0}a_ix^i=a_0=0')
        E1y = MathTex(r'Degree=n=0').set_color(self.get_text_colour())
        E1y.next_to(E1z, DOWN)
        E1b = self.make_tex(r'a_n\neq{0}')
        E1b.next_to(E1y, DOWN)

        with self.say("The degree zero polynomial has no roots."):
            self.play(Create(E1z))

        with self.say("Notice that the equation, y equals zero, can have no solutions."):
            self.play(Create(E1y))

        with self.say("This is because a n is constrained to be both zero and nonzero.") as tracker:
            self.play(Create(E1b))
            boxes = [self.box(E1b), self.box(E1y[0][7:10]), self.box(E1z[0][13:17])]
            self.wait(tracker.duration + 2)
            self.play(FadeOut(E1z, E1y, E1b, *boxes))
            self.wait(2)
