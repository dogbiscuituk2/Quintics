#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scratchpad for project Polynomials
This scratchpad is used to test code snippets and to experiment with the Manim 
library.
It is not part of the project and is not used to generate any output.
It is a standalone script that can be run from the command line.
It is used to test the parsing of MathTex objects and the painting of glyphs.
"""

from painter import *

painter = Painter()

# Function to recursively print submobjects
#def print_submobjects(mobject, indent=0):
#    for submobject in mobject.submobjects:
#        print(" " * indent + f"Submobject: {submobject}")
#        print_submobjects(submobject, indent + 2)

# Create a MathTex object
text = r'\int_{abcde}^{xyz}'
tex = MathTex(text)
#print_submobjects(tex)
painter.paint_tex(tex)
