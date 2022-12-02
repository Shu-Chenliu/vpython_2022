from vpython import*
G=6.673E-11
mass = {'earth': 5.97E24, 'moon': 7.36E22, 'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10} #10 times larger for better view 
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
scene=canvas(width=800,height=800,background=vector(0.5,0.5,0))
scene.lights = []
local_light(pos=vector(0,0,0))
theta = 5.145*pi/180.0
class as_obj(sphere):
 def kinetic_energy(self):
     return 0.5 * self.m * mag2(self.v)
 def potential_energy(self):
     return - G * mass['sun'] * self.m / mag(self.pos)
sun=sphere(pos=vector(0,0,0),radius=radius['sun'],m=mass['sun'],color=color.orange)
earth=as_obj(pos=vector(mass['moon']*moon_orbit['r']/(mass['earth']+mass['moon'])*cos(theta)+earth_orbit['r'],mass['moon']*moon_orbit['r']/(mass['earth']+mass['moon'])*sin(theta),0),radius = radius['earth'], m = mass['earth'], texture={'file':textures.earth})
moon = as_obj(pos = vector((mass['moon']*moon_orbit['r']/(mass['earth']+mass['moon'])-moon_orbit['r'])*cos(theta)+earth_orbit['r'],(mass['moon']*moon_orbit['r']/(mass['earth']+mass['moon'])-moon_orbit['r'])*sin(theta),0), radius = radius['moon'], m = mass['moon'], color = color.white)
moon.v=vector(0,0,-moon_orbit['v']-earth_orbit['v'])
earth.v=vector(0,0,moon_orbit['v']*moon.m/earth.m-earth_orbit['v'])
i0=norm(cross(moon.pos-earth.pos,moon.v-earth.v)).x
t=0
dt=60*6*60
n=0
def G_force(m1,m2, pos_vec):
     return -G * m1 * m2 / mag2(pos_vec) * norm(pos_vec)
while True:
    rate(4*365)
    scene.center=earth.pos
    moon.a=G_force(moon.m,earth.m,moon.pos-earth.pos)/moon.m+G_force(moon.m,sun.m,moon.pos-sun.pos)/moon.m
    earth.a=G_force(moon.m,earth.m,earth.pos-moon.pos)/earth.m+G_force(earth.m,sun.m,earth.pos-sun.pos)/earth.m
    moon.v=moon.v+moon.a*dt
    earth.v=earth.v+earth.a*dt
    moon.pos=moon.pos+moon.v*dt
    earth.pos=earth.pos+earth.v*dt
    i=norm(cross(moon.pos-earth.pos,moon.v-earth.v)).x
    if i>i0*0.999 and i<i0*1.001 and n==0 and t>86400*365:
        T=t/(86400*365)
        print(" period of the precession of moon’s orbit around the Earth="+str(T)+"years")
        n=1
    t=t+dt
