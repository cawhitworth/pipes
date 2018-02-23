#!/usr/bin/python3

import random

# Play with these parameters for different results
length = 5000
wrap = 20
wiggliness = 1

# 1 = Bottom -Y
# 2 = Top    +Y
# 3 = Left   -X
# 4 = Right  +X
# 5 = Near   -Z
# 6 = Far    +Z

leaving_to_entering = [ None, 2, 1, 4, 3, 6, 5 ]

class ThreeVec(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, p):
        return ThreeVec(self.x + p.x, self.y + p.y, self.z + p.z)

    def wrap(self, wrap):
        for d in (0,1,2):
            if self[d] < -wrap: self[d] = wrap
            if self[d] > wrap: self[d] = -wrap

    def __getitem__(self, d):
        if d == 0: return self.x
        if d == 1: return self.y
        if d == 2: return self.z
        raise KeyError(d)

    def __setitem__(self, d, i):
        if d == 0: self.x = i
        elif d == 1: self.y = i
        elif d == 2: self.z = i
        else: raise KeyError(d)

    def __repr__(self):
        return "<{0}, {1}, {2}>".format(self.x, self.y, self.z)

exit_face_delta = [
        ThreeVec( 0,  0,  0),
        ThreeVec( 0, -1,  0),
        ThreeVec( 0,  1,  0),
        ThreeVec(-1,  0,  0),
        ThreeVec( 1,  0,  0),
        ThreeVec( 0,  0, -1),
        ThreeVec( 0,  0,  1)
    ]

def start(size):
    p = ThreeVec(random.randint(-wrap, wrap),
          random.randint(-wrap, wrap),
          random.randint(-wrap, wrap))

    exit_face = random.randint(1,6)

    if exit_face == 1: p.y = -wrap
    if exit_face == 2: p.y = wrap
    if exit_face == 3: p.x = -wrap
    if exit_face == 4: p.x = wrap
    if exit_face == 5: p.z = -wrap
    if exit_face == 6: p.z = wrap

    return (p, exit_face)

class Segment(object):
    def __init__(self, enter, exit, position):
        self._enter = enter
        self._exit = exit
        self._pos = position

    def __repr__(self):
        return("object {{ Connect_{0}{1} translate {2} }}"
            .format(self._enter, self._exit, self._pos))

def generate_povray(segments):
    header = """
#include "pipes.inc"
#include "colors.inc"

background { color rgb <0.9, 0.9, 0.9> }
light_source {
    <-100, 100, -30>
    color White
}

light_source {
    <100, 100, 30>
    color Red
}

light_source {
    <100, -100, -100>
    color Blue
}
union {
"""
    objects = "\n".join([ str(seg) for seg in segments ])

    footer = """
    texture {
        pigment { color White }
    }
    finish {
        ambient 0.1
        diffuse 0.7
        specular 1
    }

    rotate 15 * z
    rotate 15 * y
}
"""
    return header + objects + footer

class CollisionMap(object):
    def __init__(self):
        self.m = dict()

    def is_occupied(self, p):
        if p.x in self.m:
            m2 = self.m[p.x]
            if p.y in m2:
                m3 = m2[p.y]
                return p.z in m3

    def add(self, p):
        if not p.x in self.m:
            self.m[p.x] = dict()

        m2 = self.m[p.x]

        if not p.y in m2:
            m2[p.y] = dict()

        m3 = m2[p.y]

        m3[p.z] = 1


    def is_trapped(self, p, wrap):
        for direction in range(1,7):

            d = exit_face_delta[direction]
            pp = p.add(d)
            pp.wrap(wrap)

            if not self.is_occupied(pp):
                return False

        return True

def random_other_face(face):
    return random.sample(set(range(1,7)) ^ {face}, 1)[0]

def build(length, wiggliness, wrap):
    collision_map = CollisionMap()
    (position, entering_face) = start(wrap)

    minCoord = ThreeVec(0,0,0)
    maxCoord = ThreeVec(0,0,0)

    segments = []

    while length > 0:

        while collision_map.is_trapped(position, wrap):
            (position, entering_face) = start(wrap)

        ok = False
        new_position = position
        while not ok:
            if random.random() < wiggliness:
                leaving_face = random_other_face(entering_face)
            else:
                leaving_face = leaving_to_entering[entering_face]

            new_position = position.add(exit_face_delta[leaving_face])
            new_position.wrap(wrap)

            if not collision_map.is_occupied(new_position):
                ok = True

        collision_map.add(new_position)
        segments.append(Segment(entering_face, leaving_face, position))

        for d in (0,1,2):
            minCoord[d], min(position[d], minCoord[d])
            maxCoord[d] = max(position[d], maxCoord[d])

        entering_face = leaving_to_entering[leaving_face]
        length -= 1

        position = new_position

    return (segments, minCoord, maxCoord)

def main(length, wiggliness, wrap):

    (segments, minCoord, maxCoord) = build(length, wiggliness, wrap)

    cameraX = 0
    cameraY = 0
    cameraZ = -wrap
    depth = wrap

    print("camera {{ location <{0}, {1}, {2}> look_at <{0}, {1}, {3}> }}"
            .format(cameraX, cameraY, cameraZ, 0))

    print(generate_povray(segments))

if __name__ == "__main__":
    main(length, wiggliness, wrap)
