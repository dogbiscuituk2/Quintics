import platform

from manim import *
from manim_voiceover import VoiceoverScene
from MF_Tools import *

from common import *

class Scene(VoiceoverScene):
    def construct(self):

        packages = [['python', platform.python_version()],
            *[[package, version(package)] for package in (
            'manim',
            'manim-voiceover',
            'mf-tools',
            )]]

        rows = len(packages)
        cols = [[make_text(packages[row][col]) for row in range(rows)] for col in range(2)]
        for row in range(rows):
            for col in range(2):
                cols[col][row][0].set_opacity(0)
        VersionTable = VGroup(
            VGroup(*cols[0]).arrange(DOWN, aligned_edge = LEFT),
            VGroup(*cols[1]).arrange(DOWN, aligned_edge = RIGHT)
            ).arrange(RIGHT)
        
        Credits = VGroup(
            make_text('Thank you for watching', slant=ITALIC),
            make_text(f'"{TITLE} : {SUBTITLE}"'),
            make_text(COPYRIGHT),
            make_text(''),
            make_text('Software used', slant=ITALIC),
            VersionTable,
            make_text(''),
            make_text(ATTRIBUTION, slant=ITALIC),
            ).arrange(DOWN)
        
        self.play(FadeIn(Credits))
        self.wait(10)
        self.play(FadeOut(Credits))
