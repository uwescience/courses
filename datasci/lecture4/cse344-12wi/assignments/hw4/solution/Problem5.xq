(: Homework 4 Solution
   CSE 344
   Note: xml outputs have been stripped, run them to verify your xml outputs.
:)

(: Problem 5. :)

<result> 
{
for $all in doc("mondial.xml")/mondial,
    $distinctGrps in distinct-values($all//ethnicgroups)

    where count($all//ethnicgroups[normalize-space(text()) = normalize-space($distinctGrps)]) > 10

    return <ethnicgroups num_countries="{count($all//ethnicgroups[normalize-space(text()) = normalize-space($distinctGrps)])}">
           <name>{normalize-space($distinctGrps)}</name>
	   </ethnicgroups>
} 
</result>
