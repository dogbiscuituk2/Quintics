from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from manim_voiceover.services.base import SpeechService
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.tracker import VoiceoverTracker
from MF_Tools import *

import platform
import re

#region Global 

config.max_files_cached = 999
config.verbosity = 'WARNING' # 'INFO'

TITLE = 'Solving the General Quintic Equation'
SUBTITLE = 'An Ultraradical Animation'
COPYRIGHT = '©2024 by John Michael Kerr'

PALETTE_DEFAULT = 0
PALETTE_BRIGHT = 1
PALETTE_PASTEL = 2
PALETTE_BLACK_ON_WHITE = 3
PALETTE_WHITE_ON_BLACK = 4

palette = PALETTE_BRIGHT
    
colours = (
    (0x000000, 0x000000, 0x3F3F00, 0xFF0000, 0x7F7F00, 0xFFFF00, 0x00FF00, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x7F007F, 0x7F7F7F, 0xFFFFFF),
    (0x000000, 0x000000, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, 0xFFFFFF),
    (0x000000, 0x000000, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, 0xFFFFFF),
    (0xFFFFFF, *[0x000000 for _ in range(12)]),
    (0x000000, *[0xFFFFFF for _ in range(12)]))

Background  = colours[palette][0]
Black       = colours[palette][1]
Brown       = colours[palette][2]
Red         = colours[palette][3]
Orange      = colours[palette][4]
Yellow      = colours[palette][5]
Green       = colours[palette][6]
Blue        = colours[palette][7]
Cyan        = colours[palette][8]
Magenta     = colours[palette][9]
Violet      = colours[palette][10]
Grey        = colours[palette][11]
White       = colours[palette][12]

#endregion

class SceneBase(VoiceoverScene): 

    ColourMap = []

    Level = 0
    Tex = None
    TexIndex = 0
    Tokens = []

    def box(self, *args: VMobject) -> Polygon:
        polygon = SurroundingRectangle(VGroup(*args), Yellow) 
        self.play(Create(polygon))
        return polygon
        
    def flash(self, mathTex: MathTex, run_time=2) -> None:
        self.play(Indicate(mathTex, color=White, run_time=run_time, scale_factor=2))

    def get_colour(self, char: str) -> ManimColor:
        for map in self.ColourMap:
            if (char in map[0]):
                return map[1]
        return Grey

    def init(self):
        #self.set_speech_service(AzureService(voice="en-US-AriaNeural", style="newscast-casual", global_speed=1.15))
        self.set_speech_service(GTTSService())

    def make_tex(self, *items: str) -> MathTex:
        s: str = [self.prepare_string(item) for item in items]
        print(s)
        mathTex: MathTex = MathTex(*s)
        for i in range(len(items)):
            self.paint_tex(mathTex[i])
        return mathTex

    def make_text(self, s: str, *args, **kwargs) -> Text:
        text = Text(f'|{s}', font_size=24, color=Grey, *args, **kwargs)
        text[0].set_opacity(0)
        return text

    def paint_tex(self, mathTex: MathTex) -> None:
        colour = Grey
        mathTex.set_color(colour)
        s = mathTex.tex_string
        p = 0
        q = 0
        level = 0
        escape = False
        while p < len(s):
            c = s[p]
            match c:
                case '{':
                    level += 1
                case '}':
                    level -= 1
                    if level == 0:
                        escape = False
                case '_':
                    escape = True
                case '^':
                    escape = True
                case '\\':
                    p1 = p
                    while True:
                        p += 1
                        if p >= len(s) or not s[p].isalpha():
                            break
                        word = s[p1:p]
                    q += 1
                case '|':
                    mathTex[q].set_opacity(0)
                    q += 1
                case _:
                    if not escape:
                        colour = self.get_colour(c)
                    mathTex[q].set_color(colour)
                    q += 1
                    if level == 0:
                        escape = False
            p += 1
            if q >= len(mathTex):
                return

    def parse_begin(self, what: str):
        self.parse_debug(True, what)

    def parse_end(self, what: str):
        self.parse_debug(False, what)

    def parse_debug(self, begin: bool, what: str) -> None:
        if (not begin):
            self.Level -= 1
        print(f"{self.Level * ' '}{'begin' if begin else 'end'} {what}")
        if (begin):
            self.Level += 1

    def parse_block(self):
        self.parse_begin('block')
        self.parse_token('{')
        self.parse_expression()
        self.parse_end('block')

    def parse_expression(self):
        self.parse_begin('expression')
        while self.Tokens:
            token = self.Tokens.pop(0)
            match token[0]:
                case '{':
                    self.parse_expression()
                case '}':
                    #print('end expression')
                    break
                case '\\':
                    self.parse_function(token)
                case _:
                    pass
        self.parse_end('expression')

    def parse_function(self, token):

        def parse_fn_type(f: str) -> int:
            fn_types = {
                '\\frac': 2 # Two blocks with one glyph between
            }
            return fn_types[f] if f in fn_types.keys() else 1

        self.parse_begin('function')
        match(parse_fn_type(token)):
            case 2:
                self.parse_block()
                self.TexIndex += 1
                self.parse_block()
            case 1:
                self.TexIndex += 1
        self.parse_end('function')

    def parse_tex(self, mathTex: MathTex):
        self.Tex = mathTex
        self.TexIndex = 0
        token_pattern = r"\\\w+|\{|\}|[^\\\{\}]"
        self.Tokens.clear()
        for token in re.findall(token_pattern, self.Tex.tex_string):
            self.Tokens.append(token)
        self.parse_expression()

    def parse_token(self, token):
        self.Tokens.pop(0)

    def parse_touch(self, token):
        # Process an element of the MathTex
        # Point to the next MathTex element
        print(f"parse_touch('{token}')")

    def prepare_string(self, s: str) -> str:
        if not '|' in s: s = f'|{s}'
        #if not '^' in s: s = f'{s}^|'
        return s

    def say(self, text: str):
        # Specify language & disable language check to avoid GTTS bugs.
        return self.voiceover(text, lang='en', lang_check=False)

    def set_colour_map(self, colour_map: tuple[tuple[str, ManimColor]]) -> None:
        self.ColourMap.clear()
        for item in colour_map:
            self.ColourMap.append(item)

    """

    An atom is:

    1. any single character that is not one of '\', '{', '}';
    2. a word - a backslash followed by one or more letters, for example '\frac', '\pm', '\sqrt';
    3. a string beginning with a left brace '{' and ending at the matching right brace '}'.

    Types 1 and 2 can be treated as tokens, but type 3 is a token collection.

    """

