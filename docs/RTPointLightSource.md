<!-- markdownlint-disable -->

<a href="..\blob\main\manim_rt\RTPointLightSource.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `RTPointLightSource`




**Global Variables**
---------------
- **cli_ctx_settings**
- **SCENE_NOT_FOUND_MESSAGE**
- **CHOOSE_NUMBER_MESSAGE**
- **INVALID_NUMBER_MESSAGE**
- **NO_SCENE_MESSAGE**
- **NORMAL**
- **ITALIC**
- **OBLIQUE**
- **BOLD**
- **THIN**
- **ULTRALIGHT**
- **LIGHT**
- **SEMILIGHT**
- **BOOK**
- **MEDIUM**
- **SEMIBOLD**
- **ULTRABOLD**
- **HEAVY**
- **ULTRAHEAVY**
- **RESAMPLING_ALGORITHMS**
- **ORIGIN**
- **UP**
- **DOWN**
- **RIGHT**
- **LEFT**
- **IN**
- **OUT**
- **X_AXIS**
- **Y_AXIS**
- **Z_AXIS**
- **UL**
- **UR**
- **DL**
- **DR**
- **START_X**
- **START_Y**
- **DEFAULT_DOT_RADIUS**
- **DEFAULT_SMALL_DOT_RADIUS**
- **DEFAULT_DASH_LENGTH**
- **DEFAULT_ARROW_TIP_LENGTH**
- **SMALL_BUFF**
- **MED_SMALL_BUFF**
- **MED_LARGE_BUFF**
- **LARGE_BUFF**
- **DEFAULT_MOBJECT_TO_EDGE_BUFFER**
- **DEFAULT_MOBJECT_TO_MOBJECT_BUFFER**
- **DEFAULT_POINTWISE_FUNCTION_RUN_TIME**
- **DEFAULT_WAIT_TIME**
- **DEFAULT_POINT_DENSITY_2D**
- **DEFAULT_POINT_DENSITY_1D**
- **DEFAULT_STROKE_WIDTH**
- **DEFAULT_FONT_SIZE**
- **SCALE_FACTOR_PER_FONT_POINT**
- **PI**
- **TAU**
- **DEGREES**
- **QUALITIES**
- **DEFAULT_QUALITY**
- **EPILOG**
- **CONTEXT_SETTINGS**
- **SHIFT_VALUE**
- **CTRL_VALUE**


---

<a href="..\blob\main\manim_rt\RTPointLightSource.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RTPointLightSource`
A sphere that represents a light source within a scene. 



**Args:**
 
 - <b>`center`</b>:  The location of the light source's centre. 
 - <b>`intensity`</b>:  The intensity of the light source. 
 - <b>`color`</b>:  The color of the light source. By default, this is set to yellow. 
 - <b>`radius`</b>:  The radius of the light source. 

<a href="..\blob\main\manim_rt\RTPointLightSource.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    center: Union[ndarray[Any, dtype[float64]], Tuple[float, float, float]] = array([0., 0., 0.]),
    intensity: float = 1,
    color: ManimColor = ManimColor('#FFFF00'),
    radius: float = 1,
    **kwargs
) → None
```






---

#### <kbd>property</kbd> animate

Used to animate the application of any method of :code:`self`. 

Any method called on :code:`animate` is converted to an animation of applying that method on the mobject itself. 

For example, :code:`square.set_fill(WHITE)` sets the fill color of a square, while :code:`square.animate.set_fill(WHITE)` animates this action. 

Multiple methods can be put in a single animation once via chaining: 

:
``` 

     self.play(my_mobject.animate.shift(RIGHT).rotate(PI)) 

.. warning:
``` 

     Passing multiple animations for the same :class:`Mobject` in one      call to :meth:`~.Scene.play` is discouraged and will most likely      not work properly. Instead of writing an animation like 

    :
``` 

         self.play(my_mobject.animate.shift(RIGHT), my_mobject.animate.rotate(PI)) 

     make use of method chaining. 

```
Keyword arguments that can be passed to :meth:`.Scene.play` can be passed directly after accessing ``.animate``, like so:
``` 

     self.play(my_mobject.animate(rate_func=linear).shift(RIGHT)) 

```
This is especially useful when animating simultaneous ``.animate`` calls that you want to behave differently:
``` 

     self.play(          mobject1.animate(run_time=2).rotate(PI),          mobject2.animate(rate_func=there_and_back).shift(RIGHT),      ) 

.. seealso:
``` 

     :func:`override_animate` 



```
Examples 
-------- 

.. manim:: AnimateExample 

 class AnimateExample(Scene):  def construct(self):  s = Square()  self.play(Create(s))  self.play(s.animate.shift(RIGHT))  self.play(s.animate.scale(2))  self.play(s.animate.rotate(PI / 2))  self.play(Uncreate(s)) 



.. manim:: AnimateChainExample 

 class AnimateChainExample(Scene):  def construct(self):  s = Square()  self.play(Create(s))  self.play(s.animate.shift(RIGHT).scale(2).rotate(PI / 2))  self.play(Uncreate(s)) 

.. manim:: AnimateWithArgsExample 

 class AnimateWithArgsExample(Scene):  def construct(self):  s = Square()  c = Circle() 

 VGroup(s, c).arrange(RIGHT, buff=2)  self.add(s, c) 

 self.play(  s.animate(run_time=2).rotate(PI / 2),  c.animate(rate_func=there_and_back).shift(RIGHT),  ) 

.. warning:
``` 

     ``.animate``       will interpolate the :class:`~.Mobject` between its points prior to       ``.animate`` and its points after applying ``.animate`` to it. This may       result in unexpected behavior when attempting to interpolate along paths,       or rotations.       If you want animations to consider the points between, consider using       :class:`~.ValueTracker` with updaters instead. 

---

#### <kbd>property</kbd> color





---

#### <kbd>property</kbd> depth

The depth of the mobject. 

Returns 
------- :class:`float` 

See also 
-------- :meth:`length_over_dim` 

---

#### <kbd>property</kbd> fill_color

If there are multiple colors (for gradient) this returns the first one 

---

#### <kbd>property</kbd> height

The height of the mobject. 

Returns 
------- :class:`float` 

Examples 
-------- .. manim:: HeightExample 

 class HeightExample(Scene):  def construct(self):  decimal = DecimalNumber().to_edge(UP)  rect = Rectangle(color=BLUE)  rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5) 

 decimal.add_updater(lambda d: d.set_value(rect.height)) 

 self.add(rect_copy, rect, decimal)  self.play(rect.animate.set(height=5))  self.wait() 

See also 
-------- :meth:`length_over_dim` 

---

#### <kbd>property</kbd> n_points_per_curve





---

#### <kbd>property</kbd> stroke_color





---

#### <kbd>property</kbd> width

The width of the mobject. 

Returns 
------- :class:`float` 

Examples 
-------- .. manim:: WidthExample 

 class WidthExample(Scene):  def construct(self):  decimal = DecimalNumber().to_edge(UP)  rect = Rectangle(color=BLUE)  rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5) 

 decimal.add_updater(lambda d: d.set_value(rect.width)) 

 self.add(rect_copy, rect, decimal)  self.play(rect.animate.set(width=7))  self.wait() 

See also 
-------- :meth:`length_over_dim` 



---

<a href="..\blob\main\manim_rt\RTPointLightSource.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_illumination_at`

```python
get_illumination_at(point: ndarray | tuple[float]) → float
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
