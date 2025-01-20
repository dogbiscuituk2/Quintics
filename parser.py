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

from manim import *
import re

from latex_rice import *

PAT_TOKEN = re.compile(r"\\{|\\}|\\\||\\[A-Za-z]+|\\\\|\\\,|[^&\s]")

def get_glyph_count(*args: str) -> int:
    return sum(map(len, MathTex(*args)))

class Parser():

    glyph_count: int
    glyph_index: int
    tex: SingleStringMathTex
    token_count: int
    token_index: int
    tokens: List[str] = []

    @property
    def more(self) -> bool:
        return self.token_index < self.token_count
    
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

    def parse(self, root: Mobject) -> None:
        self.parse_node(root)
    
    def parse_accent(self) -> None:
        pass
    
    def parse_aggregate(self, prototype: str) -> None:
        pass
    
    def parse_math(self) -> None:
        pass

    def parse_node(self, parent: Mobject) -> None:
        if type(parent) is SingleStringMathTex:
            self.parse_ssmt(parent)
        elif isinstance(parent, VMobject):
            for child in parent.submobjects:
                self.parse_node(child)
    
    def parse_size(self) -> None:
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

    def parse_subsequence(self) -> None:
        while self.more and self.peek != '}':
            self.parse_unit()

    def parse_subsuper(self) -> None:
        self.skip
        return self.parse_unit()

    def parse_unit(self) -> None:
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
            case '{':
                self.skip
                self.parse_subsequence()
                self.accept('}')
            case '_':
                self.parse_subsuper()
            case '^':
                self.parse_subsuper()
            case _:
                self.glyph_index += get_glyph_count(self.peek)
                self.skip

if __name__ == '__main__':
    parser = Parser()
    s = [r'\arcsin x_1^2', r'\arccos y_3^4']
    tex = MathTex(*s)
    print ('Total glyph count:', get_glyph_count(*s))
    parser.parse(tex)
