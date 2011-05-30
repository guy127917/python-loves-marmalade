
%module s3e
%{
#include "s3e.h"
%}

#define I3D_OS_S3E
%include "s3e.h"

%import "carrays.i"
%array_class(uint16, uint16Array);

%include "cdata.i"
