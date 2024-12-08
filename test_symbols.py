from painter_old import *
from base_scene import BaseScene

class TestSymbols(BaseScene):

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

        T0 = self.make_tex(
            r'''
                \alpha\beta\gamma\delta\epsilon\zeta\eta\theta\iota
                \kappa\lambda\mu\nu\xi o\pi\rho\sigma\tau\upsilon\phi
                \chi\psi\omega\varepsilon\vartheta\varkappa\varpi
                \varrho\varsigma\varphi\aleph\beth\gimel\daleth
            ''')
        
        T1 = self.make_tex(
            r'''
                AB\Gamma\Delta EZH\Theta IK\Lambda MN\Xi O\Pi P\Sigma T
                \Upsilon\Phi X\Psi\Omega
            ''')

        T2 = self.make_tex(
            r'''
                \leftarrow\rightarrow\uparrow\downarrow
                \leftrightarrow\updownarrow
                \leftharpoonup\rightharpoonup
                \leftharpoondown\rightharpoondown
                \nwarrow\swarrow\searrow\nearrow
                \Leftarrow\Rightarrow\Uparrow\Downarrow
                \Leftrightarrow\Updownarrow\rightleftharpoons
                \mapsto\longmapsto
            ''')

        T = VGroup(T0, T1, T2).arrange(DOWN, aligned_edge=LEFT)

        self.play(Create(T))
        self.wait(10)
