from manim import *
from MF_Tools import *
import platform
from scene_00_base import Scene_00_Base
from texpaint import *

TITLE = 'Solving the General Quintic Equation'
SUBTITLE = 'An Ultraradical Animation'
COPYRIGHT = '©2024 by John Michael Kerr'

class Scene_99_Credits(Scene_00_Base): 
    
    def __init__(self):
        super().__init__()

    def construct(self):

        self.init()

        packages = [['python', platform.python_version()],
            *[[package, version(package)] for package in (
            'manim',
            'manim-voiceover',
            'mf-tools',
            )]]

        rows = len(packages)
        cols = [[self.make_text(packages[row][col]) for row in range(rows)] for col in range(2)]
        for row in range(rows):
            for col in range(2):
                cols[col][row][0].set_opacity(0)
        VersionTable = VGroup(
            VGroup(*cols[0]).arrange(DOWN, aligned_edge = LEFT),
            VGroup(*cols[1]).arrange(DOWN, aligned_edge = RIGHT)
            ).arrange(RIGHT)
        
        Credits = VGroup(
            self.make_text('Thank you for watching', slant=ITALIC),
            self.make_text(f'"{TITLE} : {SUBTITLE}"'),
            self.make_text(COPYRIGHT),
            self.make_text(''),
            self.make_text('Software used:', slant=ITALIC),
            VersionTable,
            self.make_text(''),
            self.make_text('All images used in this work are in the public domain.', slant=ITALIC),
            ).arrange(DOWN)

        for credit in Credits:
            self.play(FadeIn(credit), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(Credits))
        self.wait(1)
