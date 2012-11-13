(:                            :)
(::::::::::::::::::::::::::::::)
(:     q14.xq                 :)
(:     aggregates             :)

for $x in doc("bib.xml")/bib/book
where count($x/author)>2
return $x


(:
Aggregates in XQuery:
  count = a function that counts
  avg =  computes the average
  sum = computes the sum
  distinct-values = eliminates duplicates
:)


