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

def get_glyph_count(symbols: List[Symbol]) -> int:
    return sum(symbol.glyph_count for symbol in symbols)

def get_tex_length(token: str) -> int:
    match token:
        case r'\frac':
            return 1
    try:
        return len(MathTex(token)[0])
    except Exception:
        return 0
        
#def _set_colour(symbols: List[Symbol], colour: ManimColor) -> None:
#    for symbol in symbols:
#        symbol.pen = colour

class Painter():

    colour_map: List[tuple[re.Pattern[str], int]] = []
    _options: Opt
    pen: Pen
    sticky: bool # Subscripted or superscripted atom reuses previous colour.
    tex: MathTex
    text: str
    tokens: List[Token] = []
    token_index: int
    glyph_index: int

    def __init__(self, options: Opt = Opt.DEFAULT):
        self.colour_map = [
            ('FG', Pen.GREY),
            ('BG', Pen.BLACK),
            #('oO|', Pen.BLACK),
            (r'[a-eA-E]|\\alpha|\\beta|\\gamma|\\delta|\\epsilon', Pen.RED),
            ('[f-h]', Pen.ORANGE),
            ('[i-n]', Pen.YELLOW),
            ('[p-s]', Pen.GREEN),
            ('[u-w]', Pen.CYAN),
            ('[x-z]', Pen.BLUE),
            (PAT_GREEK, Pen.ORANGE),
            (PAT_MATH, Pen.YELLOW),
            (PAT_DELIM, Pen.GREEN),
            (PAT_INT, Pen.MAGENTA),
            (PAT_LARGE, Pen.MAGENTA),
            (PAT_FUNC, Pen.YELLOW),
            (PAT_OPS, Pen.GREEN),
            (PAT_ARROW, Pen.BLUE),
            (PAT_MISC, Pen.CYAN),
            (PAT_ACCENT, Pen.YELLOW),
            (r'\\frac', Pen.GREEN),
            (r'\\sqrt|\\lim', Pen.ORANGE),
        ]
        self.options = options
        self.pen = Pen.GREY
        self.sticky = False
        self.tex = None
        self.text = ''
        self.tokens = []
        self.token_index = 0
        self.glyph_index = 0

    @property
    def back_colour(self) -> ManimColor:
        return self.get_pen_colour(self.back_pen)

    @property
    def fore_colour(self) -> ManimColor:
        return self.get_pen_colour(self.fore_pen)

    @property
    def options(self) -> Opt:
        return self._options
    
    @options.setter
    def options(self, value: Opt) -> None:
        self._options = value
    
    def get_pen_colour(self, pen: Pen) -> ManimColor:
        """
        Return the colour associated with the given pen.
        
        pen: The pen whose colour is to be returned.
        
        Returns: The colour associated with the given pen.
        """
        return PALETTE_BRIGHT[pen.value]
    
    def paint(self, root: Mobject) -> None:
        """
        Apply colours to the glyphs in the given Mobject tree.

        root: The root object to be painted.
        """
        self.paint_node(root)

    def paint_node(self, parent: Mobject) -> None:
        if type(parent) is SingleStringMathTex:
            self.paint_ssmt(parent)
        elif isinstance(parent, VMobject):
            for child in parent.submobjects:
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
        for match in re.finditer(PAT_TOKEN, text):
            span = match.span()
            start = span[0]
            end = span[1]
            length = end - start
            string = text[start:end]
            token = Token(start=start, length=length, string=string)
            self.tokens.append(token)
        self._token_count = len(self.tokens)
        self.token_index = 0
        self.glyph_index = 0
        if Opt.DEBUG_NOPAINT not in self.options:
            while self.more:
                self.paint_unit()

    def set_colour_map(self, colour_map: List[tuple[str, int]]) -> None:
        """
        Set the colour map to be used by the painter.
        
        colour_map: A List of tuples, each containing a regular expression 
        pattern and a pen index.
        
        Example:
        painter.set_colour_map((
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
        self.colour_map = [[re.compile(m[0]), m[1]] for m in colour_map]

    @property
    def back_pen(self) -> Pen:
        return self.get_token_pen('BG')

    @property
    def fore_pen(self) -> Pen:
        return self.get_token_pen('FG')

    @property
    def more(self) -> bool:
        return self.token_index < len(self.tokens)

    @property
    def peek(self) -> str:
        index = self.token_index
        return self.tokens[index].string if self.more else ''
    
    @property
    def pop(self) -> str:
        token = self.peek
        self.token_index += 1
        return token

    def accept(self, token: str) -> None:
        if (self.peek != token):
            pass
        self.token_index += 1
    
    def dump_symbols(self, flag: str, *lists: List[Symbol]) -> None:
        if Opt.DEBUG_SYMBOLS in self.options:
            frame = currentframe().f_back
            if flag == '<':
                print(frame.f_code.co_name, end=' ')
            print(flag, end=' ')
            for list in lists:
                print(*list, end=' ')
            if flag == '>':
                print()

    def dump_tex(self) -> None:
        if Opt.DEBUG_TEX in self.options:
            print(self.tex.tex_string)
            print(len(self.tokens), 'tokens:', *self.tokens)
            print(len(self.tex), 'glyphs')
            print()

    def get_colour(self, symbols: List[Symbol]) -> ManimColor:
        return symbols[0].pen if symbols else self._painter.get_colour(Pen.FG)

    def get_index_L(self, index_R: int) -> int:
        return list(filter(lambda p: p[1] == index_R, self.get_parens()))[0][0]

    def get_index_R(self, index_L: int) -> int:
        return list(filter(lambda p: p[0] == index_L, self.get_parens()))[0][1]

    def get_next_pen(self, pen: Pen) -> Pen:
        pen = Pen(pen.value + 1) if pen.value < 21 else Pen(0)
        return pen if pen != self.back_pen else self.get_next_pen(pen)

    def get_parens(self) -> Generator[Tuple[int, int], None, None]:
        lefts = []
        for index, token in enumerate(self.tokens):
            match token.string:
                case r'\left':
                    lefts.append(index)
                case r'\right':
                    yield (lefts.pop(), index)

    def get_token_pen(self, token: str) -> Pen:
        for map in self.colour_map:
            if (re.match(map[0], token)):
                return map[1]
        return self.fore_pen

    def _paint(self) -> None:
        symbols = self.paint_string()
        glyphs = self.tex
        pen = self.back_pen
        for symbol in symbols:
            start = symbol.glyph_index
            stop = start + symbol.glyph_count
            if stop > start:
                if Opt.DEBUG_COLOURS in self.options:
                    pen = self.get_next_pen(pen)
                else:
                    pen = symbol.pen
                colour = self.get_pen_colour(pen)
                for index in range(start, stop):
                    if index >= 0 and index < len(glyphs):
                        glyph = glyphs[index]
                        glyph.set_color(colour)
    
    def _paint_accent(self, token: str) -> List[Symbol]:
        g1 = self.paint_symbol()
        g2 = self.paint_unit() if self.more else []
        self.dump_symbols('<', g1, g2)
        start = g1[0].token_index
        end = g2[-1].token_index + g2[-1].token_count

        #n2 = len(MathTex(' '.join(self._tokens[start:end]))[0])

        if Opt.ACCENT in self.options:
            g1[0].pen = g2[0].pen
        self.dump_symbols('>', g1, g2)
        return g1 + g2
    
    def _paint_aggregate(self, prototype: str) -> List[Symbol]:
        g1 = self.paint_symbol()
        g2 = self.paint_shift('_')
        g3 = self.paint_shift('^')
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

    def paint_frac(self) -> List[Symbol]:
        g1 = self.paint_symbol()
        g2 = self.paint_unit()
        g3 = self.paint_unit()
        self.dump_symbols('<', g1, g2, g3)
        n1 = get_glyph_count(g1)
        n2 = get_glyph_count(g2)
        adjust(g1, n2)
        adjust(g2, -n1)
        self.dump_symbols('>', g1, g2, g3)
        return g2 + g1 + g3
    
    def paint_math(self, token: str) -> List[Symbol]:
        extra = 4 if token.endswith('brace') else 2 if token.endswith('arrow') else 1
        flip = token not in [r'\underline', r'\underbrace']
        g1 = self.paint_symbol()
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

    def paint_shift(self, token: str) -> List[Symbol]:
        '''
        If the current token is either '_' or '^' then return the next atom,
        otherwise return the empty list.

        token: The expected token, this will be either '_' or '^'.
        '''
        if self.peek == token:
            self.accept(token)
            return self.paint_unit()
        return []

    def paint_size(self, token: str) -> List[Symbol]:
        '''
        Paint a delimiter symbol correctly, when the symbol is preceded by a 
        static or dynamic size modifier.

        token: The size modifier, e.g. '\\left', '\\big', '\\Bigg'.
        '''

        def _get_gap(left_index: int, right_index: int) -> int:
            left = self.tokens[left_index]
            right = self.tokens[right_index]
            s = self.text
            snip = s[0:left.start] + s[left.end:right.start] + s[right.end:]
            #return 1 + (len(self.tex[0]) - len(MathTex(snip)[0])) // 2
            return 1 + (len(self.tex) - len(MathTex(snip)[0])) // 2

        token_index = self.token_index
        self.accept(token)
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
                gap = _get_gap(token_index, self.get_index_R(token_index))
            case r'\right': # Dynamic
                gap = _get_gap(self.get_index_L(token_index), token_index)
            case _: # Static
                gap = len(MathTex(tokens)[0])
        symbol.glyph_count = gap
        self.glyph_index += gap
        return [symbol]

    def paint_sqrt(self) -> List[Symbol]:
        g1 = self.paint_symbol()
        if self.peek == '[':
            colour = g1[0].pen
            g2 = self.paint_string('[', ']')
            for symbol in g2:
                symbol.pen = colour
            g1 += g2
        g3 = self.paint_unit() if self.more else []
        return g1 + g3
    
    def paint_string(self, begin: str = '', end: str = '') -> List[Symbol]:
        if begin:
            self.accept(begin)
        symbols = []
        while self.more and self.peek != end:
            symbols += self.paint_unit()
        if end:
            self.accept(end)
        return symbols
    
    def paint_symbol(self) -> List[Symbol]:
        return self.paint_token(self.peek)
    
    def paint_token(self, token: str) -> List[Symbol]:
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

    def paint_unit(self) -> List[Symbol]:

        def paint_sub_super():
            self.sticky = Opt.SUBSUPER in self.options
            symbols = self.paint_shift(token)
            self.sticky = False
            return symbols

        token = self.peek
        if re.match(PAT_INT, token):
            return self._paint_aggregate(prototype = r'\int')
        if re.match(PAT_LARGE, token):
            return self._paint_aggregate(prototype = r'\sum')
        if re.match(PAT_ACCENT, token):
            return self._paint_accent(token)
        if re.match(PAT_MATH, token):
            return self.paint_math(token)
        if re.match(PAT_SIZE, token):
            return self.paint_size(token)
        match token:
            case r'\frac':
                return self.paint_frac()
            case r'\sqrt':
                return self.paint_sqrt()
            case '{':
                result = self.paint_string('{', '}')
                return result
            case '_':
                return paint_sub_super()
            case '^':
                return paint_sub_super()
            case _:
                return self.paint_token(token)

if __name__ == '__main__':
    painter = Painter()
    painter.options |= Opt.DEBUG_SYMBOLS
    #s = [r'\frac{\arcsin x_1^2}{\arccos y_3^4}']
    s = [r'\frac{1}{2}']
    tex = MathTex(*s)
    painter.paint(tex)
