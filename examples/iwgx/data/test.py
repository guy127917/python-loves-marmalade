import os
import sys
import time
import threading
import math
import random
from datetime import datetime

import s3e
from iwgx import * 
from gles import *

class entity:
    def __init__(self, model, mat):
        self.model = model
        self.mat = mat

    def render(self):
        IwGxSetModelMatrix(self.mat)
        self.model.Render()

def get_pointer_state():
    return (s3e.s3ePointerGetX(), s3e.s3ePointerGetY())

def run():
    IwGxInit()
    IwGraphicsInit()
    
    IwGxSetPerspMul(IwGxGetScreenWidth()/3);

    viewMat = CIwFMat()
    viewMat.SetIdentity();
    viewMat.SetRotZ(math.pi);
    viewMat.t.z = -200.0
    IwGxSetViewMatrix(viewMat);
    
    IwGetResManager().LoadGroup("model.group")

    model = AsIwModel(IwGetResManager().GetResNamed("FunkyVic", "CIwModel"))
    
    ents = []
    for i in range(0, 10):
        modMat = CIwFMat()
        modMat.SetRotY(random.random()*math.pi)
        modMat.t.x = random.random()*1000.0 - 500.0
        modMat.t.y = random.random()*1000.0 - 500.0
        ents.append(entity(model, modMat))
    
    done = False
    angle = 0.0

    while not done:

        IwGxClear()
        
        for e in ents:
            e.mat.PostRotateY(0.05)
            e.render()
        
        IwGxFlush()
        IwGxSwapBuffers()

        #To take advantage of IwGL's automatic screen rotation support, the
        #projection matrix and viewport should be set up every frame.
        if s3e.s3eDeviceCheckQuitRequest():
            done = True
        pass

        s3e.s3ePointerUpdate()

        state = s3e.s3ePointerGetState(s3e.S3E_POINTER_BUTTON_SELECT)
        if state & s3e.S3E_POINTER_STATE_PRESSED:
            lastPos = get_pointer_state()
        elif  state & s3e.S3E_POINTER_STATE_DOWN:
            pos = get_pointer_state()
            viewMat.PostRotateY((pos[0] - lastPos[0]) * 0.05)
            viewMat.PreRotateX((pos[1] - lastPos[1]) * 0.05)
            lastPos = pos
            IwGxSetViewMatrix(viewMat);
    

        s3e.s3eDeviceYield(0)

    IwGraphicsTerminate()
    IwGxTerminate()

if __name__ == "__main__":
    run()
