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

from collections.abc import Sequence
import contextlib
from inspect import currentframe
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from latex_rice import *
from options import Opt
from painter import *

config.background_color = ManimColor("#101010")
config.max_files_cached = 999
config.verbosity = "CRITICAL"

class BaseScene(VoiceoverScene):

    def __init__(self):
        VoiceoverScene.__init__(self)

    def setup(self):
        self.set_speech_service(GTTSService())
        self._painter = Painter()

    @property
    def ink_bg(self) -> ManimColor:
        return self._painter.ink_bg

    @property
    def ink_fg(self) -> ManimColor:
        return self._painter.ink_fg
    
    @property
    def options(self) -> Opt:
        return self._painter.options
    
    @options.setter
    def options(self, value: Opt) -> None:
        self._painter.options = value

    def box(self, *args: Mobject) -> Polygon:
        b = self.box_make(*args)
        self.play(Create(b))
        return b

    def box_make(self, *args: Mobject) -> Polygon:
        result = SurroundingRectangle(*args, corner_radius=0.1)
        result.set_color(self.get_ink(Pen.YELLOW))
        return result

    def box_move(self, *args: Mobject) -> Animation:
        b = self.box_make(*args)
        result = Create(b) if self._boxes == None else ReplacementTransform(self._boxes, b)
        self._boxes = b
        return result

    def box_off(self) -> None:
        if self._boxes != None:
            self.play(Uncreate(self._boxes))
            self._boxes = None

    def box_on(self, *args: Mobject) -> None:
        self.play(self.box_move(*args))

    def flash(self, tex: MathTex, run_time=2) -> None:
        self.play(
            Indicate(
                tex,
                color=self.get_ink(Pen.WHITE),
                run_time=run_time,
                scale_factor=2))

    def get_ink(self, pen: Pen) -> ManimColor:
        return self._painter.get_ink(pen) if pen.value >= 0 else self.ink_bg
    
    def get_token_ink(self, token: str) -> ManimColor:
        return self._painter.get_token_ink(token)
    
    def make_axes(
            self,
            width: float,
            height: float,
            xrange: Sequence[float],
            yrange: Sequence[float]) -> Axes:
        axes = Axes(
            x_length=width,
            y_length=height,
            x_range=xrange,
            y_range=yrange,
            axis_config={
                'color': self.ink_fg,
                'tick_size': 0.05,
                'tip_height': 0.1,
                'tip_width': 0.1},
            x_axis_config={},
            y_axis_config={})
        return axes

    def make_matrix(
            self,
            matrix: List[List[str]],
            margin: float = MED_SMALL_BUFF,
            padding: float = 1.3) -> Matrix:
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        strings: List[str] = [[t for t in row] for row in matrix]
        matrix: Matrix = Matrix(
            strings,
            bracket_h_buff = margin,
            h_buff = padding)
        matrix.set_color(self.ink_fg)
        for row in range(rows):
            for col in range(cols):
                self.paint(matrix[0][row * cols + col])
        return matrix

    def make_ssmt(self, text: str) -> SingleStringMathTex:
        ssmt: SingleStringMathTex = SingleStringMathTex(text)
        self.paint(ssmt)
        return ssmt

    def make_ssmts(self, *args: str) -> Generator[VGroup, None, None]:
        tex = self.make_ssmt(r'\\'.join(args))
        start = 0
        for arg in args:
            end = start + get_tex_length(arg)
            yield tex[start:end]
            start = end
    
    def make_tex(self, text: str) -> MathTex:
        tex: MathTex = MathTex(text)
        self.paint(tex)
        return tex
    
    def make_texes(self, *args: str) -> VGroup:
        ssmts = VGroup(list(self.make_ssmts(*args)))
        return VGroup(*[
            self.make_tex(args[i]).move_to(ssmts[i], aligned_edge=LEFT)
            for i in range(len(args))])

    def make_text(self, text: str, *args, **kwargs) -> Text:
        return Text(text, font_size=30, color=self.ink_fg, *args, **kwargs)

    def say(self, text: str):
        frame = currentframe()
        while frame.f_code.co_name != 'construct':
            frame = frame.f_back
        print(f"{frame.f_lineno}: {text}")
        if Opt.DEBUG_SILENT in self.options:
            return contextlib.suppress()
        # Specify language & disable language check to avoid GTTS bugs.
        return self.voiceover(text, lang='en', lang_check=False)
    
    def set_inks(self, inks: dict[str, ManimColor]) -> None:
        self._painter.set_inks(inks)
    
    def set_pens(self, map: List[tuple[str, Pen]]) -> None:
        self._painter.set_pens(map)

    def substitute_tex(self, group: VGroup, index: int, value: VGroup) -> None:
        value.move_to(group[index], aligned_edge=LEFT)
        group[index] = value

#region Private Implementation

    _boxes = None
    _painter: Painter
    
    def paint(self, mob: Mobject) -> None:
        self._painter.paint(mob)

    @staticmethod
    def run(file: str) -> None:
        import os
        console.clear()
        resolutions = input("""Select Quality or 0 to cancel:
                  
            0: 480p15
            1: 720p30
            2: 1080p60
            3: 1440p60
            4: 2160p60  """)
        print('')
        for resolution in resolutions:
            if resolution in '01234':
                module_name = os.path.abspath(file).split(os.sep)[-1]
                # py -m: run library module as a script (terminates option list)
                # manim -a: all scenes, -p: preview, -q?: quality.
                command_line = f'py -m manim render -a -p -q{"lmhpk"[int(resolution)]} {module_name}'
                os.system(command_line)

#endregion
