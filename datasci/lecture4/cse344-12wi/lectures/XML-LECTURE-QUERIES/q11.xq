(:                            :)
(::::::::::::::::::::::::::::::)
(:     q11.xq                 :)
(:     basic FLWR expression  :)

for $x in doc("bib.xml")/bib/book
where $x/year/text() > 1995
return $x/title



(: try also:    
for $x in doc("bib.xml")/bib/book
where $x/@year > 1995 
return $x/title
:)


(: Same, more geek'ish
for $x in doc("bib.xml")/bib/book[year/text() > 1995] /title 
return $x
:)

(: Even better:
doc("bib.xml")/bib/book[year/text() > 1995] /title 
:)


