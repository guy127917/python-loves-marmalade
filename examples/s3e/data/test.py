import os
import sys
import time
import threading

import s3e
import colorsys

def getRgb565Bytes(r,g,b): 
    red   = int(r * 0xFF)
    green = int(g * 0xFF)
    blue  = int(b * 0xFF)
    return ( ((red >> 3) << 11) | ((green >> 2) << 5) | (blue >> 3))

def drawCircle(x,y, (r,g,b), radius=20):
    surface = s3e.s3eSurfacePtr();
    width   = s3e.s3eSurfaceGetInt(s3e.S3E_SURFACE_WIDTH);
    height  = s3e.s3eSurfaceGetInt(s3e.S3E_SURFACE_HEIGHT);
    pitch   = s3e.s3eSurfaceGetInt(s3e.S3E_SURFACE_PITCH);

    # clip circular region
    startx  = max(x - radius, 0)
    endx    = min(width, x + radius)
    starty  = max(0, y - radius)
    endy    = min(height, y + radius)

    radiusSq = radius * radius

    for iy in range (starty, endy):
        pos = iy * pitch + startx;
        for ix in range(startx, endx):
            distx = x - ix
            disty = y - iy
            # if length of this line is under the radius paint the pixel
            if distx * distx + disty * disty < radiusSq:
                bytes = getRgb565Bytes(r,g,b)
                p1 = bytes & 0xFF
                p2 = (bytes & 0xFF00) >> 8

                surface[pos]    = chr(p1)
                surface[pos+1]  = chr(p2)
            pos += 2;

def run():
    print 'hello, this is python code speaking'

    count = 0

    s3e.s3eSurfaceClear(00,0xFF,0x12)
 
    width = s3e.s3eSurfaceGetInt(s3e.S3E_SURFACE_WIDTH)
    height = s3e.s3eSurfaceGetInt(s3e.S3E_SURFACE_HEIGHT)
    pitch = s3e.s3eSurfaceGetInt(s3e.S3E_SURFACE_PITCH)
    
    print "Width %d Height %d Pitch %d" % (width, height, pitch)
    bytes = height * pitch

    surface = s3e.s3eSurfacePtr()
    print type(surface)
    print len(surface)

    colours = 360
    duration = 3.0
   
    starttime = time.time()
    # cycle through colour spectrum for duration
    for r in range(colours):
        val = getRgb565Bytes(*colorsys.hsv_to_rgb(r/float(colours), 1.0, 1.0))
        s3e.s3eSurfaceClear(*map(lambda c : int(c * 0xFF), colorsys.hsv_to_rgb(r/float(colours), 1.0, 1.0)))
        s3e.s3eSurfaceShow()

        if time.time < r * duration / colours:
            time.sleep(0.01)
    
    # copy to surface
    for i in range(1000):
        drawCircle(30,100, (0x200,0x30,0x66))
        s3e.s3eSurfaceShow()
        s3e.s3eDeviceYield(0)
    s3e.s3eSurfaceClear(0)
    s3e.s3eVideoPlay("angel_fish.jpg", 0, 0, 0, 320, 320)
    s3e.s3eAudioPlay("trumpet.wav", 0)
    time.sleep(3)

if __name__ == "__main__":
    run()
