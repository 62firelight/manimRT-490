<!-- markdownlint-disable -->

<a href="..\blob\main\manim_rt\Ray3D.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `Ray3D`




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

<a href="..\blob\main\manim_rt\Ray3D.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Ray3D`
A 3D arrow representing a ray. 



**Args:**
 
 - <b>`start`</b>:  The originating position of the ray. 
 - <b>`direction`</b>:  The direction of the ray. 
 - <b>`length`</b>:  The length of the ray. 
 - <b>`thickness`</b>:  The thickness of the ray. 
 - <b>`color`</b>:  The color of the ray. 

<a href="..\blob\main\manim_rt\Ray3D.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    start: 'ndarray' = array([-1.,  0.,  0.]),
    direction: 'ndarray' = array([1., 0., 0.]),
    length: 'float' = 1,
    thickness: 'float' = 0.02,
    color: 'ParsableManimColor' = ManimColor('#FFFFFF'),
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

<a href="..\blob\main\manim_rt\Ray3D.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_equation`

```python
get_equation(homogeneous_coordinates=False, decimal_places=1) → str
```

Write a LaTeX equation for this ray. 



**Args:**
 
 - <b>`homogeneous_coordinates`</b>:  Determine if homogeneous coordinates should be used when displaying  the equation. 
 - <b>`decimal_places`</b>:  How many decimal places to round to when displaying the equation. 



**Returns:**
 A string formatted as LaTeX representing the ray's equation. 

---

<a href="..\blob\main\manim_rt\Ray3D.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_light_vector`

```python
get_light_vector(
    hit_point_index: 'int',
    light_source: 'RTPointLightSource'
) → list
```

Calculates the "light vector," a unit vector that starts from a  given hit point and points towards a light source within the scene. 



**Args:**
 
 - <b>`hit_point_index`</b>:  The index number of the hit point. For example, 0 would be the first hit point along the ray. 
 - <b>`light_source`</b>:  The light source mobject that the unit vector will point towards. 



**Returns:**
 An array representing the light vector. 

---

<a href="..\blob\main\manim_rt\Ray3D.py#L154"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_reflected_light_vector`

```python
get_reflected_light_vector(
    hit_point_index: 'int',
    light_source: 'RTPointLightSource'
) → list
```

Calculates the "reflected light vector," which is a light vector that reflects through the normal at a given hit point. 



**Args:**
 
 - <b>`hit_point_index`</b>:  The index number of the hit point. For example, 0 would be the  first hit point along the ray. 
 - <b>`light_source`</b>:  The light source mobject that the light vector will point towards. 



**Returns:**
 An array representing the reflected light vector. 

---

<a href="..\blob\main\manim_rt\Ray3D.py#L299"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_reflected_ray`

```python
get_reflected_ray(
    hit_point_index: 'int',
    camera: 'Mobject',
    length: 'float' = 1,
    thickness: 'float' = 0.02,
    color: 'ParsableManimColor' = ManimColor('#FFFFFF')
) → Ray3D
```

Calculates a mobject version of the "reflected ray," which is the viewer vector reflected through the normal. 



**Args:**
 
 - <b>`hit_point_index`</b>:  The index number of the hit point. For example, 0 would be the first hit point along the ray. 
 - <b>`camera`</b>:  The camera mobject that the viewer vector starts from.  
 - <b>`length`</b>:  The length of the reflected ray. 
 - <b>`thickness`</b>:  The thickness of the reflected ray. 
 - <b>`color`</b>:  The color of the reflected ray. 



**Returns:**
 A Ray3D Mobject representing the reflected vector. 

---

<a href="..\blob\main\manim_rt\Ray3D.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_reflected_vector`

```python
get_reflected_vector(hit_point_index: 'int', camera: 'Mobject') → list
```

Calculates the "reflected vector," which is the viewer vector reflected through the normal.  

Not to be confused with the reflected light vector, which is the light vector reflected through the normal.  

The reflected vector is used for simulating reflected surfaces in a  ray tracer, while the reflected light vector may be used for the  Phong illumination model. 



**Args:**
 
 - <b>`hit_point_index`</b>:  The index number of the hit point. For example, 0 would be the first hit point along the ray. 
 - <b>`camera`</b>:  The camera mobject that the viewer vector starts from.  



**Returns:**
 An array representing the reflected vector. 

---

<a href="..\blob\main\manim_rt\Ray3D.py#L335"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_refracted_ray`

```python
get_refracted_ray(
    object: 'Mobject',
    length: 'float' = 1,
    refractive_index: 'float' = 1,
    thickness: 'float' = 0.02,
    color: 'ParsableManimColor' = ManimColor('#FFFFFF')
) → Ray3D
```

Calculates a "refracted ray," a ray that bends when it  passes over to another medium (e.g. air to water). 



**Args:**
 
 - <b>`object`</b>:  The boundary between medium 1 and medium 2. 
 - <b>`length`</b>:  The length of the refracted ray. 
 - <b>`refractive_index`</b>:  The refractive index of medium 1. 
 - <b>`thickness`</b>:  The thickness of the refracted ray. 
 - <b>`color`</b>:  The color of the refracted ray. 



**Returns:**
 A Ray3D Mobject representing the refracted ray. 

---

<a href="..\blob\main\manim_rt\Ray3D.py#L218"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_shadow_ray`

```python
get_shadow_ray(
    hit_point_index: 'int',
    light_source: 'RTPointLightSource',
    thickness: 'float' = 0.02,
    color: 'ParsableManimColor' = ManimColor('#FFFFFF')
) → Ray3D
```

Create a "shadow ray," a ray that starts from a given hit point and points towards a light source. 



**Args:**
 
 - <b>`hit_point_index`</b>:  The index number of the hit point. For example, 0 would be the first hit point along the ray. 
 - <b>`light_source`</b>:  The light source Mobject that the shadow ray will point towards. 
 - <b>`thickness`</b>:  The thickness of the shadow ray. 
 - <b>`color`</b>:  The color of the shadow ray. 



**Returns:**
 A Ray3D Mobject representing a shadow ray. 

---

<a href="..\blob\main\manim_rt\Ray3D.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_unit_normal`

```python
get_unit_normal(hit_point_index: 'int') → Ray3D
```

Gets the unit normal at a specific hit point along the ray. 



**Args:**
 
 - <b>`hit_point_index`</b>:  The index number of the hit point. For example, 0 would be the first hit point along the ray. 



**Returns:**
 A Ray3D Mobject representing the unit normal at the given hit point along the ray. 

---

<a href="..\blob\main\manim_rt\Ray3D.py#L189"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_viewer_vector`

```python
get_viewer_vector(hit_point_index: 'int', camera: 'Mobject') → list
```

Calculates the "viewer vector," a unit vector that starts from a given hit point and points towards the observer of a scene (i.e. a virtual camera) 



**Args:**
 
 - <b>`hit_point_index`</b>:  The index number of the hit point. For example, 0 would be the first hit point along the ray. 
 - <b>`camera`</b>:  The virtual camera that the viewer vector will point towards. 



**Returns:**
 An array representing the viewer vector.         




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
