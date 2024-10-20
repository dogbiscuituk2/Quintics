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

        LHS = VGroup(*[make_tex(f'{s}o=') for s in ['x', 'y', 'y', 'x^5', 'ax^4', 'bx^3', 'cx^2', 'dx', 'e']])
        RHS = VGroup(*[make_tex(s) for s in ['oz+h', 'ox^5+ax^4+bx^3+cx^2+dx+e=0', 'oz^5+0z^4+pz^3+qz^2+rz+s']], *Fz[9])
        ALL = VGroup(LHS, RHS)

        LHS.arrange(DOWN, aligned_edge=RIGHT)
        RHS.arrange(DOWN, aligned_edge=LEFT)
        ALL.arrange(RIGHT, aligned_edge=DOWN)
        EQU = [VGroup(LHS[i], RHS[i]) for i in range(9)]

        Y = make_matrix((['y'], ['x^5'], ['ax^4'], ['bx^3'], ['cx^2'], ['dx'], ['e']), margin = 0)
        EQ = MathTex('=').set_color(Grey)
        M = make_matrix((
            ('z^5', '0z^4', 'pz^3', 'qz^2', 'rz', 's'),
            ('z^5', '5hz^4', '10h^2z^3', '10h^3z^2', '5h^4z', 'h^5'),
            ('', 'az^4', '4ahz^3', '6ah^2z^2', '4ah^3z', 'ah^4'),
            ('', '', 'bz^3', '3bhz^2', '3bh^2z', 'bh^3'),
            ('', '', '', 'cz^2', '2chz', 'ch^2'),
            ('', '', '', '', 'dz', 'dh'),
            ('', '', '', '', '', 'e')),
            padding = 1.75)
        Z = make_matrix((('1'), ('1'), ('1'), ('1'), ('1'), ('1')), margin = 0)
        MEQ = VGroup(Y, EQ, M, Z).arrange(RIGHT, aligned_edge=DOWN)
        EQ.move_to(EQ.get_center() + 2.50 * UP)
        Z.move_to(Z.get_center() + 0.25 * UP)

        with say(self, "This is the General Form of a quintic polynomial equation in one variable, x."):
            self.play(Create(EQU[1]))
            dump(*EQU)

        with say(self, "We could solve it easily if we didn't have all these intermediate x powers."):
            box(self, *EQU[1][1][0][4:19])
            s1 = make_tex('y=x^5+e=0')
            s2 = MathTex('x=\\sqrt[5]{-e}')
            s2[0].color = Grey;
            s2[0][0].color = Red;
            s2[0][6].color = Green;
            VGroup(s1, s2).arrange(DOWN)
            self.play(
                TransformMatchingShapes(EQU[1].copy(), s1),
                Create(s2))

        with say(self, "To make a start, we might first try to get rid of the quartic, or x to the fourth, term."):
            box(self, *EQU[1][1][0][4:8])
            self.play(Uncreate(s2))
            self.play(Uncreate(s1))

        with say(self, "In other words, transform it into so-called reduced form,"):
            self.play(Create(EQU[2]))
            box(self, *EQU[2][1][0][4:8])
            dump(*EQU)

        with say(self, "where the coefficient of this term is zero."):
            self.play(Indicate(EQU[2][1][0][5], color=WHITE, scale_factor=2, run_time=2))

        with say(self, "This operation is technically known as a Tschirnhaus Transformation,"):
            image = ImageMobject("resources/Tschirnhaus.jpg")
            caption = MarkupText('Ehrenfried Walther von Tschirnhaus 1651-1708', color=Yellow).scale(0.25)
            picture = Group(image, caption).arrange(DOWN)
            picture.to_edge(RIGHT)
            self.play(FadeIn(picture))
            unbox(self)

        with say(self, "the simplest example of which is a linear substitution, such as x = z + some constant h."):
            box(self, EQU[0])
            self.play(Create(EQU[0]))

        with say(self, "Let's use this to express all these x powers in terms of z."):
            E = EQU[1][1][0]
            S = [E[2:4], E[5:8], E[9:12], E[13:16], E[17:19], E[20:21]]
            T = LHS[3:9]
            self.play([TransformMatchingShapes(S[i].copy(), T[i], path_arc=-PI/2) for i in range(6)], run_time=2)
            box(self, EQU[0][1][0][2:5])
            for i in range(5):
                T = Fz[0][i].copy().move_to(EQU[i+3][1], LEFT)
                EQU[i+3][1] = T
                self.play(TransformMatchingShapes(EQU[0][1].copy(), T))
            self.play(FadeIn(EQU[8][1]))
            unbox(self)
            dump(*EQU)

        def expand(i: int, immediate: bool = False) -> None:

            def move_box(grow: int=0) -> Animation:
                return box_move(*[EQU[j+3][1][0][k] for k in range(1, 6*(i-3)+grow) for j in range(0, 9-i)])

            if i in range(5, 9):
                self.play(move_box())
            fz = Fz[i]
            animations = []
            for j in range(1 if immediate else 0, len(fz)):
                source = EQU[j+3][1]
                target = fz[j]
                target.move_to(source, aligned_edge=LEFT)
                animation = TransformMatchingShapes(source, target)
                if immediate:
                    self.play(animation)
                else:
                    animations.append(animation)
                EQU[j+3][1] = target
            if not immediate:
                if i in range(5, 9):
                    animations.append(move_box(1))
                self.play(animations)

        with say(self, "Expand these powers."):
            self.play(FadeOut(picture))
            for i in range(1, 5):
                expand(i)
                dump(*EQU)

        with say(self, "Multiply out the binomials."):
            for i in range(5, 9):
                expand(i)
                dump(*EQU)
            unbox(self)

        with say(self, "Distribute the original coefficients."):
            expand(9, immediate=True)
            dump(*EQU)

        self.wait(5)

        self.play(FadeOut(EQU[0]), FadeOut(EQU[1]))
        self.play(TransformMatchingShapes(VGroup(*[EQU[i][0] for i in range(2, 9)]), Y), Create(EQ))
        self.play(TransformMatchingShapes(VGroup(*[EQU[i][1] for i in range(2, 9)]), M), Create(Z))
            
        self.wait(5)
