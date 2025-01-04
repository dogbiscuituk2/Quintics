#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Options class for Painter.

Opt.DEBUG causes all glyph colours to be replaced with those corresponding to 
the Pens enum, repeatedly cycling from first to last as necessary, but omitting 
the Pen used for background fill.
"""

from enum import Flag, auto

class Opt(Flag):
    NONE          = 0
    SUB           = auto() # 'x_1': 1 matches x.
    SUPER         = auto() # 'x^2': 2 matches x.
    DIFF          = auto() # r'\frac{d^2x}{dy^2}': d, \partial match x, y.
    MATH          = auto() # r'\overbrace{x}': brace matches x.
    ACCENT        = auto() # r'acute{e}': accent matches letter.
    DEBUG_COLOURS = auto() # override all colours & assign sequentially.
    DEBUG_SYMBOLS = auto() # print Symbols before & after.
    DEBUG_TEX     = auto() # print MathTex structure.
    SHIFT         = SUB | SUPER
    SYM           = MATH | ACCENT
    DEFAULT       = SHIFT | DIFF | SYM # everything except AUTO, DEBUG.
