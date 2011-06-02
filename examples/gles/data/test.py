import os
import sys
import time
import threading
from datetime import datetime

import s3e
from gles import *
from iwgl import *


def run():
    print 'hello, this is python code speaking'

    IwGLInit()
    
    print "Screen BPP  : %d\n" % (s3e.s3eSurfaceGetInt(s3e.S3E_SURFACE_PIXEL_TYPE) & s3e.S3E_SURFACE_PIXEL_SIZE_MASK)
    print "\n"
    print "Vendor     : %s\n" % glGetString( GL_VENDOR ) 
    print "Renderer   : %s\n" % glGetString( GL_RENDERER ) 
    print "Version    : %s\n" % glGetString( GL_VERSION )
    print "Extensions : %s\n" % glGetString( GL_EXTENSIONS )
    print "\n"

    glMatrixMode( GL_MODELVIEW );
    glLoadIdentity( );

    glEnable(GL_DEPTH_TEST);

    glDepthFunc(GL_LESS);

    glShadeModel(GL_SMOOTH);

    start_time = datetime.now() 
    frames = 0;
    done = False
    cube, color = getCube()

    while not done:
        #To take advantage of IwGL's automatic screen rotation support, the
        #projection matrix and viewport should be set up every frame.
        w = IwGLGetInt(IW_GL_WIDTH);
        h = IwGLGetInt(IW_GL_HEIGHT);
        glViewport( 0, 0, w, h );
        glMatrixMode( GL_PROJECTION );
        glLoadIdentity( );

        glOrthof( -2.0, 2.0, -2.0, 2.0, -20.0, 20.0 );

        # Do our drawing, too.
        glClearColor(0.0, 0.0, 0.0, 1.0);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glEnableClientState(GL_VERTEX_ARRAY);
        glEnableClientState(GL_COLOR_ARRAY);
        glColorPointer(4, GL_FLOAT, 0, color);
        glVertexPointer(3, GL_FLOAT, 0, cube);
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 24);
        glDisableClientState(GL_VERTEX_ARRAY);
        glDisableClientState(GL_COLOR_ARRAY);
        glMatrixMode(GL_MODELVIEW);
        glRotatef(5.0, 1.0, 1.0, 1.0);

        # Call IwGL swap instead of egl directly
        IwGLSwapBuffers();

        # Check for error conditions. #
        gl_error = glGetError();

        if gl_error != GL_NO_ERROR:
            fprintf( stderr, "testgl: OpenGL error: %#x\n", gl_error );

        frames += 1
        # Allow the user to see what's happening 
        #time.sleep(0.01)
        s3e.s3eDeviceYield(10);
        duration = datetime.now() - start_time
        if duration.seconds > 3:
            print duration
            print frames
            print "%f FPS" % (frames/duration.seconds)

    IwGLTerminate()

def getCube():
    cube = [
        0.5,  0.5, -0.5,   # 0
        0.5, -0.5, -0.5,   # 1
        -0.5,  0.5, -0.5,   # 3
        -0.5, -0.5, -0.5,   # 2

        -0.5,  0.5, -0.5,   # 3
        -0.5,  0.5,  0.5,   # 4
        -0.5, -0.5, -0.5,   # 2
        -0.5, -0.5,  0.5,   # 7

        0.5,  0.5, -0.5,   # 0
        0.5,  0.5,  0.5,   # 5
        0.5, -0.5, -0.5,   # 1
        0.5, -0.5,  0.5,   # 6

        0.5,  0.5,  0.5,   # 5
        -0.5,  0.5,  0.5,   # 4
        0.5, -0.5,  0.5,   # 6
        -0.5, -0.5,  0.5,   # 7

        0.5,  0.5,  0.5,   # 5
        0.5,  0.5, -0.5,   # 0
        -0.5,  0.5,  0.5,   # 4
        -0.5,  0.5, -0.5,   # 3

        0.5, -0.5,  0.5,   # 6
        0.5, -0.5, -0.5,   # 1
        -0.5, -0.5,  0.5,   # 7
        -0.5, -0.5, -0.5,   # 2
    ]
    colors = [
        1.0,  1.0,  0.0, 1.0,  # 0
        1.0,  0.0,  0.0,  1.0, # 1
        0.0,  1.0,  0.0, 1.0,  # 3
        0.0,  0.0,  0.0,  1.0, # 2

        0.0,  1.0,  0.0, 1.0,  # 3
        0.0,  1.0,  1.0,  1.0, # 4
        0.0,  0.0,  0.0, 1.0,  # 2
        0.0,  0.0,  1.0, 1.0,  # 7

        1.0,  1.0,  0.0, 1.0,  # 0
        1.0,  1.0,  1.0, 1.0,  # 5
        1.0,  0.0,  0.0, 1.0,  # 1
        1.0,  0.0,  1.0, 1.0,  # 6

        1.0,  1.0,  1.0, 1.0,  # 5
        0.0,  1.0,  1.0, 1.0,  # 4
        1.0,  0.0,  1.0, 1.0,  # 6
        0.0,  0.0,  1.0, 1.0,  # 7

        1.0,  1.0,  1.0, 1.0,  # 5
        1.0,  1.0,  0.0, 1.0,  # 0
        0.0,  1.0,  1.0, 1.0,  # 4
        0.0,  1.0,  0.0, 1.0,  # 3

        1.0,  0.0,  1.0, 1.0,  # 6
        1.0,  0.0,  0.0, 1.0,  # 1
        0.0,  0.0,  1.0, 1.0,  # 7
        0.0,  0.0,  0.0, 1.0,  # 2
    ]
    return (cube, colors)
if __name__ == "__main__":
    run()
