from manimlib import *
import numpy as np

"""
渲染:
manimgl manim_gl_for_grant_sanderson.py Introduction 可移动窗口
manimgl manim_gl_for_grant_sanderson.py Introduction -w渲染成视频
manimgl manim_gl_for_grant_sanderson.py Introduction -o渲染成视频并打开
manimgl manim_gl_for_grant_sanderson.py Introduction -so保存最后一个帧为图片

"""

class Introduction(Scene):
    def construct(self):
        title = Text("ManimGL", font_size=72, gradient=(BLUE, TEAL))
        subtitle = Text("实时渲染 + 可交互窗口", font_size=36, color=GREY_B)
        subtitle.next_to(title, DOWN)
        group = VGroup(title, subtitle)

        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.25), run_time=1.2)
        self.wait(0.3)

        badge = RoundedRectangle(corner_radius=0.2, width=8.5, height=2.6)
        badge.set_stroke(WHITE, 2).set_fill(BLACK, opacity=0.25)
        badge.move_to(group)
        self.play(FadeIn(badge), run_time=0.6)
        self.play(group.animate.to_edge(UP), badge.animate.to_edge(UP), run_time=1.0)

        hello = Text("Hello ManimGL!", font_size=56)
        self.play(FadeIn(hello, shift=DOWN * 0.4))
        self.wait(0.2)

        circle = Circle(color=BLUE).set_fill(BLUE_E, opacity=0.25)
        square = Square(color=GREEN).set_fill(GREEN_E, opacity=0.25)
        triangle = Triangle(color=YELLOW).set_fill(YELLOW_E, opacity=0.25)

        self.play(ReplacementTransform(hello, circle), run_time=1.0)
        self.play(Transform(circle, square), run_time=0.8)
        self.play(Transform(circle, triangle), run_time=0.8)

        orbit = Circle(radius=2.6, color=GREY_B)
        dot = Dot(color=RED)
        self.play(ShowCreation(orbit), FadeIn(dot))
        self.play(MoveAlongPath(dot, orbit), run_time=2.0, rate_func=linear)
        self.wait(0.3)







"""
借鉴代码：
https://3b1b.github.io/manim/getting_started/example_scenes.html


渲染:
manimgl manim_gl_for_grant_sanderson.py SurfaceExample 可移动窗口
manimgl manim_gl_for_grant_sanderson.py SurfaceExample -w渲染成视频
manimgl manim_gl_for_grant_sanderson.py SurfaceExample -o渲染成视频并打开
manimgl manim_gl_for_grant_sanderson.py SurfaceExample -so保存最后一个帧为图片
"""


class SurfaceExample(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        surface_text = Text("3D 曲面示例", font_size=36)
        surface_text.fix_in_frame()
        surface_text.to_edge(UP)
        hint = Text("拖动窗口/滚轮可改变视角", font_size=24, color=GREY_B)
        hint.fix_in_frame()
        hint.next_to(surface_text, DOWN)
        self.add(surface_text, hint)
        self.wait(0.2)

        torus1 = Torus(r1=1, r2=1)
        torus2 = Torus(r1=3, r2=1)
        sphere = Sphere(radius=3, resolution=torus1.resolution)
        day_texture = "day_world.jpg"
        night_texture = "night_world.jpg"

        surfaces = [
            TexturedSurface(surface, day_texture, night_texture)
            for surface in [sphere, torus1, torus2]
        ]

        for mob in surfaces:
            mob.shift(IN)
            mob.mesh = SurfaceMesh(mob)
            mob.mesh.set_stroke(BLUE, 1, opacity=0.5)

        # 设置相机视角
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        surface = surfaces[0]

        self.play(FadeIn(surface), ShowCreation(surface.mesh, lag_ratio=0.01, run_time=3))
        for mob in surfaces:
            mob.add(mob.mesh)
        surface.save_state()
        self.play(Rotate(surface, PI / 2), run_time=2)
        for mob in surfaces[1:]:
            mob.rotate(PI / 2)

        self.play(
            Transform(surface, surfaces[1]),
            run_time=3
        )

        self.play(
            Transform(surface, surfaces[2]),
            # 同时旋转相机来展示不同的视角
            frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES),
            run_time=3
        )
        # 让相机持续旋转
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))

        # 移动光源
        light_text = Text("你可以使用代码移动光源", font_size=30)
        light_text.move_to(surface_text)
        light_text.fix_in_frame()

        self.play(FadeTransform(surface_text, light_text))
        light = self.camera.light_source
        self.add(light)
        light.save_state()
        self.play(light.animate.move_to(3 * IN), run_time=5)
        self.play(light.animate.shift(10 * OUT), run_time=5)

        drag_text = Text("尝试使用 d 移动相机位置", font_size=30)
        drag_text.move_to(light_text)
        drag_text.fix_in_frame()

        self.play(FadeTransform(light_text, drag_text))
        self.wait(0.5)






