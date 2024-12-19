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

    def set_colour_map(self, colour_map: tuple[tuple[str, int]]):
        self._colour_map = [[re.compile(m[0]), m[1]] for m in colour_map]

    def set_scheme(self, scheme: int):
        self._scheme = scheme

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
        colour = self.get_token_colour(token)
        result = [Symbol(
            token_index = self._token_index,
            glyph_index = self._glyph_index,
            glyph_count = glyph_count,
            colour = colour)]
        self._token_index += 1
        self._glyph_index += glyph_count
        return result

    def get_colour(self, index: int):
        return self._colours[self._scheme][index]

    def get_token_colour(self, token: str):
        colours = self._colours[self._scheme]
        for map in self._colour_map:
            if (re.match(map[0], token)):
                return colours[map[1]]
        return colours[figure]

    def set_colour_map(self, colour_map: tuple[tuple[str, int]]):
        #self._colour_map = [[re.compile(m[0]), m[1]] for m in colour_map]
        self._colour_map = colour_map
        pass
