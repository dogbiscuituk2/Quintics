from manim import *
import re

class TexParser():

    Level = 0
    Tex = None
    TexIndex = 0
    Tokens = []

    def parse_begin(self, what: str):
        self.parse_debug(True, what)

    def parse_end(self, what: str):
        self.parse_debug(False, what)

    def parse_debug(self, begin: bool, what: str) -> None:
        if (not begin):
            self.Level -= 1
        print(f"{self.Level * ' '}{'begin' if begin else 'end'} {what}")
        if (begin):
            self.Level += 1

    def parse_block(self):
        self.parse_begin('block')
        self.parse_token('{')
        self.parse_expression()
        self.parse_end('block')

    def parse_expression(self):
        self.parse_begin('expression')
        while self.Tokens:
            token = self.Tokens.pop(0)
            match token[0]:
                case '{':
                    self.parse_expression()
                case '}':
                    #print('end expression')
                    break
                case '\\':
                    self.parse_function(token)
                case _:
                    pass
        self.parse_end('expression')

    def parse_function(self, token):

        def parse_fn_type(f: str) -> int:
            fn_types = {
                '\\frac': 2 # Two blocks with one glyph between
            }
            return fn_types[f] if f in fn_types.keys() else 1

        self.parse_begin('function')
        match(parse_fn_type(token)):
            case 2:
                self.parse_block()
                self.TexIndex += 1
                self.parse_block()
            case 1:
                self.TexIndex += 1
        self.parse_end('function')

    def parse_tex(self, mathTex: MathTex):
        self.Tex = mathTex
        self.TexIndex = 0
        token_pattern = r"\\\w+|\{|\}|[^\\\{\}]"
        self.Tokens.clear()
        for token in re.findall(token_pattern, self.Tex.tex_string):
            self.Tokens.append(token)
        self.parse_expression()

    def parse_token(self, token):
        self.Tokens.pop(0)

    def parse_touch(self, token):
        # Process an element of the MathTex
        # Point to the next MathTex element
        print(f"parse_touch('{token}')")

