#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scratchpad for project Polynomials"""
from painter import *

colour_map = [
    #('oO|', ghost),
    (PAT_GREEK, red),
    (PAT_MATH, brown),
    (PAT_DELIM, red),
    (PAT_LARGE, orange),
    (PAT_FUNC, yellow),
    (PAT_OPS, green),
    (PAT_ARROW, blue),
    (PAT_MISC, cyan),
    (PAT_ACCENT, violet),
    (PAT_STYLE, violet),
    (PAT_FONT, violet),
    (r'\\frac', magenta),
    (r'\\sqrt|\\lim', orange),
    (r'[a-e]|\\alpha|\\beta|\\gamma|\\delta|\\epsilon', green),
    ('h', orange),
    (r'[p-s]|\\pi|\\rho\|\\sigma|\\sin', yellow),
    ('x', red),
    ('y', magenta),
    ('z', cyan),
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

