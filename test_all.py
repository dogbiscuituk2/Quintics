from painter import *
from base_scene import BaseScene

# https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf

# LATEX Mathematical Symbols
# The more unusual symbols are not defined in base LATEX (NFSS) and require \usepackage{amssymb}

GREEK_AND_HEBREW_LETTERS = [
    [r'\alpha', r'\beta', r'\chi', r'\delta', r'\epsilon', r'\eta', r'\gamma', r'\iota'],
    [r'\kappa', r'\lambda', r'\mu', r'\nu', 'o', r'\omega', r'\phi', r'\pi'],
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
    [r'\{', r'\}', r'\langle', r'\rangle'],
    [r'\lfloor', r'\rfloor', r'\lceil', r'\rceil'],
    ['/', r'\backslash', '[', ']'],
    [r'\Uparrow', r'\uparrow', r'\Downarrow', r'\downarrow'],
    [r'\llcorner', r'\lrcorner', r'\ulcorner', r'\urcorner']]

# Use the pair \lefts1 and \rights1 to match height of delimiters s1 and s2 to the height of their contents,
# e.g. \left| expr \right| -or- \left\{ expr \right\} -or- \left\Vert expr \right.

VARIABLE_SIZED_SYMBOLS = [ # displayed formulae show larger version
    [r'\sum', r'\prod', r'\coprod'],
    [r'\int', r'\oint', r'\iint'],
    [r'\biguplus', r'\bigcap', r'\bigcup'],
    [r'\bigoplus', r'\bigotimes', r'\bigodot'],
    [r'\bigvee', r'\bigwedge', r'\bigsqcup']]

STANDARD_FUNCTION_NAMES = [ # Function names should appear in Roman, not Italic.
    [r'\arccos', r'\cos', r'\csc', r'\exp', r'\ker', r'\limsup', r'\min', r'\sinh'],
    [r'\arcsin', r'\cosh', r'\deg', r'\gcd', r'\lg', r'\ln', r'\Pr', r'\sup'],
    [r'\arctan', r'\cot', r'\det', r'\hom', r'\lim', r'\log', r'\sec', r'\tan'],
    [r'\arg', r'\coth', r'\dim', r'\inf', r'\liminf', r'\max', r'\sin', r'\tanh']]

BINARY_OPERATION_RELATION_SYMBOLS_1 = [
    [r'\ast', r'\pm', r'\cap', r'\lhd'],
    [r'\star', r'\mp', r'\cup', r'\rhd'],
    [r'\cdot', r'\amalg', r'\uplus', r'\triangleleft'],
    [r'\circ', r'\odot', r'\sqcap', r'\triangleright'], 
    [r'\bullet', r'\ominus', r'\sqcup', r'\unlhd'], 
    [r'\bigcirc', r'\oplus', r'\wedge', r'\unrhd'], 
    [r'\diamond', r'\oslash', r'\vee', r'\bigtriangledown'], 
    [r'\times', r'\otimes', r'\dagger', r'\bigtriangleup'], 
    [r'\div', r'\wr', r'\ddagger', r'\setminus'], 
    [r'\centerdot', r'\Box', r'\barwedge', r'\veebar'], 
    [r'\circledast', r'\boxplus', r'\curlywedge', r'\curlyvee'], 
    [r'\circledcirc', r'\boxminus', r'\Cap', r'\Cup'], 
    [r'\circleddash', r'\boxtimes', r'\bot', r'\top'], 
    [r'\dotplus', r'\boxdot', r'\intercal', r'\rightthreetimes'],
    [r'\divideontimes', r'\square', r'\doublebarwedge', r'\leftthreetime']]

BINARY_OPERATION_RELATION_SYMBOLS_2 = [
    [r'\equiv', r'\leq', r'\geq', r'\perp'], 
    [r'\cong', r'\prec', r'\succ', r'\mid'], 
    [r'\neq', r'\preceq', r'\succeq', r'\parallel'], 
    [r'\sim', r'\ll', r'\gg', r'\bowtie'], 
    [r'\simeq', r'\subset', r'\supset', r'\Join'], 
    [r'\approx', r'\subseteq', r'\supseteq', r'\ltimes'], 
    [r'\asymp', r'\sqsubset', r'\sqsupset', r'\rtimes'], 
    [r'\doteq', r'\sqsubseteq', r'\sqsupseteq', r'\smile'], 
    [r'\propto', r'\dashv', r'\vdash', r'\frown'], 
    [r'\models', r'\in', r'\ni', r'\notin']]

