import glob

files = glob.glob("reuters/*.*")

d = {}
for fn in files:
  f = open(fn)
  terms = f.read().split()
  for t in terms:
    key = (fn,t)
    count = d.setdefault(key, 0)
    d[key] = count + 1

#print len(d)
#print len(sorted({doc for (doc, term), count in d.iteritems()}))
#print sorted([(count, k) for k, count in d.iteritems()],reverse=True)[:100]

for (doc, term), count in d.iteritems():
  print "%s, %s, %s" % (doc, term, count)
