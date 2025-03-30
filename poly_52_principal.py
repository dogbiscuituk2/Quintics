#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import Animate, BaseScene
from labels import *
import math
from MF_Tools import *
from painter import *

#region data

e1 = (
    #('z = x²+hx+k', ''),
    r'y   &= x⁵+px³+qx²+rx+s',
    r'y   &= \prod_{i=1}^{5} (x-x_i)',
    r'X_m &= \sum_{i=1}^5 x_i^m',
    r'X_1 &= 0',
    r'X_2 &= -2p',
    r'X_3 &= -3q',
    r'X_4 &= -4r-pX_2',
    r'X_5 &= -5s-pX_3-qX_2',
    #'X_6 &= -pX_4-qX_3-rX_2',
    #'X_7 &= -pX_5-qX_4-rX_3-sX_2',
    #'X_8 &= -pX_6-qX_5-rX_4-sX_3',
    #'X_9 &= -pX_7-qX_6-rX_5-sX_4',
    #'X_{10} &= -pX_8-qX_7-rX_6-sX_5',
)

e2 = (
    r'y   &= z⁵+uz²+vz+w',
    r'y   &= \prod_{i=1}^{5} (z-z_i)',
    r'Z_m &= \sum_{i=1}^5 z_i^m',
    r'Z_1 &= 0',
    r'Z_2 &= 0',
    #r'Z_3 &= -3u',
    #r'Z_4 &= -4v',
    #r'Z_5 &= -5w',
)

#endregion

#region code

class Poly_52_Principal(BaseScene):

    """
    Principal of Newton's method.
    """

    def __init__(self):
        BaseScene.__init__(self)

    def construct(self):

        self.set_pens((
            #('o', Pen.BACKGROUND),
            ('h', Pen.ORANGE),
            ('[p-s]', Pen.GREEN),
            ('[u-w]', Pen.YELLOW),
            ('[xX]', Pen.RED),
            ('[yY]', Pen.MAGENTA),
            ('[zZ]', Pen.CYAN)))

        E1 = self.make_texes(*e1)
        E2 = self.make_texes(*e2)
        E = VGroup(E1, E2).arrange(RIGHT)
        self.play(Create(E))
        self.wait(10)

#endregion

if __name__ == "__main__":
    BaseScene.run(__file__)
