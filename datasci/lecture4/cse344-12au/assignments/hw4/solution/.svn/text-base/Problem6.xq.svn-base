(: Homework 4 Solution
   CSE 344
   Note: xml outputs have been stripped, run them to verify your xml outputs.
:)

(: Problem 8. :)

<html> 
<head>
	<title>Crossing Rivers</title>
</head>
<body>
<h1>Below is a list of countries that a river crosses</h1>
<ul>
{
let $all := doc("mondial.xml")/mondial
for $river in $all/river
	let $countries := fn:tokenize($river/@country, ' ')
	where count($countries) > 1
    order by count($countries)
    return <li>
           <font>{ string($river/name) }</font>
		   <ol>
	    { 

	        for $countryId in $countries	  
		    return <li> 
				{ string($all/country[@car_code = $countryId]/name)}
 				</li>
        }
		</ol>	
	    </li>
    
}
</ul>
</body>
</html>
