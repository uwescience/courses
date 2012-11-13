for $x in doc("bib.xml")/bib/book/author/first,
    $y in doc("bib.xml")/bib/book/author/last
let $nl := "&#10;"
return <test> {$x,$y,$nl} </test>
