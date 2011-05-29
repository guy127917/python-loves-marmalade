%module fft
%{

extern void smbFft(float *reals, float* imags, const long fftFrameSize, const long sign);
%}

void smbFft(float *reals, float* imags, const long fftFrameSize, const long sign);

%include "carrays.i"
%array_class(float, floatArray);
