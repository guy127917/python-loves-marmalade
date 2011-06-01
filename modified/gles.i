
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

%include "glplatform.h"
%include "gl.h"
%include "glext.h"
%include "egl.h"
