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





class LissajousMorph(Scene):
    def construct(self):
        # A simple plane, slightly faded
        ax = Axes(x_range=[-3, 3], y_range=[-3, 3]).set_opacity(0.3)

        # This tracks the "phase shift" to animate the morphing
        phase_tracker = ValueTracker(0)

        # Draw the curve dynamically
        # x = A * sin(a*t + phase), y = B * sin(b*t)
        curve = always_redraw(lambda: ParametricFunction(
            lambda t: ax.c2p(
                2.5 * np.sin(3 * t + phase_tracker.get_value()),
                2.5 * np.sin(2 * t)
            ),
            t_range=[0, 2 * PI],
            color=PURPLE,
            stroke_width=3
        ))

        self.add(ax, curve)

        # Animate the phase shifting from 0 to 2*PI
        self.play(
            phase_tracker.animate.set_value(2 * PI),
            run_time=6,
            rate_func=linear
        )
        self.wait()


class FourierSquareWave(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 10, 1], y_range=[-2, 2, 1])

        # Tracks how many sine waves we are adding together
        terms_tracker = ValueTracker(1)

        # The math function that adds 'n' number of sine waves
        def fourier_approx(x, n_terms):
            result = 0
            for k in range(1, int(n_terms) * 2, 2):  # Uses odd numbers: 1, 3, 5...
                result += (4 / (PI * k)) * np.sin(k * x)
            return result

        # Redraw the curve as the number of terms increases
        curve = always_redraw(lambda: ax.plot(
            lambda x: fourier_approx(x, max(1, terms_tracker.get_value())),
            color=TEAL
        ))

        # A dynamic label to show what math is happening
        label = always_redraw(lambda: Text(
            f"Sine Waves Added: {int(terms_tracker.get_value())}",
            font_size=32
        ).to_corner(UL))

        self.add(ax, curve, label)

        # Animate from 1 sine wave up to 15 added together
        self.play(
            terms_tracker.animate.set_value(15),
            run_time=6,
            rate_func=linear
        )
        self.wait()