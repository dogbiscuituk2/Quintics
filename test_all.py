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

        def show_table(table: List[List[str]]) -> None:
            page = []
            for row in table:
                line = []
                for cell in row:
                    tex = self.make_tex(cell)
                    line.append(tex)
                page.append(line)
            grid = MobjectTable(
                page,
                v_buff=0.25,
                h_buff=0.5,
                line_config={"color": ManimColor([0,0,0,0])})
            grid.scale(0.5)
            self.play(FadeIn(grid))
            self.wait(8)
            self.play(FadeOut(grid))

        def show_page(table: List[List[str]]) -> None:
            page = []
            for row in table:
                line = []
                for cell in row:
                    tex = self.make_tex(cell)
                    line.append(tex)
                    text = self.make_text(cell)
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

        self.init()

        with self.say("Expressions."):
            show_table([
                [r'\int_{abcde}^{xyz}', r'\iint_{abcde}^{xyz}', r'\iiint_{abcde}^{xyz}', r'\iiiint_{abcde}^{xyz}', r'\idotsint_{abcde}^{xyz}', r'\oint_{abcde}^{xyz}'],
                [r'\sum_{abcde}^{xyz}', r'\prod_{abcde}^{xyz}', r'\coprod_{abcde}^{xyz}', r'\bigvee_{abcde}^{xyz}', r'\bigwedge_{abcde}^{xyz}', r'\bigsqcup_{abcde}^{xyz}'],
                [r'\bigoplus_{abcde}^{xyz}', r'\bigotimes_{abcde}^{xyz}', r'\bigodot_{abcde}^{xyz}', r'\bigcup_{abcde}^{xyz}', r'\bigcap_{abcde}^{xyz}', r'\biguplus_{abcde}^{xyz}'],
                ])

        #with self.say("Scratchpad."):
        #    painter = Painter()
        #    text = r'\int_{abcde}^{xyz}'
        #    tex = MathTex(text)
        #    painter.paint_tex(tex)
        #    self.play(FadeIn(tex))
        #    self.wait(8)
        #    self.play(FadeOut(tex))
        #    text = r'\sum_{abcde}^{xyz}'
        #    tex = MathTex(text)
        #    painter.paint_tex(tex)
        #    self.play(FadeIn(tex))
        #    self.wait(8)
        #    self.play(FadeOut(tex))
        #with self.say("Greek and Hebrew Letters."):
        #    show_page(SYM_GREEK)
        #with self.say("Mathematical constructions."):
        #    show_page(SYM_MATH)
        #with self.say("Delimiters."):
        #    show_page(SYM_DELIM)
        #with self.say("Integrals. Displayed formulae show the larger version."):
        #    show_page(SYM_INT)
        #with self.say("Variable sized symbols. Displayed formulae show the larger version."):
        #    show_page(SYM_LARGE)
        #with self.say("Standard function names."):
        #    show_page(SYM_FUNC)
        #with self.say("Binary operation and relation symbols, page 1."):
        #    show_page(SYM_OPS_1)
        #with self.say("Page 2."):
        #    show_page(SYM_OPS_2)
        #with self.say("Page 3."):
        #    show_page(SYM_OPS_3)
        #with self.say("Page 4."):
        #    show_page(SYM_OPS_4)
        #with self.say("Arrow symbols, page 1."):
        #    show_page(SYM_ARROW_1)
        #with self.say("Page 2."):
        #    show_page(SYM_ARROW_2)
        #with self.say("Miscellaneous symbols."):
        #    show_page(SYM_MISC)
        #with self.say("Math mode accents."):
        #    show_page(SYM_ACCENTED)
        #with self.say("Other styles - math mode only."):
        #    show_page(SYM_STYLE)
        #with self.say("Font sizes."):
        #    show_page(SYM_FONT)
