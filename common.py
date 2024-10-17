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

def init(self):
    set_palette(PALETTE_BRIGHT)
    self.set_speech_service(GTTSService())

def set_colour_map(colour_map: tuple[tuple[str, ManimColor]]) -> None:
    global ColourMap
    ColourMap = colour_map

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
