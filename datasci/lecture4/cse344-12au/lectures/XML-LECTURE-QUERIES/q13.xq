(:                            :)
(::::::::::::::::::::::::::::::)
(:     q13.xq                 :)
(:     Nesting                :)

for $b in doc("bib.xml")/bib,
    $a in $b/book[year/text()=1995]/author
return <result>
          { $a,
            for $t in $b/book[author/last/text()=$a/last/text()]/title
            return $t
          }
       </result>


