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

text = r'\alpha'
tex = MathTex(text)

print(PAT_GREEK)
print(PAT_MATH)
print(PAT_DELIM)
print(PAT_LARGE)
print(PAT_FUNC)
print(PAT_OPS)
print(PAT_ARROW)
print(PAT_MISC)
print(PAT_ACCENT)
print(PAT_STYLE)
print(PAT_FONT)

painter.paint(tex)
