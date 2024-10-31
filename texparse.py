from enum import Enum
import logging
from manim import *
import re

logging.basicConfig(level=logging.DEBUG) # DEBUG/INFO/WARNG/ERROR/FATAL

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

Default      = 0
Bright       = 1
Pastel       = 2
BlackOnWhite = 3
WhiteOnBlack = 4

Scheme = Bright
    
colours = (
    (0x000000, 0x000000, 0x3F3F00, 0xFF0000, 0x7F7F00, 0xFFFF00, 0x00FF00, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x7F007F, 0x7F7F7F, 0xFFFFFF),
    (0x000000, 0x000000, 0x7F3319, 0xFF1933, 0xFF7F4C, 0xCCCC00, 0x33FF33, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xB2B2B2, 0xFFFFFF),
    (0x000000, 0x000000, 0xCD853F, 0xFF0000, 0xFF7F3F, 0xCCCC00, 0x33FF33, 0x0000FF, 0x00FFFF, 0xFF00FF, 0x9A72AC, 0xBBBBBB, 0xFFFFFF),
    (0xFFFFFF, *[0x000000 for _ in range(12)]),
    (0x000000, *[0xFFFFFF for _ in range(12)]))

class TexParse():

    ColourMap: tuple[tuple[str, int]]
    Level: int = 0
    Scheme: int = Bright
    Tex: MathTex = None
    TexIndex: int = 0
    Tokens: List[str] = []

    def __init__(self, scheme: int, colourMap: tuple[tuple[str, ManimColor]]):
        self.Scheme = scheme;
        self.ColourMap = colourMap

    def parse(self, mathTex: MathTex):

        def accept(token):
            pop()

        def begin(what: str):
            debug(0, what)

        def block():
            begin('block')
            accept('{')
            expression()
            end('block')

        def debug(stage_index: int, what: str) -> None:
            if (stage_index > 0):
                self.Level -= 1
            logging.debug(f"{self.Level * ' '}{['begin', 'mid', 'end'][stage_index]} {what}")
            if (stage_index < 2):
                self.Level += 1

        def end(what: str):
            debug(2, what)

        def expression():
            begin('expression')
            while self.Tokens:
                token = pop()
                match token[0]:
                    case '{':
                        expression()
                    case '}':
                        break
                    case '\\':
                        function(token)
                    case '_':
                        pass
                    case '^':
                        pass
                    case _:
                        visit(token, True)
            end('expression')

        def function(token):
            name = token[1:]
            fun = f"function {name}"
            begin(fun)
            match(name):
                case 'frac':
                    block()
                    mid(fun)
                    visit(token, False)
                    block()
                case 'sqrt':
                    visit(token, False)
                    self.TexIndex += 1
                case _:
                    visit(token, False)
            end(fun)

        def get_colour(self, char: str) -> ManimColor:
            for map in self.ColourMap:
                if (char in map[0]):
                    return map[1]
            return Grey

        def mid(what: str):
            debug(1, what)

        def pop() -> str:
            return self.Tokens.pop(0)

        def visit(token: str, paint: bool) -> None:
            logging.debug(f"Visiting character {token} at glyph position {self.TexIndex}")
            if paint:
                self.Tex[0][self.TexIndex].set_color(RED)
            self.TexIndex += 1

        logging.debug(r"0         1         2         3         4         5         6         7         8         9        10")
        logging.debug(r"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")
        logging.debug(r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}")

        self.Level = 0
        self.Tex = mathTex
        self.TexIndex = 0
        self.Tokens = re.findall(r"\\\w+|\{|\}|[^\\\{\}]", self.Tex.tex_string) 
        expression()
