from manim import *

class ColorSwitcher(Scene):
    def construct(self):
        square = Square(fill_opacity=1).scale(2)
        label = Text("Press R, G, or B", font_size=24).to_edge(UP)

        self.add(square, label)
        self.interactive_embed()  # This keeps the window open and listening

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




class PolygonExplorer(Scene):
    def construct(self):
        self.sides = 3
        # Create a polygon and center it
        self.poly = RegularPolygon(n=self.sides).scale(2)

        self.count_text = Integer(self.sides).to_edge(UP)
        label = Text("Sides: ", font_size=36).next_to(self.count_text, LEFT)

        self.add(self.poly, self.count_text, label)
        self.interactive_embed()

    def on_key_press(self, symbol, modifiers):
        # Press Up Arrow to add sides, Down Arrow to remove them
        if symbol == ord("w") or symbol == 65362:  # 'w' or Up Arrow
            self.sides += 1
        elif (symbol == ord("s") or symbol == 65364) and self.sides > 3:  # 's' or Down Arrow
            self.sides -= 1

        # Update the visual objects
        new_poly = RegularPolygon(n=self.sides).scale(2).set_color(self.poly.get_color())
        self.poly.become(new_poly)
        self.count_text.set_value(self.sides)

        super().on_key_press(symbol, modifiers)