#include "colors.inc"
#include "pipes.inc"

camera {
    location <0, 0, -3>
    look_at <0, 0, 0>
}

background { color rgb <0.9, 0.9, 0.9> }
light_source {
    <-100, 100, -30>
    color White
}

union {
    object { Connect_34 }
    object { Connect_31 translate <1, 0, 0> }
    object { Connect_23 translate <1, -1, 0> }
    object { Connect_46 translate <0, -1, 0> }
    object { Connect_52 translate <0, -1, 1> }
    object { Connect_12 translate <0, 0, 1> }
    object { Connect_15 translate <0, 1, 1> }
    object { Connect_63 translate <0, 1, 0> }
    object { Connect_41 translate <-1, 1, 0> }
    object { Connect_24 translate <-1, 0, 0> }

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
