#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mobject
 +- VMobject
    +- SVGMobject
       +- Text
       +- SingleStringMathTex
          +- MathTex

VMobject has a list of child VMobjects called submobjects.
"""

from inspect import currentframe
from manim import *
import re

from latex_rice import *
from latex_token import Token
from options import Opt
from pens import Pen
from symbol import Symbol

PAT_TOKEN = re.compile(r"\\{|\\}|\\\||\\[A-Za-z]+|\\\\|\\\,|[^&\s]")

def get_glyph_count(*args: str) -> int:
    try:
        return sum(map(len, MathTex(*args)))
    except:
        return 0

class Parser():

    colour_map: List[tuple[re.Pattern[str], int]] = []
    glyph_count: int
    glyph_index: int
    _options: Opt
    pen: Pen = Pen.BLACK
    sticky: bool = False # Subscripted or superscripted unit reuses previous colour.
    tex: SingleStringMathTex
    token_count: int
    token_index: int
    tokens: List[str] = []

    @property
    def fore_pen(self) -> Pen:
        return self.get_token_pen('FG')

    @property
    def more(self) -> bool:
        return self.token_index < self.token_count

    @property
    def options(self) -> Opt:
        return self._options
    
    @options.setter
    def options(self, value: Opt) -> None:
        self._options = value
    
    @property
    def peek(self) -> str:
        return self.tokens[self.token_index] if self.more else ''
    
    @property
    def pop(self) -> str:
        token = self.peek
        self.skip
        return token
    
    @property
    def skip(self) -> None:
        if self.more:
            self.token_index += 1
    
    def accept(self, token: str) -> None:
        if self.peek != token:
            pass
        self.skip

    def dump_symbols(self, flag: str, *lists: List[Symbol]) -> None:
        if Opt.DEBUG_SYMBOLS in self.options:
            frame = currentframe().f_back
            if flag == '<':
                print(frame.f_code.co_name, end=' ')
            print(flag, end=' ')
            for list in lists:
                print(*list, end=' ')
            if flag == '>':
                print()

    def get_token_pen(self, token: str) -> Pen:
        for map in self.colour_map:
            if (re.match(map[0], token)):
                return map[1]
        return Pen.GREY

    def parse(self, root: Mobject) -> None:
        self.parse_node(root)
    
    def parse_accent(self) -> List[Token]:
        pass
    
    def parse_aggregate(self, prototype: str) -> List[Token]:
        pass
    
    def parse_frac(self) -> List[Token]:
        g1 = self.parse_token()
        g2 = self.parse_unit()
        g3 = self.parse_unit()
        self.dump_symbols('<', g1, g2, g3)
        n1 = get_glyph_count(g1)
        n2 = get_glyph_count(g2)
        self.adjust(g1, n2)
        self.adjust(g2, -n1)
        self.dump_symbols('>', g1, g2, g3)
        return g2 + g1 + g3
    
    def parse_math(self) -> List[Token]:
        pass

    def parse_node(self, parent: Mobject) -> None:
        if type(parent) is SingleStringMathTex:
            self.parse_ssmt(parent)
        elif isinstance(parent, VMobject):
            for child in parent.submobjects:
                self.parse_node(child)
    
    def parse_size(self) -> List[Token]:
        pass
    
    def parse_sqrt(self) -> List[Token]:
        pass

    def parse_ssmt(self, tex: SingleStringMathTex) -> None:
        self.tex = tex
        self.glyph_count = len(tex)
        self.glyph_index = 0
        self.tokens.clear()
        self.tokens.extend(re.findall(PAT_TOKEN, tex.tex_string))
        self.token_count = len(self.tokens)
        self.token_index = 0
        print(f'{self.token_count} tokens, {self.glyph_count} glyphs.')
        while self.more:
            self.parse_unit()
        print(f'{self.glyph_index} glyphs painted.')

    def parse_subsequence(self) -> List[Token]:
        result = []
        while self.more and self.peek != '}':
            result.extend(self.parse_unit())
        return result

    def parse_subsuper(self) -> List[Token]:
        self.skip
        return self.parse_unit()

    def parse_token(self) -> List[Token]:
        token = self.peek
        glyph_count = get_glyph_count(token)
        if not self.sticky:
            self.pen = self.get_token_pen(token)
        symbols = [Symbol(
            token_index = self.token_index,
            token_count = 1,
            glyph_index = self.glyph_index,
            glyph_count = glyph_count,
            pen = self.pen)]
        self.skip
        self.glyph_index += glyph_count
        return symbols

    def parse_unit(self) -> List[Token]:
        token = self.peek
        if re.match(PAT_INT, token):
            return self.parse_aggregate(prototype = r'\int')
        if re.match(PAT_LARGE, token):
            return self.parse_aggregate(prototype = r'\sum')
        if re.match(PAT_ACCENT, token):
            return self.parse_accent()
        if re.match(PAT_MATH, token):
            return self.parse_math()
        if re.match(PAT_SIZE, token):
            return self.parse_size()
        match self.peek:
            case r'\frac':
                return self.parse_frac()
            case r'\sqrt':
                return self.parse_sqrt()
            case '{':
                self.skip
                self.parse_subsequence()
                self.accept('}')
            case '_':
                self.parse_subsuper()
            case '^':
                self.parse_subsuper()
            case _:
                return self.parse_token()

if __name__ == '__main__':
    parser = Parser()
    #s = [r'\frac{\arcsin x_1^2}{\arccos y_3^4}']
    s = [r'\frac{1}{2}']
    tex = MathTex(*s)
    print ('Total glyph count:', get_glyph_count(*s))
    parser.parse(tex)
