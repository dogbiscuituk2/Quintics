from base_scene import BaseScene
from painter import *
from latex_rice import *

string = r"\circlearrowright"
import re

class TestAll(BaseScene):

    def construct(self):
        self.init()

        self.set_colour_map((
            #('[Oo|]', ghost),
            (PAT_GREEK, red),
            (PAT_DELIM, red),
            (PAT_LARGE, orange),
            (PAT_FUNC, yellow),
            (PAT_OPS, green),
            (PAT_ARROW, blue),
            (PAT_MISC, cyan),
            (r'\\frac', magenta),
            (r'\\sqrt|\\lim', orange),
            (r'[a-e]|\\alpha|\\beta|\\gamma|\\delta|\\epsilon', green),
            ('h', orange),
            (r'[p-s]|\\pi|\\rho\|\\sigma|\\sin', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))
        
        def show_table(table: List[List[str]]) -> None:
            page = []
            for row in table:
                line = []
                for cell in row:
                    line.append(self.make_tex(cell))
                    line.append(self.make_text(cell))
                page.append(line)
            grid = MobjectTable(
                page,
                v_buff=0.25,
                h_buff=0.5,
                arrange_in_grid_config={"col_alignments": "clclclclclcl"[0:2*len(table[0])]},
                line_config={"color": TRANSPARENT})
            grid.scale(0.5)
            self.play(FadeIn(grid))
            self.wait(8)
            self.play(FadeOut(grid))

        with self.say("Greek and Hebrew Letters."):
            show_table(SYM_GREEK)
        #with self.say("Mathematical constructions."):
        #    show_table(SYM_MATH)
        with self.say("Delimiters."):
            show_table(SYM_DELIM)
        with self.say("Variable sized symbols. Displayed formulae show the larger version."):
            show_table(SYM_LARGE)
        with self.say("Standard function names."):
            show_table(SYM_FUNC)
        with self.say("Binary operation and relation symbols."):
            show_table(SYM_OPS_1)
            show_table(SYM_OPS_2)
            show_table(SYM_OPS_3)
            show_table(SYM_OPS_4)
        with self.say("Arrow symbols."):
            show_table(SYM_ARROW_1)
            show_table(SYM_ARROW_2)
        with self.say("Miscellaneous symbols."):
            show_table(SYM_MISC)
        #with self.say("Math mode accents."):
        #    show_table(SYM_ACCENT)
        #with self.say("Other styles - math mode only."):
        #    show_table(SYM_STYLE)
        #with self.say("Font sizes."):
        #    show_table(SYM_FONT)
