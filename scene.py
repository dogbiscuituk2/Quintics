from manim import *

#region Constants

title = (
    'Solving the General Quintic Equation',
    'An ultraradical animation by John Michael Kerr')

sections = (
    ('Part One', 'Remove the Quartic (x^4) Term'),
    ('First Checkpoint', 'Verify Removal of the Quartic Term'),
    ('Part Two', 'Remove the Cubic (x^3) Term'),
    ('Second Checkpoint', 'Verify Removal of the Cubic Term'),
    ('Part Three', 'Remove the Quadratic (x^2) Term'),
    ('Third Checkpoint', 'Verify Removal of the Quadratic Term'),
    ('Part Four', 'The Ultraradical'),
    ('Fourth Checkpoint', 'Final Verification'))

#endregion (Constants)

#region Colour Palette

def get_colour(char: str):
    #return rgb_to_color(hex_to_rgb('#ff0000'))
    for map in colour_map:
        if (char in map[0]):
            return map[1]
    return Grey

def set_colour_map(map):
    global colour_map
    colour_map = map

def make_tex(*items: str):
    string: str = [prepare_string(item) for item in items]
    mathTex: MathTex = MathTex(*string)
    for i in range(len(string)):
        paint_tex(mathTex[i], string[i])
    return mathTex

def prepare_string(string: str):
    if not '|' in string:
        string = f'|{string}'
    if not '^' in string:
        string = f'{string}^|'
    return string

def paint_tex(mathTex: MathTex, string: str):
    colour = Black
    super = False
    p: int = 0
    for substring in string.split('^'):
        for char in substring:
            symbol = mathTex[p]
            if char == '|':
                symbol.set_opacity(0)
            else:
                if not super:
                    colour = get_colour(char)
                symbol.set_color(colour)
            super = False
            p += 1
        super = True

PALETTE_BRIGHT = 0
PALETTE_PASTEL = 1

foo = (0x000000, 0x000000)

colours: list[tuple[ManimColor]] = [[rgb_to_color(rgb) for rgb in colour] for colour in [
    ((0.0, 0.0, 0.0), (0.2, 0.2, 0.2)), # Black
    ((0.5, 0.2, 0.1), (0.5, 0.2, 0.1)), # Brown
    ((1.0, 0.1, 0.2), (1.0, 0.1, 0.2)), # Red
    ((1.0, 0.5, 0.3), (1.0, 0.5, 0.3)), # Orange
    ((0.8, 0.8, 0.0), (0.8, 0.8, 0.0)), # Yellow
    ((0.2, 1.0, 0.2), (0.2, 1.0, 0.2)), # Green
    ((0.0, 1.0, 1.0), (0.0, 1.0, 1.0)), # Blue
    ((0.0, 1.0, 1.0), (0.0, 1.0, 1.0)), # Cyan
    ((1.0, 0.0, 1.0), (1.0, 0.0, 1.0)), # Magenta
    ((1.0, 0.0, 1.0), (1.0, 0.0, 1.0)), # Violet
    ((0.7, 0.7, 0.7), (0.7, 0.7, 0.7)), # Grey
    ((1.0, 1.0, 1.0), (1.0, 1.0, 1.0))] # White
]

def set_palette(palette_index: int):

    global Black, Brown, Red, Orange, Yellow, Green, Blue, Cyan, Magenta, Violet, Grey, White

    def read_colour(colour_index: int): return colours[colour_index][palette_index]

    Black   = read_colour( 0)
    Brown   = read_colour( 1)
    Red     = read_colour( 2)
    Orange  = read_colour( 3)
    Yellow  = read_colour( 4)
    Green   = read_colour( 5)
    Blue    = read_colour( 6)
    Cyan    = read_colour( 7)
    Magenta = read_colour( 8)
    Violet  = read_colour( 9)
    Grey    = read_colour(10)
    White   = read_colour(11)

set_palette(PALETTE_BRIGHT)

#endregion (Colour Palette)

class Quintic01(Scene):

    def construct(self):

        set_colour_map([
            ('0123456789', Magenta),
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Grey),
            ('z', Cyan)])

