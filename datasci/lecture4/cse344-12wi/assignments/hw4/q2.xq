     <answer>
       { 
           for $x in doc("additional-files/mondial.xml")/mondial/country[name="Peru"]/province[count(city)>1]/name
	   return <big-province> { fn:string($x) } </big-province>
       }
     </answer>