BINARY_OPERATION_RELATION_SYMBOLS_3 = [
        [r'\approxeq', r'\leqq', r'\geqq', r'\lessgtr'],
    [r'\thicksim', r'\leqslant', r'\geqslant', r'\lesseqgtr'],
    [r'\backsim', r'\lessapprox', r'\gtrapprox', r'\lesseqqgtr'],
    [r'\backsimeq', r'\lll', r'\ggg', r'\gtreqqless'],
    [r'\triangleq', r'\lessdot', r'\gtrdot', r'\gtreqless'],
    [r'\circeq', r'\lesssim', r'\gtrsim', r'\gtrless'],
    [r'\bumpeq', r'\eqslantless', r'\eqslantgtr', r'\backepsilon'],
    [r'\Bumpeq', r'\precsim', r'\succsim', r'\between'],
    [r'\doteqdot', r'\precapprox', r'\succapprox', r'\pitchfork'],
    [r'\thickapprox', r'\Subset', r'\Supset', r'\shortmid'],
    [r'\fallingdotseq', r'\subseteqq', r'\supseteqq', r'\smallfrown'],
    [r'\risingdotseq', r'\sqsubset', r'\sqsupset', r'\smallsmile'],
    [r'\varpropto', r'\preccurlyeq', r'\succcurlyeq', r'\Vdash'],
    [r'\therefore', r'\curlyeqprec', r'\curlyeqsucc', r'\vDash'],
    [r'\because', r'\blacktriangleleft', r'\blacktriangleright', r'\Vvdash'],
    [r'\eqcirc', r'\trianglelefteq', r'\trianglerighteq', r'\shortparallel'],
    [r'\neq', r'\vartriangleleft', r'\vartriangleright', r'\nshortparallel']]

BINARY_OPERATION_RELATION_SYMBOLS_4 = [
    [r'\ncong', r'\nleq', r'\ngeq', r'\nsubseteq'], 
    [r'\nmid', r'\nleqq', r'\ngeqq', r'\nsupseteq'], 
    [r'\nparallel', r'\nleqslant', r'\ngeqslant', r'\nsubseteqq'], 
    [r'\nshortmid', r'\nless', r'\ngtr', r'\nsupseteqq'], 
    [r'\nshortparallel', r'\nprec', r'\nsucc', r'\subsetneq'], 
    [r'\nsim', r'\npreceq', r'\nsucceq', r'\supsetneq'], 
    [r'\nVDash', r'\precnapprox', r'\succnapprox', r'\subsetneqq'], 
    [r'\nvDash', r'\precnsim', r'\succnsim', r'\supsetneqq'], 
    [r'\nvdash', r'\lnapprox', r'\gnapprox', r'\varsubsetneq'], 
    [r'\ntriangleleft', r'\lneq', r'\gneq', r'\varsupsetneq'], 
    [r'\ntrianglelefteq', r'\lneqq', r'\gneqq', r'\varsubsetneqq'], 
    [r'\ntriangleright', r'\lnsim', r'\gnsim', r'\varsupsetneqq'], 
    [r'\ntrianglerighteq', r'\lvertneqq', r'\gvertneqq', '']]

ARROW_SYMBOLS1 = []
ARROW_SYMBOLS2 = []
ARROW_SYMBOLS3 = []
ARROW_SYMBOLS4 = []
MISCELLANEUOS_SYMBOLS = []
MATH_MODE_ACCENTS = []
OTHER_STYLES_MATH_MODE_ONLY = []
FONT_SIZES = []
TEXT_MODE_ACCENTS_AND_SYMBOLS = []

class TestAll(BaseScene):

    def construct(self):
        self.init()

        self.set_colour_map((
            #('[Oo|]', ghost),
            (r'\\frac', magenta),
            (r'\\sqrt|\\lim', orange),
            (r'[a-e]|\\alpha|\\beta|\\gamma|\\delta|\\epsilon', green),
            ('h', orange),
            (r'[p-s]|\\pi|\\rho\|\\sigma|\\sin', yellow),
            ('x', red),
            ('y', magenta),
            ('z', cyan)))
        
        def interpose(tokens: List[List[str]]):
            G = []
            for row in range(len(tokens)):
                H = []
                for col in range(len(tokens[0])):
                    token = tokens[row][col]
                    print(token, end='')
                    tex = self.make_tex(token)
                    text = self.make_text(token)
                    H.append(tex)
                    H.append(text)
                G.append(VGroup(*H).arrange(RIGHT))
            G = VGroup(*G).arrange(DOWN)
            self.add(G)
            self.wait(10)
            self.remove(G)

        def transpose(tokens: List[List[str]]):
            G = []
            for row in range(len(tokens[0])):
                H = []
                for col in range(len(tokens)):
                    token = tokens[col][row]
                    tex = self.make_tex(token)
                    text = self.make_text(token)
                    H.append(tex)
                    H.append(text)
                G.append(VGroup(*H).arrange(RIGHT))
            G = VGroup(*G).arrange(DOWN)
            self.add(G)
            self.wait(10)
            self.remove(G)

        transpose(GREEK_AND_HEBREW_LETTERS)
        transpose(LATEX_MATH_CONSTRUCTS)
        transpose(DELIMITERS)
        transpose(VARIABLE_SIZED_SYMBOLS)
        transpose(STANDARD_FUNCTION_NAMES)
        interpose(BINARY_OPERATION_RELATION_SYMBOLS_1)
        interpose(BINARY_OPERATION_RELATION_SYMBOLS_2)
        interpose(BINARY_OPERATION_RELATION_SYMBOLS_3)
        interpose(BINARY_OPERATION_RELATION_SYMBOLS_4)
