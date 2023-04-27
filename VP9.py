from vpython import *
m=10000
n=1000
#this could run a while
dtheta=2*pi/n
rl1=0.06/m
rx1=0
m0=4*pi*(10**-7)
phim=0
while rx1<0.06:
    dm=vec(0,0,0)
    theta=0
    while theta<2*pi:
        ds=vec(0.12*dtheta*(-sin(theta)),0.12*dtheta*cos(theta),0)
        r=vec(-0.12*cos(theta)+rx1,-0.12*sin(theta),0.1)
        dm+=m0/(4*pi)*cross(ds,r)/mag(r)**3
        theta+=dtheta
    phim+=dot(dm,vec(0,0,1))*2*pi*rx1*rl1
    rx1+=rl1
print(phim)
rl2=0.12/m
rx2=0
phim2=0
while rx2<0.12:
    dm=vec(0,0,0)
    theta=0
    while theta<2*pi:
        ds=vec(0.06*dtheta*(-sin(theta)),0.06*dtheta*cos(theta),0)
        r=vec(-0.06*cos(theta)+rx2,-0.06*sin(theta),-0.1)
        dm+=m0/(4*pi)*cross(ds,r)/mag(r)**3
        theta+=dtheta
        #print(dm)
    phim2+=dot(dm,vec(0,0,1))*2*pi*rx2*rl2
    rx2+=rl2
print(phim2)
