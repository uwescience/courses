(: Homework 4 Solution
   CSE 344
   Note: xml outputs have been stripped, run them to verify your xml outputs.
:)

(: Problem 4. :)

<result> 
<country>
<name>United States</name>
{
for $province in doc("mondial.xml")/mondial/country[normalize-space(name) = "United States"]/province

    let $pop := $province/population 
    let $area := $province/area 

    let $ratio := number($pop)  div number($area)
     
    order by $ratio

    return <state>
           <name>{normalize-space($province/name)}</name>
           <population_density>{$ratio}</population_density>
	   </state>
} 
</country>
</result>
