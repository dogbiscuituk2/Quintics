from latex_rice import *
from manim import *
import re
from symbol import Symbol

ghost   = 0 # Transparent
figure  = 1 # Foreground default
ground  = 2 # Background
hilite  = 3 # Highlight background
black   = 4 # These remaining colour names are all purely logical
brown   = 5
red     = 6
orange  = 7
yellow  = 8
green   = 9
blue    = 10
cyan    = 11
magenta = 12
violet  = 13
grey    = 14
white   = 15

scheme_default          = 0
scheme_bright           = 1
scheme_pastel           = 2
scheme_black_on_white   = 3
scheme_white_on_black   = 4

TRANSPARENT = ManimColor([0,0,0,0])

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
    _scheme: int = scheme_bright

    _glyph_index: int
    _token_index: int
    _tex: MathTex
    _tokens: List[str]

    def get_colour(self, index: int):
        return self._colours[self._scheme][index]

    def paint(self, tex: MathTex) -> None:
        self._glyph_index = 0
        self._token_index = 0
        self._tex = tex
        self._tokens = re.findall(PAT_TOKEN, tex.tex_string)
        symbols = self._paint_string()
        for symbol in symbols:
            start = symbol.glyph_index
            stop = start + symbol.glyph_count
            colour_index = symbol.colour_index
            for index in range(start, stop):
                glyph = tex[0][index]
                glyph.set_color(self.get_colour(colour_index))

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
        return symbols[0].colour_index if symbols else self._painter.get_colour(figure)


    def _get_glyph_count(self, symbols: List[Symbol]) -> int:
        return sum(symbol.glyph_count for symbol in symbols)

    def _get_tex_len(self, token: str) -> int:
        match token:
            case r'\frac':
                return 1
        try:
            return len(MathTex(token)[0])
        except Exception:
            return 0

    def _get_token_colour_index(self, token: str) -> int:
        #colours = self._colours[self._scheme]
        for map in self._colour_map:
            if (re.match(map[0], token)):
                return map[1]
        return figure

    def _paint_accent(self) -> List[Symbol]:

        def dump(s: List[Symbol]):
            print(*[t for t in s])

        g1 = self._paint_symbol()
        g2 = self._paint_atom()
        dump(g1)
        dump(g2)
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
            colour = g1[0].colour_index
            g2 = self._paint_string('[', ']')
            for symbol in g2:
                symbol.colour_index = colour
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
        colour_index = self._get_token_colour_index(token)
        symbols = [Symbol(
            token_index = self._token_index,
            token_count = token_count,
            glyph_index = self._glyph_index,
            glyph_count = glyph_count,
            colour_index = colour_index,
            tokens = token)]
        self._token_index += token_count
        self._glyph_index += glyph_count
        return symbols

    def _set_colour(self, symbols: List[Symbol], colour: ManimColor) -> None:
        for symbol in symbols:
            symbol.colour_index = colour
            
#endregion
