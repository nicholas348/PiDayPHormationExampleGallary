from manim import *




"""
渲染:
manim -pql a_little_complex_manim.py RiemannIntegral
"""

class RiemannIntegral(Scene):
    def construct(self):
        title = Text("Riemann Integral", font_size=44).to_edge(UP)
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 6, 1],
            x_length=9,
            y_length=4.8,
            axis_config={"include_tip": False},
        ).to_edge(DOWN)
        curve = ax.plot(lambda x: 0.1 * (x - 2) ** 3 + 3, x_range=[0, 5], color=BLUE)

        dx = ValueTracker(0.8)

        def f(x):
            return 0.1 * (x - 2) ** 3 + 3

        rects = always_redraw(
            lambda: ax.get_riemann_rectangles(
                curve,
                x_range=[0.5, 4.5],
                dx=max(0.05, dx.get_value()),
                fill_opacity=0.6,
                stroke_width=1,
            )
        )

        approx = always_redraw(
            lambda: MathTex(
                r"\Delta x=",
                f"{dx.get_value():.2f}",
            ).scale(0.8).to_corner(UL)
        )

        n_rects = always_redraw(
            lambda: Text(
                f"rectangles: {int(np.ceil((4.5 - 0.5) / max(0.05, dx.get_value())))}",
                font_size=28,
                color=GRAY_A,
            ).to_corner(UL).shift(DOWN * 0.8)
        )

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(Create(ax), run_time=1.0)
        self.play(Create(curve), run_time=1.2)
        self.add(rects, approx, n_rects)
        self.wait(0.4)
        self.play(dx.animate.set_value(0.12), run_time=3, rate_func=smooth)
        self.wait(0.4)




"""
渲染:
manim -pql a_little_complex_manim.py PerfectSineWave
"""

class PerfectSineWave(Scene):
    def construct(self):
        title = Text("Unit Circle -> Sine", font_size=44).to_edge(UP)

        # 1. 创造坐标轴 (左侧留出空间给圆)
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5],
            x_length=7,
            y_length=3,
            axis_config={"include_tip": False}
        ).to_edge(RIGHT, buff=0.5)

        # 2. 创造一个圆，放在左侧
        circle = Circle(radius=1.5, color=BLUE).to_edge(LEFT, buff=1)
        center = circle.get_center()

        # 3. 追踪器来控制动画的进度
        t = ValueTracker(0)

        # 4. 移动的点和线条
        # 圆上的点，随着t的变化沿着圆周移动
        dot = always_redraw(lambda: Dot(color=YELLOW).move_to(
            circle.point_at_angle(t.get_value())
        ))

        radius_line = always_redraw(lambda: Line(center, dot.get_center(), color=WHITE).set_stroke(width=2, opacity=0.8))

        proj_dot = always_redraw(lambda: Dot(color=YELLOW_A).move_to(
            axes.c2p(t.get_value() % (4 * PI), np.sin(t.get_value()))
        ).scale(0.9))

        # 连接圆上点和正弦波上对应点的线条
        connection_line = always_redraw(lambda: Line(
            dot.get_center(),
            axes.c2p(t.get_value() % (4 * PI), np.sin(t.get_value())),
            color=WHITE,
            stroke_width=1,
            stroke_opacity=0.5
        ))

        # 正弦波，随着t的增加逐渐绘制出来
        sine_curve = always_redraw(lambda: axes.plot(
            lambda x: np.sin(x),
            x_range=[0, t.get_value() % (4 * PI) if t.get_value() > 0 else 0.001],
            color=YELLOW
        ))

        readout = always_redraw(
            lambda: MathTex(
                r"t=", f"{(t.get_value() % (4 * PI)):.2f}",
                r"\ \ \sin(t)=", f"{np.sin(t.get_value()):.2f}",
            ).scale(0.7).to_corner(UL)
        )

        # 5. 可视化所有元素
        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.add(axes, circle, dot, radius_line, connection_line, sine_curve, proj_dot, readout)

        # 6. 动画：让t从0增加到4*PI，展示点沿圆周移动以及正弦波的形成
        self.play(t.animate.set_value(4 * PI), run_time=8, rate_func=linear)
        self.wait(0.5)




"""
渲染:
manim -pql a_little_complex_manim.py LissajousMorph
"""

class LissajousMorph(Scene):
    def construct(self):
        title = Text("Lissajous Morph", font_size=44).to_edge(UP)
        ax = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=8, y_length=6).set_opacity(0.25)

        phase_tracker = ValueTracker(0)

        curve = always_redraw(
            lambda: ParametricFunction(
                lambda t: ax.c2p(
                    2.5 * np.sin(3 * t + phase_tracker.get_value()),
                    2.5 * np.sin(2 * t),
                ),
                t_range=[0, 2 * PI],
                color=PURPLE,
                stroke_width=4,
            ).set_color_by_gradient(PURPLE_A, BLUE_B, TEAL_B)
        )

        moving_dot = always_redraw(
            lambda: Dot(
                ax.c2p(
                    2.5 * np.sin(3 * 0 + phase_tracker.get_value()),
                    2.5 * np.sin(2 * 0),
                ),
                color=YELLOW,
            )
        )

        trail = TracedPath(moving_dot.get_center, stroke_color=YELLOW, stroke_width=2, dissipating_time=1.2)
        label = always_redraw(
            lambda: MathTex(r"\phi=", f"{phase_tracker.get_value():.2f}").scale(0.8).to_corner(UL)
        )

        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.add(ax, curve, moving_dot, trail, label)
        self.play(phase_tracker.animate.set_value(2 * PI), run_time=6, rate_func=linear)
        self.wait(0.5)




"""
渲染:
manim -pql a_little_complex_manim.py FourierSquareWave
"""

class FourierSquareWave(Scene):
    def construct(self):
        title = Text("Fourier Square Wave", font_size=44).to_edge(UP)
        ax = Axes(x_range=[0, 10, 1], y_range=[-2, 2, 1], x_length=9, y_length=4.8).to_edge(DOWN)

        terms_tracker = ValueTracker(1)

        def fourier_approx(x, n_terms):
            result = 0
            for k in range(1, int(n_terms) * 2, 2):  # 只使用奇数项
                result += (4 / (PI * k)) * np.sin(k * x)
            return result

        # 动态绘制方波
        curve = always_redraw(
            lambda: ax.plot(
                lambda x: fourier_approx(x, max(1, terms_tracker.get_value())),
                color=TEAL,
            )
        )

        # 一个用于展示当前添加了多少个正弦波的标签
        label = always_redraw(
            lambda: Text(
                f"Terms: {int(terms_tracker.get_value())}",
                font_size=32,
            ).to_corner(UL)
        )

        gibbs_hint = Text("项数越多，越接近方波 (但边缘会出现振铃)", font_size=26, color=GRAY_A)
        gibbs_hint.next_to(title, DOWN)

        self.play(FadeIn(title, shift=DOWN * 0.3), FadeIn(gibbs_hint, shift=DOWN * 0.2))
        self.add(ax, curve, label)

        for n in [1, 2, 3, 5, 8, 12, 15]:
            self.play(terms_tracker.animate.set_value(n), run_time=0.9, rate_func=smooth)
            self.wait(0.15)

        self.wait(0.5)