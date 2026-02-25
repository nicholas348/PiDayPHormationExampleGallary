from manim import *




"""
渲染:
manim -pql a_little_complex_manim.py RiemannIntegral
"""

class RiemannIntegral(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 5], y_range=[0, 6], axis_config={"include_tip": False})
        curve = ax.plot(lambda x: 0.1 * (x - 2) ** 3 + 3, color=BLUE)

        # 制造矩形来近似曲线下的面积
        rects = ax.get_riemann_rectangles(curve, x_range=[0.5, 4.5], dx=0.5, fill_opacity=0.5)

        self.add(ax, curve)
        self.play(Write(rects))
        self.wait()

        # 转换成更细的矩形来更好地近似面积
        finer_rects = ax.get_riemann_rectangles(curve, x_range=[0.5, 4.5], dx=0.1, fill_opacity=0.5)
        self.play(ReplacementTransform(rects, finer_rects), run_time=2)
        self.wait()




"""
渲染:
manim -pql a_little_complex_manim.py PerfectSineWave
"""

class PerfectSineWave(Scene):
    def construct(self):
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

        # 5. 可视化所有元素
        self.add(axes, circle, dot, connection_line, sine_curve)

        # 6. 动画：让t从0增加到4*PI，展示点沿圆周移动以及正弦波的形成
        self.play(
            t.animate.set_value(4 * PI),
            run_time=8,
            rate_func=linear
        )
        self.wait()




"""
渲染:
manim -pql a_little_complex_manim.py LissajousMorph
"""

class LissajousMorph(Scene):
    def construct(self):
        # 一个坐标轴来展示曲线
        ax = Axes(x_range=[-3, 3], y_range=[-3, 3]).set_opacity(0.3)

        # 一个追踪器来控制动画
        phase_tracker = ValueTracker(0)

        # Lissajous曲线的参数方程
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

        # 让phase_tracker从0增加到2*PI，展示Lissajous曲线的变化
        self.play(
            phase_tracker.animate.set_value(2 * PI),
            run_time=6,
            rate_func=linear
        )
        self.wait()




"""
渲染:
manim -pql a_little_complex_manim.py FourierSquareWave
"""

class FourierSquareWave(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 10, 1], y_range=[-2, 2, 1])

        # 追踪当前使用了多少个正弦波来近似方波
        terms_tracker = ValueTracker(1)

        # 一个函数来计算方波的傅里叶级数近似值
        def fourier_approx(x, n_terms):
            result = 0
            for k in range(1, int(n_terms) * 2, 2):  # 只使用奇数项
                result += (4 / (PI * k)) * np.sin(k * x)
            return result

        # 动态绘制方波
        curve = always_redraw(lambda: ax.plot(
            lambda x: fourier_approx(x, max(1, terms_tracker.get_value())),
            color=TEAL
        ))

        # 一个用于展示当前添加了多少个正弦波的标签
        label = always_redraw(lambda: Text(
            f"Sine Waves Added: {int(terms_tracker.get_value())}",
            font_size=32
        ).to_corner(UL))

        self.add(ax, curve, label)

        # 渲染动画，逐渐增加正弦波的数量
        self.play(
            terms_tracker.animate.set_value(15),
            run_time=6,
            rate_func=linear
        )
        self.wait()