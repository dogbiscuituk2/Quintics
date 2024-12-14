from context import Context
from manim import *
import re

PAT_TOKEN = r"\\{|\\}|\\\||\\[A-Za-z]+|\\\\|[^&\s]"

class Parser():

    _index: int
    _tex: MathTex
    _tokens: List[str]

    def __init__(self, tex: MathTex) -> None:
        self._index = 0
        self._tex = tex
        self._tokens = re.findall(PAT_TOKEN, tex.tex_string)

    def parse(self) -> None:
        self._parse_string(Context())

    @property
    def _more(self) -> bool:
        return self._index < len(self._tokens)

    @property
    def _next(self) -> str:
        token = self._peek
        self._index += 1
        return token

    @property
    def _peek(self) -> str:
        return self._tokens[self._index]

    def _accept(self, token: str) -> None:
        if (self._peek != token):
            pass
        self._index += 1

    def _parse_expression(self, context: Context) -> None:
        self._accept('{')
        context.level += 1
        self._parse_string(context)
        self._accept('}')
        context.level -= 1
    
    def _parse_string(self, context: Context) -> None:
        while self._more and self._peek != '}':
            self._parse_token(context)

    def _parse_subscript(self, context) -> None:
        self._accept('_')
        context.sub += 1
        self._parse_token(context)
        context.sub -= 1

    def _parse_superscript(self, context) -> None:
        self._accept('^')
        context.super += 1
        self._parse_token(context)
        context.super -= 1

    def _parse_token(self, context: Context) -> None:
        match self._peek:
            case '{':
                self._parse_expression(context)
            case '_':
                self._parse_subscript(context)
            case '^':
                self._parse_superscript(context)
            case _:
                token = self._next
                print(token, context)

if (__name__ == '__main__'):
    parser = Parser(MathTex(r'\frac{x_1}{y^2}\sum_{n=0}^\infty{x^n}'))
    parser.parse()
