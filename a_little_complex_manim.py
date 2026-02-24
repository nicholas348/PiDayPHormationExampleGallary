from manim import *


class RiemannIntegral(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 5], y_range=[0, 6], axis_config={"include_tip": False})
        curve = ax.plot(lambda x: 0.1 * (x - 2) ** 3 + 3, color=BLUE)

        # Create the rectangles
        rects = ax.get_riemann_rectangles(curve, x_range=[0.5, 4.5], dx=0.5, fill_opacity=0.5)

        self.add(ax, curve)
        self.play(Write(rects))
        self.wait()

        # Transform to smaller rectangles (better approximation)
        finer_rects = ax.get_riemann_rectangles(curve, x_range=[0.5, 4.5], dx=0.1, fill_opacity=0.5)
        self.play(ReplacementTransform(rects, finer_rects), run_time=2)
        self.wait()


class SineWaveUnitCircle(Scene):
    def construct(self):
        # Setup Axes and Circle
        axes = Axes(x_range=[-2, 8], y_range=[-2, 2], x_length=10).shift(RIGHT)
        circle = Circle(radius=1.5, color=WHITE).shift(LEFT * 3)
        dot = Dot(color=YELLOW).move_to(circle.get_right())

        # The tracing line and curve
        path = TracedPath(dot.get_center, stroke_color=YELLOW)
        moving_line = always_redraw(lambda: Line(circle.get_center(), dot.get_center(), color=RED))

        self.add(axes, circle, dot, moving_line, path)

        # Rotate the dot and move the entire scene to "draw" the wave
        self.play(
            Rotate(dot, angle=2 * PI, about_point=circle.get_center()),
            axes.animate.shift(LEFT * 5),
            run_time=4, rate_func=linear
        )


class Brachistochrone(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 5], y_range=[-3, 0])

        # Straight line vs Cycloid
        straight = ax.plot(lambda x: -0.6 * x, x_range=[0, 5], color=RED)
        cycloid = ax.plot(
            lambda x: -np.sqrt(1 - ((x - 2.5) / 2.5) ** 2) * 1.5 - 1.5,  # Simplified curve
            x_range=[0, 5], color=GREEN
        )

        dot1 = Dot(color=RED)
        dot2 = Dot(color=GREEN)

        self.add(ax, straight, cycloid)

        # Animate two dots racing
        self.play(
            MoveAlongPath(dot1, straight),
            MoveAlongPath(dot2, cycloid),
            run_time=2, rate_func=slow_into
        )


class GravityField(Scene):
    def construct(self):
        func = lambda pos: np.array([
            -pos[1] / (pos[0] ** 2 + pos[1] ** 2 + 1),  # Rotation effect
            pos[0] / (pos[0] ** 2 + pos[1] ** 2 + 1),
            0
        ])

        field = ArrowVectorField(func, x_range=[-4, 4], y_range=[-3, 3])
        self.play(StreamLines(func).create())
        self.wait()