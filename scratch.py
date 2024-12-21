#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scratchpad for project Polynomials"""
from painter import *

colour_map = [
    #('oO|', Pen.NONE),
    (PAT_GREEK, Pen.RED),
    (PAT_MATH, Pen.BROWN),
    (PAT_DELIM, Pen.RED),
    (PAT_LARGE, Pen.ORANGE),
    (PAT_FUNC, Pen.YELLOW),
    (PAT_OPS, Pen.GREEN),
    (PAT_ARROW, Pen.BLUE),
    (PAT_MISC, Pen.CYAN),
    (PAT_ACCENT, Pen.VIOLET),
    (PAT_STYLE, Pen.VIOLET),
    (PAT_FONT, Pen.VIOLET),
    (r'\\frac', Pen.GREEN),
    (r'\\sqrt|\\lim', Pen.ORANGE),
    (r'[a-eA-E]|\\alpha|\\beta|\\gamma|\\delta|\\epsilon', Pen.RED),
    ('h', Pen.ORANGE),
    ('[p-s]', Pen.YELLOW),
    ('x', Pen.RED),
    ('y', Pen.MAGENTA),
    ('z', Pen.CYAN),
]

painter = Painter()
painter.set_scheme(scheme_bright)
painter.set_colour_map(colour_map)

# Function to recursively print submobjects
def print_submobjects(mobject, indent=0):
    for submobject in mobject.submobjects:
        print(" " * indent + f"Submobject: {submobject}")
        print_submobjects(submobject, indent + 2)

# Create a MathTex object
text = r'\frac{x}{y} + \sqrt{z}'
tex = MathTex(text)
print_submobjects(tex)


# Print the submobjects and their indices
#for i, submobject in enumerate(tex.submobjects):
#    print(f"Index: {i}, Submobject: {submobject}, Text: {submobject.get_tex_string()}")

