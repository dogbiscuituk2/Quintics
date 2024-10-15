from manim import *

config.max_files_cached = 999

PALETTE_DEFAULT = 0
PALETTE_BRIGHT = 1
PALETTE_PASTEL = 2
PALETTE_BLACK_ON_WHITE = 3
PALETTE_WHITE_ON_BLACK = 4

TITLES: tuple[tuple[str]] = (
    (
        'Solving the General Quintic Equation',
        'An Ultraradical Animation ©2024 by John Michael Kerr'
    ),
    ('Introduction', 'The "Impossible" Polynomial'),
    ('Part One', 'Removing the Quartic (x<sup>4</sup>) Term'),
    ('First Checkpoint', 'Verifying Removal of the Quartic Term'),
    ('Part Two', 'Removing the Cubic (x<sup>3</sup>) Term'),
    ('Second Checkpoint', 'Verifying Removal of the Cubic Term'),
    ('Part Three', 'Removing the Quadratic (x<sup>2</sup>) Term'),
    ('Third Checkpoint', 'Verifying Removal of the Quadratic Term'),
    ('Part Four', 'The Ultraradical'),
    ('Fourth Checkpoint', 'Final Verification'))

def get_colour(char: str) -> ManimColor:
    for map in ColourMap:
        if (char in map[0]):
            return map[1]
    return Grey

def make_tex(*items: str) -> MathTex:
    s: str = [prepare_string(item) for item in items]
    mathTex: MathTex = MathTex(*s)
    for i in range(len(s)):
        paint_tex(mathTex[i], s[i])
    return mathTex

def prepare_string(s: str) -> str:
    if not '|' in s: s = f'|{s}'
    if not '^' in s: s = f'{s}^|'
    return s

def paint_tex(mathTex: MathTex, s: str) -> None:
    colour = Black
    p = 0
    super = False
    for t in s.split('^'):
        for c in t:
            m = mathTex[p]
            if c == '|':
                m.set_opacity(0)
            else:
                if not super:
                    colour = get_colour(c)
                m.set_color(colour)
            super = False
            p += 1
        super = True

def set_colour_map(colour_map: tuple[tuple[str, ManimColor]]) -> None:
    global ColourMap
    ColourMap = colour_map

colours = (
    (0x000000, 0x000000, 0x3F3F00, 0xFF0000, 0x7F7F00, 0xFFFF00, 0x00FF00, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x7F007F, 0x7F7F7F, 0xFFFFFF),
    (0x000000, 0x000000, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, 0xFFFFFF),
    (0x000000, 0x000000, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, 0xFFFFFF),
    (0xFFFFFF, *[0x000000 for _ in range(12)]),
    (0x000000, *[0xFFFFFF for _ in range(12)]))

def set_palette(palette_index: int) -> None:

    print(f'Setting palette to {palette_index}')

    global Background, Black, Brown, Red, Orange, Yellow, Green, Blue, Cyan, Magenta, Violet, Grey, White

    def read_colour(colour_index: int) -> ManimColor:
        return colours[palette_index][colour_index]
    
    Background  = read_colour( 0)
    Black       = read_colour( 1)
    Brown       = read_colour( 2)
    Red         = read_colour( 3)
    Orange      = read_colour( 4)
    Yellow      = read_colour( 5)
    Green       = read_colour( 6)
    Blue        = read_colour( 7)
    Cyan        = read_colour( 8)
    Magenta     = read_colour( 9)
    Violet      = read_colour(10)
    Grey        = read_colour(11)
    White       = read_colour(12)

class Quintic(Scene):
    def construct(self):
        pass

class Quintic01(Quintic):
    def construct(self):
        pass

class Quintic02(Quintic):

    def construct(self):

        set_palette(PALETTE_BRIGHT)
        set_colour_map((
            ('0123456789', Grey),
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))

