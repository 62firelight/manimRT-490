import numpy as np
from manim import *

from manim_rt.Helper import clamp
from manim_rt.Ray import Ray

"""
TODO for ray-object intersections:
* Check if indeterminate rotations happen with other objects
* Determine if ray objects should be immutable
* Determine if the Camera's draw_ray should be normalizing the vector's magnitude
* Generate spheres that intersect the ray at different points (2 intersection points + 1 intersection + no intersection)
* Perform automatic intersections between rays and spheres at the origin
    * Automatically figure out the normal (easy for spheres)
* Perform automatic intersections between rays and transformed spheres
    * Automatically figure out the inverse of the linear transformation (use a matrix library like NumPy??)
    * Apply the inverse linear transformation to the ray (start point of the ray + direction of the ray)
    * Then apply the transformation to the hit point to find the actual intersection
    * Also apply the transposed inverse transformation to the normal to find the actual normal
* Add option to initialize camera grid with x value and aspect ratio
    
TODO DONE:
* Add drawRay function for drawing through pixels (AKA center of grid cell) -- could try using c2p method
* Add focal length parameter
* Parameterize for grid width and height (i.e., camera resolution)
* Add draw_ray function for drawing rays anywhere (potentially based on a ray equation)
* Keep track of ray properties (ray equation, hit point, etc)
"""
    
class Camera:
    def __init__(self, projection_point_coords=[0, 0, 0], focal_length=1, width=16, height=9, total_width=5, total_height=5):
        self.projection_point_coords = projection_point_coords
        self.width = width
        self.height = height
        self.total_width = total_width
        self.total_height = total_height
        
        # Projection point made up of a 3D dot
        self.projection_point = Dot3D(projection_point_coords, radius = 0.15, color = WHITE)
        
        # Determine Z coordinate of image plane
        plane_z_coord = projection_point_coords[2] - focal_length
        
        # Grid made up of a number plane
        self.grid = NumberPlane(x_range=[0, width, 1], y_range=[-height, 0, 1], x_length=total_width, y_length=total_height)
        self.grid.move_to([projection_point_coords[0], projection_point_coords[1], projection_point_coords[2] - focal_length])

        # Determine corner coordinates
        top_left_coords = self.grid.c2p(0, 0)
        top_right_coords = self.grid.c2p(width, 0)
        bottom_left_coords = self.grid.c2p(0, -height)
        bottom_right_coords = self.grid.c2p(width, -height)
        
        # Frustum made up of 4 3D lines
        self.top_left = Line3D(projection_point_coords, [top_left_coords[0], top_left_coords[1], plane_z_coord], color=WHITE)
        self.top_right = Line3D(projection_point_coords, [top_right_coords[0], top_right_coords[1], plane_z_coord], color=WHITE)
        self.bottom_left = Line3D(projection_point_coords, [bottom_left_coords[0], bottom_left_coords[1], plane_z_coord], color=WHITE)
        self.bottom_right = Line3D(projection_point_coords, [bottom_right_coords[0], bottom_right_coords[1], plane_z_coord], color=WHITE)
        
        self.camera = Group(self.projection_point, self.top_left, self.top_right, self.bottom_left, self.bottom_right, self.grid)
        
    def draw_ray(self, x, y, distance=2, color=BLUE):
        pixel_x_coord = round(x)
        pixel_y_coord = round(y)
        
        pixel_x_coord = clamp(pixel_x_coord, 1, self.width)
        pixel_y_coord = -clamp(pixel_y_coord, 1, self.height)
        
        pixel_coords = self.grid.c2p(pixel_x_coord - 0.5, pixel_y_coord + 0.5)
        
        # TODO: creating another object inside this object method -- possibly bad design??
        ray = Ray(self.projection_point_coords, pixel_coords, distance, color)
        
        # 1 unit of this ray's distance is equivalent to the camera's focal length
        
        return ray
        
    def get_mobject(self):
        return self.camera
    
    def get_projection_point(self):
        return self.projection_point
    
    def get_top_left(self):
        return self.top_left
    
    def get_bottom_left(self):
        return self.bottom_left
    
    def get_top_right(self):
        return self.top_right
    
    def get_bottom_right(self):
        return self.bottom_right
    
    def get_grid(self):
        return self.grid

def drawCamera(projection_point_coords = [0, 0, 0], focal_length=1, number_plane_grid = True):
    """
    Legacy function. Use Camera objects to create a ManimRT Camera.
    """

    top_x_coord = 2.5 + projection_point_coords[0]
    bottom_x_coord = -2.5 + projection_point_coords[0]
    left_y_coord = 2.5 + projection_point_coords[1]
    right_y_coord = -2.5 + projection_point_coords[1]
    plane_z_coord = projection_point_coords[2]
    
    projection_point = Dot3D(projection_point_coords, radius = 0.15, color = WHITE)
    
    if number_plane_grid:
        # Grid made up of a number plane
        grid = NumberPlane(x_range = [-1, 1, 1/3], y_range = [-1, 1, 1/3], x_length = 5, y_length = 5)
        grid.move_to([projection_point_coords[0], projection_point_coords[1], projection_point_coords[2] - focal_length])
    else:
        # Grid made up of 4 3D lines
        top = Line3D([top_x_coord, left_y_coord, plane_z_coord - focal_length], [top_x_coord, right_y_coord, plane_z_coord - focal_length], color=WHITE)
        bottom = Line3D([bottom_x_coord, left_y_coord, plane_z_coord - focal_length], [bottom_x_coord, right_y_coord, plane_z_coord - focal_length], color=WHITE)
        left = Line3D([top_x_coord, left_y_coord, plane_z_coord - focal_length], [bottom_x_coord, left_y_coord, plane_z_coord - focal_length], color=WHITE)
        right = Line3D([top_x_coord, right_y_coord, plane_z_coord - focal_length], [bottom_x_coord, right_y_coord, plane_z_coord - focal_length], color=WHITE)
        grid = Group(top, bottom, left, right) 
    
    # Frustum made up of 4 3D lines
    top_left = Line3D(projection_point_coords, [top_x_coord, left_y_coord, plane_z_coord - focal_length], color=WHITE)
    bottom_left = Line3D(projection_point_coords, [bottom_x_coord, left_y_coord, plane_z_coord - focal_length], color=WHITE)
    top_right = Line3D(projection_point_coords, [top_x_coord, right_y_coord, plane_z_coord - focal_length], color=WHITE)
    bottom_right = Line3D(projection_point_coords, [bottom_x_coord, right_y_coord, plane_z_coord - focal_length], color=WHITE)
    
    camera = Group(projection_point, top_left, top_right, bottom_left, bottom_right, grid)
    
    return camera