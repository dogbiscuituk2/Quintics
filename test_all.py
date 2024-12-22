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

class TestAll(BaseScene):

    def construct(self):

        self.init()

        def show_table(table: List[List[str]]) -> None:
            page = []
            for row in table:
                line = []
                for cell in row:
                    tex = self.make_tex(cell)
                    text = self.make_text(cell)
                    line.append(tex)
                    line.append(text)
                page.append(line)
            grid = MobjectTable(
                page,
                v_buff=0.25,
                h_buff=0.5,
                arrange_in_grid_config={"col_alignments": "clclclclclcl"[0:2*len(table[0])]},
                line_config={"color": ManimColor([0,0,0,0])})
            grid.scale(0.5)
            self.play(FadeIn(grid))
            self.wait(8)
            self.play(FadeOut(grid))

        #with self.say("Greek and Hebrew Letters."):
        #    show_table(SYM_GREEK)
        #with self.say("Mathematical constructions."):
        #    show_table(SYM_MATH)
        #with self.say("Delimiters."):
        #    show_table(SYM_DELIM)
        with self.say("Integrals. Displayed formulae show the larger version."):
            show_table(SYM_INT)
        with self.say("Variable sized symbols. Displayed formulae show the larger version."):
            show_table(SYM_LARGE)
        #with self.say("Standard function names."):
        #    show_table(SYM_FUNC)
        #with self.say("Binary operation and relation symbols, page 1."):
        #    show_table(SYM_OPS_1)
        #with self.say("Page 2."):
        #    show_table(SYM_OPS_2)
        #with self.say("Page 3."):
        #    show_table(SYM_OPS_3)
        #with self.say("Page 4."):
        #    show_table(SYM_OPS_4)
        #with self.say("Arrow symbols, page 1."):
        #    show_table(SYM_ARROW_1)
        #with self.say("Page 2."):
        #    show_table(SYM_ARROW_2)
        #with self.say("Miscellaneous symbols."):
        #    show_table(SYM_MISC)
        #with self.say("Math mode accents."):
        #    show_table(SYM_ACCENTED)
        #with self.say("Other styles - math mode only."):
        #    show_table(SYM_STYLE)
        #with self.say("Font sizes."):
        #    show_table(SYM_FONT)
