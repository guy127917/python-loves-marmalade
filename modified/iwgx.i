%module iwgx
%{
#include "IwUtil.h"
#include "IwGeom.h"
#include "IwGx.h"
#include "IwGraphics.h"
#include "IwResManager.h"
%}

#define I3D_OS_S3E
#define __S3E__ 1
#define __GNUC__ 1
#define I3D_ARCH_ARM
#define IW_GENERATE_SWIG
#define __APPLE__

%import "s3eTypes.h"
%import "s3e.h"
%import "stdlib.h"
%import "stdio.h"
%import "string.h"
%import "float.h"


#undef IW_ALIGNED
#define IW_ALIGNED(x) 

%include "IwUtil.h"
%include "IwGeom.h"
%include "IwGx.h"
%include "IwGraphics.h"
%include "IwResManager.h"

%inline %{
//Casting helpers for SWIG

#define IW_MAKE_CAST_FUNC(_a) class C##_a; INLINE C##_a* As##_a(CIwResource* res) { return (C##_a*)res; }
IW_MAKE_CAST_FUNC(IwTexture);
IW_MAKE_CAST_FUNC(IwModel);
IW_MAKE_CAST_FUNC(IwAnim);
IW_MAKE_CAST_FUNC(IwAnimSkin);
IW_MAKE_CAST_FUNC(IwAnimSkel);
%}

