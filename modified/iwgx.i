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
#define __APPLE__

%import "s3eTypes.h"
%import "s3e.h"
%import "stdlib.h"
%import "stdio.h"
%import "string.h"
%import "float.h"

//The wrappers for these friend functions will not compile on GCC 
//(they are never publicly visible outside friend declarations, which GCC does not consider to be declarations)
//A couple are just inline functions where the definitions are never publicly visible
%ignore _IwGxUpdateMaterialAnims;
%ignore _IwGxDebugDumpGeomInfoNow;
%ignore IwGxVRAMDump;
%ignore _IwGraphicsSetModelChunkIDFlagsPtr;
%ignore CIwTPageInfo::GetTexture;
%ignore _IwGxUpdateMaterialAnims;
%ignore _IwGxResManagerCallbackTextureSharedTexels;
%ignore _Serialise_ResGroupResources;
%ignore _IwGxInit_InitSWTextures;
%ignore _IwGxInit_InitHWTextures;
%ignore CIwTexture::SW_VerifyModulation;
%ignore _ResGroupManagedConstructorCallback;
%ignore _ResGroupManagedDestructorCallback;
%ignore _ResGroupManagedSerialiseCallback;
%ignore _SerialiseDirectory;
%ignore _Serialise_ResGroupHST;
%ignore _Serialise_ResGroupMembers;
%ignore _Serialise_ResGroupResources;
%ignore _Serialise_ResGroupChildPaths;
%ignore _Serialise_ResGroupDirectory;
%ignore _Serialise_BlockSizes;
%ignore _PostResourceLoad;
%ignore IwResBinaryMount;
%ignore _Serialise_ResGroupResourcesOptimised;
%ignore _Serialise_ResGroupMembers();
%ignore _Serialise_ResGroupChildPaths(void);
%ignore DL_Malloc_mallinfo;
%ignore DL_Malloc_GetSize;
%ignore DL_Malloc_MORECORE;
%ignore IwTextParserAssertCallback;
%ignore _ITXReadUnknown;
%ignore IwDebugTraceLineVPrintf;
%ignore CIwMaterial g_UserFlagNames;


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

