#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utility classes for colouring MathTex objects.

The Pen class is an enumeration of the 22 colours used to colour the glyphs in 
a MathTex object. 

The list of physical names, and the PALETTE_SASHA values, are due to:

    Sasha Trubetskoy - https://sashamaps.net/docs/resources/20-colors/

The enum ordering used here reflects his "convenience" ordering. For a project 
requiring 10 colours, you might use the first 10 "Pen"s from the enumeration.
"""

from enum import Enum, auto
from typing import List
from manim import *

class Pen(Enum):
    BLACK    = 0
    WHITE    = auto()
    RED      = auto()
    GREEN    = auto()
    YELLOW   = auto()
    BLUE     = auto()
    ORANGE   = auto()
    PURPLE   = auto()
    CYAN     = auto()
    MAGENTA  = auto()
    LIME     = auto()
    PINK     = auto()
    TEAL     = auto()
    LAVENDER = auto()
    BROWN    = auto()
    BEIGE    = auto()
    MAROON   = auto()
    MINT     = auto()
    OLIVE    = auto()
    APRICOT  = auto()
    NAVY     = auto()
    GREY     = auto()

PALETTE_BRIGHT: List[ManimColor] = [
    0x000000, # black
    0xffffff, # white
    0xff0000, # red
    0x00ff00, # green
    0xffff00, # yellow
    0x3f3fff, # blue
    0xff7f00, # orange
    0x7f00ff, # purple
    0x00ffff, # cyan
    0xff00ff, # magenta
    0xbfef45, # lime
    0xfabed4, # pink
    0x5fcfcf, # teal
    0xdcbeff, # lavender
    0x9a6324, # brown
    0xfffac8, # beige
    0xaf0000, # maroon
    0xaaffc3, # mint
    0x808000, # olive
    0xffd8b1, # apricot
    0x1f1fff, # navy
    0xa9a9a9, # grey
]
PALETTE_SASHA: List[ManimColor] = [
    0x000000, # black
    0xffffff, # white
    0xe6194b, # red
    0x3cb44b, # green
    0xffe119, # yellow
    0x4363d8, # blue
    0xf58231, # orange
    0x911eb4, # purple
    0x42d4f4, # cyan
    0xf032e6, # magenta
    0xbfef45, # lime
    0xfabed4, # pink
    0x469990, # teal
    0xdcbeff, # lavender
    0x9a6324, # brown
    0xfffac8, # beige
    0x800000, # maroon
    0xaaffc3, # mint
    0x808000, # olive
    0xffd8b1, # apricot
    0x000075, # navy
    0xa9a9a9, # grey
]
PALETTE_BLACK_ON_WHITE: List[ManimColor] = [
    BLACK, WHITE, *[BLACK for _ in range(20)]
]
PALETTE_WHITE_ON_BLACK: List[ManimColor] = [
    BLACK, WHITE, *[WHITE for _ in range(20)]
]
