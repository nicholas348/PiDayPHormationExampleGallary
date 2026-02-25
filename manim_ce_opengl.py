from manim import *

"""
渲染:
manim -qm -p --renderer=opengl basic_manim.py ColorSwitcher
按下R、G、B键来切换颜色
"""
class ColorSwitcher(Scene):
    def construct(self):
        square = Square(fill_opacity=1).scale(2)
        label = Text("Press R, G, or B", font_size=24).to_edge(UP)

        self.add(square, label)
        self.interactive_embed()  # 这会让场景进入一个交互式模式，等待用户输入



    def on_key_press(self, symbol, modifiers):
        # We look for the "R", "G", and "B" keys
        if symbol == ord("r"):
            self.mobjects[0].set_color(RED)
        elif symbol == ord("g"):
            self.mobjects[0].set_color(GREEN)
        elif symbol == ord("b"):
            self.mobjects[0].set_color(BLUE)

        # Standard Manim event handling
        super().on_key_press(symbol, modifiers)



"""
渲染:
manim -qm -p --renderer=opengl basic_manim.py PolygonExplorer
按下W键增加边数，S键减少边数（最少为3）
"""
class PolygonExplorer(Scene):
    def construct(self):
        self.sides = 3
        # 创建一个正多边形，初始为三角形
        self.poly = RegularPolygon(n=self.sides).scale(2)

        self.count_text = Integer(self.sides).to_edge(UP)
        label = Text("Sides: ", font_size=36).next_to(self.count_text, LEFT)

        self.add(self.poly, self.count_text, label)
        self.interactive_embed()

    def on_key_press(self, symbol, modifiers):
        # 按下W键增加边数，S键减少边数（最少为3）
        if symbol == ord("w") or symbol == 65362:  # w键或上箭头
            self.sides += 1
        elif (symbol == ord("s") or symbol == 65364) and self.sides > 3:  # s键或下箭头，并且边数不能少于3
            self.sides -= 1

        # 更新多边形和文本显示
        new_poly = RegularPolygon(n=self.sides).scale(2).set_color(self.poly.get_color())
        self.poly.become(new_poly)
        self.count_text.set_value(self.sides)

        super().on_key_press(symbol, modifiers)