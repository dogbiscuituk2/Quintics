from manim import *
from manim_voiceover import VoiceoverScene
from MF_Tools import *

from common import *

class Quintic03(VoiceoverScene):
    def construct(self):

        init(self)
        set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))
        
        E = [make_tex(s) for s in [
            'x_1=+1,x_2=-2,x_3=-3,x_4=+4,x_5=-5', #0
            'y=(x-x_1)(x-x_2)(x-x_3)(x-x_4)(x-x_5)', #1
            'y=(x-1)(x+2)(x+3)(x-4)(x+5)', #2
            'y=(x^2+x-2)(x+3)(x-4)(x+5)', #3
            'y=(x^3+4x^2+x-6)(x-4)(x+5)', #4
            'y=(x^4-15x^2-10x+24)(x+5)', #5
            'y=x^5+5x^4-15x^3-85x^2-26x+120', #6
            'y=x^5+ax^4+bx^3+cx^2+dx+e', #7
            'a=5,b=-15,c=-85,d=-26,e=120', #8
            'y=z^5+pz^3+qz^2+rz+s', #9
            'h=-a/5=-1', #10
            'h=-1', #11
            'p=b-10=-25', #12
            'h=-1,p=-25', #13
            'q=c-3b+20=-20', #14
            'h=-1,p=-25,q=-20', #15
            'r=d-2c+3b-15=84', #16
            'h=-1,p=-25,q=-20,r=84', #17
            's=e-d+c-b+4=80', #18
            'h=-1,p=-25,q=-20,r=84,s=80', #19

            'y=z^5-25z^3-20z^2+84z+80', #15
            'y=(z+4)(z+2)(z+1)(z-2)(z-5)', #16
            'y=(z^2+6z+8)(z+1)(z-2)(z-5)', #17
            'y=(z^3+7z^2+14z+8)(z-2)(z-5)', #18
            'y=(z^4+5z^3+0z^2-20z-16)(z-5)', #19
            'y=z^5+0z^4-25z^3-20z^2+84z+80']] #20
        
        with say(self, """
                 To verify the general to reduced form transformation procedure, 
                 first start with five known roots.
                 """):
            E[0].move_to(UP*3)
            self.play(Create(E[0]))

        with say(self, "Consider the general form of the monic as a product of factors."):
            EP = make_prod('y=', '(x-x_j)', 'j=1', '5')
            EP.next_to(E[0], DOWN, buff=1)
            self.play(Create(EP))

        def mov(source, target):
            source.next_to(target, DOWN, aligned_edge=LEFT, buff=0.1)

        def sub(source, target) -> None:
            mov(target, E[0])
            #self.play(TransformMatchingShapes(source, target))
            self.play(TransformByGlyphMap(source, target))

        with say(self, "Specifically the five factors corresponding to those roots."):
            sub(EP, E[1])

        with say(self, """
                 Substitute the chosen root values into this equation. 
                 And multiply out all factors to obtain the polynomial coefficients.
                 """):
            for i in range(2, 7):
                sub(E[i-1], E[i])
            mov(E[7], E[2])
            #E[7].next_to(E[2], DOWN, aligned_edge=LEFT, buff=0)
            self.play(Create(E[7]))
            mov(E[8], E[7])
            #E[8].next_to(E[7], DOWN, aligned_edge=LEFT, buff=0)
            self.play(Create(E[8]))

        with say(self, """
                 Our goal now is to transform this polynomial into reduced form, 
                 using the coefficient conversion formulae we found earlier, 
                 and verify that our answer has the same roots as the original general quintic.
                 """):
            for i in range(9, 16):
                mov(E[i], E[i-1])
                self.play(Create(E[i]))


            #box(self, E[9])
           

        self.wait(10)