#region Functions
        
        def indicate(items: List[VMobject], size: float = 1.2) -> None:
            self.play(Indicate(VGroup(*items), color = White, scale_factor = size))

        def make_matrix(matrix: List[List[str]], margin: float = MED_SMALL_BUFF, padding: float = 1.3) -> Matrix:
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

        def pause() -> None:
            self.wait(0)

        def replace(sourceTex: MathTex, targetTex: MathTex) -> Transform:
            M2.append(targetTex)
            return ReplacementTransform(sourceTex, targetTex.move_to(sourceTex.get_center()))

        def titles_hide(titles: List[MarkupText]) -> None:
            self.play(FadeOut(*titles))

        def titles_show(section: int) -> List[MarkupText]:
            scales = (1.0, 0.6)
            title = [MarkupText(TITLES[section][i], color = (Cyan, Green)[i]).scale(scales[i]) for i in range(2)]
            VGroup(*title).arrange(DOWN, buff=0.5)
            self.play(GrowFromCenter(title[0]))
            self.wait(1)
            self.play(FadeIn(title[1]))
            self.wait(2)
            corners = ((DL, DR), (UL, UR))
            [title[i] \
                .generate_target() \
                .scale(0.4/scales[i]) \
                .set_color(Grey) \
                .to_corner(corners[0 if section == 0 else 1][i], buff=0.1) \
                for i in range(2)]
            self.play(MoveToTarget(title[0]), MoveToTarget(title[1]))
            return title

#endregion (Functions)
#region Formulae

        Y1 = make_tex('y=')
        Y2 = make_tex('x^5=', 'ax^4=', 'bx^3=', 'cx^2=', 'dx=', 'e=').arrange(DOWN, aligned_edge = RIGHT)
        E1 = make_tex('x^5+', 'ax^4+', 'bx^3+', 'cx^2+', 'dx+', 'e')
        E2 = make_tex('z^5+', '0z^4+', 'pz^3+', 'qz^2+', 'rz+', 's')
        E3 = make_tex('(z+h)^5', 'a(z+h)^4', 'b(z+h)^3', 'c(z+h)^2', 'd(z+h)', 'e').arrange(DOWN, aligned_edge = LEFT)
        E4 = make_tex(
            '(z^5+5hz^4+10h^2z^3+10h^3z^2+5h^4z+h^5)',
            'a(z^4+4hz^3+6h^2z^2+4h^3z+h^4)',
            'b(z^3+3hz^2+3h^2z+h^3)',
            'c(z^2+2hz+h^2)',
            'd(z+h)',
            'e')
        E5 = VGroup(*[make_tex(*e) for e in (
            ('z^5+', '5hz^4+', '10h^2z^3+', '10h^3z^2+', '5h^4z+', 'h^5'),
            ('az^4+', '4ahz^3+', '6ah^2z^2+', '4ah^3z+', 'ah^4'),
            ('bz^3+', '3bhz^2+', '3bh^2z+', 'bh^3'),
            ('cz^2+', '2chz+', 'ch^2'),
            ('dz+', 'dh'),
            ('e'))])

        Z2 = [] # Will hold the powers of z which fly into column vector Z1
        M2 = [] # Will hold the replacement terms for the main matrix

        E1V = E1.copy().arrange(DOWN, aligned_edge = LEFT)
        G1 = VGroup(E1, E1V).arrange(DOWN, aligned_edge = LEFT)
        Y = VGroup(Y1, Y2).arrange(DOWN, aligned_edge = RIGHT)
        VGroup(Y, G1).arrange(RIGHT, aligned_edge = UP).move_to(1.2 * LEFT)

#endregion (Formulae)
#region Main Code

