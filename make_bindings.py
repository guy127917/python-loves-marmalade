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

# Create swig C bindings to s3e headers
if os.system("swig -python -classic -I%s/s3e/h -I%s/s3e/h/GLES -I%s/modules/IwGL/h -includeall modified/%s.i" % (os.environ['AIRPLAY_ROOT'],os.environ['AIRPLAY_ROOT'], os.environ['AIRPLAY_ROOT'], module)):
    sys.exit(2)

# Make sure that the python file is somewhere that the auto lib copy script will find it
if not os.path.exists("modified/Lib"):
    os.makedirs("modified/Lib")
if os.path.exists("modified/Lib/%s.py" % module):
    os.remove("modified/Lib/%s.py" % module)
shutil.move("modified/%s.py" % module, "modified/Lib/%s.py" % module)