"""
渲染:
manimgl manim_gl_for_grant_sanderson.py TerminalTransform 可移动窗口
manimgl manim_gl_for_grant_sanderson.py TerminalTransform -w渲染成视频
manimgl manim_gl_for_grant_sanderson.py TerminalTransform -o渲染成视频并打开
manimgl manim_gl_for_grant_sanderson.py TerminalTransform -so保存最后一个帧为图片
manimgl manim_gl_for_grant_sanderson.py TerminalTransform -i 可交互模式


当你处于可交互模式时，尝试在终端中输入：

--移动点h1--
self.play(h1.animate.move_to([2, 0, 0]))

--移动点h2--
self.play(h2.animate.move_to([1, 1, 0]))
self.play(h2.animate.move_to([-1, 2, 0]))
self.play(h2.animate.move_to([4, 3, 0]))
self.play(h2.animate.move_to([-3, 2, 0]))

--重置点位置--
self.play(h1.animate.move_to([1, 0, 0]), h2.animate.move_to([0, 1, 0]))

-改变网格颜色--
moving_grid.set_style(stroke_color=RED)

-改变网格线宽--
moving_grid.set_style(stroke_width=1)
moving_grid.set_style(stroke_width=2)
moving_grid.set_style(stroke_width=3)
moving_grid.set_style(stroke_width=4)
moving_grid.set_style(stroke_width=5)
"""
class TerminalTransform(Scene):
    def construct(self):
        title = Text("Terminal Transform", font_size=42)
        title.to_edge(UP)
        title.fix_in_frame()
        hint = Text("用 -i 进入交互模式，在终端输入 self.play(...)", font_size=24, color=GREY_B)
        hint.next_to(title, DOWN)
        hint.fix_in_frame()
        self.add(title, hint)

        h1 = Dot([1, 0, 0], color=RED)
        h2 = Dot([0, 1, 0], color=GREEN)
        
        
        grid = NumberPlane(
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            }
        )
        
        #  创建一个新的网格，这个网格将被我们的矩阵变形
        moving_grid = NumberPlane(
            x_range=(-10, 10),
            y_range=(-10, 10),
            background_line_style={"stroke_color": WHITE, "stroke_width": 1}
        )

        
        matrix_tex = DecimalMatrix([[1, 0], [0, 1]], num_decimal_places=1)
        matrix_tex.to_corner(UL).fix_in_frame()

        
        v1 = Vector(color=RED).add_updater(lambda v: v.put_start_and_end_on(ORIGIN, h1.get_center()))
        v2 = Vector(color=GREEN).add_updater(lambda v: v.put_start_and_end_on(ORIGIN, h2.get_center()))
        label_v1 = Tex("\\hat{i}", color=RED).add_updater(lambda m: m.next_to(h1, UR, buff=0.1))
        label_v2 = Tex("\\hat{j}", color=GREEN).add_updater(lambda m: m.next_to(h2, UR, buff=0.1))

        
        def get_current_matrix():
            return np.array([
                [h1.get_center()[0], h2.get_center()[0], 0],
                [h1.get_center()[1], h2.get_center()[1], 0],
                [0, 0, 1]
            ])

        
        original_grid = moving_grid.copy()
        def update_grid(g):
            matrix = get_current_matrix()
            new_grid = original_grid.copy()
            new_grid.apply_matrix(matrix)
            g.become(new_grid)

        moving_grid.add_updater(update_grid)

        
        def update_matrix_tex(m):
            c1, c2 = h1.get_center(), h2.get_center()
            nm = DecimalMatrix([[c1[0], c2[0]], [c1[1], c2[1]]], num_decimal_places=1)
            nm.to_corner(UL).fix_in_frame()
            m.become(nm)

        matrix_tex.add_updater(update_matrix_tex)

        self.add(grid, moving_grid, v1, v2, h1, h2, label_v1, label_v2, matrix_tex)

        self.play(FadeIn(h1), FadeIn(h2), run_time=0.4)
        self.play(h1.animate.shift(RIGHT * 1.0), h2.animate.shift(UP * 1.0), run_time=0.8)
        self.play(h1.animate.move_to([1, 0, 0]), h2.animate.move_to([0, 1, 0]), run_time=0.8)

        self.embed()
        