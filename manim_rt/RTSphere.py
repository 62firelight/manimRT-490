from manim import *
from manim.typing import Point3D

from typing import Sequence

from manim_rt.Ray3D import Ray3D
from manim_rt.Utility import solve_quadratic

class RTSphere(Sphere):
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
        center: Point3D = ORIGIN,
        resolution: Sequence[int] | None = None,
        u_range: Sequence[float] = (0, TAU),
        v_range: Sequence[float] = (0, PI),
        **kwargs,
    ) -> None:
        # TODO: group everything up to after finding the inverse
        #       in its own method
        
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
        
        # keep track of the unit version of this
        # for display purposes
        self.unit_form = Sphere()
        
        self.refractive_index = refractive_index

        radius = 1
        
        super().__init__(
            center,
            radius,
            resolution,
            u_range,
            v_range,
            **kwargs
        )
        
        # TODO: maybe call apply_points_function_about_vector() using our computed transform here?
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
        # apply inverse transformation to the ray
        start_inverse = np.matmul(self.inverse, ray.homogeneous_start)
        direction_inverse = np.matmul(self.inverse, ray.homogeneous_direction)
        
        inhomogeneous_start_inverse = start_inverse[:3]
        inhomogeneous_direction_inverse = direction_inverse[:3]
        
        a = np.dot(inhomogeneous_direction_inverse, inhomogeneous_direction_inverse)
        b = 2 * np.dot(inhomogeneous_start_inverse, inhomogeneous_direction_inverse)
        c = np.dot(inhomogeneous_start_inverse, inhomogeneous_start_inverse) - 1
        
        hit_locations = solve_quadratic(a, b, c)
        
        hit_points = []
        normals = []
        for hit_location in hit_locations:
            # find hit point for the transformed ray
            hit_point = start_inverse + hit_location * direction_inverse
            
            # apply original transformation to find actual hit point
            hit_point = np.matmul(self.transform, hit_point)
            
            hit_point = hit_point[:3]
            
            hit_points.append(hit_point)
            
            # for spheres, the hit point will be the normal
            # (i.e., perpendicular to the sphere's surface)
            normals.append(hit_point - self.get_center())
    
        ray.hit_points = hit_points
        ray.normals = normals
    
        return hit_points