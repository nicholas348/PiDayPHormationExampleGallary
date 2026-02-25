from manimlib import *
from matplotlib import axes

"""
渲染:
manimgl manim_gl_for_grant_sanderson.py Introduction 可移动窗口
manimgl manim_gl_for_grant_sanderson.py Introduction -w渲染成视频
manimgl manim_gl_for_grant_sanderson.py Introduction -o渲染成视频并打开
manimgl manim_gl_for_grant_sanderson.py Introduction -so保存最后一个帧为图片

"""

class Introduction(Scene):
    def construct(self):
        # 在ManimGL中，Tex使用LaTeX（需要安装MikTeX或TeX Live）
        # 如果你没有安装LaTeX，可以使用Text替代Tex来显示文本，但无法渲染数学公式。
        hello = Text("Hello ManimGL!")
        
        # 将文本添加到场景中并显示
        self.play(Write(hello))
        self.wait()
        
        # 接下来，我们将文本变形成一个圆形，展示ManimGL的变形功能
        circle = Circle(color=BLUE)
        self.play(ReplacementTransform(hello, circle))
        self.wait()







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
        surface_text = Text("For 3d scenes, try using surfaces")
        surface_text.fix_in_frame()
        surface_text.to_edge(UP)
        self.add(surface_text)
        self.wait(0.1)

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

        # Set perspective
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        surface = surfaces[0]

        self.play(
            FadeIn(surface),
            ShowCreation(surface.mesh, lag_ratio=0.01, run_time=3),
        )
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
            # Move camera frame during the transition
            frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES),
            run_time=3
        )
        # Add ambient rotation
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))

        # Play around with where the light is
        light_text = Text("You can move around the light source")
        light_text.move_to(surface_text)
        light_text.fix_in_frame()

        self.play(FadeTransform(surface_text, light_text))
        light = self.camera.light_source
        self.add(light)
        light.save_state()
        self.play(light.animate.move_to(3 * IN), run_time=5)
        self.play(light.animate.shift(10 * OUT), run_time=5)

        drag_text = Text("Try moving the mouse while pressing d or s")
        drag_text.move_to(light_text)
        drag_text.fix_in_frame()

        self.play(FadeTransform(light_text, drag_text))
        self.wait()






"""
渲染:
manimgl manim_gl_for_grant_sanderson.py InteractiveTransform 可移动窗口
manimgl manim_gl_for_grant_sanderson.py InteractiveTransform -w渲染成视频
manimgl manim_gl_for_grant_sanderson.py InteractiveTransform -o渲染成视频并打开
manimgl manim_gl_for_grant_sanderson.py InteractiveTransform -so保存最后一个帧为图片
manimgl manim_gl_for_grant_sanderson.py InteractiveTransform -i 可交互模式


当你处于可交互模式时，尝试在终端中输入：

When the window opens, type these into your terminal:

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



from manimlib import *
import numpy as np

class TerminalTransform(Scene):
    def construct(self):
        # 1. Setup the interactive "Handles" (The dots)
        h1 = Dot([1, 0, 0], color=RED)
        h2 = Dot([0, 1, 0], color=GREEN)
        
        # 2. Create the Grid with custom properties
        # 'faded_line_ratio' and 'stroke_width' change the look
        grid = NumberPlane(
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            }
        )
        
        # 3. Create the "Transformable" Grid
        # This grid starts as a standard one but will be warped by our matrix
        moving_grid = NumberPlane(
            x_range=(-10, 10),
            y_range=(-10, 10),
            background_line_style={"stroke_color": WHITE, "stroke_width": 1}
        )

        # Matrix display
        matrix_tex = DecimalMatrix([[1, 0], [0, 1]], num_decimal_places=1)
        matrix_tex.to_corner(UL).fix_in_frame()

        # Vectors and Labels
        v1 = Vector(color=RED).add_updater(lambda v: v.put_start_and_end_on(ORIGIN, h1.get_center()))
        v2 = Vector(color=GREEN).add_updater(lambda v: v.put_start_and_end_on(ORIGIN, h2.get_center()))
        label_v1 = Tex("\\hat{i}", color=RED).add_updater(lambda m: m.next_to(h1, UR, buff=0.1))
        label_v2 = Tex("\\hat{j}", color=GREEN).add_updater(lambda m: m.next_to(h2, UR, buff=0.1))

        # --- THE CORE LOGIC: GRID TRANSFORMATION ---
        def get_current_matrix():
            return np.array([
                [h1.get_center()[0], h2.get_center()[0], 0],
                [h1.get_center()[1], h2.get_center()[1], 0],
                [0, 0, 1]
            ])

        # This updater warps the moving_grid based on h1 and h2
        # We start with a fresh grid and apply the matrix every frame
        original_grid = moving_grid.copy()
        def update_grid(g):
            matrix = get_current_matrix()
            new_grid = original_grid.copy()
            new_grid.apply_matrix(matrix)
            g.become(new_grid)

        moving_grid.add_updater(update_grid)

        # Matrix text updater
        def update_matrix_tex(m):
            c1, c2 = h1.get_center(), h2.get_center()
            nm = DecimalMatrix([[c1[0], c2[0]], [c1[1], c2[1]]], num_decimal_places=1)
            nm.to_corner(UL).fix_in_frame()
            m.become(nm)

        matrix_tex.add_updater(update_matrix_tex)

        self.add(grid, moving_grid, v1, v2, h1, h2, label_v1, label_v2, matrix_tex)

        self.embed()
        