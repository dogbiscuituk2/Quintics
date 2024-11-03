from manim import *
from scene_00_base import Scene_00_Base

class Scene_01_Intro(Scene_00_Base):

    def __init__(self):
        super().__init__()

    def construct(self):

        self.init()

        self.add(NumberPlane())

        s = r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}'
        t = MathTex(s)
        self.Painter.paint(t)

        self.play(Create(t))
        self.wait(10)
