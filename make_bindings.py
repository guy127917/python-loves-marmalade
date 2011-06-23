#!/usr/bin/env python
import os
import sys
import shutil

"""
This script is for making bindings which will be compiled into the python runtime
"""

if len(sys.argv) != 2:
    print "Requires single argument (module name)"
    system.exit(1)

module = sys.argv[1]
print "Creating python bindings to S3E functions for module %s" % module

options=""
output=""
includes = ["/s3e/h", "/s3e/h/std", "/s3e/h/GLES"]
if module != "s3e":
    includes += ["/modules/%s/h" % (m) for m in ["IwGL", "IwGx", "IwGraphics", "IwUtil", "IwGeom", "IwCore", "IwResManager"]]
    options = "-c++ -cpperraswarn"
    output = "-o modified/"+module + "_wrap.cpp"

incpaths = " ".join("-I%s%s" % (os.environ['MARMALADE_ROOT'], i) for i in includes)
# Create swig C bindings to s3e headers
cmdline = "swig -python -classic -O -Idummy %s %s -includeall %s modified/%s.i" % (options, incpaths, output, module)
print cmdline
if os.system(cmdline):
    sys.exit(2)

# Make sure that the python file is somewhere that the auto lib copy script will find it
if not os.path.exists("modified/Lib"):
    os.makedirs("modified/Lib")
if os.path.exists("modified/Lib/%s.py" % module):
    os.remove("modified/Lib/%s.py" % module)
shutil.move("modified/%s.py" % module, "modified/Lib/%s.py" % module)

print os.getcwd()
