from painter import *
from base_scene import BaseScene

class TestSymbols(BaseScene):

    def construct(self):
        self.init()

        T0 = self.make_tex(r'\alpha\beta\gamma\delta\epsilon\zeta\eta\theta\iota\kappa\lambda\mu\nu\xi o\pi\rho\sigma\tau\upsilon\phi\chi\psi\omega')
        T1 = self.make_tex(r'AB\Gamma\Delta EZH\Theta IK\Lambda MN\Xi O\Pi P\Sigma T\Upsilon\Phi X\Psi\Omega')
        T2 = self.make_tex(
            r'''
                \leftarrow\rightarrow\uparrow\downarrow\leftrightarrow
                \updownarrow\leftharpoonup\rightharpoonup\leftharpoondown
                \rightharpoondown\nwarrow\swarrow\searrow\nearrow
                \Leftarrow\Rightarrow\Uparrow\Downarrow\Leftrightarrow
                \Updownarrow\rightleftharpoons\mapsto\longmapsto
            ''')

        T = VGroup(T0, T1, T2).arrange(DOWN, aligned_edge=LEFT)

        self.play(Create(T))
        self.wait(10)
