from vpython import *
import numpy as np
N = 100
R, lamda = 1.0, 500E-9
d = 100E-6
k=2*pi/lamda
dx, dy = d/N, d/N
scene1 = canvas(align = 'left', height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene2 = canvas(align = 'right', x=600, height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene1.lights, scene2.lights = [], []
scene1.ambient, scene2.ambient = color.gray(0.99), color.gray(0.99)
side = np.linspace(-0.01*pi, 0.01*pi, N)
x,y = np.meshgrid(side,side)
#E_field = cos(10000*((x-0.005)**2 + (y- 0.002)**2 )) # change this to calculate the electric field of diffraction of the aperture
a=np.zeros((N,N))
for X in range(N):
    for Y in range(N):
        if (X-0.5*N)**2+(Y-0.5*N)**2<=(0.5*N)**2:
            a+=(np.cos(k*x*(X*dx-0.5*d)/R+k*y*(Y*dy-0.5*d)/R)/R*dx*dy)
E_field=a
Inte = abs(E_field) ** 2
maxI = np.amax(Inte)
for i in range(N):
    for j in range(N):
        box(canvas=scene1,pos=vector(i*dx,j*dy,0),length=dx,height=dy,width=dx,color=vector(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))
Inte = abs(E_field)
maxI = np.amax(Inte)
for i in range(N):
    for j in range(N):
        box(canvas=scene2,pos=vector(i*dx,j*dy,0),length=dx,height=dy,width=dx,color=vector(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))
b=int(N/2)
c=b
findmin=0
while True:
    if Inte[b+1,c]>=Inte[b,c] and findmin==0:
        findmax=1
        break
    else:
        b+=1
theta=(b-N/2)*0.02*pi/N
print("experimental theta=",theta)
print("theoretical theta=",1.22*lamda/d)
