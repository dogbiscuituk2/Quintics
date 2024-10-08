from manim import *

class Quintic01(Scene):
    def construct(self):

        def hide_chars(*args):
            for arg in args:
                #arg.set_color(RED)
                arg.set_opacity(0)
        
        def indicate(args):
            self.play(Indicate(VGroup(*args)))

        def make_tex(*args):
            s = [f'({arg}' for arg in args]
            S = MathTex(*s)
            for i in range(len(s)):
                t = s[i]
                T = S[i]
                T[0].set_opacity(0)
                j = 1
                super = False
                for k in range(1, len(t)):
                    c = t[k]
                    if c == '^':
                        super = True
                    else:
                        if (c == 'a'):
                            T[j].set_color(RED)
                        j += 1
            return S

        def pause():
            self.wait(0)

        def replace(S, t):
            return TransformMatchingShapes(S, MathTex(t).move_to(S.get_center()))

        y1 = r'y^1\ ='
        y2 = [r'x^5\ =', r'ax^4\ =', r'bx^3\ =', r'cx^2\ =', r'dx\ =', r'e\ =']
        e1 = ['x^5+', 'ax^4+', 'bx^3+', 'cx^2+', 'dx+', 'e']
        e2 = ['z^5+', '0z^4+', 'pz^3+', 'qz^2+', 'rz+', 's']
        e3 = ['(z+h)^5', 'a(z+h)^4', 'b(z+h)^3', 'c(z+h)^2', 'd(z+h)', 'e']
        e4 = [
                'a(z^5 + 5hz^4 + 10h^2z^3 + 10h^3z^2 + 5h^4z + h^5)',
                'a(z^4 + 4hz^3 + 6h^2z^2 + 4h^3z + h^4)',
                'b(z^3 + 3hz^2 + 3h^2z + h^3)',
                'c(z^2 + 2hz + h^2)',
                'd(z + h)',
                'e']
        e5 = [
                ['z^5+', '5hz^4+', '10h^2z^3+', '10h^3z^2+', '5h^4z+', 'h^5'],
                ['az^4+', '4ahz^3+', '6ah^2z^2+', '4ah^3z+', 'ah^4'],
                ['bz^3+', '3bhz^2+', '3bh^2z+', 'bh^3'],
                ['cz^2+', '2chz+', 'ch^2'],
                ['dz+', 'dh'],
                ['e']]
        y3 = [
                ['(ay^1)'],
                ['(ax^5)'],
                ['(ax^4)'],
                ['(bx^3)'],
                ['(cx^2)'],
                ['(dx^1)'],
                ['(ex^0)']]
        m3 = [
                ['(z^5', '(0z^4', '(pz^3', '(qz^2', '(^1rz', '(s^1'],
                ['(z^5', '(5hz^4', '(10h^2z^3', '(10h^3z^2', '(5h^4z', '(h^5'],
                ['', '(az^4', '(4ahz^3', '(6ah^2z^2', '(4ah^3z', '(ah^4'],
                ['', '', '(bz^3', '(3bhz^2', '(3bh^2z', '(bh^3'],
                ['', '', '', '(cz^2', '(2chz', '(ch^2'],
                ['', '', '', '', '(dz', '(dh^1'],
                ['', '', '', '', '', '(eh^0']]
        z0 = ['(1^0']
        z1 = [z0, z0, z0, z0, z0, z0]
        z = [
                ['1', '0', 'p', 'q', 'r', 's'],
                ['1', '5h', '10h^2', '10h^3', '5h^4', 'h^5'],
                ['', 'a', '4ah', '6ah^2', '4ah^3', 'ah^4'],
                ['', '', 'b', '3bh', '3bh^2', 'bh^3'],
                ['', '', '', 'c', '2ch', 'ch^2'],
                ['', '', '', '', 'd', 'dh'],
                ['', '', '', '', '', 'e']]
        e6 = [
                ['0=5h+a', 'a=-5h'],
                ['p=10h^2-20h^2+b', 'p=b-10h^2'],
                ['q=10h^3-30h^3+3bh+c', 'q=3bh+c-20h^3'],
                ['r=5h^4-20h^4+3bh^2+2ch+d', 'r=3bh^2+2ch+d-15h^4'],
                ['s=h^5-5h^5+bh^3+ch^2+dh+e', 's=bh^3+ch^2+dh+e-4h^5']]
        y4 = [['p'], ['q'], ['r'], ['s']]
        m4 = [
                [ '0',   '0',   '0', '-10',  '0', 'b'],
                [ '0',   '0', '-20',   '0', '3b', 'c'],
                [ '0', '-15',   '0',  '3b', '2c', 'd'],
                ['-4',   '0',   'b',   'c',  'd', 'e']]
        h4 = [['h^5'], ['h^4'], ['h^3'], ['h^2'], ['h'], ['1']]

        Y1 = make_tex(y1)
        hide_chars(Y1[0][2])
        Y2 = make_tex(*y2).arrange(DOWN, aligned_edge = RIGHT)
        E1 = make_tex(*e1)
        E2 = make_tex(*e2)
        E3 = make_tex(*e3).arrange(DOWN, aligned_edge = LEFT)
        E4 = make_tex(*e4)
        E5 = VGroup(*[make_tex(*e) for e in e5])
        Y3 = Matrix(y3, bracket_h_buff = 0)
        
        for i in range(7):
            hide_chars(Y3[0][i][0][0], Y3[0][i][0][4])

        hide_chars(
            Y3[0][0][0][1], Y3[0][0][0][3],
            Y3[0][1][0][1],
            Y3[0][2][0][4],
            Y3[0][3][0][4],
            Y3[0][4][0][4],
            Y3[0][5][0][3],
            Y3[0][6][0][2], Y3[0][6][0][3])

        M3 = Matrix(m3, bracket_h_buff = 0.2, h_buff = 1.75)

        for i in range(6):
            hide_chars(M3[0][i][0][0])
            for j in range(i, 6):
                hide_chars(M3[0][6 * (i + 1) + j][0][0])

        hide_chars(
            M3[0][4][0][1],
            M3[0][5][0][2],
            M3[0][35][0][3],
            M3[0][41][0][2], M3[0][41][0][3])

        Z1 = Matrix(z1, bracket_h_buff = 0)

        for i in range(6):
            hide_chars(Z1[0][i][0][0], Z1[0][i][0][2])

        E1V = E1.copy().arrange(DOWN, aligned_edge = LEFT)
        G1 = VGroup(E1, E1V).arrange(DOWN, aligned_edge = LEFT)
        Y = VGroup(Y1, Y2).arrange(DOWN, aligned_edge = RIGHT)
        G3 = VGroup(Y, G1).arrange(RIGHT, aligned_edge = UP).move_to(1.2 * LEFT);

