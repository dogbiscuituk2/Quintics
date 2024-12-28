#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility classes for colouring MathTex objects.

The Pen class is an enumeration of the colours used to colour the glyphs in a
MathTex object. The Scheme class is an enumeration of the colour schemes used 
to colour the glyphs in a MathTex object. The COLOURS tuple is a list of 
colours used to colour the glyphs in a MathTex object.
"""

from enum import Enum
from manim import *

class Pen(Enum):
    NONE    = 0 # Transparent
    FG      = 1 # Foreground default
    BG      = 2 # Background
    HILITE  = 3 # Highlight background
    BLACK   = 4 # These remaining colour names are all purely logical
    BROWN   = 5
    RED     = 6
    ORANGE  = 7
    YELLOW  = 8
    GREEN   = 9
    BLUE    = 10
    CYAN    = 11
    MAGENTA = 12
    VIOLET  = 13
    GREY    = 14
    WHITE   = 15

class Scheme(Enum):
    DEFAULT         = 0
    BRIGHT          = 1
    PASTEL          = 2
    BLACK_ON_WHITE  = 3
    WHITE_ON_BLACK  = 4

GHOST = ManimColor([0,0,0,0]) # transparent

COLOURS: List[List[ManimColor]] = [
    [GHOST, GREY, BLACK, LIGHT_GREY, BLACK, DARK_BROWN, RED, ORANGE, YELLOW, GREEN, PURE_BLUE, TEAL, PINK, PURPLE, GREY, WHITE],
    [GHOST, 0xB2B2B2, BLACK, DARK_GREY, BLACK, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, 0x5FBFFF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, WHITE],
    [GHOST, 0xBBBBBB, BLACK, DARK_GREY, BLACK, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, WHITE],
    [GHOST, BLACK, WHITE, GREY, *[BLACK for _ in range(12)]],
    [GHOST, WHITE, BLACK, GREY, *[WHITE for _ in range(12)]]]
