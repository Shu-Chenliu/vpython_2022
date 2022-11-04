N=int(input("how many ball do you want to lift?"))
from vpython import*
from math import*
g=9.8
k=150000
m=1
size=0.2
L=2
ek=0
t=0
totalek=0
totalpe=0
scene=canvas(width=800,height=600,center =vec(0,0,0),align ='left',background=vec(0.5,0.5,0))
oscillation=graph(width=450,align ='left',xtitle='time',ytitle='total of instant energy')
oscillation1=graph(width=450,align='left',xtitle='time',ytitle='total of average energy')
funct=gcurve(graph=oscillation,color=color.blue,width=4,label='Ek')
functb= gcurve(graph = oscillation, color=color.green,width=4,label='PE')
funct1=gcurve(graph=oscillation1,color=color.red,width=4,label='Ek')
funct1b=gcurve(graph=oscillation1,color=color.blue,width=4,label='PE')
balls=[]
for i in range(5):
    if(i<N):
        ball=sphere(pos=vec(-((2.0)**2-(1.95)**2)**0.5+0.4*i,-1.95,0),radius=size,color=color.white)
        ball.v=vec(0,0,0)
        balls.append(ball)
    if(i>=N):
        ball=sphere(pos=vec(i*0.4,-L-m*g/k,0),radius=size,color=color.white)
        ball.v=vec(0,0,0)
        balls.append(ball)
springs=[]
for i in range(5):
    spring=cylinder(pos=vec(i*0.4,0,0),radius=0.005)
    springs.append(spring)
def col(v1,v2,x1,x2):
    v1_prime = v1 + 2*(1/2)*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
    v2_prime = v2 + 2*(1/2)*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
    return (v1_prime, v2_prime) 
dt=0.0001
while True:
    rate(5000)
    t+=dt
    for i in range(5):
        springs[i].axis=balls[i].pos-springs[i].pos
        springs[i].force=-k*(mag(springs[i].axis)-L)*springs[i].axis.norm()
        balls[i].a=vec(0,-g,0)+springs[i].force/m
        balls[i].v += balls[i].a * dt
        balls[i].pos += balls[i].v * dt
    for i in range(4):
        if (mag(balls[i].pos - balls[i+1].pos) <= 0.4 and dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) <= 0) :
            (balls[i].v, balls[i+1].v) = col(balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)
    ek=0
    pe=0
    for i in range(5):
        ek+=1/2*m*(mag(balls[i].v)**2)
        totalek+=1/2*m*(mag(balls[i].v)**2)*dt
        pe+=m*9.8*(balls[i].pos.y+2+m*g/k)
        totalpe+=m*9.8*(balls[i].pos.y+2+m*g/k)*dt
    funct.plot( pos=(t,ek))
    functb.plot( pos=(t,pe))
    funct1.plot( pos=(t, totalek/t))
    funct1b.plot( pos=(t, totalpe/t))
