from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait(1)


class Shapes(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED).shift(RIGHT * 2)
        self.play(Create(circle), Create(square))

class Positioning(Scene):
    def construct(self):
        c = Circle(fill_opacity=1, color=YELLOW)
        s = Square().next_to(c, RIGHT, buff=0.5)
        self.add(c, s)

class Morphing(Scene):
    def construct(self):
        shape = Circle()
        self.add(shape)
        self.play(ReplacementTransform(shape, Square()))

class MathEquations(Scene):
    def construct(self):
        eq = MathTex("a^2 + b^2 = c^2")
        self.play(Write(eq))

class GraphExample(Scene):
    def construct(self):
        ax = Axes()
        curve = ax.plot(lambda x: x**2, x_range=[-2, 2], color=GREEN)
        self.add(ax, curve)

class MoveAlongPath(Scene):
    def construct(self):
        line = Line(LEFT*3, RIGHT*3)
        dot = Dot(color=ORANGE)
        self.add(line, dot)
        self.play(MoveAlongPath(dot, line), run_time=2)

class Grouping(Scene):
    def construct(self):
        g = VGroup(Circle(), Square()).arrange(RIGHT)
        self.play(g.animate.shift(UP * 2))

class RotateObject(Scene):
    def construct(self):
        sq = Square()
        self.play(Rotate(sq, angle=PI/2)) # Rotates 90 degrees


class Counter(Scene):
    def construct(self):
        number = Integer(0)
        self.add(number)
        self.play(ChangeDecimalToValue(number, 100), run_time=3)

class Braces(Scene):
    def construct(self):
        line = Line(LEFT, RIGHT)
        brace = Brace(line, direction=UP)
        text = brace.get_text("Distance")
        self.add(line, brace, text)

class ThreeDScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(axes)

class FlashEffect(Scene):
    def construct(self):
        c = Circle()
        self.add(c)
        self.play(Flash(c, color=YELLOW))

class ColoredText(Scene):
    def construct(self):
        text = Text("Red and Blue", t2c={"Red": RED, "Blue": BLUE})
        self.play(Write(text))

class FadeExample(Scene):
    def construct(self):
        sq = Square(fill_opacity=1)
        self.add(sq)
        self.play(FadeOut(sq))