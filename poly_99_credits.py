from manim import *
import platform
from base_scene import BaseScene

TITLE = 'Solving the General Quintic Equation'
SUBTITLE = 'An Ultraradical Animation'
COPYRIGHT = '©2024-2025 by John Michael Kerr'

class Poly_99_Credits(BaseScene):

    def __init__(self):
        BaseScene.__init__(self)

    def construct(self):

        packages = [
            ['python', platform.python_version()],
            *[
                [package, version(package)] for package in
                (
                    'manim',
                    'manim-voiceover',
                    'mf-tools',
                )
            ],
            ['ffmpeg', '7.0.2'],
        ]

        rows = len(packages)
        cols = [[self.make_text(packages[row][col]) for row in range(rows)] for col in range(2)]
        VersionTable = VGroup(
            VGroup(*cols[0]).arrange(DOWN, aligned_edge = LEFT),
            VGroup(*cols[1]).arrange(DOWN, aligned_edge = RIGHT)
            ).arrange(RIGHT)
        
        Credits = VGroup(
            self.make_text('Thank you for watching', slant=ITALIC),
            self.make_text(f'"{TITLE} : {SUBTITLE}"'),
            self.make_text(COPYRIGHT),
            self.make_text('-o-'),
            self.make_text('Free software used:', slant=ITALIC),
            VersionTable,
            self.make_text('-o-'),
            self.make_text('All images used in this work are in the public domain.', slant=ITALIC),
            ).arrange(DOWN)

        for credit in Credits:
            self.play(FadeIn(credit), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(Credits))
        self.wait(1)

if __name__ == "__main__":
    BaseScene.run(__file__)
