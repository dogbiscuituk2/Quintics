from manim import *
from manim_voiceover import VoiceoverScene
from MF_Tools import *

import platform

from common import *

config.max_files_cached = 999
config.verbosity = 'WARNING' # 'INFO'

TITLE = 'Solving the General Quintic Equation'
SUBTITLE = 'An Ultraradical Animation'
COPYRIGHT = '©2024 by John Michael Kerr'

class Scene_(VoiceoverScene): 

    def flash(self, mathTex: MathTex, run_time=2) -> None:
        self.play(Indicate(mathTex, color=White, run_time=run_time, scale_factor=2))

    def init(self):
        #self.set_speech_service(AzureService(voice="en-US-AriaNeural", style="newscast-casual", global_speed=1.15))
        self.set_speech_service(GTTSService())

    def say(self, text: str):
        # Specify language & disable language check to avoid GTTS bugs.
        return self.voiceover(text, lang='en', lang_check=False)

class Scene_01(Scene_): # Introduction 

    def __init__(self):
        super().__init__()

    def construct(self):

        self.init()

        #with self.voiceover(text=f'{TITLES[0][0]}. {TITLES[0][1]}') as tracker:
        #    titles_show(self, 0)

class Scene_02(Scene_): # The General Polynomial 

    def __init__(self):
        super().__init__()

    def construct(self):

        self.init()
        set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))
        
        #with self.voiceover(text=f'{TITLES[1][0]}. {TITLES[1][1]}'):
        #    titles_show(1)

        with self.say("This is a general polynomial in one variable, x."):
            E1 = make_tex(r'y=\sum_{i=0}^{n}a_ix^i')
            self.play(Create(E1))

        with self.say("It has degree n, where n is the highest power of x present."):
            self.flash(E1[0][9])
            E1a = MathTex(r'Degree = n').set_color(Grey)
            E1a.next_to(E1, DOWN)
            self.play(Create(E1a))
            self.flash(E1[0][2])

        with self.say("Note that this means a n is nonzero."):
            E1b = make_tex(r'a_n\neq{0}')
            E1b.next_to(E1a, DOWN)
            self.play(Create(E1b))

        with self.say("Let's unpack this sum."):
            E2 = make_tex(r'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0')
            arc = {"path_arc": PI}
            self.play(TransformByGlyphMap(E1, E2,
                ([2,3,4,5,6], ShrinkToCenter),
                ([7], [2,7,16,29,33], arc),
                ([8], [3,8,9,10,17,18,19,30,34], arc),
                ([9], [4,11,20,31], arc),
                ([10], [5,12,13,14,21,22,23], arc),
                (GrowFromCenter, [6,15,24,25,26,27,28,32])), run_time=2)
            
        with self.say("It has n roots, values of x for which y is zero."):            
            E3 = make_tex(r'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0=0')
            self.play(TransformByGlyphMap(E2, E3, ([], [35, 36])))

        with self.say("To find these values, start by dividing throughout by a n."):
            self.flash(E3[0][36])
            E3a = MathTex(r'\intertext{Let }')
            E3a.set_color(Grey)
            E3b = make_tex(r'b_i=a_i/a_n:')
            E3c = VGroup(E3a, E3b).arrange(RIGHT, aligned_edge=UP)
            E3c.next_to(E3, UP, aligned_edge=LEFT)
            self.play(FadeOut(E1a), FadeOut(E1b), Create(E3c))
            E4 = make_tex(r'x^n+b_{n-1}x^{n-1}+b_{n-2}x^{n-2}+...+b_1x+b_0=0')
            self.play(TransformMatchingShapes(E3, E4))

        with self.say("This is called the monic form, where the coefficient of the highest power of x is equal to one."):
            self.flash(E3b[0][6:8])

        with self.say("In fact this is often called the general form, as it has all the same roots as the original."):
            self.flash(VGroup(*E4[0][0:2]))
            self.play(FadeOut(E3c))

        with self.say("If we know these roots, we can express the polynomial as a product of n linear factors."):
            E5 = make_tex(r'=\prod_{j=1}^{n}(x-x_j)')
            E5.next_to(E4, DOWN)
            self.play(Create(E5))

        with self.say("Each factor corresponds to a root value of the polynomial."):
            E6 = make_tex(r'=(x-x_1)(x-x_2)(x-x_3)...(x-x_{n-1})(x-x_n)')
            E6.next_to(E4, DOWN)
            arc = {"path_arc": PI}
            self.play(TransformByGlyphMap(E5, E6,
                ([1,2,3,4,5], ShrinkToCenter),
                ([6], [1,7,13,22,30], arc),
                ([7], [2,8,14,23,31], arc),
                ([8], [3,9,15,21,32], arc),
                ([9], [4,10,16,25,33], arc),
                ([10], [5,11,17,26,27,28,34], arc),
                ([11], [6,12,18,29,35], arc),
                (GrowFromCenter, [19,20,24])), run_time=2)
            
        with self.say("x 1, x 2, and so on, up to x n"):
            for g in ((4,6), (10,12), (16,18), (19,22), (25,29), (33,35)):
                self.flash(VGroup(*E6[0][g[0]:g[1]]), run_time=1)
            self.wait(3)
            self.play(FadeOut(E4, E6))

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

class Scene_99(Scene_): # Credits 
    
    def __init__(self):
        super().__init__()

    def construct(self):

        self.init()

        packages = [['python', platform.python_version()],
            *[[package, version(package)] for package in (
            'manim',
            'manim-voiceover',
            'mf-tools',
            )]]

        rows = len(packages)
        cols = [[make_text(packages[row][col]) for row in range(rows)] for col in range(2)]
        for row in range(rows):
            for col in range(2):
                cols[col][row][0].set_opacity(0)
        VersionTable = VGroup(
            VGroup(*cols[0]).arrange(DOWN, aligned_edge = LEFT),
            VGroup(*cols[1]).arrange(DOWN, aligned_edge = RIGHT)
            ).arrange(RIGHT)
        
        Credits = VGroup(
            make_text('Thank you for watching', slant=ITALIC),
            make_text(f'"{TITLE} : {SUBTITLE}"'),
            make_text(COPYRIGHT),
            make_text(''),
            make_text('Software used:', slant=ITALIC),
            VersionTable,
            make_text(''),
            make_text('All images used in this work are in the public domain.', slant=ITALIC),
            ).arrange(DOWN)

        for credit in Credits:
            self.play(FadeIn(credit), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(Credits))
        self.wait(1)
