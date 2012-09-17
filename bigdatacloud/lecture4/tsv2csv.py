import sys

f = open(sys.argv[1])

stat = {}
for line in f:
  vals = line.split()
  print ",".join(vals)
