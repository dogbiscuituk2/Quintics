#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utility classes for colouring MathTex objects.

The Pen class is an enumeration of the colours used to colour the glyphs in a
MathTex object. The Scheme class is an enumeration of the colour schemes used 
to colour the glyphs in a MathTex object. The COLOURS tuple is a list of 
colours used to colour the glyphs in a MathTex object.

The basic list of 20 physical names, and their RGB values, are due to

    Sasha Trubetskoy: https://sashamaps.net/docs/resources/20-colors/

The enum ordering used here reflects his "convenience" ordering.
"""

from enum import Enum, auto
from manim import *

class Pen(Enum):
    BLACK    = 0
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
    WHITE    = auto()

PALETTE_DEFAULT: List[ManimColor] = [
    0x000000, # black
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
    0x9A6324, # brown
    0xfffac8, # beige
    0x800000, # maroon
    0xaaffc3, # mint
    0x808000, # olive
    0xffd8b1, # apricot
    0x000075, # navy
    0xa9a9a9, # grey
    0xffffff, # white
]
