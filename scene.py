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
            tex = MathTex(*s)
            for t in tex:
                #t[0].set_color(RED)
                t[0].set_opacity(0)
            return tex

        def pause():
            self.wait(0)

        def replace(S, t):
            return TransformMatchingShapes(S, MathTex(t).move_to(S.get_center()))

        Y1 = make_tex(r'y^1\ =')
        hide_chars(Y1[0][2])
        Y2 = make_tex(r'x^5\ =', r'ax^4\ =', r'bx^3\ =', r'cx^2\ =', r'dx\ =', r'e\ =').arrange(DOWN, aligned_edge = RIGHT)
        E1 = make_tex('x^5+', 'ax^4+', 'bx^3+', 'cx^2+', 'dx+', 'e')
        E3 = make_tex('z^5+', '0z^4+', 'pz^3+', 'qz^2+', 'rz+', 's')
        E4 = make_tex('(z+h)^5', 'a(z+h)^4', 'b(z+h)^3', 'c(z+h)^2', 'd(z+h)', 'e').arrange(DOWN, aligned_edge = LEFT)
        E5 = make_tex(
            'a(z^5 + 5hz^4 + 10h^2z^3 + 10h^3z^2 + 5h^4z + h^5)',
            'a(z^4 + 4hz^3 + 6h^2z^2 + 4h^3z + h^4)',
            'b(z^3 + 3hz^2 + 3h^2z + h^3)',
            'c(z^2 + 2hz + h^2)',
            'd(z + h)',
            'e')
        E6 = VGroup(
            make_tex('z^5+', '5hz^4+', '10h^2z^3+', '10h^3z^2+', '5h^4z+', 'h^5'),
            make_tex('az^4+', '4ahz^3+', '6ah^2z^2+', '4ah^3z+', 'ah^4'),
            make_tex('bz^3+', '3bhz^2+', '3bh^2z+', 'bh^3'),
            make_tex('cz^2+', '2chz+', 'ch^2'),
            make_tex('dz+', 'dh'),
            make_tex('e')
        )

        Y3 = Matrix([
            ['(ay^1)'],
            ['(ax^5)'],
            ['(ax^4)'],
            ['(bx^3)'],
            ['(cx^2)'],
            ['(dx^1)'],
            ['(ex^0)']], bracket_h_buff = 0)
        
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

        M3 = Matrix([
            ['(z^5', '(0z^4', '(pz^3', '(qz^2', '(^1rz', '(s^1'],
            ['(z^5', '(5hz^4', '(10h^2z^3', '(10h^3z^2', '(5h^4z', '(h^5'],
            ['', '(az^4', '(4ahz^3', '(6ah^2z^2', '(4ah^3z', '(ah^4'],
            ['', '', '(bz^3', '(3bhz^2', '(3bh^2z', '(bh^3'],
            ['', '', '', '(cz^2', '(2chz', '(ch^2'],
            ['', '', '', '', '(dz', '(dh^1'],
            ['', '', '', '', '', '(eh^0']
        ], bracket_h_buff = 0.1, h_buff = 1.6)

        for i in range(6):
            hide_chars(M3[0][i][0][0])
            for j in range(i, 6):
                hide_chars(M3[0][6 * (i + 1) + j][0][0])

        hide_chars(
            M3[0][4][0][1],
            M3[0][5][0][2],
            M3[0][35][0][3],
            M3[0][41][0][2], M3[0][41][0][3])

        z = ['(1^0']
        Z1 = Matrix([z, z, z, z, z, z], bracket_h_buff = 0)

        for i in range(6):
            hide_chars(Z1[0][i][0][0], Z1[0][i][0][2])

        E2 = E1.copy().arrange(DOWN, aligned_edge = LEFT)
        G1 = VGroup(E1, E2).arrange(DOWN, aligned_edge = LEFT)
        Y = VGroup(Y1, Y2).arrange(DOWN, aligned_edge = RIGHT)
        G3 = VGroup(Y, G1).arrange(RIGHT, aligned_edge = UP).move_to(LEFT);

# Start with the general quintic in x

        self.play(FadeIn(Y1))
        self.play(Create(E1))
        pause()

# Make a vertical copy

        self.play(TransformFromCopy(E1, E2, path_arc = 2))
        pause()

# Show the reduced quintic in z

        E3.move_to(E1, aligned_edge = LEFT)
        indicate([E1])
        self.play(ReplacementTransform(E1, E3))
        pause()

# Convert each term into an LHS

        self.play(TransformMatchingShapes(E2, Y2))
        pause()

# Add each binomial term as an RHS

        E4.move_to(E2, aligned_edge = LEFT)
        self.play(Create(E4))
        pause()

# Expand each binomial term and distribute the coefficients

        for index in range(6):
            E5[index].move_to(E4[index], aligned_edge = LEFT)
# Flash
            if index < 5:
                indicate([E4[index]])
# Expand
            if index < 4:
                self.play(TransformMatchingShapes(E4[index], E5[index]))
            else:
                E5[index].move_to(E4[index])
                E4[index].set_opacity(0)
# Distribute
            E6[index].move_to(E5[index], aligned_edge = LEFT)
            #if index < 5:
            self.play(TransformMatchingShapes(E5[index], E6[index]))
            #else:
                #E6[index].move_to(E5[index])
                #E5[index].set_opacity(0)
        pause()

# Right align the fully expanded binomials

        M = VGroup(E3, E6)
        E7 = E6.copy().arrange(DOWN, aligned_edge = RIGHT)
        E8 = VGroup(E3.copy(), E7).arrange(DOWN, aligned_edge = RIGHT)
        E8.move_to(M)
        self.play(
            Transform(E3, E8[0]),
            [Transform(E6[i], E7[i]) for i in range(6)])
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

        z = [
            ['1', '1'],
            ['0', '5h', 'a'],
            ['p', '10h^2', '4ah', 'b'],
            ['q', '10h^3', '6ah^2', '3bh', 'c'],
            ['r', '5h^4', '4ah^3', '3bh^2', '2ch', 'd']]

        def new_target(i, j):
            T = MathTex(f'z^{5 - i}' if i < 4 else 'z')
            T.move_to(M[i + 6 * j], RIGHT)
            T.generate_target()
            T.target.move_to(Z[i], DOWN)
            return T

        for i in range(5):
            T = [MoveToTarget(new_target(i, j)) for j in range(i + 2)]
            T.append(FadeOut(Z[i]))
            indicate([M[i + 6 * j] for j in range(i + 2)])
            self.play(*T)
            self.play([replace(M[i + 6 * j], z[i][j]) for j in range(i + 2)])


        self.wait(10)
