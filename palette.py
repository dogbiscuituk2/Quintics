from manim import *
import re

ghost   = 0 # Transparent
figure  = 1 # Foreground default
ground  = 2 # Background
hilite  = 3 # Highlight background
black   = 4 # These remaining colour names are all purely logical
brown   = 5
red     = 6
orange  = 7
yellow  = 8
green   = 9
blue    = 10
cyan    = 11
magenta = 12
violet  = 13
grey    = 14
white   = 15

scheme_default          = 0
scheme_bright           = 1
scheme_pastel           = 2
scheme_black_on_white   = 3
scheme_white_on_black   = 4

TRANSPARENT = ManimColor([0,0,0,0])

class Palette():

    _GHOST = [0,0,0,0] # transparent

    _colours = (
        (_GHOST, GREY, BLACK, LIGHT_GREY, BLACK, DARK_BROWN, RED, ORANGE, YELLOW, GREEN, PURE_BLUE, TEAL, PINK, PURPLE, GREY, WHITE),
        (_GHOST, 0xB2B2B2, BLACK, DARK_GREY, BLACK, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, 0x5FBFFF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, WHITE),
        (_GHOST, 0xBBBBBB, BLACK, DARK_GREY, BLACK, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, WHITE),
        (_GHOST, BLACK, WHITE, GREY, *[BLACK for _ in range(12)]),
        (_GHOST, WHITE, BLACK, GREY, *[WHITE for _ in range(12)]))

    _colour: ManimColor
    _colour_map: tuple[tuple[re.Pattern[str], int]] = []
    _scheme: int = scheme_bright

    def __init__(
            self,
            scheme: int = scheme_bright,
            colour_map: tuple[tuple[str, int]] = ()):
        self._scheme = scheme;
        if colour_map is not None:
            self._colour_map = colour_map

    def get_colour(self, index: int):
        return self._colours[self._scheme][index]

    def get_token_colour(self, token: str):
        colours = self._colours[self._scheme]
        for map in self._colour_map:
            if (re.match(map[0], token)):
                return colours[map[1]]
        return colours[figure]

    def set_colour_map(self, colour_map: tuple[tuple[str, int]]):
        self._colour_map = [[re.compile(m[0]), m[1]] for m in colour_map]
