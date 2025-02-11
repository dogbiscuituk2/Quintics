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
            
def concat(token_list: List[Token]) -> str:
    return ' '.join([token.string for token in token_list])

def get_glyph_count(symbols: List[Symbol]) -> int:
    return sum(symbol.glyph_count for symbol in symbols)

def get_tex_length(string: str) -> int:
    match string:
        case r'\frac':
            return 1
    try:
        return len(SingleStringMathTex(string))
    except Exception:
        return 0

class Painter():

    opt: Opt = Opt.DEFAULT
    palette: List[ManimColor] = PALETTE_SASHA
    pen: Pen = Pen.BACKGROUND
    pens: List[tuple[re.Pattern[str], Pen]] = []
    sticky: bool = False # Subscripted or superscripted unit reuses previous colour.

    glyph_index: int = 0
    token_index: int = 0

    @property
    def ink_bg(self) -> ManimColor:
        return config.background_color

    @property
    def ink_fg(self) -> ManimColor:
        return self.get_ink(self.get_pen('FG'))

    @property
    def options(self) -> Opt:
        return self.opt
    
    @options.setter
    def options(self, value: Opt) -> None:
        self.opt = value
    
    def get_ink(self, pen: Pen) -> ManimColor:
        return self.palette[pen.value] if pen.value >= 0 else self.ink_bg

    def get_pen(self, token: str) -> Pen:
        for map in self.pens:
            if (re.match(map[0], token)):
                return map[1]
        return Pen.GREY
    
    def paint(self, root: Mobject) -> None:
        """
        Apply colours to the glyphs in the given Mobject tree.

        root: The root object to be painted.
        """

        def paint_node(node: Mobject) -> None:

            def paint_ssmt(tex: SingleStringMathTex) -> None:
                """
                Apply colours to the glyphs in the given SingleStringMathTex object.

                tex: The SingleStringMathTex object to be painted.

                '\\left.', '\\right.' not implemented.
                """

                def more() -> bool:
                    return self.token_index < len(tokens)

                def paint_unit() -> List[Symbol]:

                    def accept(token: str) -> None:
                        if (peek() != token):
                            pass
                        self.token_index += 1
                    
                    def peek() -> str:
                        index = self.token_index
                        return tokens[index].string if more() else ''
                    
                    def pop() -> str:
                        token = peek()
                        self.token_index += 1
                        return token

                    def dump_symbols(flag: str, *lists: List[Symbol]) -> None:
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

                    def paint_accent() -> List[Symbol]:
                        g1 = paint_symbol()
                        g2 = paint_unit() if more() else []
                        dump_symbols('<', g1, g2)
                        start = g1[0].token_index
                        end = self.token_index
                        string = concat(tokens[start:end])
                        extra = get_tex_length(string) - get_glyph_count(g1 + g2)
                        g1[0].glyph_count += extra
                        adjust(g2, extra)
                        if Opt.ACCENT in self.options:
                            g1[0].pen = g2[0].pen
                        dump_symbols('>', g1, g2)
                        return g1 + g2

                    def paint_aggregate(prototype: str) -> List[Symbol]:
                        g1 = paint_symbol()
                        g2 = paint_shift('_')
                        g3 = paint_shift('^')
                        dump_symbols('<', g1, g2, g3)
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
                        dump_symbols('>', g1, g2, g3)
                        return g1 + g2 + g3

                    def paint_frac() -> List[Symbol]:
                        g1 = paint_symbol()
                        g2 = paint_unit()
                        g3 = paint_unit()
                        dump_symbols('<', g1, g2, g3)
                        n1 = get_glyph_count(g1)
                        n2 = get_glyph_count(g2)
                        adjust(g1, n2)
                        adjust(g2, -n1)
                        dump_symbols('>', g1, g2, g3)
                        return g2 + g1 + g3
                
                    def paint_math(token: str) -> List[Symbol]:
                        extra = 4 if token.endswith('brace') else 2 if token.endswith('arrow') else 1
                        flip = token not in [r'\underline', r'\underbrace']
                        g1 = paint_symbol()
                        g2 = paint_unit() if more() else []
                        dump_symbols('<', g1, g2)
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
                        dump_symbols('>', g1, g2)
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
                        if peek() == token:
                            accept(token)
                            return paint_unit()
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
                            for index, token in enumerate(tokens):
                                match token.string:
                                    case r'\left':
                                        lefts.append(index)
                                    case r'\right':
                                        yield (lefts.pop(), index)

                        def get_gap(left: int, right: int) -> int:
                            token_L = tokens[left]
                            token_R = tokens[right]
                            snip = text[0:token_L.start] + text[token_L.end:token_R.start] + text[token_R.end:]
                            return 1 + (len(tex) - get_tex_length(snip)) // 2

                        token_index = self.token_index
                        accept(token)
                        delim = pop()
                        bracket = f'{token}{delim}'
                        symbol = Symbol(
                            token_index=token_index,
                            token_count=2,
                            glyph_index=self.glyph_index,
                            glyph_count=1,
                            pen=self.get_pen(delim))
                        match token:
                            case r'\left': # Dynamic
                                gap = get_gap(token_index, get_right(token_index))
                            case r'\right': # Dynamic
                                gap = get_gap(get_left(token_index), token_index)
                            case _: # Static
                                gap = get_tex_length(bracket)
                        symbol.glyph_count = gap
                        self.glyph_index += gap
                        return [symbol]

                    def paint_sqrt() -> List[Symbol]:
                        g1 = paint_symbol()
                        if peek() == '[':
                            colour = g1[0].pen
                            g2 = paint_string('[', ']')
                            for symbol in g2:
                                symbol.pen = colour
                            g1 += g2
                        g3 = paint_unit() if more() else []
                        return g1 + g3
                
                    def paint_string(begin: str = '', end: str = '') -> List[Symbol]:
                        if begin:
                            accept(begin)
                        symbols = []
                        while more() and peek() != end:
                            symbols += paint_unit()
                        if end:
                            accept(end)
                        return symbols
                
                    def paint_symbol() -> List[Symbol]:
                        return paint_token(peek())
                
                    def paint_token(token: str) -> List[Symbol]:
                        token_count = 1
                        glyph_count = get_tex_length(token)
                        if not self.sticky:
                            self.pen = self.get_pen(token)
                        symbols = [Symbol(
                            token_index = self.token_index,
                            token_count = token_count,
                            glyph_index = self.glyph_index,
                            glyph_count = glyph_count,
                            pen = self.pen)]
                        self.token_index += token_count
                        self.glyph_index += glyph_count
                        return symbols

                    token = peek()
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

                tokens: List[Token] = []

                text: str = tex.tex_string
                if not text:
                    return
                tokens.clear()
                for match in re.finditer(PAT_TOKEN, text):
                    span = match.span()
                    start = span[0]
                    end = span[1]
                    length = end - start
                    string = text[start:end]
                    token = Token(start=start, length=length, string=string)
                    tokens.append(token)
                self.token_index = 0
                self.glyph_index = 0
                if Opt.DEBUG_NOPAINT in self.options:
                    return
                while more():
                    symbols = paint_unit()
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
                                if index >= 0 and index < len(tex):
                                    glyph = tex[index]
                                    glyph.set_color(colour)

            if type(node) is SingleStringMathTex:
                paint_ssmt(node)
            elif isinstance(node, VMobject):
                for child in node.submobjects:
                    paint_node(child)

        paint_node(root)

    def set_inks(self, inks: List[ManimColor]) -> None:
        """
        Set the palette of colours to be used by the painter.
        
        palette: A list of colours to be used by the painter.
        """
        self.palette = inks

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
        """
        self.pens = [(re.compile(p[0]), p[1]) for p in pens]

if __name__ == '__main__':
    config.verbosity = "CRITICAL"
    painter = Painter()
    painter.options |= Opt.DEBUG_SYMBOLS
