from manim import *
from manim_voiceover import VoiceoverScene
from MF_Tools import *

from common import *

class Scene(VoiceoverScene):

    def construct(self):

        init(self)
        set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))
        
        E1 = make_tex('y=\\sum_{i=0}^{n}a_ix^i')
        E2 = make_tex('y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0')
        #VGroup(E1, E2).arrange(DOWN)

        self.play(Create(E1))
        self.wait(5)

        self.play(TransformByGlyphMap(E1, E2,
            ([2,3,4,5,6], []),
            ([7], [2,7,16,29,33]),
            ([8], [3,8,9,10,17,18,19,30,34]),
            ([9], [4,11,20,31]),
            ([10], [5,12,13,14,21,22,23]),
            ([], [6,15,24,25,26,27,28,32])))
        self.wait(5)

        return
        
        equ = [
            'y=\\sum_{i=0}^{n}a_ix^i',
            'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0',
            'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0=0'
        ]
        EQU = VGroup(*[make_tex(e) for e in equ])
        EQU.arrange(DOWN, aligned_edge=LEFT)
        self.play(Create(EQU))

        return
        
        equ = [
            'y=\\sum_{i=0}^{n}a_ix^i=0',
            'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0',
            'x^n+b_{n-1}x^{n-1}+b_{n-2}x^{n-2}+...+b_1x+b_0=0'
            ]
        EQU = VGroup(*[make_tex(e) for e in equ])
        EQU.arrange(DOWN, aligned_edge=LEFT)
        self.play(Create(EQU))

        
        equ = [
            'x^5+ax^4+bx^3+cx^2+dx+e=0',
            'x^5+px^3+qx^2+rx+s=0',
            'x^5+ux^2+vx+w=0',
            'x^5+mx+n=0',
            'x^5+t=0',
            'x^5=-t',
            r'x=\sqrt[5]{-t}']
        EQU = VGroup(*[make_tex(equ[i]) for i in range(5)])
        EQU.add(MathTex(equ[5]))

        E0 = EQU[0].copy()

        with say(self, "This is the General Form of a quintic polynomial equation in one variable, x."):
            self.play(Create(EQU[0]))

        X = TransformByGlyphMap(EQU[0], EQU[1],
            ([3,4,5,6], []),
            ([8], [4]),
            ([12], [8]),
            ([16], [12]),
            ([19], [15]))

        with say(self, "Look at this"):
            self.play(X)
            self.wait(5)

        X = TransformByGlyphMap(EQU[1], EQU[2],
            ([3,4,5,6], []),
            ([8], [4]),
            ([12], [8]),
            ([15], [11]))

        with say(self, "Look at this"):
            self.play(X)
            self.wait(5)

        X = TransformByGlyphMap(EQU[2], EQU[3],
            ([3,4,5,6], []),
            ([8], [4]),
            ([11], [7]))

        with say(self, "Look at this"):
            self.play(X)
            self.wait(5)
