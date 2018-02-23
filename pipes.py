#!/usr/bin/python3

from three_vec import ThreeVec
from collision_map import CollisionMap
from utils import direction_vec

import random

# Play with these parameters for different results
length = 10000
wrap = 20
wiggliness = 0.1 

# 1 = Bottom -Y
# 2 = Top    +Y
# 3 = Left   -X
# 4 = Right  +X
# 5 = Near   -Z
# 6 = Far    +Z

class Segment(object):
    def __init__(self, enter, exit, position):
        self._enter = enter
        self._exit = exit
        self._pos = position

    def __repr__(self):
        return("object {{ Connect_{0}{1} translate {2} }}"
            .format(self._enter, self._exit, self._pos))

leaving_to_entering = [ None, 2, 1, 4, 3, 6, 5 ]

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


def generate_povray(segments):
    header = """
#include "pipes.inc"
#include "colors.inc"

light_source {
    <1000, 1000, 300>
    color Red
}

light_source {
    <1000, -1000, -1000>
    color Blue
}

light_source {
    <-1000, -1000, -1000>
    color Green
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
        diffuse 0.9
        specular 1.0
    }

    rotate 15 * z
    rotate 15 * y
}
"""
    return header + objects + footer


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

            new_position = position.add(direction_vec[leaving_face])
            new_position.wrap(wrap)

            if not collision_map.is_occupied(new_position):
                ok = True

        collision_map.add(new_position)
        segments.append(Segment(entering_face, leaving_face, position))

        for d in (0,1,2):
            minCoord[d] = min(position[d], minCoord[d])
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

    print("box {{ {0} {1} pigment {{ rgbt 1 }} hollow interior {{ media {{ scattering {{1, 0.01}} samples 20 }} }} }}".format(minCoord, maxCoord))

    print(generate_povray(segments))

if __name__ == "__main__":
    main(length, wiggliness, wrap)
