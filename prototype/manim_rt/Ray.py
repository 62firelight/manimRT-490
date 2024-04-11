from manim import *
import numpy as np



class Ray:
    def __init__(self, start_point, end_point, distance=2, color=BLUE):
        self.start_point = start_point
        self.direction = np.subtract(end_point, start_point)
        self.distance = distance
        self.color = color
        
        mobject_end_point = self.start_point + self.distance * np.array(self.direction)
        
        self.mobject = Arrow3D(start_point, mobject_end_point, color=color)
    
    def get_start_point(self):
        return self.start_point
    
    def get_direction(self):
        return self.direction
    
    def get_distance(self):
        return self.distance
    
    def get_mobject(self):
        return self.mobject
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
    def change_distance(self, distance):
        self.distance = distance
        
        mobject_end_point = self.start_point + self.distance * np.array(self.direction)
        
        self.mobject = Arrow3D(self.start_point, mobject_end_point, color=self.color)
        
        return self.mobject
    
    def generate_sphere(self, distance_to_center, radius=1):
        sphere_center = self.start_point + distance_to_center * np.array(self.direction)
        
        sphere = Sphere(sphere_center, radius)
        
        return sphere
        