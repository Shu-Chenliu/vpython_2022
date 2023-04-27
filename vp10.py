from vpython import*
fd = 120 # 120Hz
#(Your Parameters here)
R=30
L=0.2
C=20E-6
i=0
q=0
findimax=0
Elow=0
Emax=0
ip=-10
t = 0
dt = 1.0/(fd * 5000) # 5000 simulation points per cycle
T=1/fd
scene1 = graph(align = 'left', xtitle='t', ytitle='i (A) blue, v (100V) red,', background=vector(0.2, 0.6, 0.2))
scene2 = graph(align = 'left', xtitle='t', ytitle='Energy (J)', background=vector(0.2, 0.6, 0.2))
i_t = gcurve(color=color.blue, graph = scene1)
v_t = gcurve(color=color.red, graph = scene1)
E_t = gcurve(color=color.red, graph = scene2)
#(Your program here)
while t<=12*T:
    rate(10000)
    v=36*sin(2*pi*fd*t)
    vr=i*R
    vc=q/C
    vl=v-vr-vc
    i+=vl/L*dt
    q+=i*dt
    E=1/2*C*vc**2+1/2*L*i**2
    i_t.plot(pos=(t,i))
    v_t.plot(pos=(t,v))
    E_t.plot(pos=(t,E))
    if t>=9*T and findimax==0 :
        if i>ip:
            ip=i
        else:
            findimax=1
            print("i=",ip)
            phiv=asin(v/36)
            print("phi=",pi/2-phiv)
    t+=dt
    Emax=E
while t<=20*T:
    rate(10000)
    v=0
    vr=i*R
    vc=q/C
    vl=v-vr-vc
    i+=vl/L*dt
    q+=i*dt
    E=1/2*C*vc**2+1/2*L*i**2
    if E<=0.1*Emax and Elow==0:
        Elow=1
        print(t)
    i_t.plot(pos=(t,i))
    v_t.plot(pos=(t,v))
    E_t.plot(pos=(t,E))
    t+=dt
