from painter import *
from base_scene import BaseScene

class TestFunctions(BaseScene):

    def construct(self):
        self.init()

        self.set_colour_map((
            #('[Oo|]', ghost),
            (r'\\frac', magenta),
            (r'\\sqrt|\\lim', orange),
            (r'[a-e]|\\alpha|\\beta|\\gamma|\\delta|\\epsilon', green),
            ('h', orange),
            (r'[p-s]|\\pi|\\rho\|\\sigma|\\sin', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))
        
        #T0 = self.make_tex(r'\alpha\beta\gamma\delta\epsilon\zeta\eta\theta\iota\kappa\lambda\mu\nu\xi o\pi\rho\sigma\tau\upsilon\phi\chi\psi\omega')
        #T1 = self.make_tex(r'AB\Gamma\Delta EZH\Theta IK\Lambda MN\Xi O\Pi P\Sigma T\Upsilon\Phi X\Psi\Omega')
        #T2 = self.make_tex(
        #    r'''
        #        \leftarrow\rightarrow\uparrow\downarrow\leftrightarrow
        #        \updownarrow\leftharpoonup\rightharpoonup\leftharpoondown
        #        \rightharpoondown\nwarrow\swarrow\searrow\nearrow
        #        \Leftarrow\Rightarrow\Uparrow\Downarrow\Leftrightarrow
        #        \Updownarrow\rightleftharpoons\mapsto\longmapsto
        #    ''')
        T3 = self.make_tex(r'\lim_{x\rightarrow 0}\frac{\sin{x}}{x}}=1')
        #T4 = self.make_tex(r'\sum_{a=0}^\infty 2^{-a}=1')
        #T5 = self.make_tex(r'\prod_{p=1}^5 p=120')
        #T6 = self.make_tex(r'\frac{x+y}{\sqrt{z+1}}')

        #G1 = VGroup(T3, T4, T5, T6).arrange(RIGHT)
        #T = VGroup(T0, T1, T2, G1).arrange(DOWN, aligned_edge=LEFT)
        #self.play(Create(T))

        self.play(Create(T3))
        self.wait(10)

        return
