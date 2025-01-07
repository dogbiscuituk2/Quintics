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

    NONE = 0

    SUB = auto()
    """Subscripts. In 'x_1', the colour of '1' matches 'x'."""

    SUPER = auto()
    """Superscripts. In 'x^2', the colour of '2' matches 'x'."""

    DIFF = auto()
    """Differentials. In 'dx', the colour of 'd' matches 'x'."""

    MATH = auto()
    """Example: in '\\overbrace{x}', the brace colour matches 'x'."""

    ACCENT = auto()
    """Example: in '\\acute{e}', the accent colour matches 'e'."""

    DEBUG_COLOURS = auto()
    """Override all colours & assign sequential ones cyclically."""

    DEBUG_LABELS = auto()
    """Show index_labels for each MathTex or Text."""

    DEBUG_NOPAINT = auto()
    """Skip painting glyphs."""

    DEBUG_SYMBOLS = auto()
    """Print Symbols before & after."""

    DEBUG_TEX = auto()
    """Print MathTex structure."""

    SHIFT = SUB | SUPER
    SYM = MATH | ACCENT
    DEFAULT = SHIFT | DIFF | SYM
