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
                strings: List[str], 
                cols: int = 4,
                rows = 12,
                transpose: bool = False) -> None:
            
            def add_items() -> None:

                def add_tex(line: List[SVGMobject], item: str) -> None:
                    line.append(self.make_tex(item))
                    line.append(self.make_text(item))

                def add_item(row: int) -> None:
                    item = next(items)
                    if len(lines) <= row:
                        lines.append([])
                    add_tex(lines[row], item)

                try:
                    if transpose:
                        for _ in range(cols):
                            for row in range(rows):
                                add_item(row)
                    else:
                        for row in range(rows):
                            for _ in range(cols):
                                add_item(row)
                except StopIteration:
                    pass
                for line in lines:
                    while len(line) < len(lines[0]):
                        add_tex(line, '')

            items = iter(strings)
            count = len(strings)
            rows = min((count + cols - 1) // cols, rows)
            size = rows * cols
            pages = (count + size - 1) // size
            if pages > 1:
                caption = f'{caption} - Page 1 of {pages}'
            for page in range(pages):
                with self.say(caption):
                    lines: List[List[SVGMobject]] = []
                    add_items()
                    grid = MobjectTable(
                        lines,
                        v_buff=0.25,
                        h_buff=0.5,
                        arrange_in_grid_config={
                            "col_alignments": "cl" * cols},
                            line_config={"color": self.back_colour})
                    grid.scale(0.5)
                    self.play(FadeIn(grid))
                    self.wait(5)
                    self.play(FadeOut(grid))
                caption = f'Page {page + 2} of {pages}'

        self.init()
        #self._options = self._options | Opt.DEBUG

        show_group("Greek and Hebrew Letters", SYM_GREEK, transpose=True)
        show_group("Mathematical constructions", EXP_MATH, 3)
        show_group("Delimiters", EXP_DELIM, 2)
        show_group("Integrals", EXP_INT, 1)
        show_group("Variable sized symbols", SYM_LARGE)
        show_group("Standard function names", SYM_FUNC)
        show_group("Binary operation and relation symbols", SYM_OPS, 5)
        show_group("Arrow symbols", SYM_ARROW)
        show_group("Miscellaneous symbols", SYM_MISC)
        show_group("Math mode accents", EXP_ACCENT)
        show_group("Other styles - math mode only", EXP_STYLE, 1)
        show_group("Font sizes", EXP_FONT, 1)
        show_group("All symbols", SYM_ALL)
