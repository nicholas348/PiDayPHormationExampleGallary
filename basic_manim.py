from manim import *



"""
渲染:
manim -pql basic_manim.py HelloWorld
"""

class HelloWorld(Scene):
    def construct(self):
        self.camera.background_color = "#0b1020"
        title = Text("Hello, Manim!", gradient=(BLUE_B, GREEN_B)).scale(1.2)
        subtitle = Text("用 Python 做动画", font_size=36, color=GRAY_A).next_to(title, DOWN)
        underline = Underline(title, color=WHITE).set_stroke(width=3)

        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.2), Create(underline))
        self.wait(0.5)

        box = RoundedRectangle(corner_radius=0.2, width=10, height=3)
        box.set_stroke(WHITE, 2).set_fill(BLACK, opacity=0.2)
        box.move_to(VGroup(title, subtitle))
        self.play(FadeIn(box))
        self.wait(0.5)

        self.play(
            title.animate.to_edge(UP),
            subtitle.animate.next_to(title, DOWN),
            box.animate.move_to(VGroup(title, subtitle)),
            underline.animate.move_to(title.get_bottom() + DOWN * 0.15),
            run_time=1.2,
        )
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py Shapes
"""

class Shapes(Scene):
    def construct(self):
        title = Text("Shapes", font_size=44).to_edge(UP)
        circle = Circle(color=BLUE).set_fill(BLUE_E, opacity=0.4)
        square = Square(color=RED).set_fill(RED_E, opacity=0.4).shift(RIGHT * 3)
        triangle = Triangle(color=GREEN).set_fill(GREEN_E, opacity=0.4).shift(LEFT * 3)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(LaggedStart(Create(triangle), Create(circle), Create(square), lag_ratio=0.2))
        self.play(
            triangle.animate.rotate(PI / 3).scale(0.9),
            circle.animate.scale(1.2),
            square.animate.rotate(PI / 4),
            run_time=1.4,
        )
        self.play(VGroup(triangle, circle, square).animate.arrange(RIGHT, buff=1.2).shift(DOWN * 0.4))
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py Shapes
"""

class Positioning(Scene):
    def construct(self):
        title = Text("Positioning", font_size=44).to_edge(UP)
        c = Circle(fill_opacity=0.7, color=YELLOW).set_fill(YELLOW_E, opacity=0.6)
        s = Square(color=WHITE).set_fill(BLUE_E, opacity=0.25).next_to(c, RIGHT, buff=0.8)

        arrow = Arrow(c.get_right(), s.get_left(), buff=0.1)
        label = Text("next_to(...)", font_size=30).next_to(arrow, UP)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(Create(c))
        self.play(Create(s))
        self.play(GrowArrow(arrow), FadeIn(label, shift=UP * 0.2))
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py Morphing
"""

class Morphing(Scene):
    def construct(self):
        title = Text("Morphing", font_size=44).to_edge(UP)
        shape = Circle(color=BLUE).set_fill(BLUE_E, opacity=0.4)
        self.play(FadeIn(title, shift=DOWN * 0.3), Create(shape))

        target = RoundedRectangle(corner_radius=0.3, width=3.2, height=3.2, color=GREEN)
        target.set_fill(GREEN_E, opacity=0.35)
        self.play(Transform(shape, target), run_time=1.3)
        self.play(shape.animate.rotate(PI / 2).set_color(ORANGE), run_time=0.8)
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py MathEquations
"""

class MathEquations(Scene):
    def construct(self):
        title = Text("MathTex", font_size=44).to_edge(UP)
        eq = MathTex("a^2 + b^2 = c^2").scale(1.4)
        box = SurroundingRectangle(eq, color=BLUE, buff=0.3)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(Write(eq), run_time=1.2)
        self.play(Create(box))
        self.play(
            Indicate(eq[0:3], color=YELLOW),
            Indicate(eq[4:7], color=YELLOW),
            Indicate(eq[8:11], color=YELLOW),
            run_time=1.4,
        )
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py GraphExample
"""

class GraphExample(Scene):
    def construct(self):
        title = Text("Graph", font_size=44).to_edge(UP)
        ax = Axes(x_range=[-3, 3, 1], y_range=[0, 9, 1], x_length=8, y_length=4)
        ax.to_edge(DOWN)
        labels = ax.get_axis_labels(x_label="x", y_label="y")

        curve = ax.plot(lambda x: x**2, x_range=[-3, 3], color=GREEN)
        dot = Dot(color=YELLOW)
        x_tracker = ValueTracker(-3)
        dot.add_updater(lambda m: m.move_to(ax.c2p(x_tracker.get_value(), x_tracker.get_value() ** 2)))
        vline = always_redraw(lambda: ax.get_vertical_line(dot.get_bottom(), color=GRAY_B))
        coord = always_redraw(
            lambda: MathTex(
                f"x={x_tracker.get_value():.1f}",
                ",",
                f"y={x_tracker.get_value() ** 2:.1f}",
            ).scale(0.7).to_corner(UR)
        )

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(Create(ax), FadeIn(labels))
        self.play(Create(curve), run_time=1.2)
        self.add(dot, vline, coord)
        self.play(x_tracker.animate.set_value(3), run_time=3, rate_func=linear)
        dot.clear_updaters()
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py MoveAlongPath
"""

