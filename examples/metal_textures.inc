#declare rusted_shiny_metal = 
texture {
  bozo
  texture_map {
    [0.30  pigment {
             color rgb <0.71, 0.65, 0.26>
           }               
           finish {
             ambient 0.0
             diffuse 0.7
             brilliance 6.0
             phong 0.75
             phong_size 80.0
             reflection {
               0.25 , 0.25
               fresnel  off
               falloff  1.0
               exponent 1.0
               metallic 0.0
             }
           }
         ]
    [0.4   pigment {
             granite
             color_map {
               [ 0.0     rgb <0.89, 0.51, 0.28> ]
               [ 0.4     rgb <0.7, 0.13, 0.0> ]
               [ 0.5     rgb <0.69, 0.41, 0.08> ]
               [ 0.6     rgb <0.49, 0.31, 0.28> ]
               [ 1.0     rgb <0.89, 0.51, 0.28> ]
             }
             scale 0.3
             warp {
               turbulence 0.5
             }
           }
           normal {
             granite 0.5
             scale 0.01
           }             
           finish {
             ambient 0.0
             diffuse 0.4
           }
         ]
  }
  warp {
    turbulence <3.0, 2.0, 1.0>
  }
}
