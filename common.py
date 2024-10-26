import re

from typing import Generator

from manim_voiceover.services.azure import AzureService
from manim_voiceover.services.base import SpeechService
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.tracker import VoiceoverTracker

from manim import *

config.max_files_cached = 999
config.verbosity = 'WARNING' # 'INFO'

speech_services: List[SpeechService] = [
    AzureService(voice="en-US-AriaNeural", style="newscast-casual", global_speed=1.15),
    GTTSService()]

TITLES: tuple[tuple[str]] = (
    (
        'Solving the General Quintic Equation',
        'An Ultraradical Animation. ©2024 by John Michael Kerr'
    ),
    ('Introduction', 'The "Impossible" Polynomial'),
    ('Part One', 'Removing the Quartic Term'),
    ('First Checkpoint', 'Verifying Removal of the Quartic Term'),
    ('Part Two', 'Removing the Cubic Term'),
    ('Second Checkpoint', 'Verifying Removal of the Cubic Term'),
    ('Part Three', 'Removing the Quadratic Term'),
    ('Third Checkpoint', 'Verifying Removal of the Quadratic Term'),
    ('Part Four', 'The Ultraradical'),
    ('Fourth Checkpoint', 'Final Verification'))

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

_box = None

def box(self: Scene, *args: VMobject) -> None:
    self.play(box_move(*args))

def box_move(*args: VMobject) -> Animation:
    global _box
    b = SurroundingRectangle(VGroup(*args), Yellow) 
    result = Create(b) if _box == None else ReplacementTransform(_box, b)
    _box = b
    return result

def box_off(self: Scene) -> None:
    global _box
    if _box != None:
        self.play(Uncreate(_box))
        _box = None

def dump(*mathTex: MathTex) -> None:
    for t in mathTex:
        print([s.tex_string for s in t])
    print()

def get_colour(char: str) -> ManimColor:
    for map in ColourMap:
        if (char in map[0]):
            return map[1]
    return Grey

def init(self):
    self.set_speech_service(speech_services[1])

def make_matrix(matrix: List[List[str]], margin: float = MED_SMALL_BUFF, padding: float = 1.3) -> Matrix:
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    strings: List[str] = [[prepare_string(t) for t in row] for row in matrix]
    matrix: Matrix = Matrix(strings, bracket_h_buff = margin, h_buff = padding)
    matrix.set_color(Grey)
    for row in range(rows):
        for col in range(cols):
            paint_tex(matrix[0][row * cols + col][0])
    #matrix[1].set_color(Grey)
    #matrix[2].set_color(Grey)
    return matrix

def make_prod(lhs: str, term: str, start: str=None, end: str=None) -> MathTex:
    return make_sp('prod', lhs, term, start, end)

def make_sp(func: str, lhs: str, term: str, start: str=None, end: str=None) -> MathTex:
    s = '\\' + func
    if start != None:
        s = s + '_{' + start + '}'
        if end != None:
            s = s + '^{' + end + '}'
    group = VGroup(make_tex(lhs), MathTex(s).set_color(Grey), make_tex(term));
    if (start == None) == (end == None):
        group.arrange(RIGHT, buff = 0)
    else:
        if start == None:
            group.arrange(RIGHT, aligned_edge = DOWN, buff = 0)
        else:
            group.arrange(RIGHT, aligned_edge = UP, buff = 0)
    return group

def make_sum(lhs: str, term: str, start: str=None, end: str=None) -> MathTex:
    return make_sp('sum', lhs, term, start, end)

def make_tex(*items: str) -> MathTex:
    mathTex: MathTex = MathTex(*items)
    for i in range(len(items)):
        paint_tex(mathTex[i])
    return mathTex

def make_tex_old(*items: str) -> MathTex:
    s: str = [prepare_string(item) for item in items]
    mathTex: MathTex = MathTex(*s)
    for i in range(len(s)):
        paint_tex(mathTex[i])
    return mathTex

def paint_tex(mathTex: MathTex) -> None:
    colour = Grey
    mathTex.set_color(colour)
    s = mathTex.tex_string
    print(s)
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
                while True:
                    p += 1
                    if p >= len(s) or not s[p].isalpha():
                        break
                q += 1
            case _:
                if not escape:
                    colour = get_colour(c)
                mathTex[q].set_color(colour)
                q += 1
                if level == 0:
                    escape = False
        p += 1


def paint_tex_old(mathTex: MathTex) -> None:
    colour = Grey
    p = 0
    escape = False
    s = mathTex.tex_string
    print(s)
    for t in re.split('[_^{}]', s):
        for c in t:
            m = mathTex[p]
            if c in '|o':
                m.set_opacity(0)
            else:
                if not escape:
                    colour = get_colour(c)
                m.set_color(colour)
            escape = False
            p += 1
        escape = True

def prepare_string(s: str) -> str:
    if not '|' in s: s = f'|{s}'
    if not '^' in s: s = f'{s}^|'
    return s

def set_colour_map(colour_map: tuple[tuple[str, ManimColor]]) -> None:
    global ColourMap
    ColourMap = colour_map

def titles_hide(self, titles: List[MarkupText]) -> None:
    self.play(FadeOut(*titles))

def titles_show(self, section: int) -> List[MarkupText]:
    scales = (1.0, 0.6)
    title = [MarkupText(TITLES[section][i], color = (Cyan, Green)[i]).scale(scales[i]) for i in range(2)]
    VGroup(*title).arrange(DOWN, buff=0.5)
    with say(self, TITLES[section][0]):
        self.play(GrowFromCenter(title[0]))
        #self.wait(1)
    with say(self, TITLES[section][1]):
        self.play(FadeIn(title[1]))
        #self.wait(2)
    corners = ((DL, DR), (UL, UR))
    [title[i] \
        .generate_target() \
        .scale(0.3/scales[i]) \
        .set_color(Grey) \
        .to_corner(corners[0 if section == 0 else 1][i], buff=0.1) \
        for i in range(2)]
    self.play(MoveToTarget(title[0]), MoveToTarget(title[1]))
    return title
