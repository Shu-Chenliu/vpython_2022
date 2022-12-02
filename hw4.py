import numpy as np
from vpython import *
A, N, omega = 0.10, 50, 2*pi/1.0 
size, m, k, d = 0.06, 0.1, 10.0, 0.4 
##scene = canvas(title='Spring Wave', width=800, height=300, background=vec(0.5,0.5,0), center = vec((N-1)*d/2, 0, 0)) 
##balls = [sphere(radius=size, color=color.red, pos=vector(i*d, 0, 0), v=vector(0,0,0)) for i in range(N)]
##springs = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(i*d, 0, 0), axis=vector(d,0,0)) for i in range(N-1)]
##c = curve([vector(i*d, 1.0, 0) for i in range(N)], color=color.black)
g = graph(title='Dispersion Relationship', width=1200, height=600, align='left', xtitle="Wavevector",ytitle="Angular Frequency")
p = gcurve(graph=g, color=color.blue, width=2)
for n in arange(1.0,N//2,1.0):
    Unit_K= 2 * pi/(N*d)
    Wavevector = n * Unit_K
    phase = Wavevector * arange(N) * d
    ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d
    t, dt = 0, 0.0003
    T=0
    change=0
    while change<5*2:
        t+=dt
        spring_len[:-1]=ball_pos[1:]-ball_pos[:-1]
        ball_v[1:]+=(k*(spring_len[1:]-d)/m*dt-k*(spring_len[:-1]-d)/m*dt)
        spring_len[N - 1] = ball_pos[0] - ball_pos[N - 1] + N * d
        ball_v[0] +=k*(spring_len[0]-d)/m*dt-k*(spring_len[N-1]-d)/m*dt
        if ball_pos[0]*(ball_pos[0]+ball_v[0]*dt)<0 and t>3*dt:
            change+=1;
        ball_pos += ball_v*dt
    T=t/5
    p.plot(pos=(Wavevector,2*pi/T))
