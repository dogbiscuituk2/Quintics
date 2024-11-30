# https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf

# LATEX Mathematical Symbols
# The more unusual symbols are not defined in base LATEX (NFSS) and require \usepackage{amssymb}

GREEK_AND_HEBREW_LETTERS = [
    [r'\alpha', r'\beta', r'\chi', r'\delta', r'\epsilon', r'\eta', r'\gamma', r'\iota'],
    [r'\kappa', r'\lambda', r'\mu', r'\nu', o, r'\omega', r'\phi', r'\pi'],
    [r'\psi', r'\rho', r'\sigma', r'\tau', r'\theta', r'\upsilon', r'\xi', r'\zeta'],
    [r'\digamma', r'\varepsilon', r'\varkappa', r'\varphi', r'\varpi', r'\varrho', r'\varsigma', r'\vartheta'],
    [r'\Delta', r'\Gamma', r'\Lambda', r'\Omega', r'\Phi', r'\Pi', r'\Psi', r'\Sigma'],
    [r'\Theta', r'\Upsilon', r'\Xi', '', r'\aleph', r'\beth', r'\daleth', r'\gimel']]

LATEX_MATH_CONSTRUCTS = [
    [r'\frac{abc}{xyz}', r"f'", r'\sqrt{abc}', r'\sqrt[n]{abc}'],
    [r'\overline{abc}', r'\underline{abc}', r'\widehat{abc}', r'\widetilde{abc}'],
    [r'\overrightarrow{abc}', r'\overleftarrow{abc}', r'\overbrace{abc}', r'\underbrace{abc}']]

DELIMITERS = [
    ['|', r'\vert', r'\|', r'\Vert'],
    ['\{', '\}', '\langle', '\rangle'],
    ['\lfloor', '\rfloor', '\lceil', '\rceil'],
    ['/', '\backslash', '[', ']'],
    ['\Uparrow', '\uparrow', '\Downarrow', '\downarrow'],
    ['\llcorner', '\lrcorner', '\ulcorner', '\urcorner']]

# Use the pair \lefts1 and \rights1 to match height of delimiters s1 and s2 to the height of their contents,
# e.g. \left| expr \right| -or- \left\{ expr \right\} -or- \left\Vert expr \right.

VARIABLE_SIZED_SYMBOLS = [ # displayed formulae show larger version
    [r'\sum', r'\prod', r'\coprod'],
    [r'\int', r'\oint', r'\iint'],
    [r'\bigplus', r'\bigcap', r'\bigcup'],
    [r'\bigoplus', r'\bigotimes', r'\bigodot'],
    [r'\bigvee', r'\bigwedge', r'\bigsqcup']]

STANDARD_FUNCTION_NAMES = [ # Function names should appear in Roman, not Italic.
    [r'\arccos', r'\cos', r'\csc', r'\exp', r'\ker', r'\limsup', r'\min', r'\sinh'],
    [r'\arcsin', r'\cosh', r'\deg', r'\gcd', r'\lg', r'\ln', r'\Pr', r'\sup'],
    [r'\arctan', r'\cot', r'\det', r'\hom', r'\lim', r'\log', r'\sec', r'\tan'],
    [r'\arg', r'\coth', r'\dim', r'\inf', r'\liminf', r'\max', r'\sin', r'\tanh']]

BINARY_OPERATION_RELATION_SYMBOLS_1 = []
BINARY_OPERATION_RELATION_SYMBOLS_2 = []
BINARY_OPERATION_RELATION_SYMBOLS_3 = []
BINARY_OPERATION_RELATION_SYMBOLS_4 = []
ARROW_SYMBOLS1 = []
ARROW_SYMBOLS2 = []
ARROW_SYMBOLS3 = []
ARROW_SYMBOLS4 = []
MISCELLANEUOS_SYMBOLS = []
MATH_MODE_ACCENTS = []
OTHER_STYLES_MATH_MODE_ONLY = []
FONT_SIZES = []
TEXT_MODE_ACCENTS_AND_SYMBOLS = []
