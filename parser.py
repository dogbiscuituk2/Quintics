from manim import *
import re

PAT_TOKEN = r"\\{|\\}|\\\||\\[A-Za-z]+|\\\\|[^&\s]"

class Term():

    token_index: int
    glyph_index: int
    glyph_count: int

    def __init__(
            self,
            token_index: int,
            glyph_index: int,
            glyph_count: int = 1):
        self.token_index = token_index
        self.glyph_index = glyph_index
        self.glyph_count = glyph_count

    def __str__(self) -> str:
        return f'[{self.token_index},{self.glyph_index},{self.glyph_count}]'
        
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

    def parse(self) -> List[Term]:
        return self._parse_string()

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

    def _get_tex_len(self, token: str) -> int:
        try:
            tex = MathTex(token)
        except Exception:
            return 0
        return len(tex[0])

    def _parse_shift(self, token: str) -> List[Term]:
        self._accept(token)
        return self._parse_atom()
    
    def _parse_string(self) -> List[Term]:
        result = []
        while self._more and self._peek != '}':
            result += self._parse_atom()
        return result

    def _parse_shift(self, token: str) -> List[Term]:
        '''
        If the current token is either '_' or '^' then return the following atom,
        otherwise return the empty list.

        str: The expected token, '_' or '^'.
        '''
        if self._peek == token:
            self._accept(token)
            return self._parse_atom()
        return []

    def _parse_sum(self) -> List[Term]:

        middle = [Term(self._token_index, self._glyph_index)]
        self._token_index += 1

        bottom = self._parse_shift('_')
        top = self._parse_shift('^')
        top_len = len(top)
        mb_len = len(middle) + len(bottom)
        for term in top:
            term.glyph_index -= mb_len
        for term in middle:
            term.glyph_index += top_len

        print(*top)
        print(*middle)
        print(*bottom)

        return top + middle + bottom

    def _parse_atom(self) -> List[Term]:
        match self._peek:
            case r'\sum':
                return self._parse_sum()
            case '{':
                self._accept('{')
                result = self._parse_string()
                self._accept('}')
                return result
            case _:
                token = self._peek
                glyph_count = self._get_tex_len(token)
                result = [Term(self._token_index, self._glyph_index, glyph_count)]
                token = self._next
                print(token)
                self._glyph_index += glyph_count
                return result

if (__name__ == '__main__'):

    parser = Parser(MathTex(r'\sum_{i=0}^{n+1}{i^2}'))
    print('ok1')
    parser.parse()
    print('ok2')
