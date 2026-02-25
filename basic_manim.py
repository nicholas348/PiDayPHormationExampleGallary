from manim import *



"""
渲染:
manim -pql basic_manim.py HelloWorld
"""

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait(1)



"""
渲染:
manim -pql basic_manim.py Shapes
"""

class Shapes(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED).shift(RIGHT * 2)
        self.play(Create(circle), Create(square))



"""
渲染:
manim -pql basic_manim.py Shapes
"""

class Positioning(Scene):
    def construct(self):
        c = Circle(fill_opacity=1, color=YELLOW)
        s = Square().next_to(c, RIGHT, buff=0.5)
        self.add(c, s)



"""
渲染:
manim -pql basic_manim.py Morphing
"""

class Morphing(Scene):
    def construct(self):
        shape = Circle()
        self.add(shape)
        self.play(ReplacementTransform(shape, Square()))



"""
渲染:
manim -pql basic_manim.py MathEquations
"""

class MathEquations(Scene):
    def construct(self):
        eq = MathTex("a^2 + b^2 = c^2")
        self.play(Write(eq))



"""
渲染:
manim -pql basic_manim.py GraphExample
"""

class GraphExample(Scene):
    def construct(self):
        ax = Axes()
        curve = ax.plot(lambda x: x**2, x_range=[-2, 2], color=GREEN)
        self.add(ax, curve)



"""
渲染:
manim -pql basic_manim.py MoveAlongPath
"""

class MoveAlongPath(Scene):
    def construct(self):
        line = Line(LEFT*3, RIGHT*3)
        dot = Dot(color=ORANGE)
        self.add(line, dot)
        self.play(MoveAlongPath(dot, line), run_time=2)



"""
渲染:
manim -pql basic_manim.py Grouping
"""

class Grouping(Scene):
    def construct(self):
        g = VGroup(Circle(), Square()).arrange(RIGHT)
        self.play(g.animate.shift(UP * 2))



"""
渲染:
manim -pql basic_manim.py RotateObject
"""

class RotateObject(Scene):
    def construct(self):
        sq = Square()
        self.play(Rotate(sq, angle=PI/2)) # Rotates 90 degrees



"""
渲染:
manim -pql basic_manim.py Counter
"""

class Counter(Scene):
    def construct(self):
        number = Integer(0)
        self.add(number)
        self.play(ChangeDecimalToValue(number, 100), run_time=3)



"""
渲染:
manim -pql basic_manim.py Braces
"""

class Braces(Scene):
    def construct(self):
        line = Line(LEFT, RIGHT)
        brace = Brace(line, direction=UP)
        text = brace.get_text("Distance")
        self.add(line, brace, text)



"""
渲染:
manim -pql basic_manim.py ThreeDScene
"""

class ThreeDScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(axes)



"""
渲染:
manim -pql basic_manim.py FlashEffect
"""

class FlashEffect(Scene):
    def construct(self):
        c = Circle()
        self.add(c)
        self.play(Flash(c, color=YELLOW))



"""
渲染:
manim -pql basic_manim.py ColoredText
"""

class ColoredText(Scene):
    def construct(self):
        text = Text("Red and Blue", t2c={"Red": RED, "Blue": BLUE})
        self.play(Write(text))



"""
渲染：
manim -pql basic_manim.py FadeExample
"""

class FadeExample(Scene):
    def construct(self):
        sq = Square(fill_opacity=1)
        self.add(sq)
        self.play(FadeOut(sq))