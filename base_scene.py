#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Base class for scenes in project Polynomials.

The BaseScene class is used to provide common functionality to all scenes in 
the project.
The functionality includes methods for creating and manipulating boxes, 
flashing text, making matrices, making text and making MathTex objects.
The BaseScene class also provides methods for setting the colour map and 
for painting MathTex objects.
The BaseScene class is a subclass of the Manim Scene class and the Manim 
VoiceoverScene class.
"""

from inspect import currentframe
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from latex_rice import *
from options import Opt
from painter import *

config.max_files_cached = 999
config.verbosity = "CRITICAL"

class BaseScene(VoiceoverScene):

    def __init__(self):
        VoiceoverScene.__init__(self)
        self._painter = Painter()
        config.background_color = self.back_colour

    @property
    def back_colour(self) -> ManimColor:
        return self._painter.back_colour

    @property
    def fore_colour(self) -> ManimColor:
        return self._painter.fore_colour

    def box(self, *args: VMobject) -> Polygon:
        b = self.box_make(*args)
        self.play(Create(b))
        return b

    def box_make(self, *args: VMobject) -> Polygon:
        return SurroundingRectangle(VGroup(*args), self.get_colour(Pen.YELLOW))

    def box_move(self, *args: VMobject) -> Animation:
        b = self.box_make(*args)
        result = Create(b) if self._boxes == None else ReplacementTransform(self._boxes, b)
        self._boxes = b
        return result

    def box_off(self) -> None:
        if self._boxes != None:
            self.play(Uncreate(self._boxes))
            self._boxes = None

    def box_on(self, *args: VMobject) -> None:
        self.play(self.box_move(*args))

    def flash(self, tex: MathTex, run_time=2) -> None:
        self.play(
            Indicate(
                tex,
                color=self.get_colour(Pen.WHITE),
                run_time=run_time,
                scale_factor=2))

    def get_colour(self, pen: Pen) -> ManimColor:
        return self._painter.get_colour(pen)

    def init(self):
        self.set_speech_service(GTTSService())

    def make_matrix(
            self,
            matrix: List[List[str]],
            margin: float = MED_SMALL_BUFF,
            padding: float = 1.3) -> Matrix:
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        strings: List[str] = [[t for t in row] for row in matrix]
        matrix: Matrix = Matrix(strings, bracket_h_buff = margin, h_buff = padding)
        matrix.set_color(self.fore_colour)
        for row in range(rows):
            for col in range(cols):
                self._paint_tex(matrix[0][row * cols + col])
        return matrix

    def make_tex(self, text: str) -> MathTex:
        tex: MathTex = MathTex(text)
        self._paint_tex(tex)
        return tex

    def make_text(self, text: str, *args, **kwargs) -> Text:
        return Text(text, font_size=30, color=self.fore_colour, *args, **kwargs)

    def say(self, text: str):
        frame = currentframe()
        while frame.f_code.co_name != 'construct':
            frame = frame.f_back
        print(f"{frame.f_lineno}: {text}")
        # Specify language & disable language check to avoid GTTS bugs.
        return self.voiceover(text, lang='en', lang_check=False)
    
    def set_colour_map(self, map: List[tuple[str, int]]) -> None:
        self._painter.set_colour_map(map)

#region Private Implementation

    _boxes = None
    _options: Opt = Opt.DEFAULT
    _painter: Painter
    
    def _paint_tex(self, tex: MathTex) -> None:
        self._painter.paint_tex(tex, self._options)

#endregion
