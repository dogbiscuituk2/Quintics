#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Output data class for the parsing of MathTex objects.

The Symbol class is used to store the output data from the parsing of MathTex 
objects. The data includes the token and glyph indices and counts, the pen 
index and the tokens.

The token index is the index of the first token in the symbol.
The token count is the number of tokens in the symbol.
The glyph index is the index of the first glyph in the symbol.
The glyph count is the number of glyphs in the symbol.
The pen is the pen index used to colour the symbol.
The tokens are the tokens in the symbol.
"""

from pens import Pen

class Symbol():

    token_index: int
    token_count: int
    glyph_index: int
    glyph_count: int
    pen: Pen

    def __init__(
            self,
            token_index: int,
            token_count: int,
            glyph_index: int,
            glyph_count: int,
            pen: Pen) -> None:
        self.token_index = token_index
        self.token_count = token_count
        self.glyph_index = glyph_index
        self.glyph_count = glyph_count
        self.pen = pen

    def __str__(self) -> str:
        return f'{self._token_range}.{self._glyph_range}.{self.pen.name}'

    @property
    def _glyph_range(self) -> str:
        return self._make_range('G', self.glyph_index, self.glyph_count)

    @property
    def _token_range(self) -> str:
        return self._make_range('T', self.token_index, self.token_count)
    
    @staticmethod
    def _make_range(prefix: str, index: int, count: int) -> str:
        match count:
            case 0:
                return f'{prefix}x'
            case 1:
                return f'{prefix}{index}'
        return f'{prefix}{index}-{index + count - 1}'
