#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The Painter class is used to apply colours to the glyphs in a MathTex object.
The colours are determined by a colour map which is a list of tuples, each 
containing a regular expression pattern and a pen index. The pattern is used 
to match the token of a glyph and the pen index is used to determine the 
colour of the glyph. The pen index is an integer that corresponds to an index 
in the colours list. The Painter class is used to apply 
colours to the glyphs in a MathTex object.
"""

from latex_rice import *
from manim import *
from options import Opt
from pens import *
import re
from symbol import Symbol

class Painter():
    
    @property
    def background_colour(self) -> ManimColor:
        return self.get_colour(self.background_pen)

    @property
    def background_pen(self) -> Pen:
        return Pen.BLACK

    @property
    def foreground_pen(self) -> Pen:
        return Pen.WHITE

    def get_colour(self, pen: Pen) -> ManimColor:
        """
        Return the colour associated with the given pen.
        
        pen: The pen whose colour is to be returned.
        
        Returns: The colour associated with the given pen.
        """
        return PALETTE_DEFAULT[pen.value]
        
    def paint_tex(self, tex: MathTex, options: Opt) -> None:
        """
        Apply colours to the glyphs in the given MathTex object.

        tex: The MathTex object to be painted.
        """
        PAT_TOKEN = r"\\{|\\}|\\\||\\[A-Za-z]+|\\\\|\\\,|[^&\s]"
        self._tex = tex
        text = tex.tex_string
        if not text:
            return
        self._tokens = re.findall(PAT_TOKEN, text)
        self._token_index = 0
        self._glyph_index = 0
        glyphs = tex[0]
        self._glyph_count = len(glyphs)
        symbols = self._paint_string()
        pen = Pen.BLACK
        for symbol in symbols:
            start = symbol.glyph_index
            stop = start + symbol.glyph_count
            if stop > start:
                if Opt.DEBUG not in options:
                    pen = symbol.pen
                colour = self.get_colour(pen)
                pen = pen.BLACK if pen == Pen.WHITE else Pen(pen.value + 1)
                for index in range(start, stop):
                    glyph = glyphs[index]
                    glyph.set_color(colour)

    def set_colour_map(self, colour_map: List[tuple[str, int]]) -> None:
        """
        Set the colour map to be used by the painter.
        
        colour_map: A List of tuples, each containing a regular expression pattern and a pen index.
        
        Example:
        painter.set_colour_map((
            (r'\\alpha', Pen.RED),
            (r'\\beta', Pen.GREEN),
            (r'\\gamma', Pen.BLUE)))

        The above example will set the colour of the glyphs representing the Greek letters alpha, beta and gamma to red, green and blue respectively.   

        The colour map is used to determine the colour of a glyph based on the token that it represents.

        The colour map is a list of tuples, each containing a regular expression pattern and a pen index. 
        The pattern is used to match the token of a glyph and the pen index is used to determine the colour of the glyph. 
        The pen index is an integer that corresponds to an index in the colour list.
        """
        self._colour_map = [[re.compile(m[0]), m[1]] for m in colour_map]

#region Private Implementation

    def __init__(self):
        self._colour_map = [
            #('oO|', Pen.NONE),
            (r'[a-eA-E]|\\alpha|\\beta|\\gamma|\\delta|\\epsilon', Pen.RED),
            ('fgh', Pen.ORANGE),
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
        self._tex = None
        self._tokens = []
        self._token_index = 0
        self._glyph_index = 0
        self._glyph_count = 0

    _colour_map: List[tuple[re.Pattern[str], int]] = []

    _tex: MathTex
    _tokens: List[str] = []
    _token_index: int
    _glyph_index: int
    _glyph_count: int

    @property
    def _more(self) -> bool:
        return self._token_index < len(self._tokens)

    @property
    def _peek(self) -> str:
        index = self._token_index
        return self._tokens[index] if self._more else ''

    def _accept(self, token: str) -> None:
        if (self._peek != token):
            pass
        self._token_index += 1
    
    @staticmethod
    def _adjust(symbols: List[Symbol], delta: int) -> None:
        for symbol in symbols:
            symbol.glyph_index += delta

    def _get_colour(self, symbols: List[Symbol]) -> ManimColor:
        return symbols[0].pen if symbols else self._painter.get_colour(Pen.FG)

    @staticmethod
    def _get_glyph_count(symbols: List[Symbol]) -> int:
        return sum(symbol.glyph_count for symbol in symbols)

    @staticmethod
    def _get_tex_length(token: str) -> int:
        match token:
            case r'\frac':
                return 1
        try:
            return len(MathTex(token)[0])
        except Exception:
            return 0

    def _get_token_pen(self, token: str) -> Pen:
        for map in self._colour_map:
            if (re.match(map[0], token)):
                return map[1]
        return self.foreground_pen
    
    def _paint_aggregate(self, prototype: str) -> List[Symbol]:
        g1 = self._paint_symbol()
        g2 = self._paint_shift('_')
        g3 = self._paint_shift('^')
        n1 = self._get_glyph_count(g1)
        n2 = self._get_glyph_count(g2)
        n3 = self._get_glyph_count(g3)
        match prototype:
            case r'\int':
                # Expressions in the "\int" family are rendered with the 
                # integral sign(s) first on the left, then the upper and lower 
                # bounds (in that order) in the middle, and finally the 
                # integrand on the right. Note that the bounds rendering order
                # is the opposite of their occurrence order in the text,
                # necessitating the following adjustments.
                self._adjust(g2, n3)
                self._adjust(g3, -n2)
            case r'\sum':
                # Expressions in the "\sum" family are rendered with the upper
                # bounds, summation sign, and lower bounds, stacked vertically 
                # (in that order), followed by the summand on the right. Note
                # that all three items in the vertical stack require adjustment 
                # because their rendering order is completely different from 
                # their occurrence order in the text.
                self._adjust(g3, -(n1+n2))
                self._adjust(g1, n3)
                self._adjust(g2, n3)
            case _:
                # All other aggregates are rendered as-is.
                pass
        return g1 + g2 + g3

    def _paint_atom(self) -> List[Symbol]:
        token = self._peek
        if re.match(PAT_INT, token):
            return self._paint_aggregate(prototype = r'\int')
        if re.match(PAT_LARGE, token):
            return self._paint_aggregate(prototype = r'\sum')
        if re.match(PAT_MOD, token):
            return self._paint_group(token)
        match token:
            case r'\frac':
                return self._paint_frac()
            case r'\sqrt':
                return self._paint_sqrt()
            case '{':
                result = self._paint_string('{', '}')
                return result
            case '_':
                return self._paint_shift(token)
            case '^':
                return self._paint_shift(token)
            case _:
                return self._paint_token(token)

    def _paint_frac(self) -> List[Symbol]:
        g1 = self._paint_symbol()
        g2 = self._paint_atom()
        g3 = self._paint_atom()
        n1 = self._get_glyph_count(g1)
        n2 = self._get_glyph_count(g2)
        self._adjust(g1, n2)
        self._adjust(g2, -n1)
        return g2 + g1 + g3
    
    def _paint_group(self, token: str) -> List[Symbol]:
        extra = 4 if token.endswith('brace') else 2 if token.endswith('arrow') else 1
        flip = token not in [r'\underline', r'\underbrace']
        g1 = self._paint_symbol()
        g2 = self._paint_atom() if self._more else []
        n1 = self._get_glyph_count(g1)
        n2 = self._get_glyph_count(g2)
        if n1 < 1:
            g1[0].glyph_index = g2[0].glyph_index + self._get_glyph_count(g2)
            g1[0].glyph_count = extra
            if flip:
                n1 = self._get_glyph_count(g1)
                n2 = self._get_glyph_count(g2)
                self._adjust(g1, -n2)
                self._adjust(g2, +n1)
        return g1 + g2

    def _paint_shift(self, token: str) -> List[Symbol]:
        '''
        If the current token is either '_' or '^' then return the following atom,
        otherwise return the empty list.

        str: The expected token, '_' or '^'.
        '''
        if self._peek == token:
            self._accept(token)
            return self._paint_atom()
        return []

    def _paint_sqrt(self) -> List[Symbol]:
        g1 = self._paint_symbol()
        if self._peek == '[':
            colour = g1[0].pen
            g2 = self._paint_string('[', ']')
            for symbol in g2:
                symbol.pen = colour
            g1 += g2
        g3 = self._paint_atom() if self._more else []
        return g1 + g3
    
    def _paint_string(self, begin: str = '', end: str = '') -> List[Symbol]:
        if begin:
            self._accept(begin)
        symbols = []
        while self._more and self._peek != end:
            symbols += self._paint_atom()
        if end:
            self._accept(end)
        return symbols
    
    def _paint_symbol(self) -> List[Symbol]:
        return self._paint_token(self._peek)
    
    def _paint_token(self, token: str) -> List[Symbol]:
        token_count = 1
        glyph_count = self._get_tex_length(token)
        pen = self._get_token_pen(token)
        symbols = [Symbol(
            token_index = self._token_index,
            token_count = token_count,
            glyph_index = self._glyph_index,
            glyph_count = glyph_count,
            pen = pen,
            tokens = token)]
        self._token_index += token_count
        self._glyph_index += glyph_count
        return symbols

    @staticmethod
    def _set_colour(symbols: List[Symbol], colour: ManimColor) -> None:
        for symbol in symbols:
            symbol.pen = colour
            
#endregion
