from manim import *
import re

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

class Painter():
    """
    A class used to apply colours to the glyphs of a MathTex.
    """

    _GHOST = [0,0,0,0] # transparent

    _colours = (
        (_GHOST, GREY, BLACK, LIGHT_GREY, BLACK, DARK_BROWN, RED, ORANGE, YELLOW, GREEN, PURE_BLUE, TEAL, PINK, PURPLE, GREY, WHITE),
        (_GHOST, 0xB2B2B2, BLACK, DARK_GREY, BLACK, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, 0x5FBFFF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, WHITE),
        (_GHOST, 0xBBBBBB, BLACK, DARK_GREY, BLACK, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, WHITE),
        (_GHOST, BLACK, WHITE, GREY, *[BLACK for _ in range(12)]),
        (_GHOST, WHITE, BLACK, GREY, *[WHITE for _ in range(12)]))

    _colour: ManimColor
    _colour_map: tuple[tuple[re.Pattern[str], int]] = []
    _index: int = 0
    _scheme: int = scheme_bright
    _tex: MathTex = None
    _token: str
    _tokens: List[str] = []

    _sticky: int = 0
    """
    Controls retention of the current colour.
    0: no retention,
    1: retain for the next single token,
    2: retain for the following {block}.
    """

    def __init__(
            self,
            scheme: int = scheme_bright,
            colour_map: tuple[tuple[str, int]] = ()):
        """
        Sets the colour palette and character mapping scheme to be applied during paint operations.

        Parameters:
            scheme (int): The index to the palette used.
            colour_map(tuple[tuple[str, int]]): The map specifying which colour is to be applied to each glyph.
        """
        self._scheme = scheme;
        if colour_map is not None:
            self._colour_map = colour_map

    def get_colour(self, colour_index: int) -> ManimColor:
        return self._colours[self._scheme][colour_index]

    def paint(self, tex: MathTex) -> None:

        def get_glyph_count() -> int:
            print(self._token)
            try:
                g = MathTex(self._token)
                return len(g[0])
            except ValueError:
                return -1

        def get_token_colour() -> ManimColor:
            colours = self._colours[self._scheme]
            for map in self._colour_map:
                if (re.match(map[0], self._token)):
                    return colours[map[1]]
            return colours[figure]

        def paint_expression() -> None:
            while self._tokens:
                #self._token = pop()
                pop()
                if self._token == r'\\': # 2 backslashes = line continuation
                    continue
                match self._token[0]:
                    case '{':
                        paint_expression()
                    case '}':
                        self._sticky = 0
                        break
                    case '\\':
                        paint_glyph()
                    case '_' | '^':
                        self._sticky = 2 if peek() == '{' else 1
                    case _:
                        paint_glyph()

           
        def paint_glyph() -> None:
            if self._sticky == 0:
                self._colour = get_token_colour()
            size = get_glyph_count()

            if size < 0:
                return

            for _ in range(size):
                glyph = self._tex[0][self._index]
                glyph.set_color(self._colour)
                self._index += 1
            if self._sticky == 1:
                self._sticky = 0

        def peek() -> str:
            return self._tokens[0]

        def pop() -> None:
            self._token = peek()
            self._tokens.pop(0)
            #return self._token

        # A backslash followed by word character(s) is a single token.
        # Two consecutive backslashes make a null token (whitespace).
        # Otherwise, a token is just any single character, excluding
        # ampersands & whitespace.
        #self._tokens = re.findall(r"\\\w+|\\\\|[^&\s]", tex.tex_string)
        self._tokens = re.findall(r"\\{|\\}|\\\||\\[A-Za-z]+|\\\\|[^&\s]", tex.tex_string)

        tex.set_color(self.get_colour(figure))
        self._tex = tex
        self._index = 0
        paint_expression()

    def set_colour_map(self, colour_map: tuple[tuple[str, int]]) -> tuple[tuple[re.Pattern[str], int]]:
        self._colour_map = [[re.compile(m[0]), m[1]] for m in colour_map]
