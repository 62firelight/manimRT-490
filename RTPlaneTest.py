from manim import *

from manim_rt.RTPlane import RTPlane
from manim_rt.Ray3D import Ray3D

class RTPlaneTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45*DEGREES, theta=45*DEGREES)
        
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        # plane = Square(side_length=2, fill_opacity=1, fill_color=BLUE, stroke_opacity=0, shade_in_3d=True)
        plane_centre = [0.5, 0.5, -0.5]
        plane = RTPlane(plane_centre, 2, 4, 6, 45 * DEGREES, 45 * DEGREES, 45 * DEGREES)
        
        ray_start = [1, -1, 1]
        ray = Ray3D(ray_start, np.subtract(plane_centre, ray_start), 5, color=RED)
        
        hit_points = plane.get_intersection(ray)
        
        first_hit_point = hit_points[0]
        self.add(Dot3D(first_hit_point))
        print(first_hit_point)
        
        unit_normal = Ray3D(first_hit_point, ray.get_unit_normal(0), color=GREEN)
        
        self.add(axes, labels, plane, ray, unit_normal)