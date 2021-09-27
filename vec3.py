import math 
import random

class Vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x, self.y, self.z = x, y, z

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def norm(self):
        mag = self.mag()
        if mag > 0:
            self.x, self.y, self.z = self.x / mag, self.y / mag, self.z / mag
        return self

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vec3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return Vec3(self.x / other, self.y / other, self.x / other)

    def dot(self, vec2):
        return self.x * vec2.x + self.y * vec2.y + self.z * vec2.z

    def __repr__(self):
        return (self.x, self.y, self.z).__repr__()

    def clone(self):
        return Vec3(self.x, self.y, self.z)

    def clamp(self, low, high):
        return Vec3(
            min(max(self.x, low), high),
            min(max(self.y, low), high),
            min(max(self.z, low), high),
        )

    @classmethod
    def random(self):
        return Vec3(
            random.random(), 
            random.random(), 
            random.random()
        )
