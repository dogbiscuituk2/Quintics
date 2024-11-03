from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from MF_Tools import *
import platform
from texpaint import *

config.max_files_cached = 999
config.verbosity = "CRITICAL"

TITLE = 'Solving the General Quintic Equation'
SUBTITLE = 'An Ultraradical Animation'
COPYRIGHT = '©2024 by John Michael Kerr'

class Polynomials(VoiceoverScene):

#region Common 

    Painter: TexPaint = TexPaint(
        0,
        (
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))
    
    def box(self, *args: VMobject) -> Polygon:
        polygon = SurroundingRectangle(VGroup(*args), self.get_colour(Yellow))
        self.play(Create(polygon))
        return polygon

    def flash(self, mathTex: MathTex, run_time=2) -> None:
        white = self.get_colour(White)
        self.play(Indicate(mathTex, color=white, run_time=run_time, scale_factor=2))

    def get_text_colour(self) -> ManimColor:
        return self.get_colour(Grey)

    def get_colour(self, colour_index: int) -> ManimColor:
        return self.Painter.get_colour(colour_index)

    def make_tex(self, text: str) -> MathTex:
        text = self.prepare_string(text)
        mathTex: MathTex = MathTex(text)
        self.paint_tex(mathTex)
        return mathTex

    def make_text(self, s: str, *args, **kwargs) -> Text:
        text = Text(self.prepare_string(s), font_size=24, color=self.get_text_colour(), *args, **kwargs)
        text[0].set_opacity(0)
        return text;
    
    def paint_tex(self, mathTex: MathTex) -> None:
        self.Painter.paint(mathTex)

    def prepare_string(self, text: str) -> str:
        return text if '|' in text else f'|{text}'

    def say(self, text: str):
        # Specify language & disable language check to avoid GTTS bugs.
        return self.voiceover(text, lang='en', lang_check=False)
    
    def set_colour_map(self, map: tuple[tuple[str, int]]):
        self.Painter.set_colour_map(map)

    def construct(self):
        self.set_speech_service(GTTSService())

#endregion
#region Scene 1 : Introduction 

        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        s = r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}'
        t = MathTex(s)
        self.Painter.paint(t)

        self.play(Create(t))
        self.wait(10)
        self.play(Uncreate(t))

