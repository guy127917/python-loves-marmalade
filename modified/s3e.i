
%module s3e
%{
#include "s3e.h"
%}

// Typemap for s3eSurfacePtr
// Return a writeable byte array rather than a pointer type
%typemap(out) void*
{
  int buf_size = s3eSurfaceGetInt(S3E_SURFACE_HEIGHT) * s3eSurfaceGetInt(S3E_SURFACE_PITCH);
  $result = PyBuffer_FromReadWriteMemory($1, buf_size);
}

#define I3D_OS_S3E
%include "s3e.h"
