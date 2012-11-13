set size 1.0, 0.6
set terminal png
set xlabel "count"
set ylabel "# subjects"
set logscale x
set logscale y
set style data linespoints
set output '_tmp_image'
plot '_tmp_results' using 1:2 title '# subjects by count of tuples per subject'
quit
