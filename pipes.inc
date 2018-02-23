#declare Segment = union {
    cylinder {
        <0, -0.5, 0>,
        <0, 0.5, 0>,
        0.25
    }

    torus {
        0.25, 0.05
        translate -0.5 * y
    }

    torus {
        0.25, 0.05
        translate 0.5 * y
    }
}

#declare Corner = union {
    intersection {
        torus {
            0.5, 0.25
            rotate 90 * x
            translate < 0.5, -0.5, 0 >
        }

        box { < -0.5, -0.5, -0.5> <0.5, 0.5, 0.5> }
    }

    torus {
        0.25, 0.05
        translate -0.5 * y
    }

    torus {
        0.25, 0.05
        rotate 90 * z
        translate 0.5 * x
    }
}

// Faces:
// Bottom = 1
// Top = 2
// Left = 3
// Right = 4
// Near = 5
// Far = 6

#declare Connect_12 = object {
    Segment
}

#declare Connect_13 = object {
    Corner
    rotate 180 * y
}

#declare Connect_14 = object {
    Corner
}

#declare Connect_15 = object {
    Corner
    rotate 90 * y
}

#declare Connect_16 = object {
    Corner
    rotate 270 * y
}

#declare Connect_21 = object {
    Segment
}

#declare Connect_23 = object {
    Corner
    rotate 180 * z
}

#declare Connect_24 = object {
    Corner
    rotate 90 * z
}

#declare Connect_25 = object {
    Corner
    rotate 90 * z
    rotate 90 * y
}

#declare Connect_26 = object {
    Corner
    rotate 90 * z
    rotate 270 * y
}

#declare Connect_31 = object {
    Connect_13
}

#declare Connect_32 = object {
    Connect_23
}

#declare Connect_34 = object {
    Segment
    rotate 90 * z
}

#declare Connect_35 = object {
    Corner
    rotate 270 * z
    rotate 90 * x
}

#declare Connect_36 = object {
    Corner
    rotate 270 * z
    rotate 270 * x
}

#declare Connect_41 = object {
    Connect_14
}

#declare Connect_42 = object {
    Connect_24
}

#declare Connect_43 = object {
    Connect_34
}

#declare Connect_45 = object {
    Corner
    rotate 90 * x
}

#declare Connect_46 = object {
    Corner
    rotate 270 * x
}

#declare Connect_51 = object {
    Connect_15
}

#declare Connect_52 = object {
    Connect_25
}

#declare Connect_53 = object {
    Connect_35
}

#declare Connect_54 = object {
    Connect_45
}

#declare Connect_56 = object {
    Segment
    rotate 90 * x
}

#declare Connect_61 = object {
    Connect_16
}

#declare Connect_62 = object {
    Connect_26
}

#declare Connect_63 = object {
    Connect_36
}

#declare Connect_64 = object {
    Connect_46
}

#declare Connect_65 = object {
    Connect_56
}
