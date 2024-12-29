#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utility classes for colouring MathTex objects.

The Pen class is an enumeration of the colours used to colour the glyphs in a
MathTex object. The Scheme class is an enumeration of the colour schemes used 
to colour the glyphs in a MathTex object. The COLOURS tuple is a list of 
colours used to colour the glyphs in a MathTex object.
"""

from enum import Enum, auto
from manim import *

class Pen(Enum):
    NONE    = 0
    FG      = auto() # Foreground
    BG      = auto() # Background
    BLACK   = auto() # These remaining colour names are all purely logical
    BROWN   = auto()
    RED     = auto()
    ORANGE  = auto()
    YELLOW  = auto()
    GREEN   = auto()
    CYAN    = auto()
    BLUE    = auto()
    MAGENTA = auto()
    VIOLET  = auto()
    GREY    = auto()
    WHITE   = auto()

class Scheme(Enum):
    NONE            = 0
    DEFAULT         = auto()
    BRIGHT          = auto()
    PASTEL          = auto()
    MONOCHROME      = auto()
    BLACK_ON_WHITE  = auto()
    WHITE_ON_BLACK  = auto()

COLOURS: List[List[ManimColor]] = [
    [],
    [
        0, WHITE, BLACK,
        BLACK, LIGHT_BROWN, PURE_RED, ORANGE, 
        YELLOW, PURE_GREEN, TEAL, PURE_BLUE, 
        PINK, GOLD, GREY, WHITE, 
        #PINK, PURPLE_A, GREY, WHITE, 
    ],
    [
        0, 0xB2B2B2, BLACK, 
        DARK_GREY, 0x7F3319, 0xFF1933, 0xFF7F4C, 
        0xCCCC00, 0x33FF33, 0x00FFFF, 0x5FBFFF, 
        0xFF00FF, 0x9A72AC, 0xB2B2B2, WHITE,
    ],
    [
        0, 0xBBBBBB, BLACK, 
        BLACK, 0xCD853F, 0xFF0000, 0xFF7F3F, 
        0xCCCC00, 0x33FF33, 0x00FFFF, PURE_BLUE, 
        0xFF00FF, 0x9A72AC, 0xBBBBBB, WHITE,
    ],
    [
        0, BLACK, WHITE, 
        0x222222, 0x333333, 0x444444, 0x555555, 
        0x666666, 0x777777, 0x888888, 0x999999,
        0xAAAAAA, 0xBBBBBB, 0xCCCCCC, 0xDDDDDD,
    ],
    [
        0, BLACK, WHITE, 
        *[BLACK for _ in range(12)]
    ],
    [
        0, WHITE, BLACK, 
        *[WHITE for _ in range(12)]
    ],
]
