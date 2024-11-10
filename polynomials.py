from contextlib import _GeneratorContextManager
from inspect import currentframe, getframeinfo
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from MF_Tools import *
from painter import *
import platform

config.max_files_cached = 999
config.verbosity = "CRITICAL"

TITLE = 'Solving the General Quintic Equation'
SUBTITLE = 'An Ultraradical Animation'
COPYRIGHT = '©2024 by John Michael Kerr'

class Polynomials(VoiceoverScene):

#region Common 

    painter = Painter(
        0,
        (
            ('abcde', green),
            ('h', orange),
            ('pqrs', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))
    
    def box(self, *args: VMobject) -> Polygon:
        b = self.box_make(*args)
        self.play(Create(b))
        return b

    boxes = None

    def box_make(self, *args: VMobject) -> Polygon:
        return SurroundingRectangle(VGroup(*args), self.get_colour(yellow)) 

    def box_move(self, *args: VMobject) -> Animation:
        b = self.box_make(*args)
        result = Create(b) if self.boxes == None else ReplacementTransform(self.boxes, b)
        self.boxes = b
        return result

    def box_off(self) -> None:
        if self.boxes != None:
            self.play(Uncreate(self.boxes))
            self.boxes = None

    def box_on(self, *args: VMobject) -> None:
        self.play(self.box_move(*args))

    def flash(self, tex: MathTex, run_time=2) -> None:
        self.play(Indicate(tex, color=self.get_colour(white), run_time=run_time, scale_factor=2))

    def get_text_colour(self) -> ManimColor:
        return self.get_colour(grey)

    def get_colour(self, index: int) -> ManimColor:
        return self.painter.get_colour(index)

    def make_matrix(self, matrix: List[List[str]], margin: float = MED_SMALL_BUFF, padding: float = 1.3) -> Matrix:
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        strings: List[str] = [[self.prepare_string(t) for t in row] for row in matrix]
        matrix: Matrix = Matrix(strings, bracket_h_buff = margin, h_buff = padding).set_color(self.get_colour(grey))
        for row in range(rows):
            for col in range(cols):
                self.paint(matrix[0][row * cols + col])
        return matrix

    def make_tex(self, text: str) -> MathTex:
        text = self.prepare_string(text)
        tex: MathTex = MathTex(text)
        self.paint(tex)
        return tex

    #def make_tex(self, *items: str) -> MathTex:
    #    result = MathTex(*[self.prepare_string(item) for item in items])
    #    self.paint(result)
    #    return result
    #
    #    return [self.paint(MathTex(self.prepare_string(item))) for item in items]

    def make_text(self, text: str, *args, **kwargs) -> Text:
        result = Text(self.prepare_string(text), font_size=24, color=self.get_text_colour(), *args, **kwargs)
        result[0].set_opacity(0)
        return result;
    
    def paint(self, tex: MathTex) -> None:
        self.painter.paint(tex)

    def prepare_string(self, text: str) -> str:
        return text if '|' in text else f'|{text}'

    def say(self, text: str):
        line = getframeinfo(currentframe().f_back).lineno
        print(f"{line}: {text}")
        # Specify language & disable language check to avoid GTTS bugs.
        return self.voiceover(text, lang='en', lang_check=False)
    
    def set_colour_map(self, map: tuple[tuple[str, int]]):
        self.painter.set_colour_map(map)

    def construct(self):
        self.set_speech_service(GTTSService())

#endregion
#region Scene 1 : General 

        self.set_colour_map((
            ('abcde', green),
            ('h', orange),
            ('pqrs', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))
        
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

            self.flash(F5[0][37]) # The zero on the RHS

            F6a = self.make_tex(r'\frac{y}{a_n}=\frac{a_n}{a_n}x^n+\frac{a_{n-1}}{a_n}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(
                F5,
                F6a,
                (GrowFromCenter, [2,8,18,30,44,51]),
                (FadeIn, [3,4,9,10,19,20,31,32,45,46,52,53]),
                introduce_individually=True))

            F6b = MathTex(r'\intertext{Let }').set_color(self.get_text_colour())
            F6c = self.make_tex(r'b_i=a_i/a_n:')
            F6d = VGroup(F6b, F6c).arrange(RIGHT, aligned_edge=UP)
            F6d.next_to(F6a, UP, aligned_edge=LEFT)
            self.play(FadeOut(F2), FadeOut(F3), Create(F6d))

            F6e = self.make_tex( \
                r'\frac{a_n}{a_n}x^n+\frac{a_{n-1}}{a_n}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+' \
                    r'\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(F6a, F6e, ([*ir(1,5)], ShrinkToCenter)), run_time=1.5)

            F6f = self.make_tex( \
                r'x^n+\frac{a_{n-1}}{a_n}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+' \
                    r'\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(F6e, F6f, ([*ir(1,5)], ShrinkToCenter)), run_time=1.5)

            F6g = self.make_tex( \
                r'x^n+b_{n-1}x^{n-1}+\frac{a_{n-2}}{a_n}x^{n-2}+...+' \
                    r'\frac{a_1}{a_n}x+\frac{a_0}{a_n}=0')
            self.play(TransformByGlyphMap(F6f, F6g, ([8,9,10], ShrinkToCenter)), run_time=1.5)

            F6h = self.make_tex(r'x^n+b_{n-1}x^{n-1}+b_{n-2}x^{n-2}+...+b_1x+b_0=0')
            self.play(
                TransformByGlyphMap(
                    F6g,
                    F6h,
                    ([17,18,19,31,32,33,38,39,40], ShrinkToCenter),
                    remove_individually=True),
                run_time=1.5)

        with self.say("This is called the monic form, where the coefficient of the highest power of x is equal to one."):
            self.flash(F6c[0][7:9])

        with self.say("In fact this is often called the general form, as it has all the same roots as the original."):
            self.flash(VGroup(*F6a[0][3:5]))
            self.play(FadeOut(F6d))

        with self.say("If we know these roots, we can express the polynomial as a product of n linear factors."):
            F7 = self.make_tex(r'=\prod_{j=1}^{n}(x-x_j)')
            F7.next_to(F6a, DOWN)
            self.play(Create(F7))

        with self.say("Each factor corresponds to a root value of the polynomial."):
            F8 = self.make_tex(r'=(x-x_1)(x-x_2)(x-x_3)...(x-x_{n-1})(x-x_n)')
            F8.next_to(F6a, DOWN)
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
            self.play(FadeOut(F6a, F8))
            self.wait(2)

#endregion
#region Scene 2 : Quintic 

        # from: r'x^n+b_{n-1}x^{n-1}+b_{n-2}x^{n-2}+...+b_1x+b_0=0'
        # to:   r'y=x^5+ax^4+bx^3+cx^2+dx+e'

        with self.say("The degree five polynomial, the quintic, has five roots."):
            E1b = self.make_tex(r'y=x^5+ax^4+bx^3+cx^2+dx+e')
            self.play(
                TransformByGlyphMap(
                    F6h,
                    E1b,
                    (GrowFromCenter, [1,2]),
                    ([5,6,7], ShrinkToCenter),
                    ([9,10,11], [8]),
                    ([14,15,16], ShrinkToCenter),
                    ([18,19,20], [12]),
                    ([22,23,24,25], ShrinkToCenter),
                    (GrowFromCenter, [14,15,16,17]),
                    ([27], ShrinkToCenter),
                    ([31,32,33], ShrinkToCenter)
                    ))

            self.wait(10)

        return

        z = '(z+h)'
        z2 = f'{z}{z}'
        z3 = f'{z2}{z}'
        z4 = f'{z3}{z}'
        z5 = f'{z4}{z}'
        z6 = '(z^2+2hz+h^2)'
        z7 = '(z^3+3hz^2+3h^2z+h^3)'
        z8 = '(z^4+4hz^3+6h^2z^2+4h^3z+h^4)'
        z9 = 'z^5+5hz^4+10h^2z^3+10h^3z^2+5h^4z+h^5'

        Fz = [
            [self.make_tex(s) for s in t] for t in [
                [f'o{z}^5', f'a{z}^4', f'b{z}^3', f'c{z}^2', f'd{z}', 'e'],
                [f'o{z2}^4', f'a{z2}^3', f'b{z2}^2', f'c{z2}'],
                [f'o{z3}^3', f'a{z3}^2', f'b{z3}'],
                [f'o{z4}^2', f'a{z4}'],
                [f'o{z5}'],
                [f'o{z6}{z3}', f'a{z6}{z2}', f'b{z6}{z}', f'c{z6}'],
                [f'o{z7}{z2}', f'a{z7}{z}', f'b{z7}'],
                [f'o{z8}{z}', f'a{z8}'],
                [f'o{z9}'],
                [f'o{z9}', 'az^4+4ahz^3+6ah^2z^2+4ah^3z+ah^4', 'bz^3+3bhz^2+3bh^2z+bh^3', 'cz^2+2chz+ch^2', 'dz+dh', 'e']]]

        LHS = VGroup(*[self.make_tex(f'{s}o=') for s in ['x', 'y', 'y', 'x^5', 'ax^4', 'bx^3', 'cx^2', 'dx', 'e']])
        RHS = VGroup(*[self.make_tex(s) for s in ['oz+h', 'ox^5+ax^4+bx^3+cx^2+dx+e=0', 'oz^5+0z^4+pz^3+qz^2+rz+s']], *Fz[9])
        ALL = VGroup(LHS, RHS)

        LHS.arrange(DOWN, aligned_edge=RIGHT, buff=0.1)
        RHS.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        ALL.arrange(RIGHT, aligned_edge=DOWN)
        EQU = [VGroup(LHS[i], RHS[i]) for i in range(9)]

        Y = self.make_matrix((['y'], ['x^5'], ['ax^4'], ['bx^3'], ['cx^2'], ['dx'], ['e']), margin = 0)
        EQ = MathTex('=').set_color(self.get_colour(grey))
        M = self.make_matrix((
            ('z^5', '0z^4', 'pz^3', 'qz^2', 'rz', 's'),
            ('z^5', '5hz^4', '10h^2z^3', '10h^3z^2', '5h^4z', 'h^5'),
            ('', 'az^4', '4ahz^3', '6ah^2z^2', '4ah^3z', 'ah^4'),
            ('', '', 'bz^3', '3bhz^2', '3bh^2z', 'bh^3'),
            ('', '', '', 'cz^2', '2chz', 'ch^2'),
            ('', '', '', '', 'dz', 'dh'),
            ('', '', '', '', '', 'e')),
            padding = 1.75)
        Z = self.make_matrix((('1'), ('1'), ('1'), ('1'), ('1'), ('1')), margin = 0)
        VGroup(Y, EQ, M, Z).arrange(RIGHT, aligned_edge=DOWN)
        EQ.move_to(EQ.get_center() + 2.8 * UP)
        Z.move_to(Z.get_center() + 0.4 * UP)

        with self.say("We could solve it easily if we didn't have these intermediate powers."):
            self.play(Create(EQU[1]))
            self.box_on(*EQU[1][1][0][4:19])
            s1 = self.make_tex('y=x^5+e=0')
            s2 = self.make_tex('x=\\sqrt[5]{-e}')
            VGroup(s1, s2).arrange(DOWN)
            self.play(
                TransformMatchingShapes(EQU[1].copy(), s1),
                Create(s2))

        with self.say("To make a start, we might first try to get rid of the quartic, x to the fourth, term."):
            self.box_on(*EQU[1][1][0][4:8])
            self.play(Uncreate(s2))
            self.play(Uncreate(s1))

        with self.say("In other words, transform it into so-called reduced form,"):
            brace = Brace(Group(EQU[1], EQU[2]), LEFT, color=self.get_colour(grey))
            self.play(FadeIn(brace), Create(EQU[2]))
            self.box_on(*EQU[2][1][0][4:8])

        with self.say("with this coefficient equal to zero."):
            self.play(Indicate(EQU[2][1][0][5], color=self.get_colour(white), scale_factor=2, run_time=2))

        with self.say("This operation is technically known as a Tschirnhaus Transformation,"):
            image = ImageMobject("resources/Tschirnhaus.jpg")
            caption = MarkupText(
                    'Ehrenfried Walther von Tschirnhaus (1651-1708)',
                    color=self.get_colour(grey)
                ).scale(0.25).rotate(-PI/2)
            picture = Group(image, caption).arrange(RIGHT, buff=0.1)
            picture.to_corner(DR, buff=0.5)
            self.play(FadeIn(picture))
            self.box_off()

        with self.say("the simplest example of which is a linear substitution, such as x = z + some constant h."):
            self.box_on(EQU[0])
            self.play(Create(EQU[0]))

        with self.say("Let's use this to express all these x powers in terms of z."):
            E = EQU[1][1][0]
            S = [E[2:4], E[5:8], E[9:12], E[13:16], E[17:19], E[20:21]]
            T = LHS[3:9]
            self.play([TransformMatchingShapes(S[i].copy(), T[i], path_arc=-PI/2) for i in range(6)], run_time=2)
            self.box_on(EQU[0][1][0][2:5])
            for i in range(5):
                T = Fz[0][i].copy().move_to(EQU[i+3][1], LEFT)
                EQU[i+3][1] = T
                self.play(TransformMatchingShapes(EQU[0][1].copy(), T))
            self.play(FadeIn(EQU[8][1]))
            self.box_off()

        def expand(i: int, immediate: bool = False) -> None:

            def move_box(grow: int=0) -> Animation:
                return self.box_move(*[EQU[j+3][1][0][k] for k in range(1, 6*(i-3)+grow) for j in range(0, 9-i)])

            if i in range(5, 9):
                self.play(move_box())
            fz = Fz[i]
            animations = []
            for j in range(1 if immediate else 0, len(fz)):
                source = EQU[j+3][1]
                target = fz[j]
                target.move_to(source, aligned_edge=LEFT)
                animation = TransformMatchingShapes(source, target)
                if immediate:
                    self.play(animation)
                else:
                    animations.append(animation)
                EQU[j+3][1] = target
            if not immediate:
                if i in range(5, 9):
                    animations.append(move_box(1))
                self.play(animations)

        with self.say("Expand these powers."):
            self.play(FadeOut(picture))
            for i in range(1, 5):
                expand(i)

        with self.say("Multiply out the binomials."):
            for i in range(5, 9):
                expand(i)
            self.box_off()

        with self.say("Distribute the original coefficients."):
            expand(9, immediate=True)

        with self.say("Now recall that this first z equation is just the sum of the six below it."):
            self.box_on(EQU[2])
            self.wait(2)
            self.box_on(*[EQU[i] for i in range(3, 9)])
            self.wait(2)
            self.box_off()

        with self.say("All seven of these equations are identities, true for every choice of x and corresponding z."):
            self.play(FadeOut(*EQU[0], *EQU[1], brace))
            self.play(TransformMatchingShapes(VGroup(*[EQU[i][0] for i in range(2, 9)]), Y), Create(EQ))
            self.play(TransformMatchingShapes(VGroup(*[EQU[i][1] for i in range(2, 9)]), M), Create(Z))

        Z2 = [] # Will hold the powers of z which fly into column vector Z1
        M2 = [] # Will hold the replacement terms for the main matrix

        def get_element(row: int, col: int):
            return M[0][row * 6 + col]
        
        def indicate(items: List[VMobject], size: float = 1.2) -> None:
            self.play(Indicate(VGroup(*items), color = self.get_colour(white), scale_factor = size))

        def new_target(row: int, col: int):
            z = ('z^5', 'z^4', 'z^3', 'z^2', 'z', '1')
            mathTex: MathTex = self.make_tex(z[col])
            mathTex.move_to(get_element(row, col), RIGHT)
            Z2.append(mathTex)
            mathTex.generate_target()
            mathTex.target.move_to(Z[0][col], DOWN)
            return mathTex

        def rewrite(src: MathTex, tgt: MathTex) -> Transform:
            M2.append(tgt)
            s = src.tex_string.replace('^', '')
            i = s.find('z')
            if i == 1:
                maps = [([1,2], ShrinkToCenter), (GrowFromCenter, [1])]
            else:
                maps = [([i] if len(s) <= i + 1 else [i, i + 1], ShrinkToCenter)]
            return TransformByGlyphMap(src, tgt.move_to(src.get_center()), *maps)
        
        m2 = (
            ('1', '0', 'p', 'q', 'r', 's'),
            ('1', '5h', '10h^2', '10h^3', '5h^4', 'h^5'),
            ('', 'a', '4ah', '6ah^2', '4ah^3', 'ah^4'),
            ('', '', 'b', '3bh', '3bh^2', 'bh^3'),
            ('', '', '', 'c', '2ch', 'ch^2'),
            ('', '', '', '', 'd', 'dh'),
            ('', '', '', '', '', 'e'))

        with self.say("If we now consider the case z equals one, then all of these z powers vanish from the matrix."):
            for col in range(5):
                transforms: List[Transform] = []
                rows = range(col + 2)
                transforms = [MoveToTarget(new_target(row, col)) for row in rows]
                transforms.append(FadeOut(Z[0][col]))
                for row in rows:
                    transforms.append(rewrite(get_element(row, col), self.make_tex(m2[row][col])))
                indicate([get_element(row, col) for row in rows])
                self.play(*transforms)
            for row in range(7):
                M2.append(self.make_tex(m2[row][5]))

        self.wait(10)

        F1 = self.make_tex('y=x^5+ax^4+bx^3+cx^2+dx+e')
        F2 = self.make_tex('y=z^5+0z^4+pz^3+qz^2+rz+s')
        F3 = self.make_tex('z=x-h')
        F4 = self.make_tex('z=x+a/5')

        def setup(*args: str) -> MathTex:
            return VGroup(*[self.make_tex(arg) for arg in args]).arrange(DOWN, aligned_edge = LEFT).move_to(2 * LEFT + DOWN)

        F5 = setup('0=5h+a', 'p=10h^2+4ah+b'  , 'q=10h^3+6ah^2+3bh+c', 'r=5h^4+4ah^3+3bh^2+2ch+d'   , 's=h^5+a^4+bh^3+ch^2+dh+e')
        F6 = setup('a=-5h' , 'p=10h^2-20h^2+b', 'q=10h^3-30h^3+3bh+c', 'r=5h^4-20h^4+3bh^2+2ch+d'   , 's=h^5-5h^5+bh^3+ch^2+dh+e')
        F7 = setup('h=-a/5', 'p=-10h^2+b'     , 'q=-20h^3+3bh+c'     , 'r=-15h^4+3bh^2+2ch+d'       , 's=-4h^5+bh^3+ch^2+dh+e')
        F8 = setup('h=-a/5', 'p=b-10h^2'      , 'q=c+3bh-20h^3'      , 'r=d+2ch+3bh^2-15h^4'        , 's=e+dh+ch^2+bh^3-4h^5')
        F9 = setup('h=-a/5', 'p=b-2a^2/5'     , 'q=c-3ab/5+4a^3/25'  , 'r=d-2ac/5+3a^2b/25-3a^4/125', 's=e-ad/5+a^2c/25-a^3b/125-4a^5/3125')

        with self.say("Now we can read the matrix column by column, to get expressions for the new coefficients in terms of the old."):
            self.play(FadeOut(Y, EQ, M, M2[0], M2[1], Z[0][5], Z[1], Z[2], *Z2))
            for f in (F5, F6, F7, F8, F9):
                VGroup(F1, F2, F3, f).arrange(DOWN, aligned_edge = LEFT)
            VGroup(F1, F2, F4, F8).arrange(DOWN, aligned_edge = LEFT)

            M6 = [
                VGroup(*[M2[i] for i in range(2, 5)]),
                VGroup(*[M2[i] for i in range(5, 9)]),
                VGroup(*[M2[i] for i in range(9, 14)]),
                VGroup(*[M2[i] for i in range(14, 20)]),
                VGroup(*[M2[i] for i in range(20, 27)])]
            for i in range(4):
                self.play(TransformMatchingShapes(M6[i], F5[i], path_arc=PI/2))

        for i in enumerate(F5):
            print(i);
        
        return

        with self.say(
            """
            This h substitution avoids a lot of ugly fractions with powers of five denominators in the results. 
            Apply the substitution, collect like powers of h, and reorder for clarity. 
            """):
            indicate(F5[0])
            self.play(TransformMatchingShapes(F5[0], F6[0]))
            indicate(F6[0])
            for i in range(1, 5):
                indicate(F5[i][[9, 9, 8, 6][i - 1]], size = 2)
                self.play(TransformMatchingShapes(F5[i], F6[i]))
                self.play(TransformMatchingShapes(F6[i], F7[i]))
                self.play(TransformMatchingShapes(F7[i], F8[i], path_arc=PI/2))
            indicate(F6[0])
            self.play(TransformMatchingShapes(F6[0], F7[0]))
            indicate(F7[0])

        with self.say("Finally we have succeeded in eliminating the quartic term."):
            self.play(FadeIn(F1))
            self.play(FadeIn(F2))
            self.play(FadeIn(F3))
            indicate([F3])
            self.play(TransformMatchingShapes(F3, F4))
            indicate([F4])

        with self.say("Here are those ugly power of five denominators:"):
            for i in range(1, 5):
                self.play(TransformMatchingShapes(F8[i], F9[i]))

            self.wait(10)

#endregion
#region Scene 3 : Credits 

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

        return

#region Scene 1 : Introduction 

        self.set_colour_map((
            ('abcde', green),
            ('h', orange),
            ('pqrs', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))

        s = r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}'
        t = MathTex(s)
        self.painter.paint(t)

        self.play(Create(t))
        self.wait(10)
        self.play(Uncreate(t))

#endregion
#region Scene 3 : Constant 

        self.set_colour_map((
            ('abcde', green),
            ('h', orange),
            ('pqrs', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))

        E1z = self.make_tex(r'y=\sum_{i=0}^{0}a_ix^i=a_0=0')
        E1y = MathTex(r'Degree=n=0').set_color(self.get_text_colour())
        E1y.next_to(E1z, DOWN)
        E1b = self.make_tex(r'a_n\neq{0}')
        E1b.next_to(E1y, DOWN)

        with self.say("The degree zero polynomial has no roots."):
            self.play(Create(E1z))

        with self.say("Notice that the equation, y equals zero, can have no solutions."):
            self.play(Create(E1y))

        with self.say("This is because a n is constrained to be both zero and nonzero.") as tracker:
            self.play(Create(E1b))
            boxes = [self.box(E1b), self.box(E1y[0][7:10]), self.box(E1z[0][13:17])]
            self.wait(tracker.duration + 2)
            self.play(FadeOut(E1z, E1y, E1b, *boxes))
            self.wait(2)

#endregion
#region Scene 4 : Linear 

        self.set_colour_map((
            ('abcde', green),
            ('h', orange),
            ('pqrs', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))

        E1z = self.make_tex(r'y=\sum_{i=0}^{1}a_ix^i=0')
        E1y = MathTex(r'Degree=n=1').set_color(self.get_text_colour())
        E1y.next_to(E1z, DOWN)
        E1b = self.make_tex(r'a_1x+a_0=0').next_to(E1y, DOWN)
        E1c = self.make_tex(r'a_1x=-a_0').next_to(E1y, DOWN)
        E1d = self.make_tex(r'x=-a_0/a_1').next_to(E1y, DOWN)
        E1e = self.make_tex(r'x_1=-a_0/a_1').next_to(E1y, DOWN)

        with self.say(
            """
            The degree one polynomial has a single root because  
            the equation y equals zero has one solution.
            """):
            self.play(Create(E1z))
            self.play(Create(E1y))

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
            self.play(FadeOut(E1z, E1y, E1e))
            self.wait(2)

#endregion
#region Scene 5 : Quadratic 

        self.set_colour_map((
            ('abcde', green),
            ('h', orange),
            ('pqrs', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))

        E1z = self.make_tex(r'y=\sum_{i=0}^{2}a_ix^i=0')
        E1y = MathTex(r'Degree=n=2').set_color(self.get_text_colour())
        E1b = self.make_tex(r'y=ax^2+bx+c')
        E1c = self.make_tex(r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}')

        VGroup(E1z, E1y, E1b, E1c).arrange(DOWN)

        with self.say("The degree two polynomial, the quadratic, has two roots."):
            self.play(Create(E1z))
            self.play(Create(E1y))

        with self.say("It's usually solved directly, using this formula, without conversion to the monic form."):
            self.play(Create(E1b))
            self.play(Create(E1c))

            self.wait(2)
            self.play(FadeOut(E1z, E1y, E1b, E1c))
            self.wait(2)

#endregion
#region Scene 6 : Cubic 

        self.set_colour_map((
            ('abcde', green),
            ('h', orange),
            ('pqrs', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))

        E1z = self.make_tex(r'y=\sum_{i=0}^{3}a_ix^i=0')
        E1y = MathTex(r'Degree=n=3').set_color(self.get_text_colour())
        E1b = self.make_tex(r'y=x^3+ax^2+bx+c')

        G = VGroup(E1z, E1y, E1b).arrange(DOWN)

        with self.say("The degree three polynomial, the cubic, has three roots."):
            self.play(Create(E1z))
            self.play(Create(E1y))
            self.play(Create(E1b))

            self.wait(2)
            self.play(FadeOut(G))

#endregion
#region Scene 7 : Quartic 

        self.set_colour_map((
            ('abcde', green),
            ('h', orange),
            ('pqrs', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))

        E1z = self.make_tex(r'y=\sum_{i=0}^{4}a_ix^i=0')
        E1y = MathTex(r'Degree=n=4').set_color(self.get_text_colour())
        E1b = self.make_tex(r'y=x^4+ax^3+bx^2+cx+d')

        G = VGroup(E1z, E1y, E1b).arrange(DOWN)

        with self.say("The degree four polynomial, the quartic, has four roots."):
            self.play(Create(E1z))
            self.play(Create(E1y))
            self.play(Create(E1b))

            self.wait(2)
            self.play(FadeOut(G))

#endregion