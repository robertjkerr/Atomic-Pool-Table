"""
Creates distribution along a line
"""

from ball import particle
from numpy import random

import matplotlib.pyplot as plt

"""
    `distribution` Returns distribution of n particles with random velocities between -maxV and maxV and random postions between lo and hi
    `getPos` returns a list of the position of each particle
"""

def distribution(n,maxV,lo,hi):
    particles = []
    for i in range(n):
        p = float(random.uniform(lo,hi,[1]))
        v = float(random.uniform(-maxV,maxV,[1]))
        particles.append(particle(p,v))
    return particles

def focusBall(maxV,lo,hi):
    p = float(random.uniform(lo,hi,[1]))
    v = float(random.uniform(-maxV,maxV,[1]))
    return particle(p,v)

def hit(focusBall,distribution):
    for p in distribution:
        if round(p.pos,2) == round(focusBall.pos,2):
            focusBall.collide(p.v)

def propTime(dt,t,n,maxV,lo,hi):
    timeSteps = int(t/dt)
    focus = focusBall(maxV,lo,hi)
    dist = distribution(n,maxV,lo,hi)
    vList = []

    for i in range(timeSteps):
        for part in dist:
            part.move(dt)
            if round(part.pos,2) == hi or round(part.pos,2) == lo:
                part.v = -part.v
                
                
        focus.move(dt)
        if round(focus.pos,2) == hi or round(focus.pos,2) == lo:
            focus.v = -focus.v
            
        hit(focus,dist)
        vList.append(focus.pos)

    return vList

vs = propTime(0.01,20,1000,1,-1,1)




plt.plot(vs)
plt.show()


