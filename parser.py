from manim import *
import re

PAT_TOKEN = r"\\{|\\}|\\\||\\[A-Za-z]+|\\\\|[^&\s]"

class Term():

    token_index: int
    token_count: int
    glyph_index: int
    glyph_count: int

    def __init__(
            self,
            token_index: int,
            glyph_index: int,
            glyph_count: int = 1):
        token_index = token_index
        glyph_index = glyph_index
        glyph_count = glyph_count
        
class Parser():

    _glyph_index: int
    _token_index: int
    _tex: MathTex
    _tokens: List[str]

    def __init__(self, tex: MathTex) -> None:
        self._glyph_index = 0
        self._token_index = 0
        self._tex = tex
        self._tokens = re.findall(PAT_TOKEN, tex.tex_string)
        print(self._tokens)

    def parse(self) -> None:
        self._parse_string()

    @property
    def _more(self) -> bool:
        return self._token_index < len(self._tokens)

    @property
    def _next(self) -> str:
        token = self._peek
        self._token_index += 1
        return token

    @property
    def _peek(self) -> str:
        return self._tokens[self._token_index]

    def _accept(self, token: str) -> None:
        if (self._peek != token):
            pass
        self._token_index += 1

    def _parse_shift(self, token: str) -> List[Term]:
        self._accept(token)
        return self._parse_atom()
    
    def _parse_string(self) -> None:
        while self._more and self._peek != '}':
            self._parse_atom()

    def _parse_subscript(self) -> List[Term]:
        return self._parse_shift('_')

    def _parse_superscript(self) -> List[Term]:
        return self._parse_shift('^')

    def _parse_sum(self) -> List[Term]:
        middle = Term(self._token_index, self._glyph_index)
        self._token_index += 1
        bottom = self._parse_subscript() if self._peek == '_' else None
        top = self._parse_superscript() if self._peek == '^' else None

    def _parse_atom(self) -> List[Term]:
        match self._peek:
            case r'\sum':
                return self._parse_sum()
            case '{':
                self._accept('{')
                term = self._parse_atom()
                self._accept('}')
                return term
            case _:
                token = self._next
                print(token)

if (__name__ == '__main__'):

    parser = Parser(MathTex(r'\sum_{i=0}^{n+1}{i^2}'))
    print('ok1')
    parser.parse()
    print('ok2')
