from latex_rice import *
from manim import *
import re
from pens import Pen, Scheme
from symbol import Symbol

PAT_TOKEN = r"\\{|\\}|\\\||\\[A-Za-z]+|\\\\|\\\,|[^&\s]"

class Painter():

    _GHOST = [0,0,0,0] # transparent

    _colours = (
        (_GHOST, GREY, BLACK, LIGHT_GREY, BLACK, DARK_BROWN, RED, ORANGE, YELLOW, GREEN, PURE_BLUE, TEAL, PINK, PURPLE, GREY, WHITE),
        (_GHOST, 0xB2B2B2, BLACK, DARK_GREY, BLACK, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, 0x5FBFFF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, WHITE),
        (_GHOST, 0xBBBBBB, BLACK, DARK_GREY, BLACK, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, WHITE),
        (_GHOST, BLACK, WHITE, GREY, *[BLACK for _ in range(12)]),
        (_GHOST, WHITE, BLACK, GREY, *[WHITE for _ in range(12)]))

    _colour: ManimColor
    _colour_map: tuple[tuple[re.Pattern[str], int]] = []
    _scheme: Scheme = Scheme.BRIGHT

    _tex: MathTex
    _tokens: List[str]
    _token_index: int
    _glyph_index: int
    _glyph_count: int

    def get_colour(self, pen: Pen) -> ManimColor:
        return self._colours[self._scheme.value][pen.value]

    def paint_tex(self, tex: MathTex) -> None:
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
        for symbol in symbols:
            start = symbol.glyph_index
            stop = start + symbol.glyph_count
            colour = self.get_colour(symbol.pen)
            for index in range(start, stop):
                glyph = glyphs[index]
                glyph.set_color(colour)
        expected = self._glyph_count
        actual = self._get_glyph_count(symbols)
        ok = actual == expected
        if ok and len(symbols) == 1:
            return
        error = '' if ok else f'** Expected: {expected}. Actual: {actual}. **'
        print(f'({self._glyph_count}) {text} =>', *[symbol for symbol in symbols], error)

    def set_colour_map(self, colour_map: tuple[tuple[str, int]]):
        self._colour_map = [[re.compile(m[0]), m[1]] for m in colour_map]

    def set_scheme(self, scheme: int):
        self._scheme = scheme

#region Private Implementation

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
    
    def _adjust(self, symbols: List[Symbol], delta: int) -> None:
        for symbol in symbols:
            symbol.glyph_index += delta

    def _get_colour(self, symbols: List[Symbol]) -> ManimColor:
        return symbols[0].pen if symbols else self._painter.get_colour(Pen.FG)

    @staticmethod
    def _get_glyph_count(symbols: List[Symbol]) -> int:
        return sum(symbol.glyph_count for symbol in symbols)

    @staticmethod
    def _get_tex_len(token: str) -> int:
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
        return Pen.FG
    
    def _paint_accent(self) -> List[Symbol]:
        g1 = self._paint_symbol()
        g2 = self._paint_atom()
        #self._dump(g1)
        #self._dump(g2)
        self._set_colour(g1, self._get_colour(g2))
        return g1 + g2

    def _paint_atom(self) -> List[Symbol]:
        token = self._peek
        if re.match(PAT_INT, token):
            return self._paint_aggregate(prototype = r'\int')
        if re.match(PAT_LARGE, token):
            return self._paint_aggregate(prototype = r'\sum')
        if re.match(PAT_ACCENT, token):
            return self._paint_accent()
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
        self._adjust(g2, -n1)
        self._adjust(g1, n2)
        return g2 + g1 + g3
    
    def _paint_aggregate(self, prototype: str) -> List[Symbol]:
        g1 = self._paint_symbol()
        g2 = self._paint_shift('_')
        g3 = self._paint_shift('^')
        n1 = self._get_glyph_count(g1)
        n2 = self._get_glyph_count(g2)
        n3 = self._get_glyph_count(g3)
        match prototype:
            case r'\int':
                self._adjust(g2, n3)
                self._adjust(g3, -n2)
            case r'\sum':
                self._adjust(g3, -(n1+n2))
                self._adjust(g1, n3)
                self._adjust(g2, n3)
        return g1 + g2 + g3

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

    def _paint_sqrt(self):
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
    
    def _paint_symbol(self):
        return self._paint_token(self._peek)
    
    def _paint_token(self, token: str) -> List[Symbol]:
        token_count = 1
        glyph_count = self._get_tex_len(token)
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

    def _set_colour(self, symbols: List[Symbol], colour: ManimColor) -> None:
        for symbol in symbols:
            symbol.pen = colour
            
#endregion
