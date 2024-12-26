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
EXP_MATH = [
    r'\frac{x}{y}', r'\overline{ax}', r'\overrightarrow{ax}',
    "f'(x)", r'\underline{ax}', r'\overleftarrow{ax}',
    r'\sqrt{ax}', r'\widehat{ax}', r'\overbrace{ax}',
    r'\sqrt[n]{ax}', r'\widetilde{ax}', r'\underbrace{ax}',
]

class TestAll(BaseScene):

    def construct(self):

        def show_page(caption: str, items: List[str], column_count: int = 4) -> None:
            with self.say(caption):
                item_count = len(items)
                row_count = (item_count + column_count - 1) // column_count
                page = []
                for row_index in range(row_count):
                    line = []
                    for column_index in range(column_count):
                        item_index = row_index * column_count + column_index
                        item = items[item_index] if item_index < item_count else ''                       
                        tex = self.make_tex(item)
                        line.append(tex)
                        text = self.make_text(item)
                        line.append(text)
                    page.append(line)
                grid = MobjectTable(
                    page,
                    v_buff=0.25,
                    h_buff=0.5,
                    #arrange_in_grid_config={"col_alignments": "clclclclclcl"[0:2*len(page)]},
                    line_config={"color": ManimColor([0,0,0,0])})
                grid.scale(0.5)
                self.play(FadeIn(grid))
                self.wait(8)
                self.play(FadeOut(grid))

        self.init()

        show_page("Greek and Hebrew Letters", SYM_GREEK)
        show_page("Mathematical constructions", EXP_MATH)
        show_page("Delimiters", SYM_DELIM)
        show_page("Integrals", SYM_INT, 6)
        show_page("Variable sized symbols", SYM_LARGE)
        show_page("Standard function names", SYM_FUNC)
        show_page("Binary operation and relation symbols", SYM_OPS_1)
        show_page("Page 2", SYM_OPS_2)
        show_page("Page 3", SYM_OPS_3)
        show_page("Page 4", SYM_OPS_4)
        show_page("Arrow symbols", SYM_ARROW_1)
        show_page("Page 2", SYM_ARROW_2)
        show_page("Miscellaneous symbols", SYM_MISC)
        show_page("Math mode accents", EXP_ACCENT)
        show_page("Other styles - math mode only", SYM_STYLE, 1)
        show_page("Font sizes", SYM_FONT, 1)
