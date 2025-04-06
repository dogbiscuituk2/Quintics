#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from base_scene import Animate, BaseScene
from labels import *
from MF_Tools import *
from painter import *

#region data

e1 = 'z = x²+hx+k' 

e2 = (    
      r'y &= x⁵+px³+qx²+rx+s',
        r'&= \prod(x-x_i)',
    r'X_m &= \sum x_i^m',
    r'X_m &= -ma_{n-m}-\sum_{i=1}^{m-1}a_{n-m+i}X_i',
    r'X_1 &= 0',
    r'X_2 &= -2p',
    r'X_3 &= -3q',
    r'X_4 &= -4r+2p²',
    r'X_5 &= -5s-pX_3-qX_2',

    #'X_6 &= -pX_4-qX_3-rX_2',
    #'X_7 &= -pX_5-qX_4-rX_3-sX_2',
    #'X_8 &= -pX_6-qX_5-rX_4-sX_3',
    #'X_9 &= -pX_7-qX_6-rX_5-sX_4',
    #'X_{10} &= -pX_8-qX_7-rX_6-sX_5',
)

e3 = (
      r'y &= z⁵+0z³+uz²+vz+w',
        r'&= \prod(z-z_i)',
    r'Z_m &= \sum z_i^m',
    r'Z_m &= -ma_{n-m}-\sum_{i=1}^{m-1}a_{n-m+i}Z_i',
    r'Z_1 &= 0',
    r'Z_2 &= 0',
    r'Z_3 &= -3u',
    r'Z_4 &= -4v',
    r'Z_5 &= -5w',
)

#endregion

#region code

class Poly_53_Principal(BaseScene):

    def __init__(self):
        BaseScene.__init__(self)

    def construct(self):

        self.set_pens(
            ('[hk]', Pen.ORANGE),
            ('[p-s]', Pen.GREEN),
            ('[u-w]', Pen.YELLOW),
            ('[xX]', Pen.RED),
            ('[yY]', Pen.MAGENTA),
            ('[zZ]', Pen.CYAN))
        
        E1 = self.make_tex(e1)
        E2 = self.make_texes(*e2)
        E3 = self.make_texes(*e3)

        G1 = VGroup(E2, E3).arrange(RIGHT, aligned_edge=UP, buff=0.5)
        G2 = VGroup(E1, G1).arrange(DOWN)

        with self.say("Now let's get rid of the cubic term, using another transformation, "):
            self.play(Create(E2[0]))
            self.box_on(E2[0][0][5:8])

        with self.say("this time to so-called Principal Form, "):
            self.play(Create(E3[0]))
            self.box_on(E3[0])

        with self.say("with this coefficient equal to zero."):
            self.box_on(E3[0][0][5:8])
            self.play(Indicate(E3[0][0][5], color=self.get_ink(Pen.WHITE), scale_factor=2, run_time=2))

        with self.say("Last time we used a linear transformation, so this time we'll try a quadratic."):
            self.play(Create(E1))
            self.box_on(E1)

        with self.say("Let x i, represent the 5 roots of the previous, reduced form, "):
            self.play(Create(E2[1]))
            self.box_on(E2[1][0][9:11])

        with self.say("and z i, the 5 roots of this new, principal form."):
            self.play(Create(E3[1]))
            self.box_on(E3[1][0][9:11])

        with self.say("Blah blah blah"):
            self.play(Create(E2[2:]))

        with self.say("Blah blah blah"):
            self.play(Create(E3[2:]))


        self.wait(10)
        return

        with self.say(
            """
            Although we don't yet know the actual values of any of these roots, 
            in both cases we do know a lot about their so-called power sums, that is, 
            the sum of the five roots, the sum of their squares, of their cubes, and so on. 
            These power sums are simple combinations of the coefficients. 
            """):
            self.box_off()

        with self.say("So let X m be the sum of the m-th powers of the reduced polynomial, "):
            self.play(Create(E2[2]))

        with self.say("and Z m the corresponding sum for the principal form."):
            self.play(Create(E3[2]))

        with self.say("Here are the first few power sums for the reduced form."):
            self.play(Create(E2[3:]))

        with self.say("And for the principal form."):
            self.play(Create(E3[3:]))



        self.wait(10)
        self.play(FadeIn(G2))
        self.wait(10)

#endregion

if __name__ == "__main__":
    BaseScene.run(__file__)