class MoveAlongPath(Scene):
    def construct(self):
        title = Text("MoveAlongPath", font_size=44).to_edge(UP)
        path = Circle(radius=2.5, color=BLUE)
        dot = Dot(color=ORANGE)
        trail = TracedPath(dot.get_center, stroke_color=ORANGE, stroke_width=4, dissipating_time=1.0)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(Create(path))
        self.add(dot, trail)
        self.play(MoveAlongPath(dot, path), run_time=3, rate_func=linear)
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py Grouping
"""

class Grouping(Scene):
    def construct(self):
        title = Text("VGroup", font_size=44).to_edge(UP)
        g = VGroup(
            Circle(color=BLUE).set_fill(BLUE_E, opacity=0.4),
            Square(color=RED).set_fill(RED_E, opacity=0.4),
            Triangle(color=GREEN).set_fill(GREEN_E, opacity=0.4),
        ).arrange(RIGHT, buff=1)

        brace = Brace(g, direction=DOWN)
        label = brace.get_text("一个整体一起动")

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(LaggedStart(*[Create(m) for m in g], lag_ratio=0.15))
        self.play(GrowFromCenter(brace), FadeIn(label, shift=UP * 0.2))
        self.play(g.animate.shift(UP * 1.8).rotate(PI / 12), run_time=1.2)
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py RotateObject
"""

class RotateObject(Scene):
    def construct(self):
        title = Text("Rotate", font_size=44).to_edge(UP)
        sq = Square(color=WHITE).set_fill(BLUE_E, opacity=0.35).scale(1.3)
        pivot = Dot(sq.get_corner(DL), color=YELLOW)
        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(Create(sq), FadeIn(pivot))
        self.play(Rotate(sq, angle=PI / 2, about_point=pivot.get_center()), run_time=1.4)
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py Counter
"""

class Counter(Scene):
    def construct(self):
        title = Text("Counter", font_size=44).to_edge(UP)
        number = Integer(0, color=YELLOW).scale(2)
        label = Text("score", font_size=28, color=GRAY_A).next_to(number, DOWN)

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.add(number, label)
        self.play(ChangeDecimalToValue(number, 100), run_time=2.5, rate_func=smooth)
        self.play(Indicate(number, color=ORANGE))
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py Braces
"""

class Braces(Scene):
    def construct(self):
        title = Text("Brace", font_size=44).to_edge(UP)
        line = Line(LEFT * 3, RIGHT * 3)
        brace = Brace(line, direction=UP)
        text = brace.get_text("Distance").scale(0.9)
        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(Create(line))
        self.play(GrowFromCenter(brace), FadeIn(text, shift=UP * 0.2))
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py ThreeDExample
"""

class ThreeDExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        sphere = Sphere(radius=1.2, resolution=(24, 12))
        sphere.set_fill(BLUE_E, opacity=0.6).set_stroke(WHITE, 0.5)
        self.add(axes)
        self.play(FadeIn(sphere))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(Rotate(sphere, angle=PI, axis=UP), run_time=2)
        self.wait(0.5)
        self.stop_ambient_camera_rotation()



"""
渲染:
manim -pql basic_manim.py FlashEffect
"""

class FlashEffect(Scene):
    def construct(self):
        title = Text("Flash", font_size=44).to_edge(UP)
        c = Circle(color=WHITE).set_fill(BLUE_E, opacity=0.2).scale(1.4)
        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.add(c)
        self.play(Flash(c, color=YELLOW), run_time=0.6)
        self.play(Flash(c, color=ORANGE), run_time=0.6)
        self.wait(0.5)



"""
渲染:
manim -pql basic_manim.py ColoredText
"""

class ColoredText(Scene):
    def construct(self):
        title = Text("Colored Text", font_size=44).to_edge(UP)
        text = Text("Red and Blue", t2c={"Red": RED, "Blue": BLUE}).scale(1.4)
        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(Write(text))
        self.play(text.animate.set_color_by_gradient(RED, BLUE), run_time=1.2)
        self.wait(0.5)



"""
渲染：
manim -pql basic_manim.py FadeExample
"""

class FadeExample(Scene):
    def construct(self):
        title = Text("Fade", font_size=44).to_edge(UP)
        sq = Square().set_fill(PURPLE_E, opacity=0.8)
        sq.set_stroke(WHITE, 2)
        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(FadeIn(sq, scale=0.8))
        self.wait(0.3)
        self.play(FadeOut(sq, shift=DOWN * 0.5), run_time=1.2)
        self.wait(0.5)