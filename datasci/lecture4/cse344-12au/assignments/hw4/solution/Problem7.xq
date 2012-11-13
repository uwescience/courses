(: Homework 4 Solution
   CSE 344
   Note: xml outputs have been stripped, run them to verify your xml outputs.
:)

(: Problem 9. :) 

<result> 
<waterbody>
<name>Pacific Ocean</name>

{
for $all in doc("mondial.xml")/mondial,
    $pacificOcean in $all/sea[normalize-space(name) = "Pacific Ocean"]

	let $x := fn:tokenize(fn:normalize-space($pacificOcean/@country), ' ')
	
    return <adjacent_countries>
		{
			for $country in $all/country
			where fn:exists(fn:index-of($x, $country/@car_code))
			return <country>
				<name>{ string($country/name) }</name>
				</country>
		}	
		</adjacent_countries>

} 

</waterbody>
</result>
