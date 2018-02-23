#!/usr/bin/python3

import random

# Play with these parameters for different results
lengths = 10000
wrap = 20
wiggliness = 0.3

# 1 = Bottom -Y
# 2 = Top    +Y
# 3 = Left   -X
# 4 = Right  +X
# 5 = Near   -Z
# 6 = Far    +Z

exit_face_delta = [
        ( 0,  0,  0),
        ( 0, -1,  0),
        ( 0,  1,  0),
        (-1,  0,  0),
        ( 1,  0,  0),
        ( 0,  0, -1),
        ( 0,  0,  1)
    ]

leaving_to_entering = [ None, 2, 1, 4, 3, 6, 5 ]

position = (0, 0, 0)

entering_face = 3


minCoord = [0, 0, 0]
maxCoord = [0, 0, 0]

print("""
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
""")



while lengths > 0:
    if random.random() < wiggliness:
        leaving_face = random.sample(set(range(1,7)) ^ { entering_face }, 1)[0]
    else:
        leaving_face = leaving_to_entering[entering_face]

    print("    object {{ Connect_{0}{1} translate <{2}, {3}, {4}> }}"
            .format(entering_face, leaving_face, position[0], position[1], position[2]))

    position = [ p + d for p,d in zip(position, exit_face_delta[leaving_face]) ]

    for d in (0,1,2):
        if wrap != None:
            if position[d] < -wrap:
                position[d] = wrap
            if position[d] > wrap:
                position[d] = -wrap

        minCoord[d] = min(position[d], minCoord[d])
        maxCoord[d] = max(position[d], maxCoord[d])

    entering_face = leaving_to_entering[leaving_face]
    lengths -= 1

print("""
    texture {
        pigment { color White }
    }
    finish {
        ambient 0.1
        diffuse 0.7
        crand 0.01
        reflection { 0.01, 0.05 }
        specular 1
        metallic
    }

    rotate 15 * z
    rotate 15 * y
}
""")

if wrap is None:
    cameraX = (minX + maxX) / 2.0
    cameraY = (minY + maxY) / 2.0
    cameraZ = minZ - 10
else:
    cameraX = 0
    cameraY = 0
    cameraZ = -wrap

print("camera {{ location <{0}, {1}, {2}> look_at <{0}, {1}, {3}> }}"
        .format(cameraX, cameraY, cameraZ, 0))
