#!/usr/bin/env python
import os
import sys
import shutil

print "Creating python bindings to S3E functions"

# Create swig C bindings to s3e headers
if os.system("swig -python -classic -I%s/s3e/h -includeall modified/s3e.i" % os.environ['AIRPLAY_ROOT']):
    sys.exit(1)

# Make sure that the python file is somewhere that the auto lib copy script will find it
if not os.path.exists("modified/Lib"):
    os.makedirs("modified/Lib")
if os.path.exists("modified/Lib/s3e.py"):
    os.remove("modified/Lib/s3e.py")
shutil.move("modified/s3e.py", "modified/Lib/s3e.py")
