from manim import *

class Quintic01(Scene):
    def construct(self):

        def get_colour(c: str):
            if c.isnumeric():
                return PINK
            match(c):
                case 'a': return PURE_RED
                case 'b': return ORANGE
                case 'c': return YELLOW
                case 'd': return PURE_GREEN
                case 'e': return TEAL
                case 'h': return PURPLE
                case 'p': return ORANGE
                case 'q': return YELLOW
                case 'r': return PURE_GREEN
                case 's': return TEAL
                case 'x': return BLUE
                case 'y': return BLUE
                case 'z': return BLUE
            return LIGHT_GREY
        
        def indicate(args):
            self.play(Indicate(VGroup(*args), color = WHITE))

        def make_matrix(matrix, hb: float = 1.3, bhb: float = MED_SMALL_BUFF):
            rows = len(matrix)
            cols = len(matrix[0])
            s = [[f'|{t}' for t in row] for row in matrix]
            M = Matrix(s, h_buff = hb, bracket_h_buff = bhb)
            for row in range(rows):
                for col in range(cols):
                    paint_tex(M[0][row * cols + col][0], s[row][col])
            M[1].set_color(LIGHT_GREY)
            M[2].set_color(LIGHT_GREY)
            return M

        def make_tex(*args):
            s = [f'|{arg}' for arg in args]
            t = MathTex(*s)
            for i in range(len(s)):
                paint_tex(t[i], s[i])
            return t

        def paint_tex(tex: MathTex, text: str):
            colour = BLACK
            super = False
            p = 0
            for u in text.split('^'):
                for c in u:
                    t = tex[p]
                    if c == '|':
                        t.set_opacity(0)
                    else:
                        if not super:
                            colour = get_colour(c)
                        t.set_color(colour)
                    super = False
                    p += 1
                super = True

        def pause():
            self.wait(0)

        def replace(S: MathTex, t: str):
            return ReplacementTransform(S, make_tex(t).move_to(S.get_center()))

        y1 = 'y^|='
        y2 = ['x^5=', 'ax^4=', 'bx^3=', 'cx^2=', 'dx^|=', 'e^|=']
        e1 = ['x^5+', 'ax^4+', 'bx^3+', 'cx^2+', 'dx^|+', 'e^|']
        e2 = ['z^5+', '0z^4+', 'pz^3+', 'qz^2+', 'rz^|+', 's^|']
        e3 = ['(z+h)^5', 'a(z+h)^4', 'b(z+h)^3', 'c(z+h)^2', 'd(z+h)^|', 'e^|']
        e4 = [
                '(z^5+5hz^4+10h^2z^3+10h^3z^2+5h^4z+h^5)',
                'a(z^4+4hz^3+6h^2z^2+4h^3z+h^4)',
                'b(z^3+3hz^2+3h^2z+h^3)',
                'c(z^2+2hz+h^2)',
                'd(z+h)^|',
                'e^|']
        e5 = [
                ['z^5+', '5hz^4+', '10h^2z^3+', '10h^3z^2+', '5h^4z+', 'h^5'],
                ['az^4+', '4ahz^3+', '6ah^2z^2+', '4ah^3z+', 'ah^4'],
                ['bz^3+', '3bhz^2+', '3bh^2z+', 'bh^3'],
                ['cz^2+', '2chz+', 'ch^2'],
                ['dz^|+', 'dh^|'],
                ['e^|']]
        y3 = [
                ['y^|'],
                ['x^5'],
                ['ax^4'],
                ['bx^3'],
                ['cx^2'],
                ['dx^|'],
                ['e^|']]
        m1 = [
                ['z^5', '0z^4', 'pz^3', 'qz^2', 'rz^|', 's^|'],
                ['z^5', '5hz^4', '10h^2z^3', '10h^3z^2', '5h^4z', 'h^5'],
                ['', 'az^4', '4ahz^3', '6ah^2z^2', '4ah^3z', 'ah^4'],
                ['', '', 'bz^3', '3bhz^2', '3bh^2z', 'bh^3'],
                ['', '', '', 'cz^2', '2chz', 'ch^2'],
                ['', '', '', '', 'dz^|', 'dh^|'],
                ['', '', '', '', '', 'e^|']]
        z0 = ['|1|']
        z1 = [z0, z0, z0, z0, z0, z0]
        z = [
                ['1^|', '0^|', 'p^|', 'q^|', 'r^|', 's^|'],
                ['1^|', '5h^|', '10h^2', '10h^3', '5h^4', 'h^5'],
                ['', 'a^|', '4ah^|', '6ah^2', '4ah^3', 'ah^4'],
                ['', '', 'b^|', '3bh^|', '3bh^2', 'bh^3'],
                ['', '', '', 'c^|', '2ch^|', 'ch^2'],
                ['', '', '', '', 'd^|', 'dh^|'],
                ['', '', '', '', '', 'e^|']]
        e6 = [
                ['0=5h+a^|', 'a^|=-5h'],
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
        h4 = [['h^5'], ['h^4'], ['h^3'], ['h^2'], ['h^|'], ['1^|']]

        Y1 = make_tex(y1)
        Y2 = make_tex(*y2).arrange(DOWN, aligned_edge = RIGHT)
        E1 = make_tex(*e1)
        E2 = make_tex(*e2)
        E3 = make_tex(*e3).arrange(DOWN, aligned_edge = LEFT)
        E4 = make_tex(*e4)
        E5 = VGroup(*[make_tex(*e) for e in e5])

        Y3 = make_matrix(y3, bhb = 0)
        M1 = make_matrix(m1, hb = 1.75) #, bhb = 0.2)
        Z1 = make_matrix(z1, bhb = 0.2)

        E1V = E1.copy().arrange(DOWN, aligned_edge = LEFT)
        G1 = VGroup(E1, E1V).arrange(DOWN, aligned_edge = LEFT)
        Y = VGroup(Y1, Y2).arrange(DOWN, aligned_edge = RIGHT)
        G3 = VGroup(Y, G1).arrange(RIGHT, aligned_edge = UP).move_to(1.2 * LEFT)

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
        EQ.set_color(LIGHT_GREY)
        VGroup(Y3, EQ, M1, Z1).arrange(RIGHT, aligned_edge = UP)
        EQ.move_to(EQ.get_center() + 2.9 * DOWN)
        Z1.move_to(Z1.get_center() + 0.5 * DOWN)
        self.play(TransformMatchingShapes(Y, Y3))
        self.play(FadeIn(EQ))
        self.play(TransformMatchingShapes(M, M1))
        self.play(FadeIn(Z1))
        pause()

# Move all powers of z out of M and into Z
        
        M = M1[0]
        Z = Z1[0]

        def get_element(row: int, col: int):
            return M[6 * row + col]

        def new_target(row: int, col: int):
            T = make_tex(f'z^{5 - col}' if col < 4 else 'z')
            T.move_to(get_element(row, col), RIGHT)
            T.generate_target()
            T.target.move_to(Z[col], DOWN)
            return T

        for col in range(5):
            rows = range(col + 2)
            T = [MoveToTarget(new_target(row, col)) for row in rows]
            T.append(FadeOut(Z[col]))
            T.append([replace(get_element(row, col), z[row][col]) for row in rows])
            indicate([get_element(row, col) for row in rows])
            self.play(*T)
        pause()

# Transpose the 

        self.wait(3)
