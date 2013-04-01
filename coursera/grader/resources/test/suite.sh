#!/bin/bash

for e in `ls`
do
    if [ -d $e ] && [ $e != "lib" ]
    then
        cd $e
        python *tests.py
        cd ..
    fi
done