# Draw background

        self.add(Rectangle(Background, height = 10, width = 15).set_fill(Background, opacity = 1))
        titles_show(0)
        titles = titles_show(1)

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

        Y3 = make_matrix((['y'], ['x^5'], ['ax^4'], ['bx^3'], ['cx^2'], ['dx'], ['e']), margin = 0)
        M1 = make_matrix((
            ('z^5', '0z^4', 'pz^3', 'qz^2', 'rz', 's'),
            ('z^5', '5hz^4', '10h^2z^3', '10h^3z^2', '5h^4z', 'h^5'),
            ('', 'az^4', '4ahz^3', '6ah^2z^2', '4ah^3z', 'ah^4'),
            ('', '', 'bz^3', '3bhz^2', '3bh^2z', 'bh^3'),
            ('', '', '', 'cz^2', '2chz', 'ch^2'),
            ('', '', '', '', 'dz', 'dh'),
            ('', '', '', '', '', 'e')),
            padding = 1.75)
        Z1 = make_matrix((('1'), ('1'), ('1'), ('1'), ('1'), ('1')), margin = 0)

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
            z = ('z^5', 'z^4', 'z^3', 'z^2', 'z', '1')
            mathTex: MathTex = make_tex(z[col])
            mathTex.move_to(get_element(row, col), RIGHT)
            Z2.append(mathTex)
            mathTex.generate_target()
            mathTex.target.move_to(Z[col], DOWN)
            return mathTex

        m2 = (
            ('1', '0', 'p', 'q', 'r', 's'),
            ('1', '5h', '10h^2', '10h^3', '5h^4', 'h^5'),
            ('', 'a', '4ah', '6ah^2', '4ah^3', 'ah^4'),
            ('', '', 'b', '3bh', '3bh^2', 'bh^3'),
            ('', '', '', 'c', '2ch', 'ch^2'),
            ('', '', '', '', 'd', 'dh'),
            ('', '', '', '', '', 'e'))

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

        F1 = make_tex('y=x^5+ax^4+bx^3+cx^2+dx+e')
        F2 = make_tex('y=z^5+0z^4+pz^3+qz^2+rz+s')
        F3 = make_tex('z=x-h')
        F4 = make_tex('z=x+a/5')

        def setup(*args: str) -> MathTex:
            return make_tex(*args).arrange(DOWN, aligned_edge = LEFT).move_to(2 * LEFT + DOWN)

        F6 = setup('0=5h+a', 'p=10h^2+4ah+b'  , 'q=10h^3+6ah^2+3bh+c', 'r=5h^4+4ah^3+3bh^2+2ch+d', 's=h^5+a^4+bh^3+ch^2+dh+e' )
        F7 = setup('a=-5h' , 'p=10h^2-20h^2+b', 'q=10h^3-30h^3+3bh+c', 'r=5h^4-20h^4+3bh^2+2ch+d', 's=h^5-5h^5+bh^3+ch^2+dh+e')
        F8 = setup('h=-a/5', 'p=-10h^2+b'     , 'q=-20h^3+3bh+c'     , 'r=-15h^4+3bh^2+2ch+d'    , 's=-4h^5+bh^3+ch^2+dh+e'   )
        F9 = setup('h=-a/5', 'p=b-10h^2'      , 'q=c+3bh-20h^3'      , 'r=d+2ch+3bh^2-15h^4'     , 's=e+dh+ch^2+bh^3-4h^5'    )

        VGroup(F1, F2, F3, F6).arrange(DOWN, aligned_edge = LEFT)
        VGroup(F1, F2, F3, F7).arrange(DOWN, aligned_edge = LEFT)
        VGroup(F1, F2, F3, F8).arrange(DOWN, aligned_edge = LEFT)
        VGroup(F1, F2, F3, F9).arrange(DOWN, aligned_edge = LEFT)
        VGroup(F1, F2, F4, F9).arrange(DOWN, aligned_edge = LEFT)

        M6 = [
            VGroup(*[M2[i] for i in range(2, 5)]),
            VGroup(*[M2[i] for i in range(5, 9)]),
            VGroup(*[M2[i] for i in range(9, 14)]),
            VGroup(*[M2[i] for i in range(14, 20)]),
            VGroup(*[M2[i] for i in range(20, 27)])]
        for i in range(5):
            self.play(TransformMatchingShapes(M6[i], F6[i], path_arc=PI/2))

# Substitute '5h' for 'a'

        indicate(F6[0])
        self.play(TransformMatchingShapes(F6[0], F7[0]))
        indicate(F7[0])
        for i in range(1, 5):
            indicate(F6[i][[9, 9, 8, 6][i - 1]], size = 2)
            self.play(TransformMatchingShapes(F6[i], F7[i]))
            self.play(TransformMatchingShapes(F7[i], F8[i]))
            self.play(TransformMatchingShapes(F8[i], F9[i], path_arc=PI/2))
        indicate(F7[0])
        self.play(TransformMatchingShapes(F7[0], F8[0]))
        indicate(F8[0])

# Redisplay 'y' as a polynomial in 'x' and also in 'z'

        self.play(FadeIn(F1))
        self.play(FadeIn(F2))
        self.play(FadeIn(F3))
        indicate([F3])
        self.play(TransformMatchingShapes(F3, F4))
        indicate([F4])

# Redisplay p,q,r,s as a matrix

        Y4 = make_matrix((['p'], ['q'], ['r'], ['s']))
        M4 = make_matrix((
                [ '0',   '0',   '0', '-10',  '0', 'b'],
                [ '0',   '0', '-20',   '0', '3b', 'c'],
                [ '0', '-15',   '0',  '3b', '2c', 'd'],
                ['-4',   '0',   'b',   'c',  'd', 'e']))
        H4 = make_matrix((['h^5'], ['h^4'], ['h^3'], ['h^2'], ['h'], ['1']))

        self.wait(10)
        titles_hide(titles)
        self.wait(10)

#endregion (Main Code)
