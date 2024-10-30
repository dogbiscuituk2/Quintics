from manim import *
import re

class TexParse():

    Level: int = 0
    Tex: MathTex = None
    TexIndex: int = 0
    Tokens: List[str] = []

    def accept(self, token):
        self.pop()

    def begin(self, what: str):
        self.debug(True, what)

    def block(self):
        self.begin('block')
        self.accept('{')
        self.expression()
        self.end('block')

    def debug(self, begin: bool, what: str) -> None:
        if (not begin):
            self.Level -= 1
        print(f"{self.Level * ' '}{'begin' if begin else 'end'} {what}")
        if (begin):
            self.Level += 1

    def end(self, what: str):
        self.debug(False, what)

    def expression(self):
        self.begin('expression')
        while self.Tokens:
            token = self.pop()
            match token[0]:
                case '{':
                    self.expression()
                case '}':
                    #print('end expression')
                    break
                case '\\':
                    self.function(token)
                case _:
                    pass
        self.end('expression')

    def function(self, token):
        self.begin(f"function {token}")
        match(token):
            case '\\frac':
                self.block()
                self.block()
            case '\\sqrt':
                pass
            case _:
                pass
        self.end(f"function {token}")

    def parse(self, mathTex: MathTex):
        self.Tex = mathTex
        self.TexIndex = 0
        token_pattern = r"\\\w+|\{|\}|[^\\\{\}]"
        self.Tokens = re.findall(token_pattern, self.Tex.tex_string) 
        self.expression()

    def pop(self) -> str:
        return self.Tokens.pop(0)

    def touch(self, token):
        # Process an element of the MathTex
        # Point to the next MathTex element
        print(f"parse_touch('{token}')")
