(: Homework 4 Solution
   CSE 344
   Note: xml outputs have been stripped, run them to verify your xml outputs.
:)

(: Problem 3. :)

<result> 

{
for $countries in doc("mondial.xml")/mondial/country

      
    where count(distinct-values($countries/province/@id)) > 20
	order by count(distinct-values($countries/province/@id))
    return <country num_provinces="{count(distinct-values($countries/province/@id))}">
			<name>{normalize-space($countries/name)}</name>			
			</country>
} 

</result>
