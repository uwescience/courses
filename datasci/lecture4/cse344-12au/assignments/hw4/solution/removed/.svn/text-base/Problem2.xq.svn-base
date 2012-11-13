(: Homework 4 Solution
   CSE 344
   Note: xml outputs have been stripped, run them to verify your xml outputs.
:)

(: Problem 2. :)

<result> 
<country>
<name>China</name> 
{
for $provinces in doc("mondial.xml")/mondial/country[name = "China"]/province,
    $cities in $provinces/city
      
    where $cities/@id = $provinces/@capital
    order by $provinces/name
    return <province>
           <name> { normalize-space($provinces/name) } </name>
           <capital>
		   <name>{normalize-space(distinct-values($cities/name/text()))}</name>
		   </capital>
	   </province>
} 
</country>
</result>
