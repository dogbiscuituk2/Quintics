from common import *

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

config.max_files_cached = 999

class Quintic02(VoiceoverScene):
    def construct(self):

        init(self)
        set_colour_map((
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))
        
        z = '(z+h)'
        z2 = f'{z}{z}'
        z3 = f'{z2}{z}'
        z4 = f'{z3}{z}'
        z5 = f'{z4}{z}'
        z6 = '(z^2+2hz+h^2)'
        z7 = '(z^3+3hz^2+3h^2z+h^3)'
        z8 = '(z^4+4hz^3+6h^2z^2+4h^3z+h^4)'
        z9 = 'z^5+5hz^4+10h^2z^3+10h^3z^2+5h^4z+h^5'

        Fz = [[make_tex(s) for s in t] for t in [
            [f'{z}^5', f'a{z}^4', f'b{z}^3', f'c{z}^2', f'd{z}', 'e'],
            [f'{z2}^4', f'a{z2}^3', f'b{z2}^2', f'c{z2}'],
            [f'{z3}^3', f'a{z3}^2', f'b{z3}'],
            [f'{z4}^2', f'a{z4}'],
            [f'{z5}'],
            [f'{z6}{z3}', f'a{z6}{z2}', f'b{z6}{z}', f'c{z6}'],
            [f'{z7}{z2}', f'a{z7}{z}', f'b{z7}'],
            [f'{z8}{z}', f'a{z8}'],
            [f'{z9}'],
            [f'{z9}', 'az^4+4ahz^3+6ah^2z^2+4ah^3z+ah^4', 'bz^3+3bhz^2+3bh^2z+bh^3', 'cz^2+2chz+ch^2', 'dz+dh', 'e']]]

        LHS = VGroup(*[make_tex(f'{s}=') for s in ['y', 'x', 'y', 'x^5', 'ax^4', 'bx^3', 'cx^2', 'dx', 'e']])
        RHS = VGroup(*[make_tex(s) for s in ['x^5+ax^4+bx^3+cx^2+dx+e=0', 'z+h', 'z^5+0z^4+pz^3+qz^2+rz+s=0']], *Fz[9])
        ALL = VGroup(LHS, RHS)

        LHS.arrange(DOWN, aligned_edge=RIGHT)
        RHS.arrange(DOWN, aligned_edge=LEFT)
        ALL.arrange(RIGHT, aligned_edge=DOWN)
        EQU = [VGroup(LHS[i], RHS[i]) for i in range(9)]

        with self.voiceover(
            text="This is the General Form of a quintic polynomial equation in one variable, x.") as tracker:
            self.play(Create(EQU[0]))

        with self.voiceover(text="To solve it, we might first try to get rid of the quartic, or fourth power, term.") as tracker:
            term = VGroup(*[EQU[0][1][0][i] for i in range(4,7)])
            box = SurroundingRectangle(term, Yellow)
            self.play(Create(box))

        with self.voiceover(text="In other words, transform it into a reduced form, where the coefficient of this term is zero.") as tracker:
            self.remove(box)
            self.play(Create(EQU[2]))
            term = VGroup(*[EQU[2][1][0][i] for i in range(4,7)])
            box = SurroundingRectangle(term, Yellow)
            self.play(Create(box))

        with self.voiceover(text="This operation is technically known as a Tschirnhaus Transform,") as t:
            self.remove(box)

        with self.voiceover(text="the simplest example of which is a linear substitution, such as x = z + some constant h.") as tracker:
            term = EQU[1]
            self.play(Create(term))
            box = SurroundingRectangle(term, Yellow)
            self.play(Create(box))

        with self.voiceover(text="Let's use this to expand all these x powers in terms of z.") as tracker:
            E = EQU[0][1][0]
            S = [E[1:3], E[4:7], E[8:11], E[12:15], E[16:18], E[19:20]]
            T = LHS[3:9]
            self.play([TransformMatchingShapes(S[i].copy(), T[i], path_arc=-PI/2) for i in range(6)])


        self.wait(5)

"""

        for i in range(0, 10):
            fz = Fz[i]
            X = []
            for j in range(len(fz)):
                S = RHS[j+3]
                T = fz[j]
                T.move_to(S, aligned_edge=LEFT)
                X.append(TransformMatchingShapes(S, T))
                RHS[j+3] = T
            self.play(X)
            #self.wait(2)

        self.wait(10)
        

        
        L = ('y', 'z', 'y', 'x^5', 'ax^4', 'bx^3', 'cx^2', 'dx', 'e')
        Z = (
            '1',
            '(z+h)',
            '(z^2+2hz+h^2)',
            '(z^3+3hz^2+3h^2z+h^3)',
            '(z^4+4hz^3+6h^2z^2+4h^3z+h^4)',
            '(z^5+5hz^4+10h^2z^3+10h^3z^2+5h^4z+h^5)')

        R7 = (
            'x^5+ax^4+bx^3+cx^2+dx+e',
            'x+h',
            'z^5+0z^4+pz^3+qz^2+rz+s',

            '(z+h)(z^4+4hz^3+6h^2z^2+4h^3z+h^4)',
            'a(z+h)(z^3+3hz^2+3h^2z+h^3)',
            'b(z+h)(z^2+2hz+h^2)',
            'c(z+h)(z+h)',
            'd(z+h)',
            'e')
        


        R7 = (
            'x^5+ax^4+bx^3+cx^2+dx+e',
            'x+h',
            'z^5+0z^4+pz^3+qz^2+rz+s',
            Z[5], f'a({Z[4]})', f'b({Z[3]})', f'c({Z[2]})', f'd({Z[1]})', 'e')
        R8 = (Z[5], f'a({Z[4]})', f'b({Z[3]})', f'c({Z[2]})', f'd({Z[1]})', 'e')
        R9 = (
            'z^5+5hz^4+10h^2z^3+10h^3z^2+5h^4z+h^5',
            'az^4+4ahz^3+6ah^2z^2+4ah^3z+ah^4',
            'bz^3+3bhz^2+3bh^2z+bh^3',
            'cz^2+2chz+ch^2',
            'dz+dh',
            'e')
        
        LHS = VGroup(*[make_tex(f'{s}=') for s in L01])

        e01 = 'x^5+ax^4+bx^3+cx^2+dx+e=0'
        e02 = 'x+h'
        e03a = 'z^5+0z^4+pz^3+qz^2+rz+s=0'
        e03b = 'z^5+pz^3+qz^2+rz+s=0'
        e04 = ('x^5+5hx^4+10h^2x^3+10h^3x^2+5h^4x+h^5', 'x^4', '', '', '')

        LHS = VGroup(*[make_tex(f'{s}=') for s in ('y', 'z', 'y', 'x^5', 'ax^4', 'bx^3', 'cx^2', 'dx', 'e')])

        RHS = VGroup(*[make_tex(s) for s in (
        )])


        RHS = VGroup(*[make_tex(s) for s in (e01, e02, e03a, )])
            make_tex(e01),
            make_tex(e02),
            make_tex(e03a),
            make_tex(e04)) \
            .arrange(DOWN, aligned_edge=LEFT)
        
        G01 = VGroup(LHS, RHS).arrange(RIGHT, aligned_edge=DOWN)


        with self.voiceover(text="This operation is called a Tschirnhaus Transform,") as t:
            self.play(Indicate(E03[1][0][4]))
            self.remove(box)
            self.play(TransformMatchingShapes(E03[1], make_tex(e03b)))

        with self.voiceover(text="the simplest example of which is a linear substitution, such as z = x + some constant h.") as t:
            self.play(Create(E02))

        self.wait(5)

        """