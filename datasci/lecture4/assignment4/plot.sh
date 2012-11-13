#!/usr/bin/env tcsh

setenv TMP_RESULTS _tmp_results
setenv TMP_IMAGE _tmp_image

cp $1 $TMP_RESULTS
gnuplot plot.gnu
rm $TMP_RESULTS
mv $TMP_IMAGE $1.png
