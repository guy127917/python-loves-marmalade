/* Minimal main program -- everything is loaded from the library */

#include "Python.h"

extern void init_fft();

int
main(int argc, char **argv)
{
    Py_Initialize();
    init_fft();
    
    FILE *fp = fopen("swig_test.py", "r");
    PyRun_SimpleFile(fp, "swig_test.py");
    fclose(fp);
    return 0;
}
