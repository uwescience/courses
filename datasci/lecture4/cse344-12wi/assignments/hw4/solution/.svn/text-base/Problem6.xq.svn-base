(: Homework 4 Solution
   CSE 344
   Note: xml outputs have been stripped, run them to verify your xml outputs.
:)

(: Problem 6. :)

<result> 
<country>
<name>United States</name>
{
for $all in doc("mondial.xml")/mondial/country[normalize-space(name) = "United States"],
    $province in $all/province[population > 11000000]

    let $pop := $province/population 
    let $ratio := number($pop) div number($all/population)
    
    order by $ratio descending

    return <state>
           <name>{normalize-space($province/name)}</name>
           <population_ratio>{$ratio}</population_ratio>
	 </state>
} 
</country>
</result>
