import numbers
from typing import Any, Sequence
from manim import *

import numpy as np

from manim_rt.Ray3D import Ray3D
from manim_rt.Utility import clamp


class RTCamera(Axes):
    """A virtual camera that represents the observer of a scene.
    
    Parameters
    ----------
    projection_point_coords
        The 3D coordinates of the projection point.
    image_width
        The grid width of the camera's 2D image plane.
    image_height
        The grid height of the camera's 2D image plane.
    total_width
        The width of the camera's 2D image plane.
    total_height
        The height of the camera's 2D image plane.
    focal_length
        The distance from the projection point to the image plane.
    """
    def __init__(
        self,
        projection_point_coords: list = ORIGIN,
        image_width: int = 16,
        image_height: int = 9,
        total_width: int = 1,
        total_height: int = 1,
        focal_length: int = 1,
        **kwargs: dict[str, Any],
    ):
        self.projection_point_coords = projection_point_coords
        x_range=[0, image_width, 1]
        y_range=[-image_height, 0, 1]
        x_length=total_width
        y_length=total_height
        self.focal_length = focal_length
        self.image_width = image_width
        self.image_height = image_height
        self.total_width = total_width
        self.total_height = total_height
        
        # Configs 
        # ManimRT changes stroke_width from 2 to 0 
        # to hide the white lines from the Axes
        self.axis_config = {
            "stroke_width": 0,
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
        
        # Default NumberPlane parameters
        background_line_style: dict[str, Any] | None = None
        faded_line_style: dict[str, Any] | None = None
        faded_line_ratio: int = 1
        make_smooth_after_applying_functions: bool = True

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
    
        plane_z_coord = projection_point_coords[2] - focal_length
    
        self.projection_point = Dot3D(projection_point_coords, color = WHITE)
        
        self.move_to([projection_point_coords[0], projection_point_coords[1], plane_z_coord])
        
        # Determine corner coordinates
        top_left_coords = self.c2p(0, 0)
        top_right_coords = self.c2p(image_width, 0)
        bottom_left_coords = self.c2p(0, -image_height)
        bottom_right_coords = self.c2p(image_width, -image_height)
        
        # Frustum made up of 4 3D lines
        self.top_left = Line3D(projection_point_coords, [top_left_coords[0], top_left_coords[1], plane_z_coord], thickness=0.01, color=WHITE)
        self.top_right = Line3D(projection_point_coords, [top_right_coords[0], top_right_coords[1], plane_z_coord], thickness=0.01, color=WHITE)
        self.bottom_left = Line3D(projection_point_coords, [bottom_left_coords[0], bottom_left_coords[1], plane_z_coord], thickness=0.01, color=WHITE)
        self.bottom_right = Line3D(projection_point_coords, [bottom_right_coords[0], bottom_right_coords[1], plane_z_coord], thickness=0.01, color=WHITE)
        
        self.add_to_back(
            self.projection_point,
            self.top_left,
            self.top_right,
            self.bottom_left,
            self.bottom_right
        )
        
    def _init_background_lines(self) -> None:
        """A method ported over from NumberPlane. Will init all the lines of 
        NumberPlanes (faded or not)"""
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
            # self.faded_lines,
            self.background_lines,
        )
        
    def _get_lines(self) -> tuple[VGroup, VGroup]:
        """A method ported over from NumberPlane. Generate all the lines, faded and not faded.
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
        """A method ported over from NumberPlane. Generate a set of lines parallel to an axis.

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

        line = Line3D(axis_parallel_to.get_start(), axis_parallel_to.get_end(), thickness=0.001)
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
        
        # ManimRT adds or subtracts 1 to these ranges to ensure
        # that the the grid looks like it is contained within a
        # blue box
        ranges = (
            [0],
            np.arange(step, min(x_max - x_min, x_max) + 1, step),
            np.arange(-step, max(x_min - x_max, x_min) - 1, -step),
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
       
    def draw_ray(
        self,
        x: float, 
        y: float, 
        distance: float = 1, 
        thickness: float = 0.02, 
        color: ParsableManimColor = BLUE
    ):
        """Creates a ray that goes through the centre of the pixel specified by (x, y).
        
        Parameters
        ----------
        x
            The x coordinate of the pixel that the ray goes through.
        y
            The y coordinate of the pixel that the ray goes through.
        distance
            The length of the ray.
        thickness
            The thickness of the ray.
        color
            The color of the ray.
            
        Returns
        -------
        A Ray3D Mobject that goes through the centre of the pixel specified by (x, y).
        """
        if distance is None:
            distance = self.focal_length * 2
        
        pixel_x_coord = round(x)
        pixel_y_coord = round(y)
        
        pixel_x_coord = clamp(pixel_x_coord, 1, self.image_width)
        pixel_y_coord = -clamp(pixel_y_coord, 1, self.image_height)
        
        pixel_coords = self.c2p(pixel_x_coord - 0.5, pixel_y_coord + 0.5)
        
        ray_direction = pixel_coords - self.projection_point.get_center()
        
        ray = Ray3D(self.projection_point.get_center(), ray_direction, distance=distance, thickness=thickness, color=color)
        
        # 1 unit of this ray's distance is equivalent to the camera's focal length
        
        return ray
    
    def colour_pixel(
        self,
        x: float, 
        y: float,  
        color: ParsableManimColor = BLUE
    ):
        """Creates a colored Square Mobject at the pixel specified by (x, y).
        
        Parameters
        ----------
        x
            The x coordinate of the pixel.
        y 
            The y coordinate of the pixel.
        color
            The color of the Square Mobject at the specified pixel.
            
        Returns
        -------
        A Square Mobject at the pixel specified by (x, y).
        """
        pixel_x_coord = round(x)
        pixel_y_coord = round(y)
        
        pixel_x_coord = clamp(pixel_x_coord, 1, self.image_width)
        pixel_y_coord = -clamp(pixel_y_coord, 1, self.image_height)
        
        pixel_coords = self.c2p(pixel_x_coord - 0.5, pixel_y_coord + 0.5)
        
        square = Square(side_length=1, stroke_opacity=0, fill_opacity=1, fill_color=color, shade_in_3d=True)
        
        # Scale square according to the camera dimensions
        square_width = self.total_width / self.image_width
        square_height = self.total_height / self.image_height
        
        square.stretch(square_width, 0)
        square.stretch(square_height, 1)
        
        square.shift(pixel_coords)
        
        return square
    