from manim import *
from manim_voiceover import VoiceoverScene
from MF_Tools import *

from common import *

class Scene(VoiceoverScene):
    def construct(self):

        VersionTable = Table([*[[package, version(package)] for package in (
            'manim',
            'manim-voiceover',
            'mf-tools',
            )]])
        
        #self.Create(VersionTable)
        self.add(VersionTable)

        self.wait(10)