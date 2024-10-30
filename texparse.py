from manim import *
import re

class TexParse():

    Level: int = 0
    Tex: MathTex = None
    TexIndex: int = 0
    Tokens: List[str] = []

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
            print(f"{self.Level * ' '}{['begin', 'mid', 'end'][stage_index]} {what}")
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
                    case _:
                        pass
            end('expression')

        def function(token):
            name = token[1:]
            foo = f"function {name}"
            begin(foo)
            match(name):
                case 'frac':
                    block()
                    mid(foo)
                    block()
                case 'sqrt':
                    pass
                case _:
                    pass
            end(foo)

        def mid(what: str):
            debug(1, what)

        def pop() -> str:
            return self.Tokens.pop(0)

        def touch(token):
            # Process an element of the MathTex
            # Point to the next MathTex element
            print(f"parse_touch('{token}')")

        self.Tex = mathTex
        self.TexIndex = 0
        token_pattern = r"\\\w+|\{|\}|[^\\\{\}]"
        self.Tokens = re.findall(token_pattern, self.Tex.tex_string) 
        expression()
