(: Homework 4 Solution
   CSE 344
   Note: xml outputs have been stripped, run them to verify your xml outputs.
:)

(: Problem 7 :)
(: Result based on mountain/@country :)

<result> 
{
let $all := doc("mondial.xml")/mondial
for $country in $all/country
    let $a := $all/mountain[fn:exists(fn:index-of(fn:tokenize(@country, ' '), fn:string($country/@car_code)))],
        $b := count($a[height > 2000])
    where $b > 2

    return <country>
          <name> { string($country/name) } </name>
          {
	    for $aMountain in $a
	      return <mountains>
	             <name>{fn:string($aMountain/name)}</name>
		     <height>{fn:string($aMountain/height)}</height>
		     </mountains>
	  }
	</country>
	        
} </result>
