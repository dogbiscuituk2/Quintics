from manim import *
from manim_voiceover import VoiceoverScene

from common import *

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
            [f'o{z}^5', f'a{z}^4', f'b{z}^3', f'c{z}^2', f'd{z}', 'e'],
            [f'o{z2}^4', f'a{z2}^3', f'b{z2}^2', f'c{z2}'],
            [f'o{z3}^3', f'a{z3}^2', f'b{z3}'],
            [f'o{z4}^2', f'a{z4}'],
            [f'o{z5}'],
            [f'o{z6}{z3}', f'a{z6}{z2}', f'b{z6}{z}', f'c{z6}'],
            [f'o{z7}{z2}', f'a{z7}{z}', f'b{z7}'],
            [f'o{z8}{z}', f'a{z8}'],
            [f'o{z9}'],
            [f'o{z9}', 'az^4+4ahz^3+6ah^2z^2+4ah^3z+ah^4', 'bz^3+3bhz^2+3bh^2z+bh^3', 'cz^2+2chz+ch^2', 'dz+dh', 'e']]]

        for i in range(0, 9):
            Fz[i][0][0][1].set_opacity(0)

        LHS = VGroup(*[make_tex(f'{s}o=') for s in ['x', 'y', 'y', 'x^5', 'ax^4', 'bx^3', 'cx^2', 'dx', 'e']])
        RHS = VGroup(*[make_tex(s) for s in ['oz+h', 'ox^5+ax^4+bx^3+cx^2+dx+e=0', 'oz^5+0z^4+pz^3+qz^2+rz+s']], *Fz[9])
        ALL = VGroup(LHS, RHS)

        LHS.arrange(DOWN, aligned_edge=RIGHT)
        RHS.arrange(DOWN, aligned_edge=LEFT)
        ALL.arrange(RIGHT, aligned_edge=DOWN)
        EQU = [VGroup(LHS[i], RHS[i]) for i in range(9)]

        with self.voiceover(text="This is the General Form of a quintic polynomial equation in one variable, x.") as tracker:
            say(tracker)
            self.play(Create(EQU[1]))
            dump(*EQU)

        with self.voiceover(text="We could solve it if we could remove all these pesky intermediate x powers.") as tracker:
            say(tracker)
            box(self, *EQU[1][1][0][4:19])

        with self.voiceover(text="To make a start, we might first try to get rid of the quartic, or x to the fourth, term.") as tracker:
            say(tracker)
            box(self, *EQU[1][1][0][4:8])

        with self.voiceover(text="In other words, transform it into a reduced form, where the coefficient of this term is zero.") as tracker:
            say(tracker)
            #unbox(self)
            EQU[2][0][0][1].set_opacity(0)
            self.play(Create(EQU[2]))
            box(self, *EQU[2][1][0][4:8])
            dump(*EQU)

        with self.voiceover(text="This operation is technically known as a Tschirnhaus Transformation,") as tracker:
            say(tracker)
            unbox(self)

        with self.voiceover(text="the simplest example of which is a linear substitution, such as x = z + some constant h.") as tracker:
            say(tracker)
            self.play(Create(EQU[0]))
            box(self, EQU[0])

        with self.voiceover(text="Let's use this to express all these x powers in terms of z.") as tracker:
            say(tracker)
            E = EQU[1][1][0]
            S = [E[2:4], E[5:8], E[9:12], E[13:16], E[17:19], E[20:21]]
            T = LHS[3:9]
            self.play([TransformMatchingShapes(S[i].copy(), T[i], path_arc=-PI/2) for i in range(6)], run_time=2)
            for i in range(5):
                T = Fz[0][i].copy().move_to(EQU[i+3][1], LEFT)
                EQU[i+3][1] = T
                self.play(TransformMatchingShapes(EQU[0][1].copy(), T))
            self.play(FadeIn(EQU[8][1]))
            unbox(self)
            dump(*EQU)

        def expand(i: int, immediate: bool) -> None:
            fz = Fz[i]
            op_list = []
            for j in range(len(fz)):
                S = EQU[j+3][1]
                T = fz[j]
                T.move_to(S, aligned_edge=LEFT)
                op = TransformMatchingShapes(S, T)
                if immediate:
                    self.play(op)
                else:
                    op_list.append(op)
                EQU[j+3][1] = T
            if not immediate:
                self.play(op_list)

        with self.voiceover(text="Expand these powers.") as tracker:
            say(tracker)
            for i in range(1, 5):
                expand(i, False)
                dump(*EQU)

        with self.voiceover(text="Now multiply out the binomials.") as tracker:
            say(tracker)
            for i in range(5, 9):
                expand(i, False)
                dump(*EQU)

        with self.voiceover(text="Then distribute the original coefficients.") as tracker:
            say(tracker)
            expand(9, True)
            dump(*EQU)

        with self.voiceover(text="This set of expressions.") as tracker:
            say(tracker)
            box(self, *[EQU[row][1] for row in range(2, 9)])

        self.wait(5)

"""

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


        with self.voiceover(text="This operation is called a Tschirnhaus Transform,") as tracker:
            self.play(Indicate(E03[1][0][4]))
            self.remove(box)
            self.play(TransformMatchingShapes(E03[1], make_tex(e03b)))

        with self.voiceover(text="the simplest example of which is a linear substitution, such as z = x + some constant h.") as t:
            self.play(Create(E02))

        self.wait(5)

        """