class Scene01_Intro(SceneBase): 

    def __init__(self):
        super().__init__()

    def construct(self):

        self.init()

        print(r"0         1         2         3         4         5         6         7         8         9        10")
        print(r"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")
        print(r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}")
        print()

        s = r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}'
        t = MathTex(s)
        self.parse_tex(t)

        #with self.voiceover(text=f'{TITLES[0][0]}. {TITLES[0][1]}') as tracker:
        #    titles_show(self, 0)

class Scene02_General(SceneBase): 

    def __init__(self):
        super().__init__()

    def construct(self):

        self.init()
        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        ##E = self.make_tex(r'\frac{-b\pm\sqrt{b^2-4ac}}{2a}') # OK
        #E = self.make_tex(r'(-b\pm\sqrt{b^2-4ac)/2a})') # OK
        #self.play(Create(E))
        ##self.wait(10)

        #for c in E[0]:
        #    self.flash(c) # 

        #return

        with self.say("This is a general polynomial equation in one variable, x."):
            F1 = self.make_tex(r'y=\sum_{i=0}^{n}a_ix^i')
            self.play(Create(F1))

        with self.say("It has degree n, where n is the highest power of x present."):
            self.flash(F1[0][10])
            F2 = MathTex(r'Degree=n').set_color(Grey)
            F2.next_to(F1, DOWN)
            self.play(Create(F2))
            self.flash(F1[0][3])

        with self.say("Note that this means a n is nonzero."):
            F3 = self.make_tex(r'a_n\neq{0}')
            F3.next_to(F2, DOWN)
            self.play(Create(F3))

        with self.say("Let's unpack this sum."):
            F4 = self.make_tex(r'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0')
            arc = {"path_arc": PI}
            self.play(TransformByGlyphMap(F1, F4,
                ([3,4,5,6,7], ShrinkToCenter),
                ([8], [3,8,17,30,34], arc),
                ([9], [4,9,10,11,18,19,20,31,35], arc),
                ([10], [5,12,21,32], arc),
                ([11], [6,13,14,15,22,23,24], arc),
                (GrowFromCenter, [7,16,25,26,27,28,29,33])), run_time=2)
            
        with self.say("It has n roots, or values of x, for which y is zero."):            
            F5 = self.make_tex(r'y=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+...+a_1x+a_0=0')
            self.play(TransformByGlyphMap(F4, F5, ([], [36, 37])))

        with self.say("To find these values, start by dividing throughout by a n."):
            self.flash(F5[0][36])
            F6a = MathTex(r'\intertext{Let }')
            F6a.set_color(Grey)
            F6b = self.make_tex(r'b_i=a_i/a_n:')
            F6c = VGroup(F6a, F6b).arrange(RIGHT, aligned_edge=UP)
            F6c.next_to(F5, UP, aligned_edge=LEFT)
            self.play(FadeOut(F2), FadeOut(F3), Create(F6c))
            F6d = self.make_tex(r'x^n+b_{n-1}x^{n-1}+b_{n-2}x^{n-2}+...+b_1x+b_0=0')
            self.play(TransformMatchingShapes(F5, F6d))

        with self.say("This is called the monic form, where the coefficient of the highest power of x is equal to one."):
            self.flash(F6b[0][7:9])

        with self.say("In fact this is often called the general form, as it has all the same roots as the original."):
            self.flash(VGroup(*F6d[0][1:3]))
            self.play(FadeOut(F6c))

        with self.say("If we know these roots, we can express the polynomial as a product of n linear factors."):
            F7 = self.make_tex(r'=\prod_{j=1}^{n}(x-x_j)')
            F7.next_to(F6d, DOWN)
            self.play(Create(F7))

        with self.say("Each factor corresponds to a root value of the polynomial."):
            F8 = self.make_tex(r'=(x-x_1)(x-x_2)(x-x_3)...(x-x_{n-1})(x-x_n)')
            F8.next_to(F6d, DOWN)
            arc = {"path_arc": PI}
            self.play(TransformByGlyphMap(F7, F8,
                ([2,3,4,5,6], ShrinkToCenter),
                ([7], [2,8,14,23,31], arc),
                ([8], [3,9,15,24,32], arc),
                ([9], [4,10,16,22,33], arc),
                ([10], [5,11,17,26,34], arc),
                ([11], [6,12,18,27,28,29,35], arc),
                ([12], [7,13,19,30,36], arc),
                (GrowFromCenter, [20,21,25])), run_time=2)
            
        with self.say("x 1, x 2, and so on, up to x n."):
            for g in ((5,7), (11,13), (17,19), (26,30), (34,36)):
                self.flash(VGroup(*F8[0][g[0]:g[1]]), run_time=1)
            self.wait(2)
            self.play(FadeOut(F6d, F8))
            self.wait(2)

