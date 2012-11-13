(: Homework 4 Solution
   CSE 344 
   Note: xml outputs have been stripped, run them to verify your xml outputs.
:)

(: Problem 1. :)

<result>
<country>
<name>Peru</name> 
{
for $peruCities in doc("mondial.xml")/mondial/country[normalize-space(name)= "Peru"]//city/name/text()
  order by $peruCities
  return <city><name>{normalize-space($peruCities)}</name></city>
} 
</country>
</result>
