from manim import *

class QuadraticFormula(Scene):
    def construct(self):
        quadratic_formula = MathTex(r"\lambda = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        
        self.add(quadratic_formula)