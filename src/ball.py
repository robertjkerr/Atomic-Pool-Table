"""
Class for an individual particle
"""

class particle:
    """
        `move` moves the particle at velocity v for time dt
        `collide` adjusts velocity for collision with other particle of velocity v2
    """
    
    def __init__(self, initPos, initVelo):
        self.pos = initPos
        self.v = initVelo

    def move(self, dt):
        self.pos = self.pos + self.v * dt

    def collide(self, v2):
        self.v = v2


