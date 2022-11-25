#Author:Chipo
#Date:10/22/2022
#Purpose::Lab2 -body

from cs1lib import*

class Body:
    def __init__(self,m,x,y,vx,vy,pixel_radius,r,g,b):#notice that you have put the radius of the body
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.r=r
        self.g=g
        self.b=b
        self.m=m
        self.radius=pixel_radius


    def draw(self, cx, cy, pixel_per_meter):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(cx + self.x * pixel_per_meter, cy + self.y*pixel_per_meter, self.radius)


    def update_position(self,n):
        self.x=self.x+self.vx*n
        self.y=self.y+self.vy*n


    def update_velocity(self,ax,ay,n):
        self.vx=self.vx+ax*n
        self.vy=self.vy+ay*n

    def __str__(self):
        return str(self.x)+","+str(self.y)+","+str(self.vx)+","+str(self.vy)+","+str(self.r)