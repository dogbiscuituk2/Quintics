from painter import *
from base_scene import BaseScene

# https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf

# LATEX Mathematical Symbols
# The more unusual symbols are not defined in base LATEX (NFSS) and require \usepackage{amssymb}

GREEK_AND_HEBREW_LETTERS = [
    [r'\alpha', r'\kappa', r'\psi', r'\digamma', r'\Delta', r'\Theta'],
    [r'\beta', r'\lambda', r'\rho', r'\varepsilon', r'\Gamma', r'\Upsilon'],
    [r'\chi', r'\mu', r'\sigma', r'\varkappa', r'\Lambda', r'\Xi'],
    [r'\delta', r'\nu', r'\tau', r'\varphi', r'\Omega'],
    [r'\epsilon', r'o', r'\theta', r'\varpi', r'\Phi', r'\aleph'],
    [r'\eta', r'\omega', r'\upsilon', r'\varrho', r'\Pi', r'\beth'],
    [r'\gamma', r'\phi', r'\xi', r'\varsigma', r'\Psi', r'\daleth'],
    [r'\iota', r'\pi', r'\zeta', r'\vartheta', r'\Sigma', r'\gimel'],
]

LATEX_MATH_CONSTRUCTS = [
    [r'\frac{abc}{xyz}', r'\overline{abc}', r'\overrightarrow{abc}'],
    ["f'", r'\underline{abc}', r'\overleftarrow{abc}'],
    [r'\sqrt{abc}', r'\widehat{abc}', r'\overbrace{abc}'],
    [r'\sqrt[n]{abc}', r'\widetilde{abc}', r'\underbrace{abc}'],
]

DELIMITERS = [
    ['|', r'\{', r'\lfloor', '/', r'\Uparrow', r'\llcorner'],
    [r'\vert', r'\}', r'\rfloor', r'\backslash', r'\uparrow', r'\lrcorner'],
    [r'\|', r'\langle', r'\lceil', '[', r'\Downarrow', r'\ulcorner'],
    [r'\Vert', r'\rangle', r'\rceil', ']', r'\downarrow', r'\urcorner'],
]

# Use the pair \lefts1 and \rights1 to match height of delimiters s1 and s2 to the height of their contents,
# e.g. \left| expr \right| -or- \left\{ expr \right\} -or- \left\Vert expr \right.

