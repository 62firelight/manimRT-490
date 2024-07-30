from manim import *

class PhongIlluminationModel(Scene):
    def construct(self):
        phong = MathTex("I(\\boldsymbol{p})=I_ak_a + I_dk_d(",
                        "\\boldsymbol{\hat{n}}",
                        "\cdot", 
                        "\\boldsymbol{\hat{l}}", 
                        ") + I_sk_s(", 
                        "\\boldsymbol{\hat{r}}", 
                        "\cdot", 
                        "\\boldsymbol{\hat{v}}", 
                        ")^a")
        
        phong.set_color_by_tex("\\boldsymbol{\hat{n}}", BLUE)
        phong.set_color_by_tex("\\boldsymbol{\hat{l}}", YELLOW)
        phong.set_color_by_tex("\\boldsymbol{\hat{r}}", ORANGE)
        phong.set_color_by_tex("\\boldsymbol{\hat{v}}", GREEN)
        
        phong_multiple_lights = MathTex(r"I(\vec{p})=I_ak_a + \sum\limits_i(I_{d, i}k_d(\hat{n} \cdot \hat{l_i}) + I_{s, i}k_s(\hat{r_i} \cdot \hat{v})^a)")
        
        phong_multiple_lights_colours = MathTex(
        r"""
        \begin{pmatrix}
            R \\
            G \\ 
            B \\
        \end{pmatrix}
        = 
        \begin{pmatrix}
            A_rr_a \\
            A_gg_a \\ 
            A_bb_a \\
        \end{pmatrix}
        + 
        \sum\limits_i
        \begin{pmatrix}
            I_{r, i}(r_d(\hat{n} \cdot \hat{l_i}) + r_s(\hat{r_i} \cdot \hat{v})^a) \\
            I_{g, i}(g_d(\hat{n} \cdot \hat{l_i}) + g_s(\hat{r_i} \cdot \hat{v})^a) \\
            I_{b, i}(b_d(\hat{n} \cdot \hat{l_i}) + b_s(\hat{r_i} \cdot \hat{v})^a)
        \end{pmatrix}
        """)
        
        # models = VGroup(phong, phong_multiple_lights, phong_multiple_lights_colours).arrange(DOWN)
        
        # self.add(models)
        # self.play(Write(models))
        
        self.add(phong)