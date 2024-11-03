from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from texpaint import *

config.max_files_cached = 999

class Scene_00_Base(VoiceoverScene):

    Painter: TexPaint = TexPaint(
        0,
        (
            ('abcde', Green),
            ('h', Orange),
            ('pqrs', Yellow),
            ('x', Red),
            ('y', Magenta),
            ('z', Cyan)))
    
    def box(self, *args: VMobject) -> Polygon:
        polygon = SurroundingRectangle(VGroup(*args), self.get_colour(Yellow))
        self.play(Create(polygon))
        return polygon
        
    def flash(self, mathTex: MathTex, run_time=2) -> None:
        white = self.get_colour(White)
        self.play(Indicate(mathTex, color=white, run_time=run_time, scale_factor=2))

    def get_text_colour(self) -> ManimColor:
        return self.get_colour(Grey)

    def get_colour(self, colour_index: int) -> ManimColor:
        return self.Painter.get_colour(colour_index)

    def init(self):
        self.set_speech_service(GTTSService())

    def make_tex(self, text: str) -> MathTex:
        text = self.prepare_string(text)
        print(text)
        mathTex: MathTex = MathTex(text)
        self.paint_tex(mathTex)
        return mathTex

    def make_text(self, s: str, *args, **kwargs) -> Text:
        text = Text(self.prepare_string(s), font_size=24, color=self.get_text_colour(), *args, **kwargs)
        text[0].set_opacity(0)
        return text;
    
    def paint_tex(self, mathTex: MathTex) -> None:
        self.Painter.paint(mathTex)

    def prepare_string(self, text: str) -> str:
        return text if '|' in text else f'|{text}'

    def say(self, text: str):
        # Specify language & disable language check to avoid GTTS bugs.
        return self.voiceover(text, lang='en', lang_check=False)
    
    def set_colour_map(self, map: tuple[tuple[str, int]]):
        self.Painter.set_colour_map(map)
    
