(: Homework 4 Solution
   CSEP 344
   Note: xml outputs have been stripped, run them to verify your xml outputs.
:)

(: Problem 72. :)
(: Answer based on mountain/located element (is slightly different :)

<result> 
{
for $all in doc("mondial.xml")/mondial,
    $country in $all/country

    let $a := $all/mountain[located/@country = $country/@car_code][height > 2000],
        $b := count($a)
    where $b > 2

    return <country>
          <name> { string($country/name) } </name>
          {
	    for $allMountains in $all/mountain[located/@country = $country/@car_code]
	      return <mountains>
	             <name>{string($allMountains/name)}</name>
		     <height>{string($allMountains/height)}</height>
		     </mountains>
	  }
	</country>
	        
} </result>
