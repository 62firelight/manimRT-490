<!-- markdownlint-disable -->

<a href="..\blob\main\manim_rt\Utility.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `Utility`





---

<a href="..\blob\main\manim_rt\Utility.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `solve_quadratic`

```python
solve_quadratic(a: float, b: float, c: float) → list
```

Solves a quadratic equation that is set equal to 0. 



**Args:**
 
 - <b>`a`</b>:  The a value to substitute into the quadratic formula. 
 - <b>`b`</b>:  The b value to substitute into the quadratic formula. 
 - <b>`c`</b>:  The c value to substitute into the quadratic formula. 



**Returns:**
 An array containing the solution(s) to the given quadratic equation. This array will be empty if there are no solutions. 


---

<a href="..\blob\main\manim_rt\Utility.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_whole_number`

```python
is_whole_number(number: float) → bool
```

Check if a given number is considered to be an integer. 



**Args:**
 
 - <b>`number`</b>:  The number to check. 



**Returns:**
 A boolean determining whether the given number is an integer or not. 


---

<a href="..\blob\main\manim_rt\Utility.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `clamp`

```python
clamp(n: float, min: float, max: float)
```

Quick helper function for limiting numbers. 

source: https://www.geeksforgeeks.org/how-to-clamp-floating-numbers-in-python/  



**Args:**
 
 - <b>`n`</b>:  The number to limit. 
 - <b>`min`</b>:  The lower bound of the number. 
 - <b>`max`</b>:  The upper bound of the number. 



**Returns:**
 A number that falls in the domain [min, max]. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