#endregion
#region Scene 2 : General 

        self.next_section("General")

        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))
        
        with self.say("This is a general polynomial equation in one variable, x."):
            F1 = self.make_tex(r'y=\sum_{i=0}^{n}a_ix^i')
            self.play(Create(F1))

        with self.say("It has degree n, where n is the highest power of x present."):
            self.flash(F1[0][10])
            F2 = MathTex(r'Degree=n').set_color(self.get_text_colour())
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
            self.play(
                TransformByGlyphMap(
                    F1, F4,
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
            self.flash(F5[0][37])
            F6a = MathTex(r'\intertext{Let }').set_color(self.get_text_colour())
            F6b = self.make_tex(r'b_i=a_i/a_n:')
            F6c = VGroup(F6a, F6b).arrange(RIGHT, aligned_edge=UP)
            F6c.next_to(F5, UP, aligned_edge=LEFT)
            self.play(FadeOut(F2), FadeOut(F3), Create(F6c))
            F6d = self.make_tex(r'y=x^n+b_{n-1}x^{n-1}+b_{n-2}x^{n-2}+...+b_1x+b_0=0')
            self.play(TransformByGlyphMap(F5, F6d, ([3,4], ShrinkToCenter)))

        with self.say("This is called the monic form, where the coefficient of the highest power of x is equal to one."):
            self.flash(F6b[0][7:9])

        with self.say("In fact this is often called the general form, as it has all the same roots as the original."):
            self.flash(VGroup(*F6d[0][3:5]))
            self.play(FadeOut(F6c))

        with self.say("If we know these roots, we can express the polynomial as a product of n linear factors."):
            F7 = self.make_tex(r'=\prod_{j=1}^{n}(x-x_j)')
            F7.next_to(F6d, DOWN)
            self.play(Create(F7))

        with self.say("Each factor corresponds to a root value of the polynomial."):
            F8 = self.make_tex(r'=(x-x_1)(x-x_2)(x-x_3)...(x-x_{n-1})(x-x_n)')
            F8.next_to(F6d, DOWN)
            arc = {"path_arc": PI}
            self.play(
                TransformByGlyphMap(
                    F7, F8,
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

#endregion
#region Scene 3 : Constant 

        self.next_section("Constant")

        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        E1 = self.make_tex(r'y=\sum_{i=0}^{0}a_ix^i=a_0=0')
        E1a = MathTex(r'Degree=n=0').set_color(self.get_text_colour())
        E1a.next_to(E1, DOWN)
        E1b = self.make_tex(r'a_n\neq{0}')
        E1b.next_to(E1a, DOWN)

        with self.say("The constant, or degree zero polynomial, has no roots."):
            self.play(Create(E1))

        with self.say("Notice that the equation, y equals zero, can have no solutions."):
            self.play(Create(E1a))

        with self.say("This is because a n is constrained to be both zero and nonzero.") as tracker:
            self.play(Create(E1b))
            boxes = [self.box(E1b), self.box(E1a[0][7:10]), self.box(E1[0][13:17])]
            self.wait(tracker.duration + 2)
            self.play(FadeOut(E1, E1a, E1b, *boxes))
            self.wait(2)

#endregion
#region Scene 4 : Linear 

        self.next_section("Linear")

        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        E1 = self.make_tex(r'y=\sum_{i=0}^{1}a_ix^i=0')
        E1a = MathTex(r'Degree=n=1').set_color(self.get_text_colour())
        E1a.next_to(E1, DOWN)
        E1b = self.make_tex(r'a_1x+a_0=0').next_to(E1a, DOWN)
        E1c = self.make_tex(r'a_1x=-a_0').next_to(E1a, DOWN)
        E1d = self.make_tex(r'x=-a_0/a_1').next_to(E1a, DOWN)
        E1e = self.make_tex(r'x_1=-a_0/a_1').next_to(E1a, DOWN)

        with self.say(
            """
            The linear, or degree one polynomial, has a single root because  
            the equation y equals zero has one solution.
            """):
            self.play(Create(E1))
            self.play(Create(E1a))

        with self.say("Solving it is easy."):
            self.play(Create(E1b))
            self.wait(1)
            arc = {"path_arc": PI}
            self.play(TransformByGlyphMap(
                E1b, E1c,
                #([4], [5], arc),
                #([5], [6], arc),
                #([6], [7], arc),
                ([7], [4], arc),
                ([8], ShrinkToCenter)))
            self.wait(1)
            self.play(TransformByGlyphMap(
                E1c, E1d,
                #([1], [7], arc),
                #([2], [8], arc),
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

#endregion
#region Scene 5 : Quadratic 

        self.next_section("Quadratic")

        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        E1 = self.make_tex(r'y=\sum_{i=0}^{2}a_ix^i=0')
        E1a = MathTex(r'Degree=n=2').set_color(self.get_text_colour())
        E1b = self.make_tex(r'y=ax^2+bx+c')
        E1c = self.make_tex(r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}')

        VGroup(E1, E1a, E1b, E1c).arrange(DOWN)

        with self.say("The quadratic, or degree two polynomial, has two roots."):
            self.play(Create(E1))
            self.play(Create(E1a))

        with self.say("It's usually solved directly, using this formula, without conversion to the monic form."):
            self.play(Create(E1b))
            self.play(Create(E1c))

            self.wait(2)
            self.play(FadeOut(E1, E1a, E1b, E1c))
            self.wait(2)

#endregion
#region Scene 6 : Cubic 

        self.next_section("Cubic")

        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        E1 = self.make_tex(r'y=\sum_{i=0}^{3}a_ix^i=0')
        E1a = MathTex(r'Degree=n=3').set_color(self.get_text_colour())
        E1b = self.make_tex(r'y=x^3+ax^2+bx+c')

        G = VGroup(E1, E1a, E1b).arrange(DOWN)

        with self.say("The cubic, or degree three polynomial, has three roots."):
            self.play(Create(E1))
            self.play(Create(E1a))
            self.play(Create(E1b))

            self.wait(2)
            self.play(FadeOut(G))

#endregion
#region Scene 7 : Quartic 

        self.next_section("Quartic")

        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        E1 = self.make_tex(r'y=\sum_{i=0}^{4}a_ix^i=0')
        E1a = MathTex(r'Degree=n=4').set_color(self.get_text_colour())
        E1b = self.make_tex(r'y=x^4+ax^3+bx^2+cx+d')

        G = VGroup(E1, E1a, E1b).arrange(DOWN)

        with self.say("The quartic, or degree four polynomial, has four roots."):
            self.play(Create(E1))
            self.play(Create(E1a))
            self.play(Create(E1b))

            self.wait(2)
            self.play(FadeOut(G))

#endregion
#region Scene 8 : Quintic 

        self.next_section("Quintic")

        self.set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

        E1 = self.make_tex(r'y=\sum_{i=0}^{5}a_ix^i=0')
        E1a = MathTex(r'Degree=n=5').set_color(self.get_text_colour())
        E1b = self.make_tex(r'y=x^5+ax^4+bx^3+cx^2+dx+e')

        G = VGroup(E1, E1a, E1b).arrange(DOWN)

        with self.say("The quintic, or degree five polynomial, has five roots."):
            self.play(Create(E1))
            self.play(Create(E1a))
            self.play(Create(E1b))

            self.wait(2)
            self.play(FadeOut(G))

#endregion
#region Scene 9 : Credits 

        self.next_section("Credits")

        packages = [['python', platform.python_version()],
            *[[package, version(package)] for package in (
            'manim',
            'manim-voiceover',
            'mf-tools',
            )]]

        rows = len(packages)
        cols = [[self.make_text(packages[row][col]) for row in range(rows)] for col in range(2)]
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

#endregion
