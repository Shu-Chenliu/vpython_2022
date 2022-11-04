from vpython import*
g=9.8
size=0.25
height=15.0
C_drag=0.9
d=0
scene1=canvas(width=600,height=600,align='left',center=vec(0,height/2,0),background=vec(0.5,0.5,0))
oscillation=graph(width=450,height=300,align='left',xtitle='time',ytitle='speed')
funct1=gcurve(graph=oscillation,color=color.blue,width=3)
floor=box(canvas=scene1,length=30,height=0.01,width=10,color=color.blue)
ball=sphere(canvas=scene1,radius=size,color=color.red,make_trail=True,trail_radius=0.05)
a1=arrow(canvas=scene1,color=color.green,shaftwidth=0.05)
t=0
ball.pos=vec(-15,size,0)
theta=pi/4
ball.v=vec(20*cos(theta),20*sin(theta),0)
dt=0.001
bounce=0
while bounce<3:
    rate(1000)
    a1.pos=ball.pos
    a1.axis=0.5*ball.v
    funct1.plot(pos=(t,ball.v.mag))
    t+=dt
    ball.v=ball.v+vec(0,-g,0)*dt-C_drag*ball.v*dt
    ball.pos=ball.pos+ball.v*dt
    d+=ball.v.mag*dt
    if abs(ball.v.y)<=0.005 and bounce==0:
        m=text(text='largest height='+str(ball.pos.y),pos=vec(-10,10,0))
    if ball.pos.y<=size and ball.v.y<0:
        ball.v.y=-ball.v.y
        bounce+=1
a1.visible=False
msg=text(text='displacement='+str(ball.pos.x+15),pos=vec(-10,15,0))
mm=text(text='total travel distance'+str(d),pos=vec(-10,13,0))