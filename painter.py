from manim import *
import re

background   = 0
black        = 1
brown        = 2
red          = 3
orange       = 4
yellow       = 5
green        = 6
blue         = 7
cyan         = 8
magenta      = 9
violet       = 10
grey         = 11
white        = 12

scheme_default          = 0
scheme_bright           = 1
scheme_pastel           = 2
scheme_black_on_white   = 3
scheme_white_on_black   = 4

class Painter():

    colours = (
        (BLACK, BLACK, DARK_BROWN, RED, ORANGE, YELLOW, GREEN, PURE_BLUE, TEAL, PINK, PURPLE, GREY, WHITE),
        (BLACK, BLACK, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, WHITE),
        (BLACK, BLACK, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, WHITE),
        (WHITE, *[BLACK for _ in range(12)]),
        (BLACK, *[WHITE for _ in range(12)]))

    colour: ManimColor
    index: int = 0
    map: tuple[tuple[str, int]] = ()
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
            map: tuple[tuple[str, int]] = ()):
        self.scheme = scheme;
        if map is not None:
            self.map = map

    def get_colour(self, colour_index: int) -> ManimColor:
        return self.colours[self.scheme][colour_index]

    def paint(self, tex: MathTex) -> None:

        def get_token_colour(token: str) -> ManimColor:
            colours = self.colours[self.scheme]
            for map in self.map:
                m = re.match(map[0], token)
                print(f"match('{map[0]}', '{token}') = ", m)
                if (m):
                    return colours[map[1]]
            return colours[grey]

        def paint_expression():
            while self.tokens:
                token = pop()
                if token == '\\\\': # 2 backslashes = line continuation
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
                        paint_glyph(token, True)

        def paint_function(token):
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
                        while pop() != ']':
                            self.index += 1
                    self.index += 1
                case _:
                    self.index += 1
                    #paint_glyph(token, False)

        def paint_glyph(token: str, paint: bool) -> None:
            if paint:
                glyph = self.tex[0][self.index]
                #if token in ['|', 'O', 'o']:
                #    glyph.set_opacity(0)
                #else:
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

        print(*self.tokens)

        tex.set_color(self.get_colour(grey))
        self.tex = tex
        self.index = 0
        paint_expression()

    def set_colour_map(self, map: tuple[tuple[str, int]]):
        self.map = map;
