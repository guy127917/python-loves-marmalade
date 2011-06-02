
%module gles
%{
    #include "GLES/glplatform.h"
    #include "GLES/gl.h"
    #include "GLES/glext.h"
    #include "GLES/egl.h"
%}
#define I3D_OS_S3E
%import "s3eTypes.h"

%typemap(out) unsigned char* {
    $result = PyString_FromString($1);
}

%typemap(in) (const GLvoid* pointer) {
    float temp[2048];
    int i;
    for (i = 0; i < PySequence_Length($input); i++) {
        PyObject *o = PySequence_GetItem($input,i);
        if (PyNumber_Check(o)) {
            temp[i] = (float) PyFloat_AsDouble(o);
        } else {
            PyErr_SetString(PyExc_ValueError,"Sequence elements must be numbers");      
            return NULL;
        }
    }
    $1 = temp; 
}

%include "glplatform.h"
%include "gl.h"
%include "glext.h"
%include "egl.h"
