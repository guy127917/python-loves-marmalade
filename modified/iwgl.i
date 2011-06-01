
%module iwgl
%{
int IwGLInit();
void IwGLTerminate();

void IwGLSwapBuffers();

void IwGLSuspend();

void IwGLResume();

typedef enum IwGLProperty
{
    IW_GL_WIDTH,
	IW_GL_HEIGHT,
	IW_GL_ROTATE,
	
	IW_GL_VIRTUAL_WIDTH,
	IW_GL_VIRTUAL_HEIGHT,
	IW_GL_VIRTUAL_ROTATE,
	IW_GL_VIRTUAL_LETTERBOX,

	IW_GL_VIRTUAL_RESOLUTION,
	IW_GL_CONSISTENT_HANDLES,
	IW_GL_CACHE_STATE,		
	IW_GL_CACHE_TEXTURES,
	IW_GL_CACHE_VBOS,	
	IW_GL_CACHE_SURFACES,
	IW_GL_CACHE_SHADERS,
	IW_GL_CACHE_VBO_POINTERS,

	IW_GL_PROPERTY_MAX
} IwGLProperty;
int IwGLGetInt(IwGLProperty prop);
%}

int IwGLInit();

void IwGLTerminate();

void IwGLSwapBuffers();

void IwGLSuspend();

void IwGLResume();

enum IwGLProperty
{
    IW_GL_WIDTH,
	IW_GL_HEIGHT,
	IW_GL_ROTATE,
	
	IW_GL_VIRTUAL_WIDTH,
	IW_GL_VIRTUAL_HEIGHT,
	IW_GL_VIRTUAL_ROTATE,
	IW_GL_VIRTUAL_LETTERBOX,

	IW_GL_VIRTUAL_RESOLUTION,
	IW_GL_CONSISTENT_HANDLES,
	IW_GL_CACHE_STATE,		
	IW_GL_CACHE_TEXTURES,
	IW_GL_CACHE_VBOS,	
	IW_GL_CACHE_SURFACES,
	IW_GL_CACHE_SHADERS,
	IW_GL_CACHE_VBO_POINTERS,

	IW_GL_PROPERTY_MAX
};
int IwGLGetInt(IwGLProperty prop);