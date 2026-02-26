from manim import *

"""
渲染:
manim -qm -p --renderer=opengl manim_ce_opengl.py ColorSwitcher
按下R、G、B键来切换颜色
"""
class ColorSwitcher(Scene):
    def construct(self):
        self.square = Square(fill_opacity=1).scale(2)
        self.square.set_color(BLUE_E)

        title = Text("OpenGL Interactive", font_size=36).to_edge(UP)
        hint = Text("R/G/B: 切换颜色   +/-: 亮度   SPACE: 旋转", font_size=24, color=GRAY_A)
        hint.next_to(title, DOWN)

        self.brightness = 0.85
        self.color_name = "BLUE"
        self.status = always_redraw(
            lambda: Text(
                f"Color: {self.color_name}    Brightness: {self.brightness:.2f}",
                font_size=24,
                color=WHITE,
            ).to_edge(DOWN)
        )

        self.add(self.square, title, hint, self.status)
        self.interactive_embed()  # 这会让场景进入一个交互式模式，等待用户输入



    def on_key_press(self, symbol, modifiers):
        # 我们检查按下的键，并根据按键改变方块的颜色
        if symbol == ord("r"):
            self.square.set_color(RED_E)
            self.color_name = "RED"
            self.play(Flash(self.square, color=RED, flash_radius=2.2), run_time=0.3)
        elif symbol == ord("g"):
            self.square.set_color(GREEN_E)
            self.color_name = "GREEN"
            self.play(Flash(self.square, color=GREEN, flash_radius=2.2), run_time=0.3)
        elif symbol == ord("b"):
            self.square.set_color(BLUE_E)
            self.color_name = "BLUE"
            self.play(Flash(self.square, color=BLUE, flash_radius=2.2), run_time=0.3)
        elif symbol in (ord("+"), ord("=")):
            self.brightness = min(1.0, self.brightness + 0.05)
            self.square.set_fill(opacity=self.brightness)
        elif symbol in (ord("-"), ord("_")):
            self.brightness = max(0.1, self.brightness - 0.05)
            self.square.set_fill(opacity=self.brightness)
        elif symbol == ord(" "):
            self.play(Rotate(self.square, angle=PI / 2), run_time=0.35)

        # 标准的事件处理调用，确保其他按键事件仍然可以被处理
        super().on_key_press(symbol, modifiers)



"""
渲染:
manim -qm -p --renderer=opengl manim_ce_opengl.py PolygonExplorer
按下W键增加边数，S键减少边数（最少为3）
"""
class PolygonExplorer(Scene):
    def construct(self):
        self.sides = 3
        self.spin = False

        title = Text("Polygon Explorer", font_size=36).to_edge(UP)
        hint = Text("W/S 或 ↑/↓: 边数   SPACE: 旋转开关", font_size=24, color=GRAY_A)
        hint.next_to(title, DOWN)

        self.poly = RegularPolygon(n=self.sides).scale(2).set_color_by_gradient(TEAL, BLUE)
        self.count_text = Integer(self.sides).to_edge(UP)
        label = Text("Sides:", font_size=32).next_to(self.count_text, LEFT)
        self.count_text.next_to(label, RIGHT, buff=0.25)

        self.spin_state = always_redraw(
            lambda: Text(
                "Spin: ON" if self.spin else "Spin: OFF",
                font_size=24,
                color=YELLOW if self.spin else GRAY_A,
            ).to_edge(DOWN)
        )

        self.poly.add_updater(lambda m, dt: m.rotate(0.9 * dt) if self.spin else None)

        self.add(self.poly, title, hint, label, self.count_text, self.spin_state)
        self.interactive_embed()

    def on_key_press(self, symbol, modifiers):
        # 按下W键增加边数，S键减少边数（最少为3）
        if symbol == ord("w") or symbol == 65362:  # w键或上箭头
            self.sides += 1
        elif (symbol == ord("s") or symbol == 65364) and self.sides > 3:  # s键或下箭头，并且边数不能少于3
            self.sides -= 1
        elif symbol == ord(" "):
            self.spin = not self.spin

        # 更新多边形和文本显示
        new_poly = RegularPolygon(n=self.sides).scale(2).set_color_by_gradient(TEAL, BLUE)
        self.play(Transform(self.poly, new_poly), run_time=0.25)
        self.count_text.set_value(self.sides)

        super().on_key_press(symbol, modifiers)