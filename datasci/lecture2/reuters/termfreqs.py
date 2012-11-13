import glob
import string
files = glob.glob("*.txt.*")

stopwords = open("stopwords.txt").read().split()

d = {}
for fn in files:
  f = open(fn)
  contents = f.read()
  contents = filter(lambda x: x in string.printable, contents)
  clean = contents.translate(None, """,./\;:'"()-<>?!#%~`^&*$@{}|""")
  terms = clean.split()
  for term in terms:
    t = term.encode('ascii','ignore')
    if t not in stopwords:
      key = (fn,t)
      count = d.setdefault(key, 0)
      d[key] = count + 1

#print len(d)
#print len(sorted({doc for (doc, term), count in d.iteritems()}))
#print sorted([(count, k) for k, count in d.iteritems()],reverse=True)[:100]

print "doc_id,term_id,frequency"
for (doc, term), count in d.iteritems():
  print "%s,%s,%s" % (doc.replace(".","_"), term, count)
