from manim import *




"""
渲染:
manim -pql a_little_complex_manim.py RiemannIntegral
"""

class RiemannIntegral(Scene):
    def construct(self):
        title = Text("Riemann Integral", font_size=44).to_edge(UP)

        # 1. 创建坐标轴与函数曲线（我们用曲线下面的面积来直观理解“积分”）
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 6, 1],
            x_length=9,
            y_length=4.8,
            axis_config={"include_tip": False},
        ).to_edge(DOWN)

        # 2. 定义函数 f(x) 并绘制曲线
        def f(x):
            return 0.1 * (x - 2) ** 3 + 3

        curve = ax.plot(f, x_range=[0, 5], color=BLUE)

        # 3. 用 ValueTracker 控制矩形宽度 Δx：Δx 越小，矩形越多，逼近越“精细”
        dx = ValueTracker(0.8)

        # 4. Riemann 矩形（在区间 [0.5, 4.5] 上用宽为 Δx 的矩形近似曲线下方面积）
        #    always_redraw 确保 dx 改变时，矩形会实时重新生成
        rects = always_redraw(
            lambda: ax.get_riemann_rectangles(
                curve,
                x_range=[0.5, 4.5],
                dx=max(0.05, dx.get_value()),
                fill_opacity=0.6,
                stroke_width=1,
            )
        )

        # 5. 左上角显示当前 Δx 数值
        approx = always_redraw(
            lambda: MathTex(
                r"\Delta x=",
                f"{dx.get_value():.2f}",
            ).scale(0.8).to_corner(UL)
        )

        # 6. 同时显示矩形数量 n（n 大约等于区间长度 / Δx）
        n_rects = always_redraw(
            lambda: Text(
                f"rectangles: {int(np.ceil((4.5 - 0.5) / max(0.05, dx.get_value())))}",
                font_size=28,
                color=GRAY_A,
            ).to_corner(UL).shift(DOWN * 0.8)
        )

        # 7. 动画：先展示曲线与粗略矩形，再逐渐减小 Δx，让 Riemann 和逼近积分
        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.play(Create(ax), run_time=1.0)
        self.play(Create(curve), run_time=1.2)
        self.play(FadeIn(rects, approx, n_rects))
        self.wait(0.4)
        self.play(dx.animate.set_value(0.12), run_time=3, rate_func=smooth)
        self.wait(0.4)


RENDER_INSTRUCTIONS = """
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
            np.sin,
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

        # 1. 创建二维坐标轴（淡化显示，作为背景参考）
        ax = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=8, y_length=6).set_opacity(0.25)

        # 2. 相位追踪器：逐渐改变相位 φ，观察曲线形状如何“变形”
        phase_tracker = ValueTracker(0)

        # 3. Lissajous 曲线：
        #    x = A sin(3t + φ)
        #    y = A sin(2t)
        #    随着 φ 改变，闭合曲线会在不同图案之间连续过渡
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

        # 4. 曲线上的运动点 + 轨迹：帮助看出“生成曲线”的运动过程
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

        # 5. 左上角读数：实时显示当前相位 φ
        label = always_redraw(
            lambda: MathTex(r"\phi=", f"{phase_tracker.get_value():.2f}").scale(0.8).to_corner(UL)
        )

        # 6. 动画：从 φ=0 平滑变化到 2π，展示整套图案的形变过程
        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.add(ax, curve, moving_dot, trail, label)
        self.play(phase_tracker.animate.set_value(2 * PI), run_time=6, rate_func=linear)
        self.wait(0.5)




