import numbers
from typing import Sequence
from manim import *

import numpy as np

class RTCamera(Axes):
    def __init__(
        self,
        width: int = 16,
        height: int = 9,
        total_width: int = 5,
        total_height: int = 5,
        background_line_style: dict[str, Any] | None = None,
        faded_line_style: dict[str, Any] | None = None,
        faded_line_ratio: int = 1,
        make_smooth_after_applying_functions: bool = True,
        **kwargs: dict[str, Any],
    ):
        x_range=[0, width, 1]
        y_range=[-height, 0, 1]
        x_length=total_width
        y_length=total_height
        
        # configs
        self.axis_config = {
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "font_size": 24,
        }
        self.y_axis_config = {"label_direction": DR}
        self.background_line_style = {
            "stroke_color": BLUE_D,
            "stroke_width": 2,
            "stroke_opacity": 1,
        }

        self._update_default_configs(
            (self.axis_config, self.y_axis_config, self.background_line_style),
            (
                kwargs.pop("axis_config", None),
                kwargs.pop("y_axis_config", None),
                background_line_style,
            ),
        )

        # Defaults to a faded version of line_config
        self.faded_line_style = faded_line_style
        self.faded_line_ratio = faded_line_ratio
        self.make_smooth_after_applying_functions = make_smooth_after_applying_functions

        # init
        super().__init__(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config=self.axis_config,
            y_axis_config=self.y_axis_config,
            **kwargs,
        )

        self._init_background_lines()
        
    def _init_background_lines(self) -> None:
        """Will init all the lines of NumberPlanes (faded or not)"""
        if self.faded_line_style is None:
            style = dict(self.background_line_style)
            # For anything numerical, like stroke_width
            # and stroke_opacity, chop it in half
            for key in style:
                if isinstance(style[key], numbers.Number):
                    style[key] *= 0.5
            self.faded_line_style = style

        self.background_lines, self.faded_lines = self._get_lines()

        self.background_lines.set_style(
            **self.background_line_style,
        )
        self.faded_lines.set_style(
            **self.faded_line_style,
        )
        self.add_to_back(
            self.faded_lines,
            self.background_lines,
        )
        
    def _get_lines(self) -> tuple[VGroup, VGroup]:
        """Generate all the lines, faded and not faded.
         Two sets of lines are generated: one parallel to the X-axis, and parallel to the Y-axis.

        Returns
        -------
        Tuple[:class:`~.VGroup`, :class:`~.VGroup`]
            The first (i.e the non faded lines) and second (i.e the faded lines) sets of lines, respectively.
        """
        x_axis = self.get_x_axis()
        y_axis = self.get_y_axis()

        x_lines1, x_lines2 = self._get_lines_parallel_to_axis(
            x_axis,
            y_axis,
            self.y_axis.x_range[2],
            self.faded_line_ratio,
        )

        y_lines1, y_lines2 = self._get_lines_parallel_to_axis(
            y_axis,
            x_axis,
            self.x_axis.x_range[2],
            self.faded_line_ratio,
        )

        # TODO this was added so that we can run tests on NumberPlane
        # In the future these attributes will be tacked onto self.background_lines
        self.x_lines = x_lines1
        self.y_lines = y_lines1
        lines1 = VGroup(*x_lines1, *y_lines1)
        lines2 = VGroup(*x_lines2, *y_lines2)

        return lines1, lines2
    
    def _get_lines_parallel_to_axis(
        self,
        axis_parallel_to: NumberLine,
        axis_perpendicular_to: NumberLine,
        freq: float,
        ratio_faded_lines: int,
    ) -> tuple[VGroup, VGroup]:
        """Generate a set of lines parallel to an axis.

        Parameters
        ----------
        axis_parallel_to
            The axis with which the lines will be parallel.
        axis_perpendicular_to
            The axis with which the lines will be perpendicular.
        ratio_faded_lines
            The ratio between the space between faded lines and the space between non-faded lines.
        freq
            Frequency of non-faded lines (number of non-faded lines per graph unit).

        Returns
        -------
        Tuple[:class:`~.VGroup`, :class:`~.VGroup`]
            The first (i.e the non-faded lines parallel to `axis_parallel_to`) and second
             (i.e the faded lines parallel to `axis_parallel_to`) sets of lines, respectively.
        """

        line = Line3D(axis_parallel_to.get_start(), axis_parallel_to.get_end(), thickness=0.01)
        if ratio_faded_lines == 0:  # don't show faded lines
            ratio_faded_lines = 1  # i.e. set ratio to 1
        step = (1 / ratio_faded_lines) * freq
        lines1 = VGroup()
        lines2 = VGroup()
        unit_vector_axis_perp_to = axis_perpendicular_to.get_unit_vector()

        # need to unpack all three values
        x_min, x_max, _ = axis_perpendicular_to.x_range

        # account for different axis scalings (logarithmic), where
        # negative values do not exist and [-2 , 4] should output lines
        # similar to [0, 6]
        if axis_perpendicular_to.x_min > 0 and x_min < 0:
            x_min, x_max = (0, np.abs(x_min) + np.abs(x_max))

        # min/max used in case range does not include 0. i.e. if (2,6):
        # the range becomes (0,4), not (0,6).
        ranges = (
            [0],
            np.arange(step, min(x_max - x_min, x_max), step),
            np.arange(-step, max(x_min - x_max, x_min), -step),
        )

        for inputs in ranges:
            for k, x in enumerate(inputs):
                new_line = line.copy()
                new_line.shift(unit_vector_axis_perp_to * x)
                if (k + 1) % ratio_faded_lines == 0:
                    lines1.add(new_line)
                else:
                    lines2.add(new_line)
        return lines1, lines2