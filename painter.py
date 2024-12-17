from latex_rice import *
from manim import *
from palette import *
import re
from symbol import Symbol

PAT_TOKEN = r"\\{|\\}|\\\||\\[A-Za-z]+|\\\\|[^&\s]"

class Painter():

    def __init__(self, palette: Palette):
        self._palette = palette

    _palette: Palette
    _glyph_index: int
    _token_index: int
    _tex: MathTex
    _tokens: List[str]

    def paint(self, tex: MathTex) -> None:
        self._glyph_index = 0
        self._token_index = 0
        self._tex = tex
        self._tokens = re.findall(PAT_TOKEN, tex.tex_string)
        symbols = self._parse_string()
        for symbol in symbols:
            start = symbol.glyph_index
            stop = start + symbol.glyph_count
            colour = symbol.colour
            for index in range(start, stop):
                glyph = tex[0][index]
                glyph.set_color(colour)
                print(index, colour)

    def set_colour_map(self, colour_map: tuple[tuple[str, int]]):
        self._palette.set_colour_map = [[re.compile(m[0]), m[1]] for m in colour_map]

    def get_colour(self, index: int) -> ManimColor:
        return self._palette.get_colour(index)

    @property
    def _more(self) -> bool:
        return self._token_index < len(self._tokens)

    @property
    def _peek(self) -> str:
        return self._tokens[self._token_index]

    def _accept(self, token: str) -> None:
        if (self._peek != token):
            pass
        self._token_index += 1
    
    def _adjust(self, symbols: List[Symbol], delta: int) -> None:
        for symbol in symbols:
            symbol.glyph_index += delta

    def _get_glyph_count(self, symbols: List[Symbol]) -> int:
        return sum(symbol.glyph_count for symbol in symbols)

    def _get_tex_len(self, token: str) -> int:
        try:
            tex = MathTex(token)
        except Exception:
            return 0
        return len(tex[0])

    def _parse_atom(self) -> List[Symbol]:
        token = self._peek
        if re.match(PAT_LARGE, token):
            return self._parse_large()
        match token:
            case r'\frac':
                return self._parse_frac()
            case r'\sqrt':
                return self._parse_sqrt()
            case '{':
                result = self._parse_string('{', '}')
                return result
            case '_':
                return self._parse_shift(token)
            case '^':
                return self._parse_shift(token)
            case _:
                return self._parse_token(token)

    def _parse_frac(self) -> List[Symbol]:
        middle = self._parse_symbol()
        top = self._parse_atom()
        bottom = self._parse_atom()
        top_len = self._get_glyph_count(top)
        mid_len = self._get_glyph_count(middle)
        self._adjust(top, -mid_len)
        self._adjust(middle, top_len)
        return top + middle + bottom

    def _parse_large(self) -> List[Symbol]:
        middle = self._parse_symbol()
        bottom = self._parse_shift('_')
        top = self._parse_shift('^')
        top_len = self._get_glyph_count(top)
        mb_len = self._get_glyph_count(middle) + self._get_glyph_count(bottom)
        self._adjust(top, -mb_len)
        self._adjust(middle, top_len)
        self._adjust(bottom, top_len)
        return top + middle + bottom

    def _parse_shift(self, token: str) -> List[Symbol]:
        '''
        If the current token is either '_' or '^' then return the following atom,
        otherwise return the empty list.

        str: The expected token, '_' or '^'.
        '''
        if self._peek == token:
            self._accept(token)
            return self._parse_atom()
        return []

    def _parse_sqrt(self):
        outer = self._parse_symbol()
        if self._peek == '[':
            outer += self._parse_string('[', ']')
        inner = self._parse_atom()
        return outer + inner
    
    def _parse_string(self, begin: str = '', end: str = '') -> List[Symbol]:
        if begin:
            self._accept(begin)
        symbols = []
        while self._more and self._peek != end:
            symbols += self._parse_atom()
        if end:
            self._accept(end)
        return symbols
    
    def _parse_symbol(self):
        return self._parse_token(self._peek)
    
    def _parse_token(self, token: str) -> List[Symbol]:
        glyph_count = self._get_tex_len(token)
        result = [Symbol(
            token_index = self._token_index,
            glyph_index = self._glyph_index,
            glyph_count = glyph_count,
            colour = self._palette.get_token_colour(token))]
        self._token_index += 1
        self._glyph_index += glyph_count
        return result
    
if __name__ == '__main__':
    painter = Palette()
    parser = Painter(painter)
    parser.paint(MathTex(r'\prod_{i=\sin{0}}^{\cos{x^2}+1}{i^2}'))
