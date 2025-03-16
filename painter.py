#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The Painter class is used to apply colours to the glyphs in a MathTex object.
The colours are determined by a colour map which is a list of tuples, each 
containing a regular expression pattern and a pen index. The pattern is used 
to match the token of a glyph and the pen index is used to determine the 
colour of the glyph. 
The pen index is an integer that corresponds to an index in the colours list. 
The Painter class is used to apply colours to the glyphs in a MathTex object.

Mobject
+-- VMobject
    +-- VMobjectFromSVGPath
    +-- Polygram
    |   +-- Polygon
    |       +- Rectangle
    +- SVGMobject
       +- Text
       +- SingleStringMathTex
          +- MathTex

VMobject has a list of child VMobjects called submobjects.
"""

from inspect import currentframe
from latex_rice import *
from latex_token import Token
from manim import *
from options import Opt
from pens import *
import re
from symbol import Symbol
from typing import Generator, Tuple

PAT_SEP_FACTORS = '*|/'
PAT_SEP_TERMS = r'=|\+|-' # Term separators in an expression
PAT_TOKEN = r'\\{|\\}|\\\||\\[A-Za-z]+|\\\\|\\\,|[^&\s]'
            
def concat(token_list: List[Token]) -> str:
    return ' '.join([token.string for token in token_list])

def ensure_parsed(smt: SingleStringMathTex) -> SingleStringMathTex:
    try:
        _ = smt.Symbols
    except AttributeError:
        Painter().scan(smt)
    return smt

def get_glyph_count(symbols: List[Symbol]) -> int:
    return sum(symbol.glyph_count for symbol in symbols)

def get_glyph_ranges(smt: SingleStringMathTex, pat: str) -> List[range]:
    """
    Example:
    smt = SingleStringMathTex('y=ax^2+bx+c')
    pat = '[a-z]'
    print(get_glyph_ranges(smt, pat))

    Output:
        [range(0, 1), range(2, 3), range(3, 4), range(6, 7), range(7, 8), range(9, 10)]
    """
    return [symbol.slice for symbol in get_token_symbols(smt, pat)]

def get_glyph_starts(smt: SingleStringMathTex, pat: str) -> List[int]:
    """
    Example:
    smt = SingleStringMathTex('y=ax^2+bx+c')
    pat = '[a-z]'
    print(get_glyph_starts(smt, pat))

    Output:
        [0, 2, 3, 6, 7, 9]
    """
    return [symbol.glyph_index for symbol in get_token_symbols(smt, pat)]

def get_smt_symbols(smt: SingleStringMathTex) -> List[Symbol]:
    return ensure_parsed(smt).symbols

def get_smt_tokens(smt: SingleStringMathTex) -> List[Token]:
    return ensure_parsed(smt).tokens

def get_tex_length(string: str) -> int:
    match string:
        case r'\frac':
            return 1
    try:
        return len(SingleStringMathTex(prep_text(string)))
    except Exception:
        return 0

def get_token_symbols(smt: SingleStringMathTex, pat: str ) -> List[Symbol]:
    """
    Find every Symbol containing a given single token pattern in a
    SingleStringMathTex.

    Args:
        smt : The SingleStringMathTex to be processed.
        pat : A regex pattern matching a single token.

    Returns:
        A List[Symbol] of every symbol in the SingleStringMathTex
        containing he given single token pattern.

    Example:
        smt = SingleStringMathTex('y=ax^2+bx+c')
        pat = '[a-z]'
        print(get_token_symbols(smt, pat))

    Output:
        [T0.G0.GREY, T2.G2.GREY, T3.G3.GREY, T7.G6.GREY, T8.G7.GREY, T10.G9.GREY]
    """
    result = []
    tokens: List[Token] = get_smt_tokens(smt)
    symbols: List[Symbol] = get_smt_symbols(smt)
    for token_index, token in enumerate(tokens):
        if re.match(pat, token.string):
            for symbol in symbols:
                offset = token_index - symbol.token_index
                if offset >= 0 and offset < symbol.token_count:
                    result.append(symbol)
    return result

_subscripts = '₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ'
_superscripts = '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ𐞥ʳˢᵗᵘᵛʷˣʸᶻᴬᴮꟲᴰᴱꟳᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾꟴᴿᵀᵁⱽᵂ𐞲'
_sub_super_table = str.maketrans(
    f'{_subscripts}{_superscripts}',
    '0123456789+-=()aehijklmnoprstuvx'
    '0123456789+-=()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTUVWY')

def prep_text(text: str) -> str:
    """
    Nonbreak space: ·
    """

    def encode_sub_super(text: str, is_sub: bool) -> str:

        def handle_match(match: re.Match[str], symbol: str) -> str:
            text = match.string[match.start() : match.end()].translate(_sub_super_table)
            return f'{symbol}{text}' if len(text) < 2 else f'{symbol}{{{text}}}'

        (pattern, symbol) = (_subscripts, '_') if is_sub else (_superscripts, '^')
        return re.sub(f'[{pattern}]+', lambda match: handle_match(match, symbol), text)

    for is_sub in [True, False]:
        text = encode_sub_super(text, is_sub)
    return text.replace('·', r'\phantom{o}')

def shift_glyphs(symbols: List[Symbol], shift: int) -> None:
    for symbol in symbols:
        symbol.glyph_index += shift

def split_smt(smt: SingleStringMathTex, pat: str = PAT_SEP_TERMS) -> List[VGroup]:
    """
    Partition a SingleStringMathTex using a pattern of separators.

    Args:
        smt : The SingleStringMathTex to be processed.
        pat : A pattern matching any separator. Defaults to '=', '+' or '-'.

    Returns:
        A List[VGroup] of every subset of the SingleStringMathTex glyphs. The 
        'zeroth' VGroup is the first term, the next is the first separator, 
        and so on; the last VGroup is the last term. 
        In other words, the even-numbered VGroups (starting at zero) are the 
        terms, and the odd-numbered groups are the separators.

    Examples:
        smt = SingleStringMathTex('y=x^5+5hx^4+10h^2x^3+10h^3x^2+5h^4x+h^5')
        print([len(s) for s in split_smt(smt)])
        Output: [1, 1, 2, 1, 4, 1, 6, 1, 6, 1, 4, 1, 2]
    """
    ranges: List[range] = get_glyph_ranges(smt, pat)
    result = []
    p = 0
    for r in ranges:
        q = r.start
        result.append(smt[p:q])
        p = q
        q = r.stop
        result.append(smt[p:q])
        p = q
    result.append(smt[p:])
    return result

class Painter():

    opt: Opt = Opt.DEFAULT
    palette: List[ManimColor] = PALETTE_SASHA
    pen: Pen = Pen.BACKGROUND
    pens: List[tuple[re.Pattern[str], Pen]] = []
    sticky: bool = False # Subscripted or superscripted unit reuses previous colour.

    glyph_index: int = 0
    token_index: int = 0

    @property
    def ink_bg(self) -> ManimColor:
        return config.background_color

    @property
    def ink_fg(self) -> ManimColor:
        return self.get_token_ink('FG')

    @property
    def options(self) -> Opt:
        return self.opt
    
    @options.setter
    def options(self, value: Opt) -> None:
        self.opt = value
    
    def get_ink(self, pen: Pen) -> ManimColor:
        return self.palette[pen.value] if pen.value >= 0 else self.ink_bg

    def get_pen(self, token: str) -> Pen:
        for map in self.pens:
            if (re.match(map[0], token)):
                return map[1]
        return Pen.GREY
    
    def get_token_ink(self, token: str) -> ManimColor:
        return self.get_ink(self.get_pen(token))
    
    def paint(self, root: Mobject) -> None:
        self.scan(root, apply_paint = True)

    def scan(self, root: Mobject, apply_paint: bool = False) -> None:

        def scan_node(node: Mobject) -> None:

            def scan_smt(smt: SingleStringMathTex) -> None:
                """
                Apply colours to the glyphs in the given SingleStringMathTex object.

                tex: The SingleStringMathTex object to be parsed.

                '\\left.', '\\right.' not implemented.
                """

                def more() -> bool:
                    return self.token_index < len(smt.tokens)

                def scan_unit() -> List[Symbol]:

                    def accept(token: str) -> None:
                        if (peek() != token):
                            pass
                        self.token_index += 1
                    
                    def peek() -> str:
                        index = self.token_index
                        return smt.tokens[index].string if more() else ''
                    
                    def pop() -> str:
                        token = peek()
                        self.token_index += 1
                        return token

                    def dump_symbols(flag: str, *lists: List[Symbol]) -> None:
                        if Opt.DEBUG_SYMBOLS in self.options:
                            frame = currentframe().f_back
                            if flag == '<':
                                print(frame.f_code.co_name, end=' ')
                            print(flag, end=' ')
                            for list in lists:
                                if list:
                                    print(*list, end=' ')
                            if flag == '>':
                                print()

                    def scan_accent() -> List[Symbol]:
                        g1 = scan_symbol()
                        g2 = scan_unit() if more() else []
                        dump_symbols('<', g1, g2)
                        start = g1[0].token_index
                        end = self.token_index
                        string = concat(smt.tokens[start:end])
                        shift = get_tex_length(string) - get_glyph_count(g1 + g2)
                        g1[0].glyph_count += shift
                        shift_glyphs(g2, shift)
                        if Opt.ACCENT in self.options:
                            g1[0].pen = g2[0].pen
                        dump_symbols('>', g1, g2)
                        return g1 + g2

                    def scan_aggregate(prototype: str) -> List[Symbol]:
                        g1 = scan_symbol()
                        g2 = scan_shift('_')
                        g3 = scan_shift('^')
                        dump_symbols('<', g1, g2, g3)
                        n1 = get_glyph_count(g1)
                        n2 = get_glyph_count(g2)
                        n3 = get_glyph_count(g3)
                        match prototype:
                            case r'\int':
                                # Expressions in the "\int" family are rendered with the 
                                # integral sign(s) first on the left, then the upper and lower 
                                # bounds (in that order) in the middle, and finally the 
                                # integrand on the right. Note that the bounds rendering order
                                # is the opposite of their occurrence order in the text,
                                # necessitating the following adjustments.
                                shift_glyphs(g2, n3)
                                shift_glyphs(g3, -n2)
                            case r'\sum':
                                # Expressions in the "\sum" family are rendered with the upper
                                # bounds, summation sign, and lower bounds, stacked vertically 
                                # (in that order), followed by the summand on the right. Note
                                # that all three items in the vertical stack require adjustment 
                                # because their rendering order is completely different from 
                                # their occurrence order in the text.
                                shift_glyphs(g3, -(n1+n2))
                                shift_glyphs(g1, n3)
                                shift_glyphs(g2, n3)
                            case _:
                                # All other aggregates are rendered as-is.
                                pass
                        dump_symbols('>', g1, g2, g3)
                        return g1 + g2 + g3

                    def scan_frac() -> List[Symbol]:
                        g1 = scan_symbol()
                        g2 = scan_unit()
                        g3 = scan_unit()
                        dump_symbols('<', g1, g2, g3)
                        n1 = get_glyph_count(g1)
                        n2 = get_glyph_count(g2)
                        shift_glyphs(g1, n2)
                        shift_glyphs(g2, -n1)
                        dump_symbols('>', g1, g2, g3)
                        return g2 + g1 + g3
                
                    def scan_math(token: str) -> List[Symbol]:
                        extra = 4 if token.endswith('brace') else 2 if token.endswith('arrow') else 1
                        flip = token not in [r'\underline', r'\underbrace']
                        g1 = scan_symbol()
                        g2 = scan_unit() if more() else []
                        dump_symbols('<', g1, g2)
                        n1 = get_glyph_count(g1)
                        n2 = get_glyph_count(g2)
                        if n1 < 1:
                            g1[0].glyph_index = g2[0].glyph_index + get_glyph_count(g2)
                            g1[0].glyph_count = extra
                            if flip:
                                n1 = get_glyph_count(g1)
                                n2 = get_glyph_count(g2)
                                shift_glyphs(g1, -n2)
                                shift_glyphs(g2, +n1)
                        dump_symbols('>', g1, g2)
                        return g1 + g2

                    def scan_phantom() -> List[Symbol]:
                        pop()
                        glyph_index = self.glyph_index
                        scan_unit()
                        self.glyph_index = glyph_index
                        return []

                    def scan_script():
                        self.sticky = Opt.SUBSUPER in self.options
                        symbols = scan_shift(token)
                        self.sticky = False
                        return symbols

                    def scan_shift(token: str) -> List[Symbol]:
                        '''
                        If the current token is either '_' or '^' then return the next unit,
                        otherwise return the empty list.

                        token: The expected token, this will be either '_' or '^'.
                        '''
                        if peek() == token:
                            accept(token)
                            return scan_unit()
                        return []

                    def scan_size(token: str) -> List[Symbol]:
                        '''
                        Paint a delimiter symbol correctly, when the symbol is preceded by a 
                        static or dynamic size modifier.

                        token: The size modifier, e.g. '\\left', '\\big', '\\Bigg'.
                        '''

                        def get_left(right: int) -> int:
                            return list(filter(lambda p: p[1] == right, get_parens()))[0][0]
                    
                        def get_right(left: int) -> int:
                            return list(filter(lambda p: p[0] == left, get_parens()))[0][1]

                        def get_parens() -> Generator[Tuple[int, int], None, None]:
                            lefts = []
                            for index, token in enumerate(smt.tokens):
                                match token.string:
                                    case r'\left':
                                        lefts.append(index)
                                    case r'\right':
                                        yield (lefts.pop(), index)

                        def get_gap(left: int, right: int) -> int:
                            token_L = smt.tokens[left]
                            token_R = smt.tokens[right]
                            snip = text[0:token_L.start] + text[token_L.end:token_R.start] + text[token_R.end:]
                            return 1 + (len(smt) - get_tex_length(snip)) // 2

                        token_index = self.token_index
                        accept(token)
                        delim = pop()
                        bracket = f'{token}{delim}'
                        symbol = Symbol(
                            token_index=token_index,
                            token_count=2,
                            glyph_index=self.glyph_index,
                            glyph_count=1,
                            pen=self.get_pen(delim))
                        match token:
                            case r'\left': # Dynamic
                                gap = get_gap(token_index, get_right(token_index))
                            case r'\right': # Dynamic
                                gap = get_gap(get_left(token_index), token_index)
                            case _: # Static
                                gap = get_tex_length(bracket)
                        symbol.glyph_count = gap
                        self.glyph_index += gap
                        return [symbol]

                    def scan_sqrt() -> List[Symbol]:
                        g1 = scan_symbol()
                        if peek() == '[':
                            colour = g1[0].pen
                            g2 = scan_string('[', ']')
                            for symbol in g2:
                                symbol.pen = colour
                            g1 += g2
                        g3 = scan_unit() if more() else []
                        return g1 + g3
                
                    def scan_string(begin: str = '', end: str = '') -> List[Symbol]:
                        if begin:
                            accept(begin)
                        symbols = []
                        while more() and peek() != end:
                            symbols += scan_unit()
                        if end:
                            accept(end)
                        return symbols
                
                    def scan_symbol() -> List[Symbol]:
                        return scan_token(peek())
                
                    def scan_token(token: str) -> List[Symbol]:
                        token_count = 1
                        glyph_count = get_tex_length(token)
                        if not self.sticky:
                            self.pen = self.get_pen(token)
                        symbols = [Symbol(
                            token_index = self.token_index,
                            token_count = token_count,
                            glyph_index = self.glyph_index,
                            glyph_count = glyph_count,
                            pen = self.pen)]
                        self.token_index += token_count
                        self.glyph_index += glyph_count
                        return symbols

                    token = peek()
                    if re.match(PAT_INT, token):
                        return scan_aggregate(prototype = r'\int')
                    if re.match(PAT_LARGE, token):
                        return scan_aggregate(prototype = r'\sum')
                    if re.match(PAT_ACCENT, token):
                        return scan_accent()
                    if re.match(PAT_MATH, token):
                        return scan_math(token)
                    if re.match(PAT_SIZE, token):
                        return scan_size(token)
                    match token:
                        case r'\frac':
                            return scan_frac()
                        case r'\phantom':
                            return scan_phantom()
                        case r'\sqrt':
                            return scan_sqrt()
                        case '{':
                            result = scan_string('{', '}')
                            return result
                        case '_':
                            return scan_script()
                        case '^':
                            return scan_script()
                        case _:
                            return scan_token(token)

                smt.tokens = []
                smt.symbols = []
                text: str = smt.tex_string
                if not text:
                    return
                for match in re.finditer(PAT_TOKEN, text):
                    span = match.span()
                    start = span[0]
                    end = span[1]
                    length = end - start
                    string = text[start:end]
                    token = Token(start=start, length=length, string=string)
                    smt.tokens.append(token)
                self.token_index = 0
                self.glyph_index = 0
                while more():
                    symbols = scan_unit()
                    smt.symbols.extend(symbols)
                    if apply_paint:
                        pen = Pen.BACKGROUND
                        for symbol in symbols:
                            start = symbol.glyph_index
                            stop = start + symbol.glyph_count
                            if stop > start:
                                if Opt.DEBUG_COLOURS in self.options:
                                    pen = Pen(pen.value + 1) if pen.value < 21 else Pen(0)
                                else:
                                    pen = symbol.pen
                                colour = self.get_ink(pen)
                                for index in range(start, stop):
                                    if index >= 0 and index < len(smt):
                                        glyph = smt[index]
                                        glyph.set_color(colour)

            if type(node) is SingleStringMathTex:
                scan_smt(node)
            elif isinstance(node, VMobject):
                for child in node.submobjects:
                    scan_node(child)

        scan_node(root)

    def set_inks(self, inks: List[ManimColor]) -> None:
        """
        Set the palette of colours to be used by the painter.
        
        palette: A list of colours to be used by the painter.
        """
        self.palette = inks

    def set_pens(self, pens: List[tuple[str, Pen]]) -> None:
        """
        Set the colour map to be used by the painter.
        
        pens: A List of tuples, each comprising a regular expression 
        pattern and a Pen.
        
        Example:
        painter.set_pens((
            (r'\\alpha', Pen.RED),
            (r'\\beta', Pen.GREEN),
            (r'\\gamma', Pen.BLUE)))

        The above example will set the colour of the glyphs representing the 
        Greek letters alpha, beta, gamma to red, green, blue respectively.
        """
        self.pens = [(re.compile(p[0]), p[1]) for p in pens]

if __name__ == '__main__':
    config.verbosity = "CRITICAL"

    src = 'x' + _subscripts + _superscripts
    tgt = prep_text(src)
    print(tgt)

    #smt = SingleStringMathTex('y=x^5+5hx^4+10h^2x^3+10h^3x^2+5h^4x+h^5')
    #print([len(s) for s in split_smt(smt)])
