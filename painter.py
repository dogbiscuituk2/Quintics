from manim import *
import re

Background   = 0
Black        = 1
Brown        = 2
Red          = 3
Orange       = 4
Yellow       = 5
Green        = 6
Blue         = 7
Cyan         = 8
Magenta      = 9
Violet       = 10
Grey         = 11
White        = 12

SchemeDefault       = 0
SchemeBright        = 1
SchemePastel        = 2
SchemeBlackOnWhite  = 3
SchemeWhiteOnBlack  = 4

class Painter():

    colours = (
        (BLACK, BLACK, DARK_BROWN, RED, ORANGE, YELLOW, GREEN, PURE_BLUE, TEAL, PINK, PURPLE, GREY, WHITE),
        (BLACK, BLACK, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, WHITE),
        (BLACK, BLACK, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, PURE_BLUE, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, WHITE),
        (WHITE, *[BLACK for _ in range(12)]),
        (BLACK, *[WHITE for _ in range(12)]))

    colour: ManimColor
    map: tuple[tuple[str, int]] = ()
    scheme: int = SchemeBright
    sticky: int = 0
    tex: MathTex = None
    texIndex: int = 0
    tokens: List[str] = []

    def __init__(
            self,
            scheme: int = SchemeBright,
            map: tuple[tuple[str, int]] = ()):
        self.scheme = scheme;
        if map is not None:
            self.map = map

    def get_colour(self, colour_index: int) -> ManimColor:
        return self.colours[self.scheme][colour_index]

    def paint(self, mathTex: MathTex):

        def accept(token):
            pop()

        def get_token_colour(token: str) -> ManimColor:
            for map in self.map:
                if (token in map[0]):
                    return self.colours[self.scheme][map[1]]
            return self.colours[self.scheme][Grey]

        def paint_block():
            accept('{')
            paint_expression()

        def paint_expression():
            while self.tokens:
                token = pop()
                match token[0]:
                    case '{':
                        paint_expression()
                    case '}':
                        self.sticky = 0
                        break
                    case '\\':
                        paint_function(token)
                    case '_'|'^':
                        self.sticky = 2 if peek() == '{' else 1
                    case _:
                        paint_glyph(token, True)

        def paint_function(token):
            match(token):
                case r'\frac':
                    paint_block()
                    paint_glyph(token, False)
                    paint_block()
                case r'\sqrt':
                    paint_glyph(token, False)
                    self.texIndex += 1
                case _:
                    paint_glyph(token, False)

        def paint_glyph(token: str, paint: bool) -> None:
            if paint:
                glyph = self.tex[0][self.texIndex]
                if token in ['|', 'o']:
                    glyph.set_opacity(0)
                else:
                    if self.sticky == 0:
                        self.colour = get_token_colour(token)
                    glyph.set_color(self.colour)
                    if self.sticky == 1:
                        self.sticky = 0
            self.texIndex += 1

        def peek() -> str:
            return self.tokens[0]

        def pop() -> str:
            token = peek()
            self.tokens.pop(0)
            return token

        self.level = 0
        self.tex = mathTex
        self.texIndex = 0
        self.tokens = re.findall(r"\\\w+|\{|\}|[^\\\{\}]", self.tex.tex_string)
        self.tex.set_color(self.get_colour(Grey))
        paint_expression()

    def set_colour_map(self, map: tuple[tuple[str, int]]):
        self.map = map;