#region Terms

        y1 = 'y='
        y2 = ('x^5=', 'ax^4=', 'bx^3=', 'cx^2=', 'dx=', 'e=')
        e1 = ('x^5+', 'ax^4+', 'bx^3+', 'cx^2+', 'dx+', 'e')
        e2 = ('z^5+', '0z^4+', 'pz^3+', 'qz^2+', 'rz+', 's')
        e3 = ('(z+h)^5', 'a(z+h)^4', 'b(z+h)^3', 'c(z+h)^2', 'd(z+h)', 'e')

        e4 = (
                '(z^5+5hz^4+10h^2z^3+10h^3z^2+5h^4z+h^5)',
                'a(z^4+4hz^3+6h^2z^2+4h^3z+h^4)',
                'b(z^3+3hz^2+3h^2z+h^3)',
                'c(z^2+2hz+h^2)',
                'd(z+h)',
                'e')
        e5 = (
                ('z^5+', '5hz^4+', '10h^2z^3+', '10h^3z^2+', '5h^4z+', 'h^5'),
                ('az^4+', '4ahz^3+', '6ah^2z^2+', '4ah^3z+', 'ah^4'),
                ('bz^3+', '3bhz^2+', '3bh^2z+', 'bh^3'),
                ('cz^2+', '2chz+', 'ch^2'),
                ('dz+', 'dh'),
                ('e'))
        y3 = (['y'], ['x^5'], ['ax^4'], ['bx^3'], ['cx^2'], ['dx'], ['e'])
        m1 = (
                ('z^5', '0z^4', 'pz^3', 'qz^2', 'rz', 's'),
                ('z^5', '5hz^4', '10h^2z^3', '10h^3z^2', '5h^4z', 'h^5'),
                ('', 'az^4', '4ahz^3', '6ah^2z^2', '4ah^3z', 'ah^4'),
                ('', '', 'bz^3', '3bhz^2', '3bh^2z', 'bh^3'),
                ('', '', '', 'cz^2', '2chz', 'ch^2'),
                ('', '', '', '', 'dz', 'dh'),
                ('', '', '', '', '', 'e'))
        z0 = ('1')
        z1 = (z0, z0, z0, z0, z0, z0)
        z2 = ('z^5', 'z^4', 'z^3', 'z^2', 'z', '1')
        m2 = (
                ('1', '0', 'p', 'q', 'r', 's'),
                ('1', '5h', '10h^2', '10h^3', '5h^4', 'h^5'),
                ('', 'a', '4ah', '6ah^2', '4ah^3', 'ah^4'),
                ('', '', 'b', '3bh', '3bh^2', 'bh^3'),
                ('', '', '', 'c', '2ch', 'ch^2'),
                ('', '', '', '', 'd', 'dh'),
                ('', '', '', '', '', 'e'))

        f1 = 'y=x^5+ax^4+bx^3+cx^2+dx+e'
        f2 = 'y=z^5+0z^4+pz^3+qz^2+rz+s'
        f3 = 'z=x-h=x+a/5'

        f6 = (
                '0=5h+a',
                'p=10h^2+4ah+b',
                'q=10h^3+6ah^2+3bh+c',
                'r=5h^4+4ah^3+3bh^2+2ch+d',
                's=h^5+a^4+bh^3+ch^2+dh+e')
        f7 = (
                'a=-5h',
                'p=10h^2-20h^2+b',
                'q=10h^3-30h^3+3bh+c',
                'r=5h^4-20h^4+3bh^2+2ch+d',
                's=h^5-5h^5+bh^3+ch^2+dh+e')
        f8 = (
                'h=-a/5',
                'p=-10h^2+b',
                'q=-20h^3+3bh+c',
                'r=-15h^4+3bh^2+2ch+d',
                's=-4h^5+bh^3+ch^2+dh+e')
        f9 = (
                'h=-a/5',
                'p=b-10h^2',
                'q=3bh+c-20h^3',
                'r=3bh^2+2ch+d-15h^4',
                's=bh^3+ch^2+dh+e-4h^5')
        
        y4 = (('p'), ('q'), ('r'), ('s'))
        m4 = (
                ( '0',   '0',   '0', '-10',  '0', 'b'),
                ( '0',   '0', '-20',   '0', '3b', 'c'),
                ( '0', '-15',   '0',  '3b', '2c', 'd'),
                ('-4',   '0',   'b',   'c',  'd', 'e'))
        h4 = (('h^5'), ('h^4'), ('h^3'), ('h^2'), ('h'), ('1'))

