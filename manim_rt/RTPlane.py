from typing import Sequence
from manim import *

from manim_rt.Ray3D import Ray3D


class RTPlane(Square):
    """A plane with transformations that are applied and tracked.
    
    Args:
        translation: The translation transformation to apply to the plane.
        x_scale: The scale of the plane along the X axis.
        y_scale: The scale of the plane along the Y axis.
        z_scale: The scale of the plane along the Z axis.
        x_rotation: The rotation of the plane along the X axis.
        y_rotation: The rotation of the plane along the Y axis.
        z_rotation: The rotation of the plane along the Z axis.
        refractive_index: The refractive index of the plane.
        color: The color of the plane.
        opacity: The opacity of the plane.
    """
    def __init__(
        self,
        translation: Sequence[float] = [0, 0, 0],
        x_scale: float = 1,
        y_scale: float = 1,
        z_scale: float = 1,
        x_rotation: float = 0,
        y_rotation: float = 0,
        z_rotation: float = 0,
        refractive_index: float = 1,
        color=WHITE,
        opacity=1,
        **kwargs
    ):
        # get 3x3 scale matrix
        self.scale_matrix = np.array([
            [x_scale, 0, 0],
            [0, y_scale, 0],
            [0, 0, z_scale]
        ])
        
        # get 3x3 rotation matrix
        self.rot_matrix = np.identity(3)
        self.rot_matrix = np.matmul(rotation_matrix(x_rotation, RIGHT), self.rot_matrix)
        self.rot_matrix = np.matmul(rotation_matrix(y_rotation, UP), self.rot_matrix)
        self.rot_matrix = np.matmul(rotation_matrix(z_rotation, OUT), self.rot_matrix)
        
        # get 4x4 translation vector 
        # (only last column changes)
        self.translation = np.array([
            [1, 0, 0, translation[0]],  
            [0, 1, 0, translation[1]],
            [0, 0, 1, translation[2]],
            [0, 0, 0, 1],
        ])
        
        # combine scale and rotation matrices
        self.transform = np.matmul(self.rot_matrix, self.scale_matrix)
        
        # ensure the linear transformation is stored as homogeneous coordinates
        self.transform = np.c_[self.transform, np.array([0, 0, 0])]
        self.transform = np.r_[self.transform, np.array([[0, 0, 0, 1]])]
        
        # combine translation matrix with scale and rotation matrices
        self.transform = np.matmul(self.translation, self.transform)
        
        # calculate inverse
        self.inverse = np.linalg.inv(self.transform)
        
        self.refractive_index = refractive_index
        
        # keep track of the unit version of this
        # for display purposes
        self.unit_form = Square(side_length=1, fill_color=BLUE, fill_opacity=1, stroke_opacity=0)
        
        super().__init__(
            side_length=1,
            fill_color=BLUE,
            fill_opacity=1,
            stroke_opacity=0,
            shade_in_3d=True,
            **kwargs
        )
        
        self.set_color(color)
        self.set_opacity(opacity)
        
        self.stretch(x_scale, 0)
        self.stretch(y_scale, 1)
        self.stretch(z_scale, 2)
        
        self.rotate(x_rotation, RIGHT)
        self.rotate(y_rotation, UP)
        self.rotate(z_rotation, OUT)
        
        self.shift(translation)
        
    def get_intersection(
        self,
        ray: Ray3D
    ):
        """Calculates the intersection point(s) between this plane and a given ray.
        
        Args:
            ray: A Ray3D Mobject to calculate intersection point(s) with.
            
        Returns:
            An array containing the intersection point(s) with the given ray. 
        The array is empty if there are no intersection points.
        """
        # apply inverse transformation to the ray
        start_inverse = np.matmul(self.inverse, ray.homogeneous_start)
        direction_inverse = np.matmul(self.inverse, ray.homogeneous_direction)
        
        inhomogeneous_start_inverse = start_inverse[:3]
        inhomogeneous_direction_inverse = direction_inverse[:3]
        
        z0 = start_inverse[2]
        dz = direction_inverse[2]
        
        hit_location = -z0 / dz
        hit_locations = [hit_location]
        
        hit_points = []
        normals = []
        for hit_location in hit_locations:
            # find hit point for the transformed ray
            hit_point = start_inverse + hit_location * direction_inverse
            
            # apply original transformation to find actual hit point
            hit_point = np.matmul(self.transform, hit_point)
            
            hit_point = hit_point[:3]
            
            hit_points.append(hit_point)
            
            # for planes, the normal will point in either +ve or -ve Z direction
            normal = [0, 0, 1, 0]
            if np.dot(normal[:3], ray.direction) > 0:
                normal = [0, 0, -1, 0]
            
            inverse_transform_transpose = np.linalg.inv(np.transpose(self.transform))
            
            normal_transformed = np.matmul(inverse_transform_transpose, normal)
            
            normals.append(normal_transformed[:3])
    
        ray.hit_points = hit_points
        ray.normals = normals
    
        return hit_points