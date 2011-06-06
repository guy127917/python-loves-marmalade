/* Minimal main program -- everything is loaded from the library */

#include "Python.h"

#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif

#include "IwUtil.h"

int
main(int argc, char **argv)
{
	/* 754 requires that FP exceptions run in "no stop" mode by default,
	 * and until C vendors implement C99's ways to control FP exceptions,
	 * Python requires non-stop mode.  Alas, some platforms enable FP
	 * exceptions by default.  Here we disable them.
	 */
    IwUtilInit();

    int ret = Py_Main(argc, argv);

    IwUtilTerminate();
    return ret;
}