#endregion (Terms)
#region Functions
        
        def indicate(items: List[VMobject], size: float = 1.2):
            self.play(Indicate(VGroup(*items), color = White, scale_factor = size))

        def make_matrix(matrix: List[List[str]], margin: float = MED_SMALL_BUFF, padding: float = 1.3):
            rows: int = len(matrix)
            cols: int = len(matrix[0])
            strings: List[str] = [[prepare_string(t) for t in row] for row in matrix]
            matrix: Matrix = Matrix(strings, bracket_h_buff = margin, h_buff = padding)
            for row in range(rows):
                for col in range(cols):
                    paint_tex(matrix[0][row * cols + col][0], strings[row][col])
            matrix[1].set_color(Grey)
            matrix[2].set_color(Grey)
            return matrix

        def make_tex(*items: str):
            string: str = [prepare_string(item) for item in items]
            mathTex: MathTex = MathTex(*string)
            for i in range(len(string)):
                paint_tex(mathTex[i], string[i])
            return mathTex

        def pause():
            self.wait(0)

        def replace(sourceTex: MathTex, targetTex: MathTex):
            M2.append(targetTex)
            return ReplacementTransform(sourceTex, targetTex.move_to(sourceTex.get_center()))

#endregion (Functions)
#region Formulae

        Y1 = make_tex(y1)
        Y2 = make_tex(*y2).arrange(DOWN, aligned_edge = RIGHT)
        E1 = make_tex(*e1)
        E2 = make_tex(*e2)
        E3 = make_tex(*e3).arrange(DOWN, aligned_edge = LEFT)
        E4 = make_tex(*e4)
        E5 = VGroup(*[make_tex(*e) for e in e5])

        Y3 = make_matrix(y3, margin = 0)
        M1 = make_matrix(m1, padding = 1.75)
        Z1 = make_matrix(z1, margin = 0)
        Z2 = [] # Will hold the powers of z which fly into column vector Z1
        M2 = [] # Will hold the replacement terms for the main matrix

        E1V = E1.copy().arrange(DOWN, aligned_edge = LEFT)
        G1 = VGroup(E1, E1V).arrange(DOWN, aligned_edge = LEFT)
        Y = VGroup(Y1, Y2).arrange(DOWN, aligned_edge = RIGHT)
        G3 = VGroup(Y, G1).arrange(RIGHT, aligned_edge = UP).move_to(1.2 * LEFT)

        F1 = make_tex(f1)
        F2 = make_tex(f2)
        F3 = make_tex(f3)
        F6 = make_tex(*f6).arrange(DOWN, aligned_edge = LEFT).move_to(2 * LEFT + DOWN)
        F7 = make_tex(*f7).arrange(DOWN, aligned_edge = LEFT).move_to(2 * LEFT + DOWN)
        F8 = make_tex(*f8).arrange(DOWN, aligned_edge = LEFT).move_to(2 * LEFT + DOWN)
        F9 = make_tex(*f9).arrange(DOWN, aligned_edge = LEFT).move_to(2 * LEFT + DOWN)

#endregion (Formulae)
#region Main Code

# Start with the general quintic in x

        self.play(FadeIn(Y1))
        self.play(Create(E1))
        pause()

# Make a vertical copy

        self.play(TransformFromCopy(E1, E1V, path_arc = 2))
        pause()

# Show the reduced quintic in z

        E2.move_to(E1, aligned_edge = LEFT)
        indicate([E1])
        self.play(ReplacementTransform(E1, E2))
        pause()

# Convert each x-term into an LHS

        self.play(TransformMatchingShapes(E1V, Y2))
        pause()

# Add each binomial x-term as an RHS

        E3.move_to(E1V, aligned_edge = LEFT)
        self.play(Create(E3))
        pause()

# Expand each binomial x-term and distribute the coefficients

        for i in range(6):
            E4[i].move_to(E3[i], aligned_edge = LEFT)
# Flash
            if i < 5:
                indicate([E3[i]])
