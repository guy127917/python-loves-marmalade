#!/bin/bash

mkdir -p data/lib/python2.7
mkdir -p data/include/python2.7

# copy python libraries to runtime directory
cp -r upstream/Lib/ data/lib/python2.7
# copy configuration files to runtime directory
cp -r modified/config data/lib/python2.7/
cp modified/pyconfig.h data/include/python2.7/

exit $?
