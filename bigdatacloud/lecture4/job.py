f = open("hadoop_job.tsv")

for line in f:
  vals = line.split()
  print "\t".join(vals[0:6])

