#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test all the symbols in the LaTeX Rice document.

This scene is used to test all the symbols in the LaTeX Rice document. These 
are grouped into categories and displayed in a table, in both MathTex and text 
form, coloured according to the colour map. 
"""

from base_scene import BaseScene
from latex_rice import *
from painter import *

class TestAll(BaseScene):

    def __init__(self):
        BaseScene.__init__(self)

    def construct(self):

        def show_group(
                caption: str, 
                items: List[str], 
                cols: int = 4) -> None:
            count = len(items)
            index = 0
            rows = 17
            size = rows * cols
            pages = (count + size - 1) // size
            if pages > 1:
                caption = f'{caption} - Page 1'
            for page in range(pages):
                with self.say(caption):
                    lines = []
                    for _ in range(rows):
                        line = []
                        for _ in range(cols):
                            item = items[index] if index < count else ''                       
                            tex = self.make_tex(item)
                            line.append(tex)
                            text = self.make_text(item)
                            line.append(text)
                            index += 1
                        lines.append(line)
                        if (index >= count):
                            break
                    grid = MobjectTable(
                        lines,
                        v_buff=0.25,
                        h_buff=0.5,
                        arrange_in_grid_config={
                            "col_alignments": "clclclclclcl"[0:2*cols]},
                        line_config={"color": self.back_colour})
                    grid.scale(0.5)
                    self.play(FadeIn(grid))
                    self.wait(5)
                    self.play(FadeOut(grid))
                caption = f'Page {page + 2}'

        self.init()
        self._options = self._options | Opt.DEBUG

        #show_group("Greek and Hebrew Letters", SYM_GREEK)
        #show_group("Mathematical constructions", EXP_MATH, 3)
        #show_group("Delimiters", SYM_DELIM, 6)
        show_group("Integrals", EXP_INT, 1)
        #show_group("Variable sized symbols", SYM_LARGE)
        #show_group("Standard function names", SYM_FUNC)
        #show_group("Binary operation and relation symbols", SYM_OPS, 5)
        #show_group("Arrow symbols", SYM_ARROW)
        #show_group("Miscellaneous symbols", SYM_MISC)
        #show_group("Math mode accents", EXP_ACCENT)
        #show_group("Other styles - math mode only", EXP_STYLE, 1)
        #show_group("Font sizes", EXP_FONT, 1)
        #show_group("All symbols", SYM_ALL)
