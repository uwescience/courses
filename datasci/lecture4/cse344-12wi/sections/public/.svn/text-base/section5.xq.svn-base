(: SECTION 4 -- Saxon , XML and XPath 
   The following examples use the mondial.xml file and the mondial.dtd DTD
   We use saxon to run and xmllint for formatting the results (xmllint --format)
:)



(: What are the names of all the countries? this is simple specification of the exact path :) 

<result>
{  doc("mondial.xml")/mondial/country/name }
</result>


(: What does this do? :)
<result>
{  doc("mondial.xml")/mondial/./country/name }
</result>


(: What about this? :)
<result>
{  doc("mondial.xml")/mondial/country/../country/name }
</result>


(: The construct // matches a country at any depth of the XML tree :)

<result>
{ doc("mondial.xml")//country }
</result>


(: For the country with car code equal to "D" (Germany), find the neighboring countries
   Here we use the XPath predicate [@car_code="D"] and also the construct @, which
   refers to attributes of the XML nodes :)

<result>
{ doc("mondial.xml")//country[@car_code="D"]/border }
</result>


(: Find the names of the countries with population at least 10 million
   The construct text() returns the text content of the node :)

<result>
{ doc("mondial.xml")//country[population/text() >= 10000000]/name }
</result>


(: Which cities have population at least 4 million? :)

<result> 
{ doc("mondial.xml")//city[population >= 4000000]/name } 
</result>


(: Find the name of the cities for the countries that are encompassed by europe:)

<result> 
{ doc("mondial.xml")//country[encompassed/@continent="europe"]//city/name } 
</result>


(: Which rivers have source at the nortern hemisphere? :)

<result> 
{  doc("mondial.xml")//river[source/latitude > 0.0]/name } 
</result>
   
   
(: Which are the rivers which start at Austria? Notice here that the country is not referenced
   by its name inside the river tag, but by its car code :)
      
<result> 
{ doc("mondial.xml")//river[source/@country = (//country[name='Austria']/@car_code)]/name} 
</result>


(: Which countries are encompassed by both Asia and Europe ? We can write this query in two ways :)

(: This uses two predicates. One will be evaluated first and then the other:)
<result>
{ doc("mondial.xml")//country[encompassed/@continent="asia"][encompassed/@continent="europe"]/name }
</result>


(: This uses the construct "and" and uses a single predicate:)
<result> 
{ doc("mondial.xml")//country[encompassed/@continent='europe' and encompassed/@continent='asia']/name  }
</result>
   

(: Which are the countries that neighbor France and have either a population more then 20 million
   or a total GDP over 10000? :)
<result> 
{ doc("mondial.xml")//country[border/@country = (//country[name='France']/@car_code)]
                             [population > 20000000 or gdp_total > 10000]/name
} 
</result>


(: Which countries have at least 90% muslim population? :)

(: The following XPath query does NOT work! This finds the countries that have muslims and some 
   religion that has percentage at least 90% :)
<result>
{ doc("mondial.xml")//country[religions[@percentage >= 90] = 'Muslim']/name }
</result>

(: Instead, we use nested predicates :)
<result>
{ doc("mondial.xml")//country[religions[@percentage >= 90] = 'Muslim']/name }
</result>


   
