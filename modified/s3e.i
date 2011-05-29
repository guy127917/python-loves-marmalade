
%module s3e
%{
#include "s3e.h"
%}

#define I3D_OS_S3E
%include "s3e.h"

%import "carrays.i"
%import "cdata.i"
%array_class(int, intArray);
