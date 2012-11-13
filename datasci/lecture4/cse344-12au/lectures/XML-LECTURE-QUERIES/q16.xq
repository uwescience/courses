(:                            :)
(::::::::::::::::::::::::::::::)
(:     q16.xq                 :)
(:     Regrouping             :)

for $b in doc("bib.xml")/bib
let $y1:= (distinct-values($b/book/year/text())),
    $y2:= (distinct-values($b/book/@year)),
    $y:=($y1, $y2)   (: means concatenation :)
for $x in $y
return 
    <answer>
        <year> { $x } </year>
        { for $z in $b/book[(year/text()=$x) or (@year=$x)]/title
          return $z
        }
    </answer>
