(:                            :)
(::::::::::::::::::::::::::::::)
(:     q12.xq                 :)
(:     return clause          :)

for $x in doc("bib.xml")/bib/book
return <answer>
           <title> { $x/title/text() } </title>
           <year>{ $x/year/text() } </year>
       </answer>


(: why do we use { and } ?  what happens without them ? :)


