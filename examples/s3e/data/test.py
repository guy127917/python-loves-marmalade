import os
import sys
import time
import threading

import s3e
import colorsys

def getRgb565Byte(r,g,b): 
    red   = int(r * 0xFF)
    green = int(g * 0xFF)
    blue  = int(b * 0xFF)
    return ( ((red >> 3) << 11) | ((green >> 2) << 5) | (blue >> 3))

def run():
    print 'hello, this is python code speaking'

    count = 0

    s3e.s3eSurfaceClear(00,0xFF,0x12)
 
    width = s3e.s3eSurfaceGetInt(s3e.S3E_SURFACE_WIDTH)
    height = s3e.s3eSurfaceGetInt(s3e.S3E_SURFACE_HEIGHT)
    pitch = s3e.s3eSurfaceGetInt(s3e.S3E_SURFACE_PITCH)
    
    print "Width %d Height %d Pitch %d" % (width, height, pitch)
    bytes = height * pitch

    # construct a string of bytes for surface
    # There is an issue with the SWIG bindings ATM that means we have to pass the buffer
    # as a string, thus the last byte has to be zero. This can be fixed by treating using
    # a typemap in the binding (I think)
    surface = bytearray(bytes-1)
    ptr = s3e.s3eSurfacePtr()
    colours = 360
    duration = 3.0
    
    # cycle through colour spectrum for duration
    for r in range(colours):
        val = getRgb565Byte(*colorsys.hsv_to_rgb(r/float(colours), 1.0, 1.0))
        #s3e.memmove(ptr, surface_string)
        s3e.s3eSurfaceClear(*map(lambda c : int(c * 0xFF), colorsys.hsv_to_rgb(r/float(colours), 1.0, 1.0)))
        s3e.s3eSurfaceShow()
        time.sleep(duration / colours)
    
    for i in range(bytes-1):
        surface[i] = 0x22
    # copy to surface
    surface_string = str(surface)
    s3e.memmove(ptr, surface_string)
    s3e.s3eSurfaceShow()
    time.sleep(1)

    s3e.s3eVideoPlay("angel_fish.jpg", 0, 0, 0, 320, 320)
    time.sleep(3)
    

if __name__ == "__main__":
    run()
