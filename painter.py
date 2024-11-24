from manim import *
import re

ghost   = 0 # transparent
ground  = 1 # background
black   = 2
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

    GHOST = [0,0,0,0] # transparent

    colours = (
        (GHOST, BLACK, BLACK, DARK_BROWN, RED, ORANGE, YELLOW, GREEN, PURE_BLUE, TEAL, PINK, PURPLE, GREY, WHITE),
        (GHOST, BLACK, BLACK, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, WHITE),
        (GHOST, BLACK, BLACK, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, WHITE),
        (GHOST, WHITE, *[BLACK for _ in range(12)]),
        (GHOST, BLACK, *[WHITE for _ in range(12)]))

    colour: ManimColor
    colour_map: tuple[tuple[str, int]] = ()
    index: int = 0
    scheme: int = scheme_bright
    tex: MathTex = None
    tokens: List[str] = []

    sticky: int = 0
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
        self.scheme = scheme;
        if colour_map is not None:
            self.colour_map = colour_map

    def get_colour(self, colour_index: int) -> ManimColor:
        return self.colours[self.scheme][colour_index]

    def paint(self, tex: MathTex) -> None:

        def get_token_colour(token: str) -> ManimColor:
            colours = self.colours[self.scheme]
            for map in self.colour_map:
                if (re.match(map[0], token)):
                    return colours[map[1]]
            return colours[grey]

        def paint_expression():
            while self.tokens:
                token = pop()
                if token == r'\\': # 2 backslashes = line continuation
                    continue
                match token[0]:
                    case '{':
                        paint_expression()
                    case '}':
                        self.sticky = 0
                        break
                    case '\\':
                        paint_function(token)
                    case '_' | '^':
                        self.sticky = 2 if peek() == '{' else 1
                    case _:
                        paint_glyph(token)

        def paint_function(token: str):
            match(token):
                case r'\frac':
                    pop() # '{'
                    paint_expression()
                    self.index += 1
                    pop() # '{'
                    paint_expression()
                case r'\sqrt':
                    self.index += 1
                    if peek() == '[':
                        pop()
                        while token := pop() != ']':
                            self.index += 1
                    self.index += 1
                case _:
                    paint_glyph(token)

        def paint_glyph(token: str) -> None:
            glyph = self.tex[0][self.index]
            if self.sticky == 0:
                self.colour = get_token_colour(token)
            glyph.set_color(self.colour)
            if self.sticky == 1:
                self.sticky = 0
            self.index += 1

        def peek() -> str:
            return self.tokens[0]

        def pop() -> str:
            token = peek()
            self.tokens.pop(0)
            return token

        # A backslash followed by word character(s) is a single token.
        # Two consecutive backslashes make a null token (whitespace).
        # Otherwise, a token is just any single character, excluding
        # ampersands & whitespace.
        self.tokens = re.findall(r"\\\w+|\\\\|[^&\s]", tex.tex_string)

        #print(*self.tokens)

        tex.set_color(self.get_colour(grey))
        self.tex = tex
        self.index = 0
        paint_expression()

    def set_colour_map(self, colour_map: tuple[tuple[str, int]]):
        self.colour_map = colour_map;