VARIABLE_SIZED_SYMBOLS = [ # displayed formulae show larger version
    [r'\sum', r'\int', r'\biguplus', r'\bigoplus', r'\bigvee'],
    [r'\prod', r'\oint', r'\bigcap', r'\bigotimes', r'\bigwedge'],
    [r'\coprod', r'\iint', r'\bigcup', r'\bigodot', r'\bigsqcup'],
]
STANDARD_FUNCTION_NAMES = [ # Function names should appear in Roman, not Italic.
    [r'\arccos', r'\arcsin', r'\arctan', r'\arg'],
    [r'\cos', r'\cosh', r'\cot', r'\coth'],
    [r'\csc', r'\deg', r'\det', r'\dim'],
    [r'\exp', r'\gcd', r'\hom', r'\inf'],
    [r'\ker', r'\lg', r'\lim', r'\liminf'],
    [r'\limsup', r'\ln ', r'\log', r'\max'],
    [r'\min', r'\Pr', r'\sec', r'\sin'],
    [r'\sinh', r'\sup', r'\tan', r'\tanh'],
]
BINARY_OPERATION_RELATION_SYMBOLS_1_A = [
    [r'\ast', r'\pm', r'\cap', r'\lhd'],
    [r'\star', r'\mp', r'\cup', r'\rhd'],
    [r'\cdot', r'\amalg', r'\uplus', r'\triangleleft'],
    [r'\circ', r'\odot', r'\sqcap', r'\triangleright'],
    [r'\bullet', r'\ominus', r'\sqcup', r'\unlhd'],
    [r'\bigcirc', r'\oplus', r'\wedge', r'\unrhd'],
    [r'\diamond', r'\oslash', r'\vee', r'\bigtriangledown'],
    [r'\times', r'\otimes', r'\dagger', r'\bigtriangleup'],
    [r'\div', r'\wr', r'\ddagger', r'\setminus'],
]
BINARY_OPERATION_RELATION_SYMBOLS_1_B = [
    [r'\centerdot', r'\Box', r'\barwedge', r'\veebar'],
    [r'\circledast', r'\boxplus', r'\curlywedge', r'\curlyvee'],
    [r'\circledcirc', r'\boxminus', r'\Cap', r'\Cup'],
    [r'\circleddash', r'\boxtimes', r'\bot', r'\top'],
    [r'\dotplus', r'\boxdot', r'\intercal', r'\rightthreetimes'],
    [r'\divideontimes', r'\square', r'\doublebarwedge', r'\leftthreetimes'],
]
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
    [r'\models', r'\in', r'\ni', r'\notin'],
]
BINARY_OPERATION_RELATION_SYMBOLS_3_A = [
    [r'\approxeq', r'\leqq', r'\geqq', r'\lessgtr'],
    [r'\thicksim', r'\leqslant', r'\geqslant', r'\lesseqgtr'],
    [r'\backsim', r'\lessapprox', r'\gtrapprox', r'\lesseqqgtr'],
    [r'\backsimeq', r'\lll', r'\ggg', r'\gtreqqless'],
    [r'\triangleq', r'\lessdot', r'\gtrdot', r'\gtreqless'],
    [r'\circeq', r'\lesssim', r'\gtrsim', r'\gtrless'],
    [r'\bumpeq', r'\eqslantless', r'\eqslantgtr', r'\backepsilon'],
    [r'\Bumpeq', r'\precsim', r'\succsim', r'\between'],
    [r'\doteqdot', r'\precapprox', r'\succapprox', r'\pitchfork'],
]
BINARY_OPERATION_RELATION_SYMBOLS_3_B = [
    [r'\thickapprox', r'\Subset', r'\Supset', r'\shortmid'],
    [r'\fallingdotseq', r'\subseteqq', r'\supseteqq', r'\smallfrown'],
    [r'\risingdotseq', r'\sqsubset', r'\sqsupset', r'\smallsmile'],
    [r'\varpropto', r'\preccurlyeq', r'\succcurlyeq', r'\Vdash'],
    [r'\therefore', r'\curlyeqprec', r'\curlyeqsucc', r'\vDash'],
    [r'\because', r'\blacktriangleleft', r'\blacktriangleright', r'\Vvdash'],
    [r'\eqcirc', r'\trianglelefteq', r'\trianglerighteq', r'\shortparallel'],
    [r'\neq', r'\vartriangleleft', r'\vartriangleright', r'\nshortparallel'],
]
BINARY_OPERATION_RELATION_SYMBOLS_4_A = [
    [r'\ncong', r'\nleq', r'\ngeq', r'\nsubseteq'],
    [r'\nmid', r'\nleqq', r'\ngeqq', r'\nsupseteq'],
    [r'\nparallel', r'\nleqslant', r'\ngeqslant', r'\nsubseteqq'],
    [r'\nshortmid', r'\nless', r'\ngtr', r'\nsupseteqq'],
    [r'\nshortparallel', r'\nprec', r'\nsucc', r'\subsetneq'],
    [r'\nsim', r'\npreceq', r'\nsucceq', r'\supsetneq'],
]
BINARY_OPERATION_RELATION_SYMBOLS_4_B = [
    [r'\nVDash', r'\precnapprox', r'\succnapprox', r'\subsetneqq'],
    [r'\nvDash', r'\precnsim', r'\succnsim', r'\supsetneqq'],
    [r'\nvdash', r'\lnapprox', r'\gnapprox', r'\varsubsetneq'],
    [r'\ntriangleleft', r'\lneq', r'\gneq', r'\varsupsetneq'],
    [r'\ntrianglelefteq', r'\lneqq', r'\gneqq', r'\varsubsetneqq'],
    [r'\ntriangleright', r'\lnsim', r'\gnsim', r'\varsupsetneqq'],
    [r'\ntrianglerighteq', r'\lvertneqq', r'\gvertneqq'],
]
ARROW_SYMBOLS_1 = [
    [r'\leftarrow', r'\longleftarrow', r'\uparrow'],
    [r'\Leftarrow', r'\Longleftarrow', r'\Uparrow'],
    [r'\rightarrow', r'\longrightarrow', r'\downarrow'],
    [r'\Rightarrow', r'\Longrightarrow', r'\Downarrow'],
    [r'\leftrightarrow', r'\longleftrightarrow', r'\updownarrow'],
    [r'\Leftrightarrow', r'\Longleftrightarrow', r'\Updownarrow'],
]
ARROW_SYMBOLS_2 = [
    [r'\mapsto', r'\longmapsto', r'\nearrow'],
    [r'\hookleftarrow', r'\hookrightarrow', r'\searrow'],
    [r'\leftharpoonup', r'\rightharpoonup', r'\swarrow'],
    [r'\leftharpoondown', r'\rightharpoondown', r'\nwarrow'],
    [r'\rightleftharpoons', r'\leadsto'],
]
ARROW_SYMBOLS_3 = [
    [r'\dashrightarrow', r'\dashleftarrow', r'\leftleftarrows'],
    [r'\leftrightarrows', r'\Lleftarrow', r'\twoheadleftarrow'],
    [r'\leftarrowtail', r'\looparrowleft', r'\leftrightharpoons'],
    [r'\curvearrowleft', r'\circlearrowleft', r'\Lsh'],
    [r'\upuparrows', r'\upharpoonleft', r'\downharpoonleft'],
    [r'\multimap', r'\leftrightsquigarrow', r'\rightrightarrows'],
    [r'\rightleftarrows', r'\rightrightarrows', r'\rightleftarrows'],
    [r'\twoheadrightarrow', r'\rightarrowtail', r'\looparrowright'],
    [r'\rightleftharpoons', r'\curvearrowright', r'\circlearrowright'],
    [r'\Rsh', r'\downdownarrows', r'\upharpoonright'],
    [r'\downharpoonright', r'\rightsquigarrow'],
]
ARROW_SYMBOLS_4 = [
    [r'\nleftarrow', r'\nrightarrow', r'\nLeftarrow'],
    [r'\nRightarrow', r'\nleftrightarrow', r'\nLeftrightarrow'],
]
MISCELLANEUOS_SYMBOLS_1 = [
    [r'\infty', r'\forall', r'\Bbbk', r'\wp'],
    [r'\nabla', r'\exists', r'\bigstar', r'\angle'],
    [r'\partial', r'\nexists', r'\diagdown', r'\measuredangle'],
    [r'\eth', r'\emptyset', r'\diagup', r'\sphericalangle'],
    [r'\clubsuit', r'\varnothing', r'\Diamond', r'\complement'],
    [r'\diamondsuit', r'\imath', r'\Finv', r'\triangledown'],
    [r'\heartsuit', r'\jmath', r'\Game', r'\triangle'],
    [r'\spadesuit', r'\ell', r'\hbar', r'\vartriangle'],
]
MISCELLANEUOS_SYMBOLS_2 = [
    [r'\cdots', r'\iiiint', r'\hslash', r'\blacklozenge'],
    [r'\vdots', r'\iiint', r'\lozenge', r'\blacksquare'],
    [r'\ldots', r'\iint', r'\mho', r'\blacktriangle'],
    [r'\ddots', r'\sharp', r'\prime', r'\blacktriangledown'],
    [r'\Im', r'\flat', r'\square', r'\backprime'],
    [r'\Re', r'\natural', r'\surd', r'\circledS'],
]
MATH_MODE_ACCENTS = [
    [r'\acute{a}', r'\bar{a}', r'\Acute{\Acute{A}}', r'\Bar{\Bar{A}}'],
    [r'\breve{a}', r'\check{a}', r'\Breve{\Breve{A}}', r'\Check{\Check{A}}'],
    [r'\ddot{a}', r'\dot{a}', r'\Ddot{\Ddot{A}}', r'\Dot{\Dot{A}}'],
    [r'\grave{a}', r'\hat{a}', r'\Grave{\Grave{A}}', r'\Hat{\Hat{A}}'],
    [r'\tilde{a}', r'\vec{a}', r'\Tilde{\Tilde{A}}', r'\Vec{\Vec{A}}'],
]
OTHER_STYLES_MATH_MODE_ONLY = [
    [r'\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZ}'],
    [r'\mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}'],
    [r'\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}'],
    [r'\mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}'],
    [r'\mathbf{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}'],
]

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
            for line in tokens:
                H = []
                for token in line:
                    print(token, end=' ')
                    tex = self.make_tex(token)
                    text = self.make_text(token)
                    H.append(tex)
                    H.append(text)
                G.append(VGroup(*H).arrange(RIGHT))
            G = VGroup(*G).arrange(DOWN)
            self.add(G)
            self.wait(5)
            self.remove(G)

        def transpose(tokens: List[List[str]]):
            G = []
            for row in range(len(tokens[0])):
                H = []
                for col in range(len(tokens)):
                    token = tokens[col][row]

                    #tex = self.make_tex(token)
                    #text = self.make_text(token)
                    #H.append(tex)
                    #H.append(text)

                    textext = self.make_tex(f'{token}&\\displaytext{{ {token} }}')
                    H.append(textext)

                G.append(VGroup(*H).arrange(RIGHT))
            G = VGroup(*G).arrange(DOWN)
            self.add(G)
            self.wait(10)
            self.remove(G)

        interpose(GREEK_AND_HEBREW_LETTERS)
        interpose(LATEX_MATH_CONSTRUCTS)
        interpose(DELIMITERS)
        interpose(VARIABLE_SIZED_SYMBOLS)
        interpose(STANDARD_FUNCTION_NAMES)
        interpose(BINARY_OPERATION_RELATION_SYMBOLS_1_A)
        interpose(BINARY_OPERATION_RELATION_SYMBOLS_1_B)
        interpose(BINARY_OPERATION_RELATION_SYMBOLS_2)
        interpose(BINARY_OPERATION_RELATION_SYMBOLS_3_A)
        interpose(BINARY_OPERATION_RELATION_SYMBOLS_3_B)
        interpose(BINARY_OPERATION_RELATION_SYMBOLS_4_A)
        interpose(BINARY_OPERATION_RELATION_SYMBOLS_4_B)
        interpose(ARROW_SYMBOLS_1)
        interpose(ARROW_SYMBOLS_2)
        interpose(ARROW_SYMBOLS_3)
        interpose(ARROW_SYMBOLS_4)
        interpose(MISCELLANEUOS_SYMBOLS_1)
        interpose(MISCELLANEUOS_SYMBOLS_2)
        interpose(MATH_MODE_ACCENTS)
        interpose(OTHER_STYLES_MATH_MODE_ONLY)
