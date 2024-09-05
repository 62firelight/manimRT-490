<!-- markdownlint-disable -->

<a href="..\blob\main\manim_rt\RTCamera.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `RTCamera`




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

<a href="..\blob\main\manim_rt\RTCamera.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RTCamera`
A virtual camera that represents the observer of a scene. 



**Args:**
 
 - <b>`projection_point_coords`</b>:  The 3D coordinates of the projection point. 
 - <b>`image_width`</b>:  The grid width of the camera's 2D image plane. 
 - <b>`image_height`</b>:  The grid height of the camera's 2D image plane. 
 - <b>`total_width`</b>:  The width of the camera's 2D image plane. 
 - <b>`total_height`</b>:  The height of the camera's 2D image plane. 
 - <b>`focal_length`</b>:  The distance from the projection point to the image plane. 

<a href="..\blob\main\manim_rt\RTCamera.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    projection_point_coords: list = array([0., 0., 0.]),
    image_width: int = 16,
    image_height: int = 9,
    total_width: int = 1,
    total_height: int = 1,
    focal_length: int = 1,
    **kwargs: dict[str, Any]
)
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

<a href="..\blob\main\manim_rt\RTCamera.py#L276"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `colour_pixel`

```python
colour_pixel(
    x: float,
    y: float,
    color: Union[ManimColor, int, str, Tuple[int, int, int], Tuple[float, float, float], Tuple[int, int, int, int], Tuple[float, float, float, float], ndarray[Any, dtype[int64]], ndarray[Any, dtype[float64]]] = ManimColor('#58C4DD')
)
```

Creates a colored Square Mobject at the pixel specified by (x, y). 



**Args:**
 
 - <b>`x`</b>:  The x coordinate of the pixel. 
 - <b>`y`</b>:  The y coordinate of the pixel. 
 - <b>`color`</b>:  The color of the Square Mobject at the specified pixel. 



**Returns:**
 A Square Mobject at the pixel specified by (x, y). 

---

<a href="..\blob\main\manim_rt\RTCamera.py#L237"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `draw_ray`

```python
draw_ray(
    x: float,
    y: float,
    length: float = 1,
    thickness: float = 0.02,
    color: Union[ManimColor, int, str, Tuple[int, int, int], Tuple[float, float, float], Tuple[int, int, int, int], Tuple[float, float, float, float], ndarray[Any, dtype[int64]], ndarray[Any, dtype[float64]]] = ManimColor('#58C4DD')
)
```

Creates a ray that goes through the centre of the pixel specified by (x, y). 



**Args:**
 
 - <b>`x`</b>:  The x coordinate of the pixel that the ray goes through. 
 - <b>`y`</b>:  The y coordinate of the pixel that the ray goes through. 
 - <b>`length`</b>:  The length of the ray. 
 - <b>`thickness`</b>:  The thickness of the ray. 
 - <b>`color`</b>:  The color of the ray. 



**Returns:**
 A Ray3D Mobject that goes through the centre of the pixel specified by (x, y). 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
