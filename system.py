# Author:Chipo
# Date:10/22/2022
# Purpose::Lab2 -system

from math import sqrt


class System:
    def __init__(self, body_list):
        self.body_list = body_list

    def draw(self, cx, cy, r):  # r is pixels_per_meter
        for i in self.body_list:
            i.draw(cx, cy, r)

    def compute_accelerations(self, n):  # function takes in index i as parameter n
        G = 6.67384e-11
        ax = 0
        ay = 0
        for j in self.body_list:
            if self.body_list[n] != j:
                dx = j.x - self.body_list[n].x
                dy = j.y - self.body_list[n].y
                r2 = dx * dx + dy * dy

                # computing acceleration
                a = G * j.m / (r2)

                # Updating accelerations in x and y components
                ax = ax + a * (dx / sqrt(r2))
                ay = ay + a * (dy / sqrt(r2))

        return (ax, ay)

    def update(self, n):

        # Updating positions in all planets
        i = 0
        while i < len(self.body_list):
            self.body_list[i].update_position(n)
            i = i + 1

        # calculating the accelerations and thus updating accelerations in all planets
        i = 0
        while i < len(self.body_list):
            (ax, ay) = self.compute_accelerations(i)
            self.body_list[i].update_velocity(ax, ay, n)
            i = i + 1
