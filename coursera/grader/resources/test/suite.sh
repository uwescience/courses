#!/bin/bash

for e in `ls`
do
    if [ -d $e ]
    then
        cd $e
        python *tests.py
        cd ..
    fi
done
