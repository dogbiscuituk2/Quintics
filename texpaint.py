#import logging
from manim import *
import re

#logging.basicConfig(level=logging.DEBUG) # DEBUG/INFO/WARNG/ERROR/FATAL

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

class TexPaint():

    colours = (
        (0x000000, 0x000000, 0x3F3F00, 0xFF0000, 0x7F7F00, 0xFFFF00, 0x00FF00, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x7F007F, 0x7F7F7F, 0xFFFFFF),
        (0x000000, 0x000000, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, 0xFFFFFF),
        (0x000000, 0x000000, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, 0xFFFFFF),
        (0xFFFFFF, *[0x000000 for _ in range(12)]),
        (0x000000, *[0xFFFFFF for _ in range(12)]))

    colour: ManimColor
    level: int = 0
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

        def begin(what: str):
            debug(0, what)

        def debug(stage_index: int, what: str) -> None:
            if (stage_index > 0):
                self.level -= 1
            #logging.info(f"{self.level * ' '}{['begin', 'mid', 'end'][stage_index]} {what}")
            if (stage_index < 2):
                self.level += 1

        def end(what: str):
            debug(2, what)

        def get_token_colour(token: str) -> ManimColor:
            for map in self.map:
                if (token in map[0]):
                    return self.colours[self.scheme][map[1]]
            return self.colours[self.scheme][Grey]

        def mid(what: str):
            debug(1, what)

        def paint_block():
            begin('block')
            accept('{')
            paint_expression()
            end('block')

        def paint_expression():
            begin('expression')
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
            end('expression')

        def paint_function(token):
            name = token[1:]
            fun = f"function {name}"
            begin(fun)
            match(name):
                case 'frac':
                    paint_block()
                    mid(fun)
                    paint_glyph(token, False)
                    paint_block()
                case 'sqrt':
                    paint_glyph(token, False)
                    self.texIndex += 1
                case _:
                    paint_glyph(token, False)
            end(fun)

        def paint_glyph(token: str, paint: bool) -> None:
            #logging.debug(f"Visiting character {token} at glyph position {self.texIndex}")
            if paint:
                glyph = self.tex[0][self.texIndex]
                if token == '|':
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

        #logging.info(r"0         1         2         3         4         5         6         7         8         9        10")
        #logging.info(r"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")
        #logging.info(mathTex.tex_string)

        self.level = 0
        self.tex = mathTex
        self.texIndex = 0
        self.tokens = re.findall(r"\\\w+|\{|\}|[^\\\{\}]", self.tex.tex_string)
        self.tex.set_color(self.get_colour(Grey))
        paint_expression()

    def set_colour_map(self, map: tuple[tuple[str, int]]):
        self.map = map;
