from manim import *
from manim.typing import Point3D

from typing import Sequence

class RTSphere(Sphere):
    def __init__(
        self,
        center: Point3D = ORIGIN,
        x_scale: float = 1,
        y_scale: float = 1,
        z_scale: float = 1,
        x_rotation: float = 0,
        y_rotation: float = 0,
        z_rotation: float = 0,
        resolution: Sequence[int] | None = None,
        u_range: Sequence[float] = (0, TAU),
        v_range: Sequence[float] = (0, PI),
        **kwargs,
    ) -> None:
        # get 3x1 translation vector
        self.translation = np.array([center[0], center[1], center[2]])
        self.inverse_translation = np.negative(self.translation)
        
        # get 3x3 scale matrix
        self.scale_matrix = np.array([
            [x_scale, 0, 0],
            [0, y_scale, 0],
            [0, 0, z_scale]
        ])
        
        # get 3x3 rotation matrix
        self.rot_matrix = np.zeros((3, 3))
        if x_rotation != 0:
            self.rot_matrix += rotation_matrix(x_rotation, RIGHT)
        if y_rotation != 0:
            self.rot_matrix += rotation_matrix(y_rotation, UP)
        if z_rotation != 0:
            self.rot_matrix += rotation_matrix(z_rotation, OUT)
        
        # combine scale and rotation matrices and compute inverse
        self.transform = self.scale_matrix + self.rot_matrix
        self.inverse_scale_rot_matrix = np.linalg.inv(self.transform)
        
        # combine scale and rotation matrices with translation vector
        self.transform = np.c_[self.transform, self.translation]
        
        # ensure the linear transformation is stored as homogeneous coordinates
        self.transform = np.r_[self.transform, np.array([[0, 0, 0, 1]])]
        
        # combine inverse scale and inverse rotation matrices with inverse translation vector
        self.inverse = np.c_[self.inverse_scale_rot_matrix, self.inverse_translation]
        
        # ensure the inverse transformation is stored as homogeneous coordinates
        self.inverse = np.r_[self.inverse, np.array([[0, 0, 0, 1]])]
        
        self.unit_form = Sphere()

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
        
        print(self.transform)
        print(self.inverse)
        