(:                            :)
(::::::::::::::::::::::::::::::)
(:     q05.xq pretty printed  :)

for $x in doc("bib.xml")/bib/book/author/text()
return normalize-space($x)