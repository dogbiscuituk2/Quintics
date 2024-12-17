from manim import ManimColor

class Symbol():

    token_index: int
    glyph_index: int
    glyph_count: int
    colour: ManimColor

    def __init__(
            self,
            token_index: int,
            glyph_index: int,
            glyph_count: int,
            colour: ManimColor):
        self.token_index = token_index
        self.glyph_index = glyph_index
        self.glyph_count = glyph_count
        self.colour = colour

    def __str__(self) -> str:
        return f'[{self.token_index},{self.glyph_index},{self.glyph_count},{self.colour}]'
