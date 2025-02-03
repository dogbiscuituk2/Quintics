#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The Painter class is used to apply colours to the glyphs in a MathTex object.
The colours are determined by a colour map which is a list of tuples, each 
containing a regular expression pattern and a pen index. The pattern is used 
to match the token of a glyph and the pen index is used to determine the 
colour of the glyph. 
The pen index is an integer that corresponds to an index in the colours list. 
The Painter class is used to apply colours to the glyphs in a MathTex object.

Mobject
 +- VMobject
    +- SVGMobject
       +- Text
       +- SingleStringMathTex
          +- MathTex

VMobject has a list of child VMobjects called submobjects.
"""

from inspect import currentframe
from latex_rice import *
from latex_token import Token
from manim import *
from options import Opt
from pens import *
import re
from symbol import Symbol
from typing import Generator, Tuple

PAT_TOKEN = r"\\{|\\}|\\\||\\[A-Za-z]+|\\\\|\\\,|[^&\s]"

def adjust(symbols: List[Symbol], delta: int) -> None:
    for symbol in symbols:
        symbol.glyph_index += delta

def make_pen(pattern: str, pen: Pen) -> tuple[str, Pen]:
    """
    Create a new pen to be used by the painter.
    
    pattern: A regular expression pattern used to match the token of a glyph.
    
    pen: The pen to be used to determine the colour of the glyph.
    
    Returns: A tuple containing the pattern and the pen.
    """
    return ([re.compile(pattern), pen])

def permute(*lists: List[Symbol]) -> None: # TODO: use it!
    deltas = [lists[i+1][0].glyph_index - lists[i][0].glyph_index for i in range(len(lists))]
    for i, list in enumerate(lists):
        adjust(list, deltas[i])
            
def concat_tokens(tokens: List[Token]) -> str:
    return ' '.join([token.string for token in tokens])

def get_glyph_count(symbols: List[Symbol]) -> int:
    return sum(symbol.glyph_count for symbol in symbols)

def get_tex_length(token: str) -> int:
    match token:
        case r'\frac':
            return 1
    try:
        return len(SingleStringMathTex(token))
    except Exception:
        return 0

class Painter():

    glyph_index: int
    opt: Opt
    palette: List[ManimColor] = PALETTE_SASHA
    pen: Pen
    pens: List[tuple[re.Pattern[str], Pen]] = []
    sticky: bool # Subscripted or superscripted unit reuses previous colour.
    tex: MathTex
    text: str
    token_index: int
    tokens: List[Token] = []

    def __init__(self, options: Opt = Opt.DEFAULT):
        self.options = options
        self.pen = Pen.GREY
        self.sticky = False
        self.tex = None
        self.text = ''
        self.tokens = []
        self.token_index = 0
        self.glyph_index = 0

    @property
    def ink_bg(self) -> ManimColor:
        return config.background_color

    @property
    def ink_fg(self) -> ManimColor:
        return self.get_ink(self.pen_fg)

    @property
    def options(self) -> Opt:
        return self.opt
    
    @options.setter
    def options(self, value: Opt) -> None:
        self.opt = value
    
    def get_ink(self, pen: Pen) -> ManimColor:
        """
        Return the colour associated with the given pen.
        
        pen: The pen whose colour is to be returned.
        
        Returns: The colour associated with the given pen.
        """
        return self.palette[pen.value] if pen.value >= 0 else self.ink_bg
    
    def paint(self, root: Mobject) -> None:
        """
        Apply colours to the glyphs in the given Mobject tree.

        root: The root object to be painted.
        """
        self.paint_node(root)

    def paint_node(self, node: Mobject) -> None:
        if type(node) is SingleStringMathTex:
            self.paint_ssmt(node)
        elif isinstance(node, VMobject):
            for child in node.submobjects:
                self.paint_node(child)

    def paint_ssmt(self, tex: SingleStringMathTex) -> None:
        """
        Apply colours to the glyphs in the given SingleStringMathTex object.

        tex: The SingleStringMathTex object to be painted.

        '\\left.', '\\right.' not implemented.
        """
        self.tex = tex
        text = tex.tex_string
        if not text:
            return
        self.text = text
        self.tokens.clear()
        for match in re.finditer(PAT_TOKEN, text):
            span = match.span()
            start = span[0]
            end = span[1]
            length = end - start
            string = text[start:end]
            token = Token(start=start, length=length, string=string)
            self.tokens.append(token)
        self.token_index = 0
        self.glyph_index = 0
        if Opt.DEBUG_NOPAINT in self.options:
            return
        while self.more:
            symbols = self.paint_unit()
            glyphs = self.tex
            pen = Pen.BACKGROUND
            for symbol in symbols:
                start = symbol.glyph_index
                stop = start + symbol.glyph_count
                if stop > start:
                    if Opt.DEBUG_COLOURS in self.options:
                        pen = Pen(pen.value + 1) if pen.value < 21 else Pen(0)
                    else:
                        pen = symbol.pen
                    colour = self.get_ink(pen)
                    for index in range(start, stop):
                        if index >= 0 and index < len(glyphs):
                            glyph = glyphs[index]
                            glyph.set_color(colour)

    def set_palette(self, palette: List[ManimColor]) -> None:
        """
        Set the palette of colours to be used by the painter.
        
        palette: A list of colours to be used by the painter.
        """
        self.palette = palette

#region Pens

    def add_pen(self, pattern: str, pen: Pen) -> None:
        """
        Add a new pen to the colour map.
        
        pattern: A regular expression pattern used to match the token of a glyph.
        
        pen: The pen to be used to determine the colour of the glyph.
        """
        self.pens.insert(0, make_pen(pattern, pen))

    def get_token_pen(self, token: str) -> Pen:
        for map in self.pens:
            if (re.match(map[0], token)):
                return map[1]
        return Pen.WHITE

    def remove_pen(self, pattern: str) -> None:
        """
        Remove a pen from the colour map.
        
        pattern: The regular expression pattern used to match the token of a glyph.
        """
        self.pens = [p for p in self.pens if p[0].pattern != pattern]

    def set_pens(self, pens: List[tuple[str, Pen]]) -> None:
        """
        Set the colour map to be used by the painter.
        
        pens: A List of tuples, each comprising a regular expression 
        pattern and a Pen.
        
        Example:
        painter.set_pens((
            (r'\\alpha', Pen.RED),
            (r'\\beta', Pen.GREEN),
            (r'\\gamma', Pen.BLUE)))

        The above example will set the colour of the glyphs representing the 
        Greek letters alpha, beta, gamma to red, green, blue respectively.

        The colour map is used to determine the colour of a glyph based on the 
        token that it represents.

        The colour map is a list of tuples, each having a regular expression 
        pattern and a Pen. 
        The pattern is used to match the token of a glyph, and the Pen is used 
        to determine the colour of the glyph.
        """
        self.pens = [make_pen(p[0], p[1]) for p in pens]

#endregion

    @property
    def more(self) -> bool:
        return self.token_index < len(self.tokens)

    @property
    def peek(self) -> str:
        index = self.token_index
        return self.tokens[index].string if self.more else ''

    @property
    def pen_fg(self) -> Pen:
        return self.get_token_pen('FG')
    
    @property
    def pop(self) -> str:
        token = self.peek
        self.token_index += 1
        return token
    
    def dump_symbols(self, flag: str, *lists: List[Symbol]) -> None:
        if Opt.DEBUG_SYMBOLS in self.options:
            frame = currentframe().f_back
            if flag == '<':
                print(frame.f_code.co_name, end=' ')
            print(flag, end=' ')
            for list in lists:
                if list:
                    print(*list, end=' ')
            if flag == '>':
                print()

    def dump_tex(self) -> None:
        if Opt.DEBUG_TEX in self.options:
            print(self.tex.tex_string)
            print(len(self.tokens), 'tokens:', *self.tokens)
            print(len(self.tex), 'glyphs')
            print()

    def paint_unit(self) -> List[Symbol]:

        def accept(token: str) -> None:
            if (self.peek != token):
                pass
            self.token_index += 1

        def paint_accent() -> List[Symbol]:
            g1 = paint_symbol()
            g2 = self.paint_unit() if self.more else []
            self.dump_symbols('<', g1, g2)
            start = g1[0].token_index
            end = self.token_index
            string = concat_tokens(self.tokens[start:end])
            extra = get_tex_length(string) - get_glyph_count(g1 + g2)
            g1[0].glyph_count += extra
            adjust(g2, extra)
            if Opt.ACCENT in self.options:
                g1[0].pen = g2[0].pen
            self.dump_symbols('>', g1, g2)
            return g1 + g2

        def paint_aggregate(prototype: str) -> List[Symbol]:
            g1 = paint_symbol()
            g2 = paint_shift('_')
            g3 = paint_shift('^')
            self.dump_symbols('<', g1, g2, g3)
            n1 = get_glyph_count(g1)
            n2 = get_glyph_count(g2)
            n3 = get_glyph_count(g3)
            match prototype:
                case r'\int':
                    # Expressions in the "\int" family are rendered with the 
                    # integral sign(s) first on the left, then the upper and lower 
                    # bounds (in that order) in the middle, and finally the 
                    # integrand on the right. Note that the bounds rendering order
                    # is the opposite of their occurrence order in the text,
                    # necessitating the following adjustments.
                    adjust(g2, n3)
                    adjust(g3, -n2)
                case r'\sum':
                    # Expressions in the "\sum" family are rendered with the upper
                    # bounds, summation sign, and lower bounds, stacked vertically 
                    # (in that order), followed by the summand on the right. Note
                    # that all three items in the vertical stack require adjustment 
                    # because their rendering order is completely different from 
                    # their occurrence order in the text.
                    adjust(g3, -(n1+n2))
                    adjust(g1, n3)
                    adjust(g2, n3)
                case _:
                    # All other aggregates are rendered as-is.
                    pass
            self.dump_symbols('>', g1, g2, g3)
            return g1 + g2 + g3

        def paint_frac() -> List[Symbol]:
            g1 = paint_symbol()
            g2 = self.paint_unit()
            g3 = self.paint_unit()
            self.dump_symbols('<', g1, g2, g3)
            n1 = get_glyph_count(g1)
            n2 = get_glyph_count(g2)
            adjust(g1, n2)
            adjust(g2, -n1)
            self.dump_symbols('>', g1, g2, g3)
            return g2 + g1 + g3
    
        def paint_math(token: str) -> List[Symbol]:
            extra = 4 if token.endswith('brace') else 2 if token.endswith('arrow') else 1
            flip = token not in [r'\underline', r'\underbrace']
            g1 = paint_symbol()
            g2 = self.paint_unit() if self.more else []
            self.dump_symbols('<', g1, g2)
            n1 = get_glyph_count(g1)
            n2 = get_glyph_count(g2)
            if n1 < 1:
                g1[0].glyph_index = g2[0].glyph_index + get_glyph_count(g2)
                g1[0].glyph_count = extra
                if flip:
                    n1 = get_glyph_count(g1)
                    n2 = get_glyph_count(g2)
                    adjust(g1, -n2)
                    adjust(g2, +n1)
            self.dump_symbols('>', g1, g2)
            return g1 + g2

        def paint_script():
            self.sticky = Opt.SUBSUPER in self.options
            symbols = paint_shift(token)
            self.sticky = False
            return symbols

        def paint_shift(token: str) -> List[Symbol]:
            '''
            If the current token is either '_' or '^' then return the next unit,
            otherwise return the empty list.

            token: The expected token, this will be either '_' or '^'.
            '''
            if self.peek == token:
                accept(token)
                return self.paint_unit()
            return []

        def paint_size(token: str) -> List[Symbol]:
            '''
            Paint a delimiter symbol correctly, when the symbol is preceded by a 
            static or dynamic size modifier.

            token: The size modifier, e.g. '\\left', '\\big', '\\Bigg'.
            '''

            def get_left(right: int) -> int:
                return list(filter(lambda p: p[1] == right, get_parens()))[0][0]
        
            def get_right(left: int) -> int:
                return list(filter(lambda p: p[0] == left, get_parens()))[0][1]

            def get_parens() -> Generator[Tuple[int, int], None, None]:
                lefts = []
                for index, token in enumerate(self.tokens):
                    match token.string:
                        case r'\left':
                            lefts.append(index)
                        case r'\right':
                            yield (lefts.pop(), index)

            def get_gap(left: int, right: int) -> int:
                token_L = self.tokens[left]
                token_R = self.tokens[right]
                s = self.text
                snip = s[0:token_L.start] + s[token_L.end:token_R.start] + s[token_R.end:]
                return 1 + (len(self.tex) - get_tex_length(snip)) // 2

            token_index = self.token_index
            accept(token)
            delim = self.pop
            tokens = f'{token}{delim}'
            symbol = Symbol(
                token_index=token_index,
                token_count=2,
                glyph_index=self.glyph_index,
                glyph_count=1,
                pen=self.get_token_pen(delim))
            match token:
                case r'\left': # Dynamic
                    gap = get_gap(token_index, get_right(token_index))
                case r'\right': # Dynamic
                    gap = get_gap(get_left(token_index), token_index)
                case _: # Static
                    gap = get_tex_length(tokens)
            symbol.glyph_count = gap
            self.glyph_index += gap
            return [symbol]

        def paint_sqrt() -> List[Symbol]:
            g1 = paint_symbol()
            if self.peek == '[':
                colour = g1[0].pen
                g2 = paint_string('[', ']')
                for symbol in g2:
                    symbol.pen = colour
                g1 += g2
            g3 = self.paint_unit() if self.more else []
            return g1 + g3
    
        def paint_string(begin: str = '', end: str = '') -> List[Symbol]:
            if begin:
                accept(begin)
            symbols = []
            while self.more and self.peek != end:
                symbols += self.paint_unit()
            if end:
                accept(end)
            return symbols
    
        def paint_symbol() -> List[Symbol]:
            return paint_token(self.peek)
    
        def paint_token(token: str) -> List[Symbol]:
            token_count = 1
            glyph_count = get_tex_length(token)
            if not self.sticky:
                self.pen = self.get_token_pen(token)
            symbols = [Symbol(
                token_index = self.token_index,
                token_count = token_count,
                glyph_index = self.glyph_index,
                glyph_count = glyph_count,
                pen = self.pen)]
            self.token_index += token_count
            self.glyph_index += glyph_count
            return symbols

        token = self.peek
        if re.match(PAT_INT, token):
            return paint_aggregate(prototype = r'\int')
        if re.match(PAT_LARGE, token):
            return paint_aggregate(prototype = r'\sum')
        if re.match(PAT_ACCENT, token):
            return paint_accent()
        if re.match(PAT_MATH, token):
            return paint_math(token)
        if re.match(PAT_SIZE, token):
            return paint_size(token)
        match token:
            case r'\frac':
                return paint_frac()
            case r'\sqrt':
                return paint_sqrt()
            case '{':
                result = paint_string('{', '}')
                return result
            case '_':
                return paint_script()
            case '^':
                return paint_script()
            case _:
                return paint_token(token)

if __name__ == '__main__':
    config.verbosity = "CRITICAL"
    painter = Painter()
    painter.options |= Opt.DEBUG_SYMBOLS
    #s = [r'\frac{\arcsin x_1^2}{\arccos y_3^4}']
    #s = [r'\frac{1}{2}']
    #tex = MathTex(*s)
    #painter.paint(tex)
    for s in SYM_ACCENT:
        print(get_tex_length(s), s)
