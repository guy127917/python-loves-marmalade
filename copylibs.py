#!/usr/bin/env python
#create libs if they don't already exist
import os
import shutil
from os.path import join

root = os.path.dirname(__file__)

print "Copying python runtime libraries..."

# copy python libraries to runtime directory
if not os.path.exists("data/lib/python2.7"):
    shutil.copytree(join(root, "upstream/Lib/"), "data/lib/python2.7/")

if not os.path.exists("data/lib/python2.7/config"):
    shutil.copytree(join(root, "modified/config"), "data/lib/python2.7/config/")
if not os.path.exists("data/include"):
    os.makedirs("data/include/python2.7")
    shutil.copyfile(join(root, "modified/pyconfig.h"), "data/include/python2.7/pyconfig.h")

