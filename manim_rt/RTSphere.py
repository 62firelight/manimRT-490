from manim import *
from manim.typing import Point3D

from typing import Sequence

from manim_rt.Ray3D import Ray3D
from manim_rt.Utility import solve_quadratic


class RTSphere(Sphere):
    """A sphere with transformations that are applied and tracked.
    
    Args:
        translation: The translation transformation to apply to the sphere.
        x_scale: The scale of the sphere along the X axis.
        y_scale: The scale of the sphere along the Y axis.
        z_scale: The scale of the sphere along the Z axis.
        x_rotation: The rotation of the sphere along the X axis.
        y_rotation: The rotation of the sphere along the Y axis.
        z_rotation: The rotation of the sphere along the Z axis.
        refractive_index: The refractive index of the sphere.
        color: The color of the sphere.
        opacity: The opacity of the sphere.
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
        **kwargs,
    ) -> None:        
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
        
        super().__init__(
            center = ORIGIN,
            radius = 1,
            resolution = None,
            u_range = (0, TAU),
            v_range = (0, PI),
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
        """Calculates the intersection point(s) between this sphere and a given ray.
        
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
    
    @staticmethod
    def generate_sphere(
        ray: Ray3D,
        distance_along_ray: float = 1,
        x_scale: float = 1,
        y_scale: float = 1,
        z_scale: float = 1,
        x_rotation: float = 0,
        y_rotation: float = 0,
        z_rotation: float = 0,
        refractive_index: float = 1,
        color: ParsableManimColor = WHITE,
        opacity: float = 1,
    ):
        """Generates a sphere along a given ray. 
        Useful for guaranteeing an intersection point with a ray.
        
        Args:
            ray: A Ray3D Mobject to use for generating a sphere.
            distance_along_ray: The distance along the ray at which a sphere will be generated.
            translation: The translation transformation to apply to the sphere.
            x_scale: The scale of the sphere along the X axis.
            y_scale: The scale of the sphere along the Y axis.
            z_scale: The scale of the sphere along the Z axis.
            x_rotation: The rotation of the sphere along the X axis.
            y_rotation: The rotation of the sphere along the Y axis.
            z_rotation: The rotation of the sphere along the Z axis.
            refractive_index: The refractive index of the sphere.
            color: The color of the sphere.
            opacity: The opacity of the sphere.
        """
        sphere_center = ray.start + distance_along_ray * np.array(ray.direction)
        
        sphere = RTSphere(sphere_center, x_scale, y_scale, z_scale, x_rotation, y_rotation, z_rotation, refractive_index, color)
        
        return sphere