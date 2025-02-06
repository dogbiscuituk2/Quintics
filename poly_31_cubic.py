#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import BaseScene
from MF_Tools import *
from painter import *

class Poly_31_Cubic(BaseScene):

    def __init__(self):
        BaseScene.__init__(self)

    def construct(self):

        self.set_pens((
            ('[a-e]', Pen.GREEN),
            ('h', Pen.ORANGE),
            ('[p-s]', Pen.YELLOW),
            ('x', Pen.RED),
            ('y', Pen.MAGENTA),
            ('z', Pen.CYAN)))

        E1z = self.make_ssmt(r'y=\sum_{i=0}^{3}a_ix^i=0')
        E1y = MathTex(r'Degree=n=3').set_color(self.get_text_colour())
        E1b = self.make_ssmt(r'y=x^3+ax^2+bx+c')

        G = VGroup(E1z, E1y, E1b).arrange(DOWN)

        with self.say("The degree three polynomial, the cubic, has three roots."):
            self.play(Create(E1z))
            self.play(Create(E1y))
            self.play(Create(E1b))

            self.wait(2)
            self.play(FadeOut(G))

if __name__ == "__main__":
    import os
    module_name = os.path.abspath(__file__).split(os.sep)[-1]
    # py -m: run library module as a script (terminates option list)
    # manim -a: all scenes, -p: preview, -ql: 480p15, -qm: 720p30,
    # -qh: 1080p60, -qp: 1440p60, -qk: 2160p60.
    command_line = f'py -m manim render -a -p -ql {module_name}'
    print(command_line)
    os.system(command_line)
