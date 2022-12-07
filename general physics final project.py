theta=float(input("what theta do you want the ball to start??"))##請人cin角度
N=int(input("how many balls do you want to simulate??"))##有幾顆球
import numpy as np
from vpython import *
g = 9.8
size, m = 0.02, 0.5 
L, k = 0.5, 15000
scene = canvas(width=500, height=500, center=vec(0, -0.2, 0), background=vec(0.5,0.5,0))
ceiling = box(length=0.8, height=0.005, width=0.8, color=color.blue)
balls=[sphere(radius = size,color=color.red,make_trail=True,trail_type="points",retain=20,pos=vec(L*sin(theta)+N*m*g/k*tan(theta),-L*cos(theta)-N*m*g/k-(N-i)*m*g/k-i*L,0),v=vec(0,0,0))for i in range(N)]
springs=[cylinder(radius=0.005,pos=vec(L*sin(theta)+N*m*g/k*tan(theta),-L*cos(theta)-N*m*g/k-(N-1-i)*m*g/k-(i-1)*L,0))for i in range(N)]
springs[0].pos=vec(0,0,0)
balls[0].v=vec(0,0,0.5)
##ball_1 = sphere(radius = size, color=color.red,make_trail=True, trail_type="points", retain=20)
##spring_1 = cylinder(radius=0.005) # default pos = vec(0, 0, 0)
##ball_1.v = vec(0, 0, 0.5)
##ball_1.pos = vec(L*sin(theta)+2*m*g/k*tan(theta),-L*cos(theta)-2*m*g/k,0)##想像有人在用fx的力拉第一顆球
##spring_2 = cylinder(radius=0.005 ,pos = vec(L*sin(theta)+2*m*g/k*tan(theta),-L*cos(theta)-2*m*g/k,0))
##ball_2 = sphere(radius = size, color=color.red,make_trail=True, trail_type="points", retain=20)
##ball_2.v = vec(0, 0, 0)
##ball_2.pos = vec(L*sin(theta)+2*m*g/k*tan(theta),-L*cos(theta)-3*m*g/k-L,0)
dt = 0.001
t = 0

while True:
 rate(1000)
 t += dt
 for i in range(N):
    if i!=0:
        springs[i].pos=balls[i-1].pos
        springs[i].axis=balls[i].pos-balls[i-1].pos
 springs[0].pos=vec(0,0,0)
 springs[0].axis=balls[0].pos-springs[0].pos
 for i in range(N):
    springs[i].force= - k * (mag(springs[i].axis) - L) * springs[i].axis.norm()
 for i in range(N):
    if i!=N-1:
        balls[i].a=vector(0, - g, 0)+springs[i].force/m-springs[i+1].force/m
    if i==N-1:
        balls[i].a=vector(0, - g, 0)+springs[i].force
    balls[i].v+=balls[i].a*dt
    balls[i].pos+=balls[i].v*dt
 ##spring_2.pos=ball_1.pos
 ##spring_1.axis = ball_1.pos - spring_1.pos #spring extended from endpoint to ball
 ##spring_2.axis = ball_2.pos - ball_1.pos
 ##spring_1_force = - k * (mag(spring_1.axis) - L) * spring_1.axis.norm() # to get spring force vector
 ##spring_2_force = - k * (mag(spring_2.axis) - L) * spring_2.axis.norm()
 ##ball_1.a = vector(0, - g, 0) + spring_1_force / m -spring_2_force / m # ball acceleration = - g in y + spring force /m
 ##ball_2.a = vector(0, - g, 0) + spring_2_force / m
 ##ball_1.v += ball_1.a*dt
 ##ball_2.v += ball_2.a*dt
 ##ball_1.pos += ball_1.v*dt
 ##ball_2.pos += ball_2.v*dt