# Start with the general quintic in x

        self.play(FadeIn(Y1))
        self.play(Create(E1))
        pause()

# Make a vertical copy

        self.play(TransformFromCopy(E1, E1V, path_arc = 2))
        pause()

# Show the reduced quintic in z

        E2.move_to(E1, aligned_edge = LEFT)
        indicate([E1])
        self.play(ReplacementTransform(E1, E2))
        pause()

# Convert each x-term into an LHS

        self.play(TransformMatchingShapes(E1V, Y2))
        pause()

# Add each binomial x-term as an RHS

        E3.move_to(E1V, aligned_edge = LEFT)
        self.play(Create(E3))
        pause()

# Expand each binomial x-term and distribute the coefficients

        for i in range(6):
            E4[i].move_to(E3[i], aligned_edge = LEFT)
# Flash
            if i < 5:
                indicate([E3[i]])
# Expand
            if i < 4:
                self.play(TransformMatchingShapes(E3[i], E4[i]))
            else:
                E4[i].move_to(E3[i])
                E3[i].set_opacity(0)
# Distribute
            E5[i].move_to(E4[i], aligned_edge = LEFT)
            #if i < 5:
            self.play(TransformMatchingShapes(E4[i], E5[i]))
            #else:
                #E5[i].move_to(E4[i])
                #E4[i].set_opacity(0)
        pause()

# Right align the fully expanded binomials

        M = VGroup(E2, E5)
        E7 = E5.copy().arrange(DOWN, aligned_edge = RIGHT)
        E8 = VGroup(E2.copy(), E7).arrange(DOWN, aligned_edge = RIGHT)
        E8.move_to(M)
        self.play(
            Transform(E2, E8[0]),
            [Transform(E5[i], E7[i]) for i in range(6)])
        pause()

# Convert to matrix equation Y=MZ

        EQ = MathTex('=')
        VGroup(Y3, EQ, M3, Z1).arrange(RIGHT, aligned_edge = UP)
        EQ.move_to(EQ.get_center() + 2.9 * DOWN)
        Z1.move_to(Z1.get_center() + 0.5 * DOWN)
        self.play(TransformMatchingShapes(Y, Y3))
        self.play(FadeIn(EQ))
        self.play(TransformMatchingShapes(M, M3))
        self.play(FadeIn(Z1))
        pause()

# Move all powers of z out of M and into Z
        
        M = M3[0]
        Z = Z1[0]

        def get_element(row, column):
            return M[6 * row + column]

        def new_target(row, column):
            T = MathTex(f'z^{5 - column}' if column < 4 else 'z')
            T.move_to(get_element(row, column), RIGHT)
            T.generate_target()
            T.target.move_to(Z[column], DOWN)
            return T

        for column in range(5):
            rows = range(column + 2)
            T = [MoveToTarget(new_target(row, column)) for row in rows]
            T.append(FadeOut(Z[column]))
            indicate([get_element(row, column) for row in rows])
            self.play(*T)
            self.play([replace(get_element(row, column), z[row][column]) for row in rows])

# Highlight the second column of M

        def get_column(column):
            return VGroup(*[get_element(row, column) for row in range(column + 2)])

        for column in range(6):
            self.play(Indicate(get_column(column)))

        self.wait(3)
