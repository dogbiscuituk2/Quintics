import re

from typing import Generator

from manim_voiceover.services.azure import AzureService
from manim_voiceover.services.base import SpeechService
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.tracker import VoiceoverTracker

from manim import *

config.max_files_cached = 999
config.verbosity = 'WARNING'

#region Box

_box = None

def box(self: Scene, *args: VMobject) -> None:
    self.play(box_move(*args))

def box_move(*args: VMobject) -> Animation:
    global _box
    b = SurroundingRectangle(VGroup(*args), Yellow) 
    result = Create(b) if _box == None else ReplacementTransform(_box, b)
    _box = b
    return result

def unbox(self: Scene) -> None:
    global _box
    if _box != None:
        self.play(Uncreate(_box))
        _box = None

#endregion Box

#region Colours

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

def paint_tex(mathTex: MathTex, s: str) -> None:
    colour = Black
    p = 0
    escape = False
    #for t in s.split('^'):
    for t in re.split('[_^]', s):
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

#endregion Colours

#region Debug

def dump(*args) -> None:
    for arg in args:
        print([s.tex_string for s in arg])
    print()

#endregion Debug

#region Init

def init(self):
    self.set_speech_service(speech_services[1])

#endregion Init

#region Speech

speech_services: List[SpeechService] = [
    AzureService(voice="en-US-AriaNeural", style="newscast-casual", global_speed=1.15),
    GTTSService(())]

def say(self, text: str): # -> Generator[VoiceoverTracker, None, None]:
    tracker = self.voiceover(text)
    #print(tracker.data['input_text'])
    print(text)
    print()
    return tracker

#endregion

#region Text

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

#endregion Text
