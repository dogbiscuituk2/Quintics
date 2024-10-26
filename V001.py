from manim import *
from manim_voiceover import VoiceoverScene
from MF_Tools import *

from common import *

class Scene(VoiceoverScene):
    def construct(self):

        def say(text: str):
            # Specify language & disable language check to avoid GTTS bugs.
            return self.voiceover(text, lang='en', lang_check=False)

        init(self)
        set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))
        
        with say("This is a general polynomial in one variable, x."):
            E1 = make_tex(r'y=\sum_{i=0}^{n}a_ix^i')
            self.play(Create(E1))

        self.next_section()

        with say("It has degree n, where n is the highest power of x present."):
            self.play(Indicate(E1[0][9], color=White, run_time=2, scale_factor=2))
            E1a = MathTex(r'Degree = n').set_color(Grey)
            E1a.next_to(E1, DOWN)
            self.play(Create(E1a))
            self.play(Indicate(E1[0][2]), color=White, run_time=2, scale_factor=2)

        with say("Note that this means a n is nonzero."):
            E1b = make_tex(r'a_n\neq{0}')
            E1b.next_to(E1a, DOWN)
            self.play(Create(E1b))

        with say("Let's unpack this sum."):
            E2 = make_tex(r'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0')
            arc = {"path_arc": PI}
            self.play(TransformByGlyphMap(E1, E2,
                ([2,3,4,5,6], ShrinkToCenter),
                ([7], [2,7,16,29,33], arc),
                ([8], [3,8,9,10,17,18,19,30,34], arc),
                ([9], [4,11,20,31], arc),
                ([10], [5,12,13,14,21,22,23], arc),
                ([], [6,15,24,25,26,27,28,32], arc)), run_time=2)
            
        with say("It has up to n, distinct roots, values of x for which y is zero."):            
            E3 = make_tex(r'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0=0')
            self.play(TransformByGlyphMap(E2, E3, ([], [35, 36])))

        with say("To find these values, start by dividing throughout by a n."):
            self.play(Indicate(E3[0][36]), color=White, run_time=2, scale_factor=2)
            E3a = MathTex(r'\intertext{Let }')
            E3a.set_color(Grey)
            E3b = make_tex(r'b_i=a_i/a_n:')
            E3c = VGroup(E3a, E3b).arrange(RIGHT, aligned_edge=UP)
            E3c.next_to(E3, UP, aligned_edge=LEFT)
            self.play(FadeOut(E1a), FadeOut(E1b), Create(E3c))
            E4 = make_tex(r'x^n+b_{n-1}x^{n-1}+b_{n-2}x^{n-2}+...+b_1x+b_0=0')
            self.play(TransformMatchingShapes(E3, E4))

        with say("This is called the monic form, where the coefficient of the highest power of x is equal to one."):
            self.play(Indicate(VGroup(*E4[0][0:2])))

            #E4 = make_tex(r'y=b_nx^n+b_{n-1}x^{n-1}+b_{n-2}x^{n-2}+...+b_1x+b_0=0')
            #self.play(TransformMatchingShapes(E3, E4))

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
