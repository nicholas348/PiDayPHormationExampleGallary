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


class PerfectSineWave(Scene):
    def construct(self):
        # 1. Create a Coordinate System (Scaled to fit the right side)
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5],
            x_length=7,
            y_length=3,
            axis_config={"include_tip": False}
        ).to_edge(RIGHT, buff=0.5)

        # 2. Create the Circle (Shifted to the left)
        circle = Circle(radius=1.5, color=BLUE).to_edge(LEFT, buff=1)
        center = circle.get_center()

        # 3. The Math "Engine" (Tracks the angle from 0 to 4*PI)
        t = ValueTracker(0)

        # 4. The Moving Parts (Redrawn every frame)
        # The dot traveling around the circle
        dot = always_redraw(lambda: Dot(color=YELLOW).move_to(
            circle.point_at_angle(t.get_value())
        ))

        # The horizontal line connecting the circle-dot to the wave-dot
        connection_line = always_redraw(lambda: Line(
            dot.get_center(),
            axes.c2p(t.get_value() % (4 * PI), np.sin(t.get_value())),
            color=WHITE,
            stroke_width=1,
            stroke_opacity=0.5
        ))

        # The Sine Wave itself
        sine_curve = always_redraw(lambda: axes.plot(
            lambda x: np.sin(x),
            x_range=[0, t.get_value() % (4 * PI) if t.get_value() > 0 else 0.001],
            color=YELLOW
        ))

        # 5. Visualizing
        self.add(axes, circle, dot, connection_line, sine_curve)

        # Animate the tracker to "drive" the whole scene
        self.play(
            t.animate.set_value(4 * PI),
            run_time=8,
            rate_func=linear
        )
        self.wait()



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