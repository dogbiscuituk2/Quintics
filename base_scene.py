from inspect import currentframe, getframeinfo
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from latex_rice import *
from painter import *

config.max_files_cached = 999
config.verbosity = "CRITICAL"

class BaseScene(VoiceoverScene):

    def box(self, *args: VMobject) -> Polygon:
        b = self.box_make(*args)
        self.play(Create(b))
        return b

    _boxes = None
    _painter: Painter = Painter()
    _scheme: int = scheme_bright

    def box_make(self, *args: VMobject) -> Polygon:
        return SurroundingRectangle(VGroup(*args), self.get_colour(yellow)) 

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
        self.play(Indicate(tex, color=self.get_colour(white), run_time=run_time, scale_factor=2))

    def get_text_colour(self) -> ManimColor:
        return self.get_colour(grey)

    def get_colour(self, index: int) -> ManimColor:
        return self._painter.get_colour(index)

    def init(self):
        self.set_speech_service(GTTSService())

    def make_matrix(self, matrix: List[List[str]], margin: float = MED_SMALL_BUFF, padding: float = 1.3) -> Matrix:
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        strings: List[str] = [[self.prepare_string(t) for t in row] for row in matrix]
        matrix: Matrix = Matrix(strings, bracket_h_buff = margin, h_buff = padding).set_color(self.get_colour(grey))
        for row in range(rows):
            for col in range(cols):
                self.paint(matrix[0][row * cols + col])
        return matrix

    def make_tex(self, text: str) -> MathTex:
        text = self.prepare_string(text)
        tex: MathTex = MathTex(text)
        self.paint(tex)
        return tex

    def make_text(self, text: str, *args, **kwargs) -> Text:
        result = Text(self.prepare_string(text), font_size=30, color=self.get_text_colour(), *args, **kwargs)
        return result;
    
    def paint(self, tex: MathTex) -> None:
        self._painter.paint(tex)

    def prepare_string(self, text: str) -> str:
        return text # if '|' in text else f'|{text}'

    def say(self, text: str):
        line_number = getframeinfo(currentframe().f_back).lineno
        print(f"{line_number}: {text}")
        # Specify language & disable language check to avoid GTTS bugs.
        return self.voiceover(text, lang='en', lang_check=False)
    
    def set_colour_map(self, map: tuple[tuple[str, int]]):
        self._painter.set_colour_map(map)
