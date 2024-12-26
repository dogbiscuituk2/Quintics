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
    [r'\acute{a}', r'\bar{a}', r'\Acute{\Acute{A}}', r'\Bar{\Bar{A}}'],
    [r'\breve{a}', r'\check{a}', r'\Breve{\Breve{A}}', r'\Check{\Check{A}}'],
    [r'\ddot{a}', r'\dot{a}', r'\Ddot{\Ddot{A}}', r'\Dot{\Dot{A}}'],
    [r'\grave{a}', r'\hat{a}', r'\Grave{\Grave{A}}', r'\Hat{\Hat{A}}'],
    [r'\tilde{a}', r'\vec{a}', r'\Tilde{\Tilde{A}}', r'\Vec{\Vec{A}}'],
]
EXP_MATH = [
    [r'\frac{x}{y}', r'\overline{ax}', r'\overrightarrow{ax}'],
    ["f'(x)", r'\underline{ax}', r'\overleftarrow{ax}'],
    [r'\sqrt{ax}', r'\widehat{ax}', r'\overbrace{ax}'],
    [r'\sqrt[n]{ax}', r'\widetilde{ax}', r'\underbrace{ax}'],
]

class TestAll(BaseScene):

    def construct(self):

        def show_page_old(items: List[str]) -> None:
            item_count = len(items)
            column_count = 1 if item_count <= 10 else 4
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

        def show_page_very_old(table: List[List[str]]) -> None:
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

        with self.say("Greek and Hebrew Letters."):
            show_page_old(SYM_GREEK)
        #with self.say("Mathematical constructions."):
        #    show_page_old(EXP_MATH)
        #with self.say("Delimiters."):
        #    show_page_old(SYM_DELIM)
        #with self.say("Integrals. Displayed formulae show the larger version."):
        #    show_page_old(SYM_INT)
        #with self.say("Variable sized symbols. Displayed formulae show the larger version."):
        #    show_page_old(SYM_LARGE)
        #with self.say("Standard function names."):
        #    show_page_old(SYM_FUNC)
        #with self.say("Binary operation and relation symbols, page 1."):
        #    show_page_old(SYM_OPS_1)
        #with self.say("Page 2."):
        #    show_page_old(SYM_OPS_2)
        #with self.say("Page 3."):
        #    show_page_old(SYM_OPS_3)
        #with self.say("Page 4."):
        #    show_page_old(SYM_OPS_4)
        #with self.say("Arrow symbols, page 1."):
        #    show_page_old(SYM_ARROW_1)
        #with self.say("Page 2."):
        #    show_page_old(SYM_ARROW_2)
        #with self.say("Miscellaneous symbols."):
        #    show_page_old(SYM_MISC)
        #with self.say("Math mode accents."):
        #    show_page_old(EXP_ACCENT)
        #with self.say("Other styles - math mode only."):
        #    show_page_old(SYM_STYLE)
        #with self.say("Font sizes."):
        #    show_page_old(SYM_FONT)
