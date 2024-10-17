from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

config.max_files_cached = 999

PALETTE_DEFAULT = 0
PALETTE_BRIGHT = 1
PALETTE_PASTEL = 2
PALETTE_BLACK_ON_WHITE = 3
PALETTE_WHITE_ON_BLACK = 4
    
colours = (
    (0x000000, 0x000000, 0x3F3F00, 0xFF0000, 0x7F7F00, 0xFFFF00, 0x00FF00, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x7F007F, 0x7F7F7F, 0xFFFFFF),
    (0x000000, 0x000000, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, 0xFFFFFF),
    (0x000000, 0x000000, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, 0xFFFFFF),
    (0xFFFFFF, *[0x000000 for _ in range(12)]),
    (0x000000, *[0xFFFFFF for _ in range(12)]))

def get_colour(char: str) -> ManimColor:
    for map in ColourMap:
        if (char in map[0]):
            return map[1]
    return Grey

def init(self):
    self.set_speech_service(GTTSService())

def make_tex(*items: str) -> MathTex:
    s: str = [prepare_string(item) for item in items]
    mathTex: MathTex = MathTex(*s)
    for i in range(len(s)):
        paint_tex(mathTex[i], s[i])
    return mathTex

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

def prepare_string(s: str) -> str:
    if not '|' in s: s = f'|{s}'
    if not '^' in s: s = f'{s}^|'
    return s

def set_colour_map(colour_map: tuple[tuple[str, ManimColor]]) -> None:
    global ColourMap
    ColourMap = colour_map

palette = PALETTE_BRIGHT

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
