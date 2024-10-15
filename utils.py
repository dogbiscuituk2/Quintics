from manim import ManimColor, MathTex

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

                    if c == 'h':
                        print(f'Fetching colour for "h": {colour}')

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

set_palette(0)
