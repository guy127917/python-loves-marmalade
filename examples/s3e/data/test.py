import os
import sys
import time
import threading

import s3e

def foo():
    i = 0
    while i < 3:
        print "foo %d" % i
        time.sleep(1)
        i += 1

def run():
    for i in xrange(10):
        print 'hello, this is python code speaking'

    count = 0

    s3e.s3eSurfaceClear(00,0xFF,0x12)
    s3e.s3eVideoPlay("angel_fish.jpg", 0, 0, 0, 320, 320)
     
#    ptr = s3e.s3eSurfacePtr()
#    ptr = cdata(ptr, 100)
    
#    for i in range(100):
#        ptr[i] = '\x43'

#    s3e.s3eSurfaceShow()

    #t = threading.Thread(target=foo)
    #t.start()
    time.sleep(3)
    

if __name__ == "__main__":
    run()