# Expand
            if i < 4:
                self.play(TransformMatchingShapes(E3[i], E4[i]))
            else:
                E4[i].move_to(E3[i])
                E3[i].set_opacity(0)
# Distribute
            E5[i].move_to(E4[i], aligned_edge = LEFT)
            #if i < 5:
            self.play(TransformMatchingShapes(E4[i], E5[i]))
            #else:
                #E5[i].move_to(E4[i])
                #E4[i].set_opacity(0)
        pause()

# Right align the fully expanded binomials

        M = VGroup(E2, E5)
        E7 = E5.copy().arrange(DOWN, aligned_edge = RIGHT)
        E8 = VGroup(E2.copy(), E7).arrange(DOWN, aligned_edge = RIGHT)
        E8.move_to(M)
        self.play(
            Transform(E2, E8[0]),
            [Transform(E5[i], E7[i]) for i in range(6)])
        pause()

# Convert to matrix equation Y=MZ

        EQ = MathTex('=')
        EQ.set_color(Grey)
        VGroup(Y3, EQ, M1, Z1).arrange(RIGHT, aligned_edge = UP)
        EQ.move_to(EQ.get_center() + 2.9 * DOWN)
        Z1.move_to(Z1.get_center() + 0.5 * DOWN)
        self.play(TransformMatchingShapes(Y, Y3))
        self.play(FadeIn(EQ))
        self.play(TransformMatchingShapes(M, M1))
        self.play(FadeIn(Z1))
        pause()

# Move all powers of z out of M and into Z
        
        M = M1[0]
        Z = Z1[0]

        def get_element(row: int, col: int):
            return M[row * 6 + col]

        def new_target(row: int, col: int):
            mathTex: MathTex = make_tex(z2[col])
            mathTex.move_to(get_element(row, col), RIGHT)
            Z2.append(mathTex)
            mathTex.generate_target()
            mathTex.target.move_to(Z[col], DOWN)
            return mathTex

        for col in range(6):
            transforms: List[Transform] = []
            rows = range(col + 2)
            if col < 5:
                transforms = [MoveToTarget(new_target(row, col)) for row in rows]
                transforms.append(FadeOut(Z[col]))
            for row in rows:
                transforms.append(replace(get_element(row, col), make_tex(m2[row][col])))
            if col < 5:
                indicate([get_element(row, col) for row in rows])
            self.play(*transforms)
        pause()

        self.wait(3)

# Hide everything except the relevant submatrix

        self.play(FadeOut(Y3, EQ, M1, M2[0], M2[1], Z1[0][5], Z1[1], Z1[2] , *Z2))

# Transpose the matrix

        VGroup(F1, F2, F3, F6).arrange(DOWN, aligned_edge = LEFT)
        VGroup(F1, F2, F3, F7).arrange(DOWN, aligned_edge = LEFT)
        VGroup(F1, F2, F3, F8).arrange(DOWN, aligned_edge = LEFT)
        VGroup(F1, F2, F3, F9).arrange(DOWN, aligned_edge = LEFT)

        M6 = [
            VGroup(*[M2[i] for i in range(2, 5)]),
            VGroup(*[M2[i] for i in range(5, 9)]),
            VGroup(*[M2[i] for i in range(9, 14)]),
            VGroup(*[M2[i] for i in range(14, 20)]),
            VGroup(*[M2[i] for i in range(20, 27)])]
        for i in range(5):
            self.play(TransformMatchingShapes(M6[i], F6[i]))

# Substitute '5h' for 'a'

        indicate(F6[0])
        self.play(TransformMatchingShapes(F6[0], F7[0]))
        indicate(F7[0])
        for i in range(1, 5):
            indicate(F6[i][[9, 9, 8, 6][i - 1]], size = 2)
            self.play(TransformMatchingShapes(F6[i], F7[i]))
            self.play(TransformMatchingShapes(F7[i], F8[i]))
            self.play(TransformMatchingShapes(F8[i], F9[i]))
        indicate(F7[0])
        self.play(TransformMatchingShapes(F7[0], F8[0]))
        indicate(F8[0])

# Redisplay 'y' as a polynomial in 'x' and also in 'z'

        self.play(FadeIn(F1))
        self.play(FadeIn(F2))
        self.play(FadeIn(F3))

        self.wait(10)

#endregion (Main Code)
