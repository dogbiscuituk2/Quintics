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

    SUBSUPER = auto()
    """Subscript/Superscript. In x_2^3, the colour of 2 & 3 matches x."""

    DIFF = auto()
    """Differentials. In dx, the colour of d matches x."""

    MATH = auto()
    """Example: in \\overbrace{x}, the brace colour matches x."""

    ACCENT = auto()
    """Example: in \\acute{e}, the accent colour matches e."""

    DEBUG_COLOURS = auto()
    """Override all colours & assign sequential ones cyclically."""

    DEBUG_FAST = auto()
    """Skip animations."""

    DEBUG_LABELS = auto()
    """Show index_labels for each MathTex or Text."""

    DEBUG_NOPAINT = auto()
    """Skip the re-painting of glyphs."""

    DEBUG_SILENT = auto()
    """Mute all voiceover calls."""

    DEBUG_SYMBOLS = auto()
    """Show Symbols before & after."""

    DEBUG_TEX = auto()
    """Show MathTex structure."""

    SYM = MATH | ACCENT
    DEFAULT = SUBSUPER | DIFF | SYM
