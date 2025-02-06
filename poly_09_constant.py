#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import BaseScene
from MF_Tools import *
from painter import *

class Poly_09_Constant(BaseScene):

    def __init__(self):
        BaseScene.__init__(self)

    def construct(self):

        self.set_pens((
            (r'\\frac', Pen.RED),
            (r'\\sqrt', Pen.ORANGE),
            (r'[a-e]|\\alpha|\\beta|\\gamma|\\delta|\\epsilon', Pen.GREEN),
            ('h', Pen.ORANGE),
            (r'[p-s]|\\pi|\\rho\|\\sigma', Pen.YELLOW),
            ('x', Pen.RED),
            ('y', Pen.MAGENTA),
            ('z', Pen.CYAN)))

        E1z = self.make_tex(r'y=\sum_{i=0}^{0}a_ix^i=a_0=0')
        E1y = MathTex(r'Degree=n=0').set_color(self.ink_fg)
        E1y.next_to(E1z, DOWN)
        E1b = self.make_tex(r'a_n\neq{0}')
        E1b.next_to(E1y, DOWN)

        with self.say("The degree zero polynomial has no roots."):
            self.play(Create(E1z))

        with self.say("Notice that the equation, y equals zero, can have no solutions."):
            self.play(Create(E1y))

        with self.say("This is because a n is constrained to be both zero and nonzero.") as tracker:
            self.play(Create(E1b))
            #b1 = self.box(E1b)
            #b2 = self.box(E1y[0][7:10])
            b3 = self.box(E1z[0][13:17])
            boxes = VGroup(b1, b2, b3)
            self.wait(tracker.duration + 2)
            self.play(FadeOut(E1z, E1y, E1b, *boxes))
            self.wait(2)

if __name__ == "__main__":
    import os
    module_name = os.path.abspath(__file__).split(os.sep)[-1]
    # py -m: run library module as a script (terminates option list)
    # manim -a: all scenes, -p: preview, -ql: 480p15, -qm: 720p30,
    # -qh: 1080p60, -qp: 1440p60, -qk: 2160p60.
    command_line = f'py -m manim render -a -p -ql {module_name}'
    print(command_line)
    os.system(command_line)
