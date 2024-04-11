from manim import *

class RayFormula(Scene):
    def construct(self):
        ray_formula = MathTex('\overrightarrow{p} = \overrightarrow{p_0} = \lambda\overrightarrow{d}')
        ray_symbol_meanings = BulletedList(
        "$p_0$ is the start of the ray", 
        "$\overrightarrow{d}$ is the direction of the ray",
        "$\lambda$ is the distance along the ray",
        "So $\overrightarrow{p}$ is the point $\lambda$ units along the ray"
        )
        self.play(Create(VGroup(ray_formula, ray_symbol_meanings).arrange(DOWN)))
