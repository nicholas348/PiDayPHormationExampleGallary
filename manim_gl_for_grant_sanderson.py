from manimlib import *


class Introduction(Scene):
    def construct(self):
        # In ManimGL, Text uses system fonts, 
        # while Tex uses LaTeX (requires MikTeX or TeX Live)
        hello = Text("Hello ManimGL!")
        
        # Animations are called via self.play
        self.play(Write(hello))
        self.wait()
        
        # Example of a transformation
        circle = Circle(color=BLUE)
        self.play(ReplacementTransform(hello, circle))
        self.wait()