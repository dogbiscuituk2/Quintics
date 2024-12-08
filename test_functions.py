from painter_old import *
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
        
        T1 = self.make_tex(r'\sin\alpha+\cos\beta+\tan\gamma+\csc\alpha+\sec\beta+\cot\gamma')
        T2 = self.make_tex(r'\arcsin\alpha+\arctan\gamma+\sinh\alpha+\cosh\beta+\tanh\gamma')
        T3 = self.make_tex(r'\exp{x}')
        
        T = VGroup(T1, T2).arrange(DOWN, aligned_edge=LEFT)
        self.play(Create(T))

        self.wait(10)

        return
