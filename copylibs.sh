#!/bin/bash

mkdir -p example/data/lib/python2.7
mkdir -p example/data/include/python2.7

cp -r upstream/Lib/ example/data/lib/python2.7
cp -r config example/data/lib/python2.7/
cp modified/pyconfig.h example/data/include/python2.7/

exit $?
