from manim import *


class PresentationIntroOutro(ThreeDScene):
    def construct(self):
        title = Text("The Ray Tracing Algorithm").scale(1.5)
        
        header1 = Text("Animation and Voiceover by", weight=BOLD)
        name1 = Text("Luke Tang")
        credit1 = VGroup(header1, name1).arrange(DOWN)
        
        header2 = Text("Supervised by", weight=BOLD)
        name2 = Text("Dr. Steven Mills")
        credit2 = VGroup(header2, name2).arrange(DOWN)
        
        self.add(title)