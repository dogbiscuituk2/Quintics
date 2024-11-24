from manim import *
import re

ghost   = 0 # Transparent.
ground  = 1 # Background.
black   = 2 # All other colour names including black & white are purely logical & palette dependent.
brown   = 3
red     = 4
orange  = 5
yellow  = 6
green   = 7
blue    = 8
cyan    = 9
magenta = 10
violet  = 11
grey    = 12
white   = 13

scheme_default          = 0
scheme_bright           = 1
scheme_pastel           = 2
scheme_black_on_white   = 3
scheme_white_on_black   = 4

class Painter():
    """
    A class used to apply colours to the glyphs of a MathTex.
    """

    GHOST = [0,0,0,0] # transparent

    colours = (
        (GHOST, BLACK, BLACK, DARK_BROWN, RED, ORANGE, YELLOW, GREEN, PURE_BLUE, TEAL, PINK, PURPLE, GREY, WHITE),
        (GHOST, BLACK, BLACK, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, WHITE),
        (GHOST, BLACK, BLACK, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, WHITE),
        (GHOST, WHITE, *[BLACK for _ in range(12)]),
        (GHOST, BLACK, *[WHITE for _ in range(12)]))

    _colour: ManimColor
    _colour_map: tuple[tuple[re.Pattern[str], int]] = []
    _index: int = 0
    _scheme: int = scheme_bright
    _tex: MathTex = None
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
        return self.colours[self._scheme][colour_index]

    def paint(self, tex: MathTex) -> None:

        def get_token_colour(token: str) -> ManimColor:
            colours = self.colours[self._scheme]
            for map in self._colour_map:
                if (re.match(map[0], token)):
                    return colours[map[1]]
            return colours[grey]

        def paint_expression() -> None:
            while self._tokens:
                token = pop()
                if token == r'\\': # 2 backslashes = line continuation
                    continue
                match token[0]:
                    case '{':
                        paint_expression()
                    case '}':
                        self._sticky = 0
                        break
                    case '\\':
                        paint_function(token)
                    case '_' | '^':
                        self._sticky = 2 if peek() == '{' else 1
                    case _:
                        paint_glyph(token)

        def paint_function(token: str) -> None:
            match(token):
                case r'\frac':
                    pop() # '{'
                    paint_expression()
                    self._index += 1
                    pop() # '{'
                    paint_expression()
                case r'\sqrt':
                    self._index += 1
                    if peek() == '[':
                        pop()
                        while token := pop() != ']':
                            self._index += 1
                    self._index += 1
                case _:
                    paint_glyph(token)

        def paint_glyph(token: str) -> None:
            glyph = self._tex[0][self._index]
            if self._sticky == 0:
                self._colour = get_token_colour(token)
            glyph.set_color(self._colour)
            if self._sticky == 1:
                self._sticky = 0
            self._index += 1

        def peek() -> str:
            return self._tokens[0]

        def pop() -> str:
            token = peek()
            self._tokens.pop(0)
            return token

        # A backslash followed by word character(s) is a single token.
        # Two consecutive backslashes make a null token (whitespace).
        # Otherwise, a token is just any single character, excluding
        # ampersands & whitespace.
        self._tokens = re.findall(r"\\\w+|\\\\|[^&\s]", tex.tex_string)

        #print(*self.tokens)

        tex.set_color(self.get_colour(grey))
        self._tex = tex
        self._index = 0
        paint_expression()

    def set_colour_map(self, colour_map: tuple[tuple[str, int]]) -> tuple[tuple[re.Pattern[str], int]]:
        self._colour_map = [[re.compile(m[0]), m[1]] for m in colour_map]
