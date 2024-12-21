from manim import ManimColor
from typing import List

class Symbol():

    token_index: int
    glyph_index: int
    glyph_count: int
    colour_index: ManimColor
    tokens: str

    def __init__(
            self,
            token_index: int,
            token_count: int,
            glyph_index: int,
            glyph_count: int,
            colour_index: ManimColor,
            tokens: str) -> None:
        self.token_index = token_index
        self.token_count = token_count
        self.glyph_index = glyph_index
        self.glyph_count = glyph_count
        self.colour_index = colour_index
        self.tokens = tokens

    @property
    def glyph_range(self) -> str:
        return self._make_range('G', self.glyph_index, self.glyph_count)

    @property
    def token_range(self) -> str:
        return self._make_range('T', self.token_index, self.token_count)
    
    def _make_range(self, prefix: str, index: int, count: int) -> str:
        match count:
            case 0:
                return f'{prefix}x'
            case 1:
                return f'{prefix}{index}'
        return f'{prefix}{index}-{index + count - 1}'

    def __str__(self) -> str:
        return f'({self.token_range} {self.glyph_range} {self.colour_index} {self.tokens})'