class Scene03_Constant(SceneBase): 

    def __init__(self):
        super().__init__()

    def construct(self):

        self.init()
        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        E1 = self.make_tex(r'y=\sum_{i=0}^{0}a_ix^i=a_0=0')
        E1a = MathTex(r'Degree=n=0').set_color(Grey)
        E1a.next_to(E1, DOWN)
        E1b = self.make_tex(r'a_n\neq{0}')
        E1b.next_to(E1a, DOWN)

        with self.say("The degree zero polynomial has no roots."):
            self.play(Create(E1))

        with self.say("Notice that the equation, y equals zero, can have no solutions."):
            self.play(Create(E1a))

        with self.say("This is because a n is constrained to be both zero and nonzero.") as tracker:
            self.play(Create(E1b))
            boxes = [self.box(E1b), self.box(E1a[0][7:10]), self.box(E1[0][13:17])]
            self.wait(tracker.duration + 2)
            self.play(FadeOut(E1, E1a, E1b, *boxes))
            self.wait(2)

class Scene04_Linear(SceneBase): 

    def __init__(self):
        super().__init__()

    def construct(self):

        self.init()
        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        E1 = self.make_tex(r'y=\sum_{i=0}^{1}a_ix^i=0')
        E1a = MathTex(r'Degree=n=1').set_color(Grey)
        E1a.next_to(E1, DOWN)
        E1b = self.make_tex(r'a_1x+a_0=0').next_to(E1a, DOWN)
        E1c = self.make_tex(r'a_1x=-a_0').next_to(E1a, DOWN)
        E1d = self.make_tex(r'x=-a_0/a_1').next_to(E1a, DOWN)
        E1e = self.make_tex(r'x_1=-a_0/a_1').next_to(E1a, DOWN)

        with self.say(
            """
            The degree one polynomial has a single root because  
            the equation y equals zero has one solution.
            """):
            self.play(Create(E1))
            self.play(Create(E1a))

        with self.say("Solving it is easy."):
            self.play(Create(E1b))
            self.wait(1)
            arc = {"path_arc": PI}
            self.play(TransformByGlyphMap(E1b, E1c,
                ([4], [5], arc),
                ([5], [6], arc),
                ([6], [7], arc),
                ([7], [4], arc),
                ([8], ShrinkToCenter)))
            self.wait(1)
            self.play(TransformByGlyphMap(E1c, E1d,
                ([1], [7], arc),
                ([2], [8], arc),
                ([3], [1], arc),
                ([4], [2], arc),
                ([5], [3], arc),
                ([6], [4], arc),
                ([7], [5], arc),
                (FadeIn, [6])))
            self.wait(1)
            self.play(TransformByGlyphMap(E1d, E1e, (GrowFromCenter, [2])))
            self.wait(2)
            self.play(FadeOut(E1, E1a, E1e))
            self.wait(2)

