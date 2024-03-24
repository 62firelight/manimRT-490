from manim import *


def drawCamera(focal_point_coords = [0, 0, 5], number_plane_grid = True):
        top_x_coord = 2.5 + focal_point_coords[0]
        bottom_x_coord = -2.5 + focal_point_coords[0]
        left_y_coord = 2.5 + focal_point_coords[1]
        right_y_coord = -2.5 + focal_point_coords[1]
        plane_z_coord = focal_point_coords[2]
        
        focal_point = Dot3D(focal_point_coords, radius = 0.15, color = WHITE)
        
        if number_plane_grid:
            # Grid made up of a number plane
            # TODO: parameterize for grid width and height (i.e., camera resolution)
            grid = NumberPlane(x_range = [-1, 1, 1/3], y_range = [-1, 1, 1/3], x_length = 5, y_length = 5)
            grid.move_to([focal_point_coords[0], focal_point_coords[1], focal_point_coords[2] - 5])
        else:
            # Grid made up of 4 3D lines
            top = Line3D([top_x_coord, left_y_coord, plane_z_coord - 5], [top_x_coord, right_y_coord, plane_z_coord - 5], color=WHITE)
            bottom = Line3D([bottom_x_coord, left_y_coord, plane_z_coord - 5], [bottom_x_coord, right_y_coord, plane_z_coord - 5], color=WHITE)
            left = Line3D([top_x_coord, left_y_coord, plane_z_coord - 5], [bottom_x_coord, left_y_coord, plane_z_coord - 5], color=WHITE)
            right = Line3D([top_x_coord, right_y_coord, plane_z_coord - 5], [bottom_x_coord, right_y_coord, plane_z_coord - 5], color=WHITE)
            grid = Group(top, bottom, left, right) 
        
        # Frustum made up of 4 3D lines
        top_left = Line3D(focal_point_coords, [top_x_coord, left_y_coord, plane_z_coord - 5], color=WHITE)
        bottom_left = Line3D(focal_point_coords, [bottom_x_coord, left_y_coord, plane_z_coord - 5], color=WHITE)
        top_right = Line3D(focal_point_coords, [top_x_coord, right_y_coord, plane_z_coord - 5], color=WHITE)
        bottom_right = Line3D(focal_point_coords, [bottom_x_coord, right_y_coord, plane_z_coord - 5], color=WHITE)
        
        camera = Group(focal_point, top_left, top_right, bottom_left, bottom_right, grid)
        
        return camera