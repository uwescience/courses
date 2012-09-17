f = open("hadoop_task.tsv")

stat = {}
for line in f:
  vals = line.split()
  status = vals[-1]
  stat.setdefault(status,1)
  stat[status] += 1

print stat
