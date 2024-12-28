#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lists of Latex tokens.

The tokens are grouped into categories such as Greek letters, mathematical 
symbols, delimiters, integrals, large operators, functions, operators, arrows, 
miscellaneous symbols, accents, styles and fonts.
The tokens are used to create regular expression patterns that are used to 
match the tokens in a MathTex object.
The patterns are used to colour the tokens in the MathTex object.

The tokens are taken from the following sources:
- LATEX Mathematical Symbols
- TEX Mathematical Symbols
- The Comprehensive LATEX Symbol List
"""

from re import escape
from typing import List

def make_pattern(symbols: List[str]) -> str:
    matches = map(
        escape,
        [symbol for symbol in symbols if symbol])
    return f"^({'|'.join(matches)})$"

# https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf
# LATEX Mathematical Symbols
# The more unusual symbols are not defined in base LATEX (NFSS) and require 
# \usepackage{amssymb} Use the pair \lefts1 and \rights1 to match height of 
# delimiters s1 and s2 to the height of their contents,
# eg \left| expr \right| or \left\{ expr \right\} or \left\Vert expr \right.

SYM_GREEK = [
    r'\alpha', r'\nu', r'\Gamma', r'\varepsilon',
    r'\beta', r'\xi',  r'\Delta', r'\vartheta',
    r'\gamma', 'o', r'\Theta', r'\varkappa',
    r'\delta', r'\pi', r'\Lambda', r'\varpi',
    r'\epsilon', r'\rho', r'\Xi', r'\varrho',
    r'\zeta', r'\sigma', r'\Pi', r'\varsigma',
    r'\eta', r'\tau', r'\Sigma', r'\varphi',
    r'\theta', r'\upsilon', r'\Upsilon', '',
    r'\iota', r'\phi', r'\Phi', r'\aleph',
    r'\kappa', r'\chi', r'\Psi', r'\beth',
    r'\lambda', r'\psi', r'\Omega', r'\gimel',
    r'\mu', r'\omega', r'\digamma', r'\daleth',
]
SYM_MATH = [
    r'\overline', r'\overrightarrow',
    r'\underline', r'\overleftarrow',
    r'\widehat', r'\overbrace',
    r'\widetilde', r'\underbrace',
]
SYM_DELIM = [
    '|', r'\{', r'\lfloor', '/', r'\Uparrow', r'\llcorner',
    r'\vert', r'\}', r'\rfloor', r'\backslash', r'\uparrow', r'\lrcorner',
    r'\|', r'\langle', r'\lceil', '[', r'\Downarrow', r'\ulcorner',
    r'\Vert', r'\rangle', r'\rceil', ']', r'\downarrow', r'\urcorner',
]
SYM_INT = [
    r'\int', r'\iint', r'\iiint', r'\iiiint', r'\idotsint', r'\oint',
]
SYM_LARGE = [ # Displayed formulae show larger version.
    r'\sum', r'\biguplus', r'\bigoplus', r'\bigvee',
    r'\prod', r'\bigcap', r'\bigotimes', r'\bigwedge',
    r'\coprod', r'\bigcup', r'\bigodot', r'\bigsqcup',
]
SYM_FUNC = [ # Should appear in Roman, not Italic.
    r'\arccos', r'\arcsin', r'\arctan', r'\arg',
    r'\cos', r'\cosh', r'\cot', r'\coth',
    r'\csc', r'\deg', r'\det', r'\dim',
    r'\exp', r'\gcd', r'\hom', r'\inf',
    r'\ker', r'\lg', r'\lim', r'\liminf',
    r'\limsup', r'\ln', r'\log', r'\max',
    r'\min', r'\Pr', r'\sec', r'\sin',
    r'\sinh', r'\sup', r'\tan', r'\tanh',
]
SYM_OPS = [
    r'\ast', r'\pm', r'\cap', r'\lhd',
    r'\star', r'\mp', r'\cup', r'\rhd',
    r'\cdot', r'\amalg', r'\uplus', r'\triangleleft',
    r'\circ', r'\odot', r'\sqcap', r'\triangleright',
    r'\bullet', r'\ominus', r'\sqcup', r'\unlhd',
    r'\bigcirc', r'\oplus', r'\wedge', r'\unrhd',
    r'\diamond', r'\oslash', r'\vee', r'\bigtriangledown',
    r'\times', r'\otimes', r'\dagger', r'\bigtriangleup',
    r'\div', r'\wr', r'\ddagger', r'\setminus',
    r'\centerdot', r'\Box', r'\barwedge', r'\veebar',
    r'\circledast', r'\boxplus', r'\curlywedge', r'\curlyvee',
    r'\circledcirc', r'\boxminus', r'\Cap', r'\Cup',
    r'\circleddash', r'\boxtimes', r'\bot', r'\top',
    r'\dotplus', r'\boxdot', r'\intercal', r'\rightthreetimes',
    r'\divideontimes', r'\square', r'\doublebarwedge', r'\leftthreetimes',
    r'\equiv', r'\leq', r'\geq', r'\perp', 
    r'\cong', r'\prec', r'\succ', r'\mid', 
    r'\neq', r'\preceq', r'\succeq', r'\parallel', 
    r'\sim', r'\ll', r'\gg', r'\bowtie', 
    r'\simeq', r'\subset', r'\supset', r'\Join', 
    r'\approx', r'\subseteq', r'\supseteq', r'\ltimes', 
    r'\asymp', r'\sqsubset', r'\sqsupset', r'\rtimes', 
    r'\doteq', r'\sqsubseteq', r'\sqsupseteq', r'\smile', 
    r'\propto', r'\dashv', r'\vdash', r'\frown', 
    r'\models', r'\in', r'\ni', r'\notin',
    r'\approxeq', r'\leqq', r'\geqq', r'\lessgtr',
    r'\thicksim', r'\leqslant', r'\geqslant', r'\lesseqgtr',
    r'\backsim', r'\lessapprox', r'\gtrapprox', r'\lesseqqgtr',
    r'\backsimeq', r'\lll', r'\ggg', r'\gtreqqless',
    r'\triangleq', r'\lessdot', r'\gtrdot', r'\gtreqless',
    r'\circeq', r'\lesssim', r'\gtrsim', r'\gtrless',
    r'\bumpeq', r'\eqslantless', r'\eqslantgtr', r'\backepsilon',
    r'\Bumpeq', r'\precsim', r'\succsim', r'\between',
    r'\doteqdot', r'\precapprox', r'\succapprox', r'\pitchfork',
    r'\thickapprox', r'\Subset', r'\Supset', r'\shortmid',
    r'\fallingdotseq', r'\subseteqq', r'\supseteqq', r'\smallfrown',
    r'\risingdotseq', r'\sqsubset', r'\sqsupset', r'\smallsmile',
    r'\varpropto', r'\preccurlyeq', r'\succcurlyeq', r'\Vdash',
    r'\therefore', r'\curlyeqprec', r'\curlyeqsucc', r'\vDash',
    r'\because', r'\blacktriangleleft', r'\blacktriangleright', r'\Vvdash',
    r'\eqcirc', r'\trianglelefteq', r'\trianglerighteq', r'\shortparallel',
    r'\neq', r'\vartriangleleft', r'\vartriangleright', r'\nshortparallel',
    r'\ncong', r'\nleq', r'\ngeq', r'\nsubseteq',
    r'\nmid', r'\nleqq', r'\ngeqq', r'\nsupseteq',
    r'\nparallel', r'\nleqslant', r'\ngeqslant', r'\nsubseteqq',
    r'\nshortmid', r'\nless', r'\ngtr', r'\nsupseteqq',
    r'\nshortparallel', r'\nprec', r'\nsucc', r'\subsetneq',
    r'\nsim', r'\npreceq', r'\nsucceq', r'\supsetneq',
    r'\nVDash', r'\precnapprox', r'\succnapprox', r'\subsetneqq',
    r'\nvDash', r'\precnsim', r'\succnsim', r'\supsetneqq',
    r'\nvdash', r'\lnapprox', r'\gnapprox', r'\varsubsetneq',
    r'\ntriangleleft', r'\lneq', r'\gneq', r'\varsupsetneq',
    r'\ntrianglelefteq', r'\lneqq', r'\gneqq', r'\varsubsetneqq',
    r'\ntriangleright', r'\lnsim', r'\gnsim', r'\varsupsetneqq',
    r'\ntrianglerighteq', r'\lvertneqq', r'\gvertneqq', '',
]
SYM_ARROW = [
    r'\leftarrow', r'\rightarrow', r'\leftrightarrow', r'\uparrow',
    r'\nleftarrow', r'\nrightarrow', r'\nleftrightarrow', r'\downarrow',
    r'\longleftarrow', r'\longrightarrow', r'\longleftrightarrow', r'\updownarrow',
    r'\Leftarrow', r'\Rightarrow', r'\Leftrightarrow', r'\Uparrow',
    r'\nLeftarrow', r'\nRightarrow', r'\nLeftrightarrow', r'\Downarrow',
    r'\Longleftarrow', r'\Longrightarrow', r'\Longleftrightarrow', r'\Updownarrow',
    r'\leftleftarrows', r'\rightrightarrows', r'\leftrightarrows', r'\rightleftarrows',
    r'\hookleftarrow', r'\hookrightarrow', r'\leftrightsquigarrow', r'\upuparrows',
    r'\leftharpoonup', r'\rightharpoonup', r'\rightleftharpoons', r'\downdownarrows',
    r'\leftharpoondown', r'\rightharpoondown', r'\leftrightharpoons', r'\multimap',
    r'\upharpoonleft', r'\upharpoonright', r'\downharpoonleft', r'\downharpoonright',
    r'\dashleftarrow', r'\dashrightarrow', r'\mapsto', r'\longmapsto',
    r'\Lleftarrow', r'\Rrightarrow', r'\rightsquigarrow', r'\leadsto',
    r'\twoheadleftarrow', r'\twoheadrightarrow', r'\leftarrowtail', r'\rightarrowtail',
    r'\looparrowleft', r'\looparrowright', r'\curvearrowleft', r'\curvearrowright',
    r'\circlearrowleft', r'\circlearrowright', r'\Lsh', r'\Rsh',
    r'\nearrow', r'\searrow', r'\swarrow', r'\nwarrow',
]
SYM_MISC = [
    r'\infty', r'\forall', r'\Bbbk', r'\wp',
    r'\nabla', r'\exists', r'\bigstar', r'\angle',
    r'\partial', r'\nexists', r'\diagdown', r'\measuredangle',
    r'\eth', r'\emptyset', r'\diagup', r'\sphericalangle',
    r'\clubsuit', r'\varnothing', r'\Diamond', r'\complement',
    r'\diamondsuit', r'\imath', r'\Finv', r'\triangledown',
    r'\heartsuit', r'\jmath', r'\Game', r'\triangle',
    r'\spadesuit', r'\ell', r'\hbar', r'\vartriangle',
    r'\cdots', r'\iiiint', r'\hslash', r'\blacklozenge',
    r'\vdots', r'\iiint', r'\lozenge', r'\blacksquare',
    r'\ldots', r'\iint', r'\mho', r'\blacktriangle',
    r'\ddots', r'\sharp', r'\prime', r'\blacktriangledown',
    r'\Im', r'\flat', r'\square', r'\backprime',
    r'\Re', r'\natural', r'\surd', r'\circledS',
]
SYM_ACCENT = [
    r'\acute', r'\bar', r'\Acute', r'\Bar',
    r'\breve', r'\check', r'\Breve', r'\Check',
    r'\ddot', r'\dot', r'\Ddot', r'\Dot',
    r'\grave', r'\hat', r'\Grave', r'\Hat',
    r'\tilde', r'\vec', r'\Tilde', r'\Vec',
]
SYM_STYLE = [
    r'\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZ}',
    r'\mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}',
    r'\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}',
    r'\mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}',
    r'\mathbf{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}',
]
SYM_FONT = [
    r'\displaystyle \int f^{-1}(x-x_a)\,dx}',
    r'\textstyle \int f^{-1}(x-x_a)\,dx}',
    r'\scriptstyle \int f^{-1}(x-x_a)\,dx}',
    r'\scriptscriptstyle \int f^{-1}(x-x_a)\,dx}',
]

PAT_GREEK = make_pattern(SYM_GREEK)
PAT_MATH = make_pattern(SYM_MATH)
PAT_DELIM = make_pattern(SYM_DELIM)
PAT_INT = make_pattern(SYM_INT)
PAT_LARGE = make_pattern(SYM_LARGE)
PAT_FUNC = make_pattern(SYM_FUNC)
PAT_OPS = make_pattern(SYM_OPS)
PAT_ARROW = make_pattern(SYM_ARROW)
PAT_MISC = make_pattern(SYM_MISC)
PAT_ACCENT = make_pattern(SYM_ACCENT)
PAT_STYLE = make_pattern(SYM_STYLE)
PAT_FONT = make_pattern(SYM_FONT)
PAT_SYM = make_pattern(SYM_MATH + SYM_ACCENT)

# https://www.cmor-faculty.rice.edu/~heinken/latex/symbol-list.pdf
# TEX Mathematical Symbols - Paul Taylor - 1 June 1993
# The following mathematical symbols are available in plain TEX, 
# mssymb.tex (or amssymb.sty) and stmaryrd.sty (#).

SYM_ALL = [
    r'\aleph',
    r'\alpha',
    r'\amalg',
    r'\angle',
    r'\approx',
    r'\approxeq',
    r'\arccos',
    r'\arcsin',
    r'\arctan',
    r'\arg',
#   r'\Arrownot',
#   r'\arrownot',
    r'\ast',
    r'\asymp',
    r'\backepsilon',
    r'\backprime',
    r'\backsim',
    r'\backsimeq',
    r'\backslash',
#   r'\baro',
    r'\barwedge',
#   r'\bbslash',
    r'\because',
    r'\beta',
    r'\beth',
    r'\between',
#   r'\bigbox',
    r'\bigcap',
    r'\bigcirc',
    r'\bigcup',
#   r'\bigcurlyvee',
#   r'\bigcurlywedge',
#   r'\biginterleave',
#   r'\bignplus',
    r'\bigodot',
    r'\bigoplus',
    r'\bigotimes',
#   r'\bigparallel',
#   r'\bigsqcap',
    r'\bigsqcup',
    r'\bigstar',
    r'\bigtriangledown',
#   r'\bigtriangledown',
    r'\bigtriangleup',
#   r'\bigtriangleup',
    r'\biguplus',
    r'\bigvee',
    r'\bigwedge',
#   r'\binampersand',
#   r'\bindnasrepma',
    r'\blacklozenge',
    r'\blacksquare',
    r'\blacktriangle',
    r'\blacktriangledown',
    r'\blacktriangleleft',
    r'\blacktriangleright',
    r'\bmod',
    r'\bot',
    r'\bowtie',
#   r'\boxast',
#   r'\boxbar',
#   r'\boxbox',
#   r'\boxbslash',
#   r'\boxcircle',
#   r'\boxdot',
    r'\boxdot',
#   r'\boxempt',
    r'\boxminus',
    r'\boxplus',
#   r'\boxslash',
    r'\boxtimes',
    r'\bullet',
    r'\Bumpeq',
    r'\bumpeq',
    r'\Cap',
    r'\cap',
    r'\cdot',
    r'\cdotp',
    r'\cdots',
    r'\centerdot',
    r'\checkmark',
    r'\chi',
    r'\circ',
    r'\circeq',
    r'\circlearrowleft',
    r'\circlearrowright',
    r'\circledast',
    r'\circledcirc',
    r'\circleddash',
    r'\circledR',
    r'\circledS',
    r'\clubsuit',
    r'\colon',
    r'\complement',
    r'\cong',
    r'\coprod',
    r'\copyright',
    r'\cos',
    r'\cosh',
    r'\cot',
    r'\coth',
    r'\csc',
    r'\Cup',
    r'\cup',
    r'\curlyeqprec',
    r'\curlyeqsucc',
    r'\curlyvee',
#   r'\curlyveedownarrow',
#   r'\curlyveeuparrow',
    r'\curlywedge',
#   r'\curlywedgedownarrow',
#   r'\curlywedgeuparrow',
    r'\curvearrowleft',
    r'\curvearrowright',
    r'\dag',
    r'\dagger',
    r'\daleth',
    r'\dashv',
    r'\ddag',
    r'\ddagger',
    r'\ddots',
    r'\deg',
    r'\Delta',
    r'\delta',
    r'\det',
    r'\diamond',
    r'\diamondsuit',
    r'\digamma',
    r'\dim',
    r'\div',
    r'\divideontimes',
    r'\Doteq',
    r'\doteq',
    r'\doteqdot',
    r'\dotplus',
    r'\dots',
    r'\doublebarwedge',
    r'\doublecap',
    r'\doublecup',
    r'\Downarrow',
    r'\downarrow',
    r'\downdownarrows',
    r'\downharpoonleft',
    r'\downharpoonright',
    r'\ell',
    r'\emptyset',
    r'\epsilon',
    r'\eqcirc',
    r'\eqsim',
    r'\eqslantgtr',
    r'\eqslantless',
    r'\equiv',
    r'\eta',
    r'\eth',
    r'\exists',
    r'\exp',
    r'\fallingdotseq',
#   r'\fatbslash',
#   r'\fatsemi',
#   r'\fatslash',
    r'\flat',
    r'\forall',
    r'\frown',
    r'\Gamma',
    r'\gamma',
    r'\gcd',
    r'\geq',
    r'\geqq',
    r'\geqslant',
    r'\gg',
    r'\ggg',
    r'\gggtr',
    r'\gimel',
    r'\gnapprox',
    r'\gneq',
    r'\gneqq',
    r'\gnsim',
    r'\gtrapprox',
    r'\gtrdot',
    r'\gtreqless',
    r'\gtreqqless',
    r'\gtrless',
    r'\gtrsim',
    r'\gvertneqq',
    r'\hbar',
    r'\hbar',
    r'\heartsuit',
    r'\hom',
    r'\hslash',
    r'\iff',
    r'\Im',
    r'\imath',
    r'\in',
    r'\inf',
    r'\infty',
#   r'\inplus',
    r'\intercal',
#   r'\interleave',
    r'\intop',
    r'\iota',
    r'\jmath',
    r'\kappa',
    r'\ker',
    r'\Lambda',
    r'\lambda',
    r'\langle',
#   r'\Lbag',
#   r'\lbag',
    r'\lbrace',
    r'\lceil',
    r'\ldotp',
    r'\ldots',
    r'\Leftarrow',
    r'\leftarrow',
    r'\leftarrowtail',
#   r'\leftarrowtriangle',
    r'\leftharpoondown',
    r'\leftharpoonup',
    r'\leftleftarrows',
    r'\Leftrightarrow',
    r'\leftrightarrow',
#   r'\leftrightarroweq',
    r'\leftrightarrows',
#   r'\leftrightarrowtriangle',
    r'\leftrightharpoons',
    r'\leftrightsquigarrow',
#   r'\leftslice',
    r'\leftthreetimes',
    r'\leq',
    r'\leqq',
    r'\leqslant',
    r'\lessapprox',
    r'\lessdot',
    r'\lesseqgtr',
    r'\lesseqqgtr',
    r'\lessgtr',
    r'\lesssim',
    r'\lfloor',
    r'\lg',
    r'\lhook',
#   r'\lightning',
    r'\lim',
    r'\liminf',
    r'\limsup',
    r'\ll',
#   r'\llbracket',
#   r'\llceil',
    r'\llcorner',
    r'\Lleftarrow',
#   r'\llfloor',
    r'\lll',
    r'\llless',
#   r'\llparenthesis',
    r'\ln',
    r'\lnapprox',
    r'\lneq',
    r'\lneqq',
    r'\lnsim',
    r'\log',
#   r'\Longarrownot',
#   r'\longarrownot',
    r'\Longleftarrow',
    r'\longleftarrow',
    r'\Longleftrightarrow',
    r'\longleftrightarrow',
#   r'\Longmapsfrom',
#   r'\longmapsfrom',
#   r'\Longmapsto',
    r'\longmapsto',
    r'\Longrightarrow',
    r'\longrightarrow',
    r'\looparrowleft',
    r'\looparrowright',
    r'\lozenge',
    r'\lrcorner',
    r'\Lsh',
    r'\ltimes',
    r'\lvertneqq',
    r'\maltese',
#   r'\Mapsfrom',
#   r'\mapsfrom',
#   r'\Mapsfromchar',
#   r'\mapsfromchar',
#   r'\Mapsto',
#   r'\Mapstochar',
    r'\mapstochar',
    r'\max',
    r'\measuredangle',
#   r'\merge',
    r'\mho',
    r'\mid',
    r'\min',
#   r'\minuso',
    r'\models',
#   r'\moo',
    r'\mp',
    r'\mu',
    r'\multimap',
    r'\nabla',
### r'\napprox',
    r'\natural',
    r'\ncong',
    r'\nearrow',
    r'\neg',
    r'\neq',
    r'\nexists',
    r'\ngeq',
    r'\ngeqq',
    r'\ngeqslant',
    r'\ngtr',
    r'\ni',
#   r'\niplus',
    r'\nLeftarrow',
    r'\nleftarrow',
    r'\nLeftrightarrow',
    r'\nleftrightarrow',
    r'\nleq',
    r'\nleqq',
    r'\nleqslant',
    r'\nless',
    r'\nmid',
#   r'\nnearrow',
#   r'\nnwarrow',
    r'\not',
    r'\notin',
    r'\nparallel',
#   r'\nplus',
    r'\nprec',
    r'\npreceq',
    r'\nRightarrow',
    r'\nrightarrow',
    r'\nshortmid',
    r'\nshortparallel',
    r'\nsim',
    r'\nsubseteq',
    r'\nsubseteqq',
    r'\nsucc',
    r'\nsucceq',
    r'\nsupseteq',
    r'\nsupseteqq',
    r'\ntriangleleft',
    r'\ntrianglelefteq',
#   r'\ntrianglelefteqslant',
    r'\ntriangleright',
    r'\ntrianglerighteq',
#   r'\ntrianglerighteqslant',
    r'\nu',
    r'\nVDash',
    r'\nVdash',
    r'\nvDash',
    r'\nvdash',
    r'\nwarrow',
#   r'\obar',
#   r'\oblong',
#   r'\obslash',
    r'\odot',
#   r'\ogreaterthan',
    r'\ointop',
#   r'\olessthan',
    r'\Omega',
    r'\omega',
    r'\ominus',
    r'\oplus',
    r'\oslash',
    r'\otimes',
#   r'\ovee',
#   r'\owedge',
    r'\P',
    r'\parallel',
    r'\partial',
    r'\perp',
    r'\Phi',
    r'\phi',
    r'\Pi',
    r'\pi',
    r'\pitchfork',
    r'\pm',
    r'\Pr',
    r'\prec',
    r'\precapprox',
    r'\preccurlyeq',
    r'\preceq',
    r'\precnapprox',
    r'\precneqq',
    r'\precnsim',
    r'\precsim',
    r'\prime',
    r'\prod',
    r'\propto',
    r'\Psi',
    r'\psi',
    r'\rangle',
#   r'\Rbag',
#   r'\rbag',
    r'\rbrace',
    r'\rceil',
    r'\Re',
    r'\Relbar',
    r'\relbar',
    r'\restriction',
    r'\rfloor',
    r'\rho',
    r'\rhook',
    r'\Rightarrow',
    r'\rightarrow',
    r'\rightarrowtail',
#   r'\rightarrowtriangle',
    r'\rightharpoondown',
    r'\rightharpoonup',
    r'\rightleftarrows',
    r'\rightleftharpoons',
    r'\rightleftharpoons',
    r'\rightrightarrows',
#   r'\rightslice',
    r'\rightsquigarrow',
    r'\rightthreetimes',
    r'\risingdotseq',
    r'\rmoustache',
#   r'\rrbracket',
#   r'\rrceil',
#   r'\rrfloor',
    r'\Rrightarrow',
#   r'\rrparenthesis',
    r'\Rsh',
    r'\rtimes',
    r'\S',
    r'\searrow',
    r'\sec',
    r'\setminus',
    r'\sharp',
#   r'\shortdownarrow',
#   r'\shortleftarrow',
    r'\shortmid',
    r'\shortparallel',
#   r'\shortrightarrow',
#   r'\shortuparrow',
    r'\Sigma',
    r'\sigma',
    r'\sim',
    r'\simeq',
    r'\sin',
    r'\sinh',
    r'\smallfrown',
    r'\smallint',
    r'\smallsetminus',
    r'\smallsmile',
    r'\smile',
    r'\spadesuit',
    r'\sphericalangle',
    r'\sqcap',
    r'\sqcup',
    r'\sqrt',
    r'\sqsubset',
    r'\sqsubseteq',
    r'\sqsupset',
    r'\sqsupseteq',
    r'\square',
#   r'\ssearrow',
#   r'\sslash',
#   r'\sswarrow',
    r'\star',
    r'\Subset',
    r'\subset',
    r'\subseteq',
    r'\subseteqq',
    r'\subsetneq',
    r'\subsetneqq',
#   r'\subsetplus',
#   r'\subsetpluseq',
    r'\succ',
    r'\succapprox',
    r'\succcurlyeq',
    r'\succeq',
    r'\succnapprox',
    r'\succneqq',
    r'\succnsim',
    r'\succsim',
    r'\sum',
    r'\sup',
    r'\Supset',
    r'\supset',
    r'\supseteq',
    r'\supseteqq',
    r'\supsetneq',
    r'\supsetneqq',
#   r'\supsetplus',
#   r'\supsetpluseq',
    r'\surd',
    r'\swarrow',
#   r'\talloblong',
    r'\tan',
    r'\tanh',
    r'\tau',
### r'\TeX',
    r'\therefore',
    r'\Theta',
    r'\theta',
    r'\thickapprox',
    r'\thicksim',
    r'\times',
    r'\top',
    r'\triangle',
    r'\triangledown',
    r'\triangleleft',
    r'\trianglelefteq',
#   r'\trianglelefteqslant',
    r'\triangleq',
    r'\triangleright',
    r'\trianglerighteq',
#   r'\trianglerighteqslant',
    r'\twoheadleftarrow',
    r'\twoheadrightarrow',
    r'\ulcorner',
    r'\Uparrow',
    r'\uparrow',
    r'\Updownarrow',
    r'\updownarrow',
    r'\upharpoonleft',
    r'\upharpoonright',
    r'\uplus',
    r'\Upsilon',
    r'\upsilon',
    r'\upuparrows',
    r'\urcorner',
#   r'\varbigcirc',
#   r'\varcopyright',
#   r'\varcurlyvee',
#   r'\varcurlywedge',
    r'\varepsilon',
    r'\varkappa',
    r'\varnothing',
#   r'\varoast',
#   r'\varobar',
#   r'\varobslash',
#   r'\varocircle',
#   r'\varodot',
#   r'\varogreaterthan',
#   r'\varolessthan',
#   r'\varominus',
#   r'\varoplus',
#   r'\varoslash',
#   r'\varotimes',
#   r'\varovee',
#   r'\varowedge',
    r'\varphi',
    r'\varpi',
    r'\varpropto',
    r'\varrho',
    r'\varsigma',
    r'\varsubsetneq',
    r'\varsubsetneqq',
    r'\varsupsetneq',
    r'\varsupsetneqq',
    r'\vartheta',
#   r'\vartimes',
    r'\vartriangle',
    r'\vartriangleleft',
    r'\vartriangleright',
    r'\Vdash',
    r'\vDash',
    r'\vdash',
    r'\vdots',
    r'\vee',
    r'\veebar',
    r'\Vert',
    r'\vert',
    r'\Vvdash',
    r'\wedge',
    r'\wp',
    r'\wr',
    r'\Xi',
    r'\xi',
#   r'\Ydown',
    r'\yen',
#   r'\Yleft',
#   r'\Yright',
#   r'\Yup',
    r'\zeta',
]

PAT_ALL = make_pattern(SYM_ALL)