class Scene05_Quadratic(SceneBase): 

    def __init__(self):
        super().__init__()

    def construct(self):

        self.init()
        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        E1 = self.make_tex(r'y=\sum_{i=0}^{2}a_ix^i=0')
        E1a = MathTex(r'Degree=n=2').set_color(Grey)
        #E1a.next_to(E1, DOWN)
        E1b = self.make_tex(r'y=ax^2+bx+c')
        E1c = self.make_tex(r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}')
        #E1c.next_to(E1a, DOWN)
        VGroup(E1, E1a, E1b, E1c).arrange(DOWN)

        with self.say("The so-called quadratic, or degree two polynomial, has two roots."):
            self.play(Create(E1))
            self.play(Create(E1a))

        with self.say("It's usually solved directly, without conversion to the monic form."):
            self.play(Create(E1b))
            self.play(Create(E1c))

            self.wait(2)
            self.play(FadeOut(E1, E1a))
            self.wait(2)

class Scene06_Cubic(SceneBase): 

    def __init__(self):
        super().__init__()

    def construct(self):
        pass

class Scene07_Quartic(SceneBase): 

    def __init__(self):
        super().__init__()

    def construct(self):
        pass

class Scene08_Quintic(SceneBase): 

    def __init__(self):
        super().__init__()

    def construct(self):
        pass

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

class Scene99_Credits(SceneBase): 
    
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
        cols = [[self.make_text(packages[row][col]) for row in range(rows)] for col in range(2)]
        for row in range(rows):
            for col in range(2):
                cols[col][row][0].set_opacity(0)
        VersionTable = VGroup(
            VGroup(*cols[0]).arrange(DOWN, aligned_edge = LEFT),
            VGroup(*cols[1]).arrange(DOWN, aligned_edge = RIGHT)
            ).arrange(RIGHT)
        
        Credits = VGroup(
            self.make_text('Thank you for watching', slant=ITALIC),
            self.make_text(f'"{TITLE} : {SUBTITLE}"'),
            self.make_text(COPYRIGHT),
            self.make_text(''),
            self.make_text('Software used:', slant=ITALIC),
            VersionTable,
            self.make_text(''),
            self.make_text('All images used in this work are in the public domain.', slant=ITALIC),
            ).arrange(DOWN)

        for credit in Credits:
            self.play(FadeIn(credit), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(Credits))
        self.wait(1)
