#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test all the symbols in the LaTeX Rice document.

This scene is used to test all the symbols in the LaTeX Rice document. The
symbols are grouped into categories and displayed in a table. The symbols are
coloured according to the colour map and the colour scheme. The symbols are
displayed in both MathTex and text form. The symbols are displayed in a grid
with the MathTex object above the text object. The symbols are displayed in
groups according to their category. The symbols are displayed in a sequence of
scenes.
"""

from base_scene import BaseScene
from latex_rice import *
from painter import *

string = r"\circlearrowright"

EXP_ACCENT = [
    r'\acute{a}', r'\bar{a}', r'\Acute{\Acute{A}}', r'\Bar{\Bar{A}}',
    r'\breve{a}', r'\check{a}', r'\Breve{\Breve{A}}', r'\Check{\Check{A}}',
    r'\ddot{a}', r'\dot{a}', r'\Ddot{\Ddot{A}}', r'\Dot{\Dot{A}}',
    r'\grave{a}', r'\hat{a}', r'\Grave{\Grave{A}}', r'\Hat{\Hat{A}}',
    r'\tilde{a}', r'\vec{a}', r'\Tilde{\Tilde{A}}', r'\Vec{\Vec{A}}',
]
EXP_INT = [
    r'\int_0^1 x\,dx', 
    r'\iint_{x=0,y=0}^{x=1,y=1} xy\,dy\,dx', 
    r'\iiint xyz\,dz\,dy\,dx', 
    r'\iiiint xyzw\,dw\,dz\,dy\,dx',
    r'\idotsint x_0x_1x_2\,...\,x_n\,dx_0\,dx_1\,dx_2\,...\,dx_n', 
    r'\oint_0^{2\pi}f(\theta)\,d\theta',
]
EXP_MATH = [
    r'\frac{x}{y}', r'\overline{ax}', r'\overrightarrow{ax}',
    "f'(x)", r'\underline{ax}', r'\overleftarrow{ax}',
    r'\sqrt{ax}', r'\widehat{ax}', r'\overbrace{ax}',
    r'\sqrt[n]{ax}', r'\widetilde{ax}', r'\underbrace{ax}',
]

class TestAll(BaseScene):

    def construct(self):

        def show_group(caption: str, items: List[str], column_count: int = 4) -> None:
            item_count = len(items)
            item_index = 0
            row_count = 17
            page_size = row_count * column_count
            page_count = (item_count + page_size - 1) // page_size
            if page_count > 1:
                caption = f'{caption} - Page 1'
            for page_index in range(page_count):
                with self.say(caption):
                    page = []
                    for _ in range(row_count):
                        line = []
                        for _ in range(column_count):
                            item = items[item_index] if item_index < item_count else ''                       
                            tex = self.make_tex(item)
                            line.append(tex)
                            text = self.make_text(item)
                            line.append(text)
                            item_index += 1
                        page.append(line)
                        if (item_index >= item_count):
                            break
                    grid = MobjectTable(
                        page,
                        v_buff=0.25,
                        h_buff=0.5,
                        arrange_in_grid_config={"col_alignments": "clclclclclcl"[0:2*column_count]},
                        line_config={"color": GHOST})
                    grid.scale(0.5)
                    self.play(FadeIn(grid))
                    self.wait(5)
                    self.play(FadeOut(grid))
                caption = f'Page {page_index + 2}'

        self.init()

        show_group("Greek and Hebrew Letters", SYM_GREEK)
        show_group("Mathematical constructions", EXP_MATH, 3)
        show_group("Delimiters", SYM_DELIM, 6)
        show_group("Integrals", EXP_INT, 1)
        show_group("Variable sized symbols", SYM_LARGE)
        show_group("Standard function names", SYM_FUNC)
        show_group("Binary operation and relation symbols", SYM_OPS, 5)
        show_group("Arrow symbols", SYM_ARROW)
        show_group("Miscellaneous symbols", SYM_MISC)
        show_group("Math mode accents", EXP_ACCENT)
        show_group("Other styles - math mode only", SYM_STYLE, 1)
        show_group("Font sizes", SYM_FONT, 1)
        show_group("All symbols", SYM_ALL